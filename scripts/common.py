"""Shared helpers: paths, env loading, slug, logging, paper IO."""
from __future__ import annotations

import json
import logging
import os
import re
from dataclasses import dataclass, field, asdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Iterable

import yaml
from dotenv import load_dotenv
from slugify import slugify as _slugify

ROOT = Path(__file__).resolve().parent.parent
PAPERS_DIR = ROOT / "src" / "content" / "papers"
REPOS_DIR = ROOT / "src" / "content" / "repos"
CACHE_DIR = ROOT / ".cache"
PAPERS_DIR.mkdir(parents=True, exist_ok=True)
CACHE_DIR.mkdir(parents=True, exist_ok=True)

load_dotenv(ROOT / ".env", override=False)


# --- robust env readers -----------------------------------------------------
# GitHub Actions injects unset `vars.X` / `secrets.X` as EMPTY STRINGS, not as
# absent keys. So `os.environ.get("X", default)` returns "" (not the default),
# and `int(os.environ.get("X", "30"))` becomes int("") -> ValueError. These
# helpers treat empty/whitespace as "absent".

def env_str(key: str, default: str = "") -> str:
    v = os.environ.get(key)
    return v.strip() if v and v.strip() else default


def env_int(key: str, default: int) -> int:
    v = os.environ.get(key)
    if v is None or not v.strip():
        return default
    try:
        return int(v.strip())
    except ValueError:
        return default


def safe_tags(tags) -> list[str]:
    """Tags become single URL path segments. '/' '\\' (LLMs emit e.g.
    'AI/NLP') break Astro's [tag] route. Replace them, collapse whitespace,
    dedupe, keep order."""
    out: list[str] = []
    for t in tags or []:
        if not isinstance(t, str):
            continue
        s = re.sub(r"\s+", " ", t.replace("/", "-").replace("\\", "-")).strip().strip("-").strip()
        if s and s not in out:
            out.append(s)
    return out


def env_float(key: str, default: float) -> float:
    v = os.environ.get(key)
    if v is None or not v.strip():
        return default
    try:
        return float(v.strip())
    except ValueError:
        return default


# --- LLM usage accounting ---------------------------------------------------
# Pipeline scripts run as separate processes (process.py -> process_news.py ->
# push_feishu.py), so token usage is accumulated in a JSON file the final
# notify step reads. Runs are sequential, so plain read-modify-write is safe.

USAGE_FILE = CACHE_DIR / "usage.json"


def reset_usage() -> None:
    if USAGE_FILE.exists():
        USAGE_FILE.unlink()


def add_usage(model: str, usage) -> None:
    """Accumulate per-model token usage. `usage` is the OpenAI SDK usage
    object (DeepSeek adds prompt_cache_hit_tokens). Best-effort: never raise."""
    try:
        if usage is None:
            return
        u = usage.model_dump() if hasattr(usage, "model_dump") else dict(usage)
        data = {}
        if USAGE_FILE.exists():
            try:
                data = json.loads(USAGE_FILE.read_text(encoding="utf-8"))
            except Exception:
                data = {}
        m = data.setdefault(model, {"prompt_tokens": 0, "completion_tokens": 0,
                                    "cache_hit_tokens": 0, "calls": 0})
        m["prompt_tokens"] += int(u.get("prompt_tokens") or 0)
        m["completion_tokens"] += int(u.get("completion_tokens") or 0)
        m["cache_hit_tokens"] += int(u.get("prompt_cache_hit_tokens") or 0)
        m["calls"] += 1
        USAGE_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2),
                              encoding="utf-8")
    except Exception as exc:  # accounting must never break the pipeline
        log.warning("add_usage failed (%s): %s", model, exc)


log = logging.getLogger("agent")
if not log.handlers:
    h = logging.StreamHandler()
    h.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s | %(message)s"))
    log.addHandler(h)
    log.setLevel(env_str("LOG_LEVEL", "INFO"))


@dataclass
class RawPaper:
    """Result of the fetch stage — pre-filter, pre-summary."""
    arxiv_id: str           # e.g. "2511.12345" (no "v1" suffix)
    title: str
    abstract: str
    authors: list[str]
    url: str                # https://arxiv.org/abs/<id>
    pdf_url: str            # https://arxiv.org/pdf/<id>
    primary_category: str   # e.g. "cs.IR"
    categories: list[str] = field(default_factory=list)
    published: str = ""     # ISO date
    source: str = ""        # "arxiv" or "huggingface-daily"
    hf_upvotes: int = 0     # HF Daily Papers signal


def now_iso_date() -> str:
    return datetime.now(timezone.utc).date().isoformat()


_ID_RE = re.compile(r"(\d{4}\.\d{4,5})")


def normalize_arxiv_id(raw: str) -> str:
    """Strip version suffix and URL prefix from arxiv ids."""
    m = _ID_RE.search(raw or "")
    return m.group(1) if m else raw.strip()


def make_slug(title: str, arxiv_id: str) -> str:
    base = _slugify(title or "paper", max_length=60, word_boundary=True)
    return f"{base}-{arxiv_id.replace('.', '')}" if base else arxiv_id


def existing_arxiv_ids() -> set[str]:
    ids: set[str] = set()
    for f in PAPERS_DIR.glob("*.md"):
        text = f.read_text(encoding="utf-8", errors="ignore")
        m = re.search(r"^arxiv_id:\s*['\"]?([^'\"\n]+)['\"]?", text, re.M)
        if m:
            ids.add(normalize_arxiv_id(m.group(1)))
    return ids


def _read_frontmatter(path: Path) -> dict:
    """Parse the YAML frontmatter block of a content .md file. Returns {} on
    any malformed file — dedup must never crash the pipeline."""
    text = path.read_text(encoding="utf-8", errors="ignore")
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        return yaml.safe_load(parts[1]) or {}
    except Exception:
        return {}


def recent_repo_names(days: int = 7) -> set[str]:
    """Repo full-names (owner/name, lowercased) broadcast in the prior `days`
    daily digests, read from src/content/repos/<date>.md frontmatter.

    Used to suppress re-broadcasting a project that already appeared in the
    last week. The window is the `days` digests *before* today — today's own
    file is excluded so same-day re-runs don't blank out the list."""
    today = datetime.now(timezone.utc).date()
    cutoff = today - timedelta(days=days)
    names: set[str] = set()
    if not REPOS_DIR.exists():
        return names
    for f in REPOS_DIR.glob("*.md"):
        try:
            d = datetime.strptime(f.stem, "%Y-%m-%d").date()
        except ValueError:
            continue
        if d < cutoff or d >= today:   # keep [today-days, today-1]
            continue
        for r in (_read_frontmatter(f).get("repos") or []):
            n = (r.get("name") or "").strip().lower()
            if n:
                names.add(n)
    return names


def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2, default=str), encoding="utf-8")


def read_json(path: Path):
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))
