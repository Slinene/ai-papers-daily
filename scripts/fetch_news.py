"""Stage 1b: pull AI industry news from public sources (no auth required).

Output: .cache/raw_news.json — deduped list of NewsItem dicts.

Sources:
  - Hacker News Algolia search API: focused keyword queries, last 48h, points>=5
  - Reddit RSS: r/LocalLLaMA, r/MachineLearning, r/singularity, r/OpenAI

Why these: HN aggregates serious tech discussion (release notes, technical
posts, blog announcements); Reddit captures community pulse + memes filtered
out by the downstream LLM relevance pass. Both are public, no auth needed.
"""
from __future__ import annotations

import os
import re
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone

import feedparser
import httpx

from common import CACHE_DIR, env_int, env_str, log, write_json

UA = "ai-papers-daily/0.1 (https://github.com/Slinene/ai-papers-daily)"
TIMEOUT = 20.0

HN_API = "https://hn.algolia.com/api/v1/search"
HN_QUERIES = [
    q.strip() for q in env_str(
        "NEWS_HN_QUERIES",
        # Western frontier
        "LLM,ChatGPT,OpenAI,Anthropic,Claude,Gemini,Llama,Mistral,"
        "AI agent,Agentic AI,RAG,fine-tuning,Meta AI,DeepMind,"
        # Chinese big tech
        "ByteDance,Alibaba Qwen,Tencent AI,Baidu Ernie,"
        "DeepSeek,Moonshot Kimi,Zhipu ChatGLM,01-ai Yi",
    ).split(",") if q.strip()
]
HN_WINDOW_HOURS = env_int("NEWS_HN_WINDOW_HOURS", 48)
HN_MIN_POINTS = env_int("NEWS_HN_MIN_POINTS", 5)
HN_PER_QUERY = env_int("NEWS_HN_PER_QUERY", 10)

REDDIT_FEEDS = [
    f.strip() for f in env_str(
        "NEWS_REDDIT_SUBS",
        "LocalLLaMA,MachineLearning,singularity,OpenAI",
    ).split(",") if f.strip()
]
REDDIT_PER_SUB = env_int("NEWS_REDDIT_PER_SUB", 25)

# Chinese AI media RSS — covers domestic big-tech news (字节/阿里/腾讯/DeepSeek/Moonshot...).
# - qbitai (量子位): AI-only, high precision
# - infoq-ai (InfoQ 中国 AI 频道): AI + cloud/eng, generally on-topic
# - 36kr (36 氪): general tech, will need Chinese keyword filter downstream
CHINESE_FEEDS: list[tuple[str, str, bool]] = [
    ("qbitai",   "https://www.qbitai.com/feed",   True),   # ai_focused=True
    ("infoq-ai", "https://www.infoq.cn/feed/ai",  True),
    ("36kr",     "https://36kr.com/feed",         False),  # general tech, needs filter
]
CN_PER_FEED = env_int("NEWS_CN_PER_FEED", 20)
CN_WINDOW_HOURS = env_int("NEWS_CN_WINDOW_HOURS", 48)

# Industry / applied-ML blog RSS — high signal for an e-commerce / recsys /
# agent practitioner (production write-ups + curated digests). All AI-focused
# so they bypass the keyword gate. Blogs post infrequently → wider window.
BLOG_FEEDS: list[tuple[str, str]] = [
    ("amazon-science", "https://www.amazon.science/index.rss"),
    ("eugeneyan",      "https://eugeneyan.com/rss/"),
    ("netflix-tech",   "https://netflixtechblog.com/feed"),
    ("spotify-eng",    "https://engineering.atspotify.com/feed/"),
    ("hf-blog",        "https://huggingface.co/blog/feed.xml"),
    ("smol-ai-news",   "https://news.smol.ai/rss.xml"),
    ("import-ai",      "https://jack-clark.net/feed/"),
    ("latent-space",   "https://www.latent.space/feed"),
    ("lilian-weng",    "https://lilianweng.github.io/index.xml"),
]
BLOG_PER_FEED = env_int("NEWS_BLOG_PER_FEED", 8)
BLOG_WINDOW_HOURS = env_int("NEWS_BLOG_WINDOW_HOURS", 168)  # 7 days


