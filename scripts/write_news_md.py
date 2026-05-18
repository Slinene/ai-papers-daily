"""Stage 3b: render processed_news.json as one src/content/news/{date}.md.

Frontmatter matches src/content/config.ts -> news collection schema.
Each day overwrites its own file (so re-running on the same day refreshes
the digest in place rather than appending).
"""
from __future__ import annotations

import yaml

from common import CACHE_DIR, ROOT, log, now_iso_date, read_json, safe_tags

NEWS_DIR = ROOT / "src" / "content" / "news"
NEWS_DIR.mkdir(parents=True, exist_ok=True)


def main():
    data = read_json(CACHE_DIR / "processed_news.json") or {}
    topics = data.get("topics") or []
    items = data.get("items") or []
    date = data.get("date") or now_iso_date()

    if not topics:
        log.info("no news topics to write")
        return

    for t in topics:
        t["tags"] = safe_tags(t.get("tags") or [])

    fm = {
        "date": date,
        "collected": now_iso_date(),
        "topic_count": len(topics),
        "item_count": sum(len(t.get("sources") or []) for t in topics),
        "topics": topics,
    }
    fm_yaml = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, default_flow_style=False)

    # Body: human-readable rendering of the same content (Astro detail page can render)
    body_lines = [f"# {date} · AI 行业动态\n"]
    for i, t in enumerate(topics, 1):
        body_lines.append(f"## {i}. {t['title']}")
        body_lines.append("")
        body_lines.append(t.get("summary", ""))
        body_lines.append("")
        for s in t.get("sources", []):
            label = s.get("source", "")
            pts = f" · {s['points']}pts" if s.get("points") else ""
            body_lines.append(f"- [{s.get('title','')}]({s.get('url','')}) `{label}{pts}`")
        body_lines.append("")

    path = NEWS_DIR / f"{date}.md"
    content = f"---\n{fm_yaml}---\n\n" + "\n".join(body_lines) + "\n"
    path.write_text(content, encoding="utf-8")
    log.info("wrote %s (%d topics, %d items)",
             path.name, len(topics), sum(len(t.get("sources") or []) for t in topics))


if __name__ == "__main__":
    main()
