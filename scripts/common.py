"""Shared helpers: paths, env loading, slug, logging, paper IO."""
from __future__ import annotations

import json
import logging
import os
import re
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

from dotenv import load_dotenv
from slugify import slugify as _slugify

ROOT = Path(__file__).resolve().parent.parent
PAPERS_DIR = ROOT / "src" / "content" / "papers"
CACHE_DIR = ROOT / ".cache"
PAPERS_DIR.mkdir(parents=True, exist_ok=True)
CACHE_DIR.mkdir(parents=True, exist_ok=True)

load_dotenv(ROOT / ".env", override=False)

log = logging.getLogger("agent")
if not log.handlers:
    h = logging.StreamHandler()
    h.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s | %(message)s"))
    log.addHandler(h)
    log.setLevel(os.environ.get("LOG_LEVEL", "INFO"))


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


def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2, default=str), encoding="utf-8")


def read_json(path: Path):
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))