@dataclass
class NewsItem:
    title: str
    url: str
    source: str        # "hn" | "reddit:LocalLLaMA" | "cn:qbitai" | "cn:36kr" | ...
    published: str     # ISO date (YYYY-MM-DD), best-effort
    points: int = 0    # HN points or Reddit score (best-effort)
    comments: int = 0
    snippet: str = ""
    fetched_query: str = ""  # which HN query surfaced this (debug aid)
    ai_focused: bool = False  # source-level signal: bypass keyword filter downstream


def _strip_html(s: str) -> str:
    return re.sub(r"<[^>]+>", "", s or "").strip()


def fetch_hn(query: str) -> list[NewsItem]:
    cutoff = int(
        (datetime.now(timezone.utc) - timedelta(hours=HN_WINDOW_HOURS)).timestamp()
    )
    params = {
        "query": query,
        "tags": "story",
        "numericFilters": f"created_at_i>{cutoff},points>={HN_MIN_POINTS}",
        "hitsPerPage": HN_PER_QUERY,
    }
    try:
        with httpx.Client(timeout=TIMEOUT, headers={"User-Agent": UA}) as cli:
            r = cli.get(HN_API, params=params)
            r.raise_for_status()
            data = r.json()
    except Exception as exc:
        log.warning("hn fetch failed query=%s: %s", query, exc)
        return []
    out: list[NewsItem] = []
    for h in data.get("hits", []):
        url = h.get("url") or f"https://news.ycombinator.com/item?id={h['objectID']}"
        title = h.get("title") or h.get("story_title") or ""
        if not title:
            continue
        out.append(NewsItem(
            title=title[:300],
            url=url,
            source="hn",
            published=(h.get("created_at") or "")[:10],
            points=int(h.get("points") or 0),
            comments=int(h.get("num_comments") or 0),
            snippet=(h.get("story_text") or "")[:400],
            fetched_query=query,
        ))
    return out


def fetch_chinese_feed(name: str, url: str, ai_focused: bool) -> list[NewsItem]:
    log.info("fetching cn:%s", name)
    cutoff = datetime.now(timezone.utc) - timedelta(hours=CN_WINDOW_HOURS)
    try:
        with httpx.Client(timeout=TIMEOUT, headers={"User-Agent": UA}, follow_redirects=True) as cli:
            r = cli.get(url)
            r.raise_for_status()
            body = r.content
    except Exception as exc:
        log.warning("cn fetch failed %s: %s", name, exc)
        return []

    try:
        feed = feedparser.parse(body)
    except Exception as exc:
        log.warning("cn parse failed %s: %s", name, exc)
        return []

    out: list[NewsItem] = []
    for e in feed.entries[:CN_PER_FEED]:
        title = (e.get("title") or "").strip()
        link = e.get("link") or ""
        if not title or not link:
            continue
        published = ""
        if e.get("published_parsed"):
            t = e["published_parsed"]
            pub_dt = datetime(*t[:6], tzinfo=timezone.utc)
            if pub_dt < cutoff:
                continue
            published = pub_dt.date().isoformat()
        out.append(NewsItem(
            title=title[:300],
            url=link,
            source=f"cn:{name}",
            published=published,
            snippet=_strip_html(e.get("summary", ""))[:400],
            ai_focused=ai_focused,
        ))
    return out


