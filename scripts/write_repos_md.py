"""Stage 3c: render processed_repos.json -> src/content/repos/{date}.md.

Frontmatter matches src/content/config.ts -> repos collection. Same-day
re-runs overwrite in place.
"""
from __future__ import annotations

import yaml

from common import CACHE_DIR, ROOT, log, now_iso_date, read_json, safe_tags

REPOS_DIR = ROOT / "src" / "content" / "repos"
REPOS_DIR.mkdir(parents=True, exist_ok=True)


def main():
    data = read_json(CACHE_DIR / "processed_repos.json") or {}
    repos = data.get("repos") or []
    date = data.get("date") or now_iso_date()
    if not repos:
        log.info("no repos to write")
        return

    for r in repos:
        r["tags"] = safe_tags(r.get("tags") or [])

    fm = {
        "date": date,
        "collected": now_iso_date(),
        "repo_count": len(repos),
        "repos": repos,
    }
    fm_yaml = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False,
                             default_flow_style=False)

    body_lines = [f"# {date} · 今日热门 AI 项目\n"]
    for i, r in enumerate(repos, 1):
        body_lines.append(f"## {i}. [{r['name']}]({r['url']}) ★{r.get('stars',0)}")
        body_lines.append("")
        body_lines.append(r.get("one_liner", ""))
        body_lines.append("")
        if r.get("capability"):
            body_lines.append(f"**能力**：{r['capability']}")
            body_lines.append("")
        if r.get("value"):
            body_lines.append(f"**借鉴价值**：\n{r['value']}")
            body_lines.append("")

    path = REPOS_DIR / f"{date}.md"
    path.write_text(f"---\n{fm_yaml}---\n\n" + "\n".join(body_lines) + "\n",
                    encoding="utf-8")
    log.info("wrote %s (%d repos)", path.name, len(repos))


if __name__ == "__main__":
    main()
