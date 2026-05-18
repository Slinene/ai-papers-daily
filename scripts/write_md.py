"""Stage 3: render processed papers as markdown files into src/content/papers/.

Each .md gets frontmatter that matches src/content/config.ts. Writes a
sidecar .cache/today_papers.json so the push script can find what's new
without rescanning git diffs.
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import yaml

from common import (
    CACHE_DIR,
    PAPERS_DIR,
    log,
    make_slug,
    now_iso_date,
    read_json,
    safe_tags,
    write_json,
)


def render_one(p: dict) -> Path:
    title_en = (p.get("title") or "").strip()
    title_zh = (p.get("title_zh") or "").strip()
    slug = make_slug(title_zh or title_en, p["arxiv_id"])
    date = (p.get("published") or now_iso_date())[:10]
    path = PAPERS_DIR / f"{date}-{slug}.md"

    fm = {
        "title": title_en,                              # English primary
        "title_zh": title_zh or None,                   # Chinese secondary
        "authors": (p.get("authors") or [])[:10],
        "affiliations": (p.get("affiliations") or [])[:6],
        "arxiv_id": p["arxiv_id"],
        "url": p["url"],
        "pdf_url": p.get("pdf_url") or "",
        "published": date,
        "collected": now_iso_date(),
        "category": p.get("category") or "Other",
        "direction": p.get("direction") or "",
        "tags": safe_tags(p.get("tags") or []),
        "one_liner": p.get("one_liner", ""),
        "practical_value": p.get("practical_value") or "",
        "score": int(p.get("score", 0)),
        "source": p.get("source", ""),
        "depth": p.get("depth", "abstract"),
    }
    # drop empty optional fields so the YAML is clean
    if not fm["pdf_url"]:
        fm.pop("pdf_url")
    if not fm["title_zh"]:
        fm.pop("title_zh")
    if not fm["affiliations"]:
        fm.pop("affiliations")
    if not fm["direction"]:
        fm.pop("direction")
    if not fm["practical_value"]:
        fm.pop("practical_value")

    fm_yaml = yaml.safe_dump(
        fm, allow_unicode=True, sort_keys=False, default_flow_style=False
    )
    body = (p.get("summary_md") or p.get("one_liner") or "").strip()
    content = f"---\n{fm_yaml}---\n\n{body}\n"
    path.write_text(content, encoding="utf-8")
    return path


def main():
    items = read_json(CACHE_DIR / "processed_papers.json") or []
    written: list[str] = []
    for p in items:
        try:
            path = render_one(p)
        except Exception as exc:
            log.warning("write failed for %s: %s", p.get("arxiv_id"), exc)
            continue
        written.append(path.name)
        log.info("wrote %s", path.name)

    write_json(CACHE_DIR / "today_papers.json", {
        "wrote": written,
        "count": len(written),
        "date": now_iso_date(),
        "generated_at": datetime.now(timezone.utc).isoformat(),
    })
    log.info("wrote %d markdown files", len(written))


if __name__ == "__main__":
    main()