def fetch_blog_feed(name: str, url: str) -> list[NewsItem]:
    log.info("fetching blog:%s", name)
    cutoff = datetime.now(timezone.utc) - timedelta(hours=BLOG_WINDOW_HOURS)
    try:
        with httpx.Client(timeout=TIMEOUT, headers={"User-Agent": UA}, follow_redirects=True) as cli:
            r = cli.get(url)
            r.raise_for_status()
            body = r.content
    except Exception as exc:
        log.warning("blog fetch failed %s: %s", name, exc)
        return []
    try:
        feed = feedparser.parse(body)
    except Exception as exc:
        log.warning("blog parse failed %s: %s", name, exc)
        return []
    out: list[NewsItem] = []
    for e in feed.entries[:BLOG_PER_FEED]:
        title = (e.get("title") or "").strip()
        link = e.get("link") or ""
        if not title or not link:
            continue
        published = ""
        if e.get("published_parsed"):
            t = e["published_parsed"]
            pub_dt = datetime(*t[:6], tzinfo=timezone.utc)
            if pub_dt < cutoff:
                continue
            published = pub_dt.date().isoformat()
        out.append(NewsItem(
            title=title[:300],
            url=link,
            source=f"blog:{name}",
            published=published,
            snippet=_strip_html(e.get("summary", ""))[:400],
            ai_focused=True,  # curated AI/ML blogs — skip keyword gate
        ))
    return out


def fetch_reddit_sub(sub: str) -> list[NewsItem]:
    url = f"https://www.reddit.com/r/{sub}/.rss?limit={REDDIT_PER_SUB}"
    log.info("fetching reddit r/%s", sub)
    try:
        # feedparser doesn't honor custom UA reliably across versions — fetch
        # via httpx first, then parse the bytes.
        with httpx.Client(timeout=TIMEOUT, headers={"User-Agent": UA}, follow_redirects=True) as cli:
            r = cli.get(url)
            r.raise_for_status()
            body = r.content
    except Exception as exc:
        log.warning("reddit fetch failed r/%s: %s", sub, exc)
        return []

    try:
        feed = feedparser.parse(body)
    except Exception as exc:
        log.warning("reddit parse failed r/%s: %s", sub, exc)
        return []

    out: list[NewsItem] = []
    for e in feed.entries:
        title = (e.get("title") or "").strip()
        link = e.get("link") or ""
        if not title or not link:
            continue
        published = ""
        if e.get("published_parsed"):
            t = e["published_parsed"]
            published = datetime(*t[:6], tzinfo=timezone.utc).date().isoformat()
        out.append(NewsItem(
            title=title[:300],
            url=link,
            source=f"reddit:{sub}",
            published=published,
            snippet=_strip_html(e.get("summary", ""))[:400],
        ))
    return out


def main():
    items: dict[str, NewsItem] = {}  # dedup by URL

    log.info("HN: %d queries × %d/page", len(HN_QUERIES), HN_PER_QUERY)
    for q in HN_QUERIES:
        for it in fetch_hn(q):
            if it.url not in items:
                items[it.url] = it
        time.sleep(0.25)  # be polite to Algolia

    log.info("Reddit: %d subs × %d each", len(REDDIT_FEEDS), REDDIT_PER_SUB)
    for sub in REDDIT_FEEDS:
        for it in fetch_reddit_sub(sub):
            if it.url not in items:
                items[it.url] = it
        time.sleep(1.0)  # be polite to reddit

    log.info("Chinese feeds: %d sources × %d each (window=%dh)",
             len(CHINESE_FEEDS), CN_PER_FEED, CN_WINDOW_HOURS)
    for name, url, ai_focused in CHINESE_FEEDS:
        for it in fetch_chinese_feed(name, url, ai_focused):
            if it.url not in items:
                items[it.url] = it
        time.sleep(0.5)

    log.info("Blog feeds: %d sources × %d each (window=%dh)",
             len(BLOG_FEEDS), BLOG_PER_FEED, BLOG_WINDOW_HOURS)
    for name, url in BLOG_FEEDS:
        for it in fetch_blog_feed(name, url):
            if it.url not in items:
                items[it.url] = it
        time.sleep(0.5)

    raws = sorted(items.values(), key=lambda x: x.points, reverse=True)
    log.info("collected %d unique news items", len(raws))
    write_json(CACHE_DIR / "raw_news.json", [asdict(i) for i in raws])


if __name__ == "__main__":
    main()
