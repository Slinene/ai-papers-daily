"""Convert .cache/archive_topics.json -> src/content/archive_papers/{topic}/{slug}.md.

Driven by scripts/extract_archive.cjs which parses the HTML topics array.
Each paper becomes a Markdown file with full frontmatter (topic, detail.*)
and a structured body that the Astro detail page can render directly.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml
from slugify import slugify

from common import ROOT, log, read_json

ARCHIVE_DIR = ROOT / "src" / "content" / "archive_papers"
SRC_JSON = ROOT / ".cache" / "archive_topics.json"


def make_slug(title: str, idx: int) -> str:
    base = slugify(title or "paper", max_length=70, word_boundary=True, allow_unicode=False)
    return base or f"paper-{idx}"


def render_body(paper: dict) -> str:
    """Produce a long-form markdown body from detail.* so the Astro detail page
    can render it via <Content />. Keep section headings stable so styling
    in the .astro detail page can target them."""
    lines: list[str] = []
    if paper.get("idea"):
        lines.append(paper["idea"].strip())
        lines.append("")

    detail = paper.get("detail") or {}
    SECTIONS = [
        ("contribution", "核心贡献"),
        ("background",   "背景"),
        ("method",       "方法"),
        ("experiments",  "实验结果"),
        ("pros",         "优点"),
        ("cons",         "局限"),
        ("inspiration",  "对后续工作的启发"),
        ("takeaway",     "一句话总结"),
    ]
    for key, label in SECTIONS:
        v = (detail.get(key) or "").strip()
        if not v:
            continue
        lines.append(f"## {label}")
        lines.append("")
        lines.append(v)
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def write_one(topic: dict, paper: dict, idx: int) -> Path:
    slug = make_slug(paper["title"], idx)
    sub = ARCHIVE_DIR / topic["id"]
    sub.mkdir(parents=True, exist_ok=True)
    path = sub / f"{slug}.md"

    fm: dict = {
        "title": paper["title"],
        "authors": paper.get("authors") or None,
        "affiliation": paper.get("affiliation") or None,
        "date": paper.get("date") or None,
        "venue": paper.get("venue") or None,
        "topic": topic["id"],
        "topic_name": topic["name"],
        "topic_icon": topic.get("icon") or None,
        "idea": paper.get("idea") or None,
        "paperUrl": paper.get("paperUrl") or None,
        "codeUrl": paper.get("codeUrl") if paper.get("codeUrl") else None,
        "tags": paper.get("tags") or [],
        "unverified": bool(paper.get("unverified")),
        "detail": paper.get("detail") or None,
    }
    # drop None values for cleaner YAML
    fm = {k: v for k, v in fm.items() if v is not None and v != ""}

    fm_yaml = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, default_flow_style=False)
    body = render_body(paper)
    path.write_text(f"---\n{fm_yaml}---\n\n{body}", encoding="utf-8")
    return path


def main():
    topics = read_json(SRC_JSON)
    if not topics:
        log.error("no archive data at %s — run scripts/extract_archive.cjs first", SRC_JSON)
        sys.exit(1)

    # Clean existing files for the topics being imported (idempotent re-runs)
    for t in topics:
        sub = ARCHIVE_DIR / t["id"]
        if sub.exists():
            for f in sub.glob("*.md"):
                f.unlink()

    written = 0
    for t in topics:
        for i, p in enumerate(t.get("papers") or []):
            try:
                path = write_one(t, p, i)
            except Exception as exc:
                log.warning("failed for %s/%s: %s", t["id"], p.get("title"), exc)
                continue
            written += 1
            log.info("wrote %s", path.relative_to(ROOT))

    log.info("imported %d papers across %d topics", written, len(topics))


if __name__ == "__main__":
    main()
