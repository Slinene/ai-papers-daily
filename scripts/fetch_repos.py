"""Stage 1c: pull the day's hot AI code repos from the GitHub Search API.

Output: .cache/raw_repos.json — deduped repos with a README excerpt.

Heat signal (no official trending API): two queries, merged + deduped —
  A. Rising:  recently created + already starred  (fresh viral projects)
  B. Active:  pushed in the last few days + high stars (big projects shipping)

Auth: optional GITHUB_TOKEN (Actions auto-provides one as 5000/hr;
unauthenticated is 60/hr which still covers ~1 search + ~12 README fetches).
"""
from __future__ import annotations

import base64
import re
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone

import httpx

from common import CACHE_DIR, env_int, env_str, log, recent_repo_names, write_json

GITHUB_TOKEN = env_str("GITHUB_TOKEN")
UA = "ai-papers-daily/0.1 (+https://github.com/Slinene/ai-papers-daily)"
API = "https://api.github.com"

# GitHub search caps boolean operators (~5) and query length (256), so a big
# "A OR B OR C ..." string 422s. Use one short query per TOPIC instead —
# topic: qualifiers are robust, need no free-text OR, and are well-indexed.
QUERY_TOPICS = [
    t.strip() for t in env_str(
        "REPOS_TOPICS",
        "llm,llm-agent,ai-agent,agent,rag,multi-agent,"
        "recommender-system,generative-ai,llmops,llm-inference",
    ).split(",") if t.strip()
]
RISING_DAYS = env_int("REPOS_RISING_DAYS", 21)      # "newly created" window
RISING_MIN_STARS = env_int("REPOS_RISING_MIN_STARS", 60)
ACTIVE_DAYS = env_int("REPOS_ACTIVE_DAYS", 3)       # "recently pushed" window
ACTIVE_MIN_STARS = env_int("REPOS_ACTIVE_MIN_STARS", 800)
PER_QUERY = env_int("REPOS_PER_QUERY", 25)
MAX_REPOS = env_int("REPOS_MAX", 18)
DEDUP_DAYS = env_int("REPOS_DEDUP_DAYS", 7)   # skip repos broadcast this past week
README_MAX_CHARS = env_int("REPOS_README_MAX_CHARS", 4000)
TIMEOUT = 25.0


@dataclass
class Repo:
    name: str            # owner/name
    url: str
    description: str
    stars: int
    language: str
    topics: list[str] = field(default_factory=list)
    pushed_at: str = ""
    created_at: str = ""
    readme: str = ""
    heat: str = ""        # "rising" | "active"


def _headers(raw: bool = False) -> dict:
    h = {"User-Agent": UA, "Accept": "application/vnd.github+json",
         "X-GitHub-Api-Version": "2022-11-28"}
    if raw:
        h["Accept"] = "application/vnd.github.raw"
    if GITHUB_TOKEN:
        h["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return h


def _search(q: str, label: str) -> list[Repo]:
    params = {"q": q, "sort": "stars", "order": "desc", "per_page": PER_QUERY}
    try:
        with httpx.Client(timeout=TIMEOUT) as cli:
            r = cli.get(f"{API}/search/repositories", params=params, headers=_headers())
            r.raise_for_status()
            data = r.json()
    except Exception as exc:
        log.warning("repo search failed (%s): %s", label, exc)
        return []
    out: list[Repo] = []
    for it in data.get("items", []):
        out.append(Repo(
            name=it.get("full_name", ""),
            url=it.get("html_url", ""),
            description=(it.get("description") or "").strip()[:400],
            stars=int(it.get("stargazers_count") or 0),
            language=it.get("language") or "",
            topics=it.get("topics") or [],
            pushed_at=(it.get("pushed_at") or "")[:10],
            created_at=(it.get("created_at") or "")[:10],
            heat=label,
        ))
    return out


def _fetch_readme(full_name: str) -> str:
    try:
        with httpx.Client(timeout=TIMEOUT) as cli:
            r = cli.get(f"{API}/repos/{full_name}/readme", headers=_headers(raw=True))
            if r.status_code != 200:
                return ""
            text = r.text
    except Exception as exc:
        log.warning("readme fetch failed %s: %s", full_name, exc)
        return ""
    # strip HTML comments / badges noise, collapse blank runs
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()[:README_MAX_CHARS]


def main():
    now = datetime.now(timezone.utc)
    rising_since = (now - timedelta(days=RISING_DAYS)).date().isoformat()
    active_since = (now - timedelta(days=ACTIVE_DAYS)).date().isoformat()
    # unauthenticated search is ~10 req/min; with GITHUB_TOKEN ~30/min
    sleep_s = 1.0 if GITHUB_TOKEN else 7.0

    by_name: dict[str, Repo] = {}
    for topic in QUERY_TOPICS:
        # rising: newly created but already gathering stars
        q = f"topic:{topic} created:>={rising_since} stars:>={RISING_MIN_STARS}"
        log.info("repo search [rising] %s", q)
        for rp in _search(q, "rising"):
            if rp.name and rp.name not in by_name:
                by_name[rp.name] = rp
        time.sleep(sleep_s)
    # one active-popular sweep for the highest-signal topics
    for topic in QUERY_TOPICS[:4]:
        q = f"topic:{topic} pushed:>={active_since} stars:>={ACTIVE_MIN_STARS}"
        log.info("repo search [active] %s", q)
        for rp in _search(q, "active"):
            if rp.name and rp.name not in by_name:
                by_name[rp.name] = rp
        time.sleep(sleep_s)

    # Dedup against the past week's digests: a project already broadcast in the
    # last DEDUP_DAYS days shouldn't be repeated. Done before README fetch + LLM
    # so it also saves those calls. Names compared lowercased.
    if DEDUP_DAYS > 0:
        seen = recent_repo_names(DEDUP_DAYS)
        if seen:
            before = len(by_name)
            by_name = {k: v for k, v in by_name.items() if k.lower() not in seen}
            log.info("repo dedup: dropped %d already broadcast in last %dd, %d remain",
                     before - len(by_name), DEDUP_DAYS, len(by_name))

    repos = sorted(by_name.values(), key=lambda x: x.stars, reverse=True)[:MAX_REPOS]
    log.info("collected %d unique repos; fetching READMEs", len(repos))
    for rp in repos:
        rp.readme = _fetch_readme(rp.name)
        time.sleep(0.4)

    write_json(CACHE_DIR / "raw_repos.json", [asdict(r) for r in repos])
    log.info("wrote %d repos", len(repos))


if __name__ == "__main__":
    main()
