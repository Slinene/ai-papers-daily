"""Stage 1: fetch raw paper candidates from arXiv + HuggingFace Daily Papers.

Output: .cache/raw_papers.json (list[RawPaper]) — already deduped against
existing markdown files in src/content/papers/.
"""
from __future__ import annotations

import json
import os
import re
import time
from dataclasses import asdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

import feedparser
import httpx

from common import (
    CACHE_DIR,
    RawPaper,
    env_int,
    env_str,
    existing_arxiv_ids,
    log,
    normalize_arxiv_id,
    write_json,
)

# Data sources — extend by overriding ARXIV_CATEGORIES env var.
#   cs.IR  information retrieval / recsys (核心)
#   cs.LG  machine learning
#   cs.CL  computation and language / NLP
#   cs.AI  artificial intelligence
#   cs.CV  computer vision (含 multimodal 工作)
#   cs.MM  multimedia
#   cs.HC  human-computer interaction (Agent UX、interactive eval)
#   stat.ML statistics ML
ARXIV_CATEGORIES = [
    c.strip()
    for c in env_str(
        "ARXIV_CATEGORIES",
        "cs.IR,cs.LG,cs.CL,cs.AI,cs.CV,cs.MM,cs.HC,stat.ML",
    ).split(",")
    if c.strip()
]
# 30/cat keeps total candidate count similar to the 4-cat × 80 baseline
ARXIV_PER_CAT = env_int("ARXIV_PER_CAT", 30)
HF_DAILY_URL = "https://huggingface.co/api/daily_papers"
HF_LIMIT = env_int("HF_LIMIT", 50)
TIMEOUT = 30.0


def _arxiv_query(category: str, max_results: int) -> str:
    return (
        "http://export.arxiv.org/api/query"
        f"?search_query=cat:{category}"
        "&sortBy=submittedDate&sortOrder=descending"
        f"&max_results={max_results}"
    )


def fetch_arxiv(category: str) -> list[RawPaper]:
    url = _arxiv_query(category, ARXIV_PER_CAT)
    log.info("fetching arxiv category=%s", category)
    feed = feedparser.parse(url)
    out: list[RawPaper] = []
    for e in feed.entries:
        aid = normalize_arxiv_id(e.get("id", ""))
        if not aid:
            continue
        published = e.get("published", "")[:10]
        cats = [t["term"] for t in e.get("tags", []) if "term" in t]
        out.append(RawPaper(
            arxiv_id=aid,
            title=re.sub(r"\s+", " ", e.title).strip(),
            abstract=re.sub(r"\s+", " ", e.summary).strip(),
            authors=[a.name for a in e.get("authors", [])],
            url=f"https://arxiv.org/abs/{aid}",
            pdf_url=f"https://arxiv.org/pdf/{aid}",
            primary_category=category,
            categories=cats,
            published=published,
            source=f"arxiv-{category}",
        ))
    return out


def fetch_hf_daily() -> list[RawPaper]:
    log.info("fetching huggingface daily papers")
    out: list[RawPaper] = []
    try:
        with httpx.Client(timeout=TIMEOUT) as cli:
            r = cli.get(HF_DAILY_URL)
            r.raise_for_status()
            data = r.json()
    except Exception as exc:
        log.warning("hf daily fetch failed: %s", exc)
        return out

    for item in data[:HF_LIMIT]:
        p = item.get("paper") or {}
        aid = normalize_arxiv_id(p.get("id") or p.get("arxivId") or "")
        if not aid:
            continue
        title = (p.get("title") or "").strip()
        abstract = (p.get("summary") or "").strip()
        authors = [a.get("name", "") for a in (p.get("authors") or []) if a.get("name")]
        upvotes = int(p.get("upvotes") or 0)
        published = (item.get("publishedAt") or p.get("publishedAt") or "")[:10]
        out.append(RawPaper(
            arxiv_id=aid,
            title=title,
            abstract=abstract,
            authors=authors,
            url=f"https://arxiv.org/abs/{aid}",
            pdf_url=f"https://arxiv.org/pdf/{aid}",
            primary_category="hf",
            categories=[],
            published=published,
            source="huggingface-daily",
            hf_upvotes=upvotes,
        ))
    return out


def main():
    seen = existing_arxiv_ids()
    log.info("already have %d papers locally", len(seen))

    candidates: dict[str, RawPaper] = {}

    # HF first — its upvote signal helps later ranking
    for p in fetch_hf_daily():
        if p.arxiv_id in seen:
            continue
        candidates[p.arxiv_id] = p

    for cat in ARXIV_CATEGORIES:
        try:
            for p in fetch_arxiv(cat):
                if p.arxiv_id in seen:
                    continue
                if p.arxiv_id in candidates:
                    # merge: keep HF upvote info, but prefer arxiv abstract if longer
                    prev = candidates[p.arxiv_id]
                    if len(p.abstract) > len(prev.abstract):
                        prev.abstract = p.abstract
                    if p.authors and not prev.authors:
                        prev.authors = p.authors
                    if not prev.categories:
                        prev.categories = p.categories
                else:
                    candidates[p.arxiv_id] = p
            time.sleep(3)  # arXiv API politeness
        except Exception as exc:
            log.warning("arxiv fetch failed for %s: %s", cat, exc)

    raws = list(candidates.values())
    log.info("found %d new candidate papers", len(raws))

    write_json(CACHE_DIR / "raw_papers.json", [asdict(p) for p in raws])


if __name__ == "__main__":
    main()
