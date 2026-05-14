"""Stage 4: push today's new papers to a Feishu group via custom bot webhook.

Reads .cache/today_papers.json + the markdown files it points to, assembles
a 飞书 interactive card per chunk (max ~8 papers per card to stay under
size limits), POSTs to FEISHU_WEBHOOK. If FEISHU_SECRET is set, signs the
request per 飞书自定义机器人 spec.
"""
from __future__ import annotations

import base64
import hashlib
import hmac
import os
import time

import httpx
import yaml

from common import CACHE_DIR, PAPERS_DIR, log, now_iso_date, read_json

FEISHU_WEBHOOK = os.environ.get("FEISHU_WEBHOOK", "").strip()
FEISHU_SECRET = os.environ.get("FEISHU_SECRET", "").strip()

SITE_URL = os.environ.get("SITE_URL", "https://example.github.io").rstrip("/")
BASE_PATH = os.environ.get("BASE_PATH", "/ai-papers-daily").strip("/")
SITE_BASE = f"{SITE_URL}/{BASE_PATH}" if BASE_PATH else SITE_URL

PAPERS_PER_CARD = 8


def feishu_sign(secret: str, ts: int) -> str:
    """飞书自定义机器人签名：base64(hmac-sha256("{ts}\n{secret}", "")).

    The key is the salted string itself; the body is empty bytes.
    """
    key = f"{ts}\n{secret}".encode("utf-8")
    digest = hmac.new(key, b"", digestmod=hashlib.sha256).digest()
    return base64.b64encode(digest).decode("utf-8")


def load_today_papers() -> list[dict]:
    summary = read_json(CACHE_DIR / "today_papers.json")
    if not summary:
        return []
    out: list[dict] = []
    for fname in summary.get("wrote", []):
        path = PAPERS_DIR / fname
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        parts = text.split("---", 2)
        if len(parts) < 3:
            continue
        try:
            fm = yaml.safe_load(parts[1]) or {}
        except Exception as exc:
            log.warning("parse fm failed %s: %s", fname, exc)
            continue
        fm["_slug"] = path.stem
        out.append(fm)
    out.sort(key=lambda x: x.get("score", 0), reverse=True)
    return out


def build_card(papers: list[dict], chunk_idx: int, chunk_total: int) -> dict:
    today = now_iso_date()
    subtitle = f"今日新增 {len(papers)} 篇"
    if chunk_total > 1:
        subtitle += f" · 第 {chunk_idx + 1}/{chunk_total} 组"

    elements: list[dict] = []
    for i, p in enumerate(papers):
        tags = " ".join(f"`#{t}`" for t in (p.get("tags") or [])[:5])
        category = p.get("category", "")
        score = int(p.get("score", 0))
        depth_mark = " ⭐" if p.get("depth") == "full_pdf" else ""
        title = p.get("title", "")
        one_liner = p.get("one_liner", "")
        url_site = f"{SITE_BASE}/paper/{p['_slug']}"
        url_arxiv = p.get("url") or f"https://arxiv.org/abs/{p.get('arxiv_id','')}"

        md = (
            f"**[{title}]({url_site})**{depth_mark}\n"
            f"`{category}` · score {score}/10 · {tags}\n"
            f"{one_liner}"
        )
        elements.append({"tag": "markdown", "content": md})
        elements.append({
            "tag": "action",
            "actions": [
                {
                    "tag": "button",
                    "text": {"tag": "plain_text", "content": "📖 阅读卡片"},
                    "type": "primary",
                    "url": url_site,
                },
                {
                    "tag": "button",
                    "text": {"tag": "plain_text", "content": "📄 arXiv 原文"},
                    "type": "default",
                    "url": url_arxiv,
                },
            ],
        })
        if i < len(papers) - 1:
            elements.append({"tag": "hr"})

    elements.append({
        "tag": "note",
        "elements": [
            {"tag": "plain_text", "content": f"全部论文与归档 → {SITE_BASE}"}
        ],
    })

    return {
        "msg_type": "interactive",
        "card": {
            "config": {"wide_screen_mode": True},
            "header": {
                "title": {"tag": "plain_text", "content": f"📄 AI Papers Daily · {today}"},
                "subtitle": {"tag": "plain_text", "content": subtitle},
                "template": "blue",
            },
            "elements": elements,
        },
    }


def post(payload: dict) -> None:
    if not FEISHU_WEBHOOK:
        log.warning("FEISHU_WEBHOOK not set — skipping push")
        return
    body = dict(payload)
    if FEISHU_SECRET:
        ts = int(time.time())
        body["timestamp"] = str(ts)
        body["sign"] = feishu_sign(FEISHU_SECRET, ts)
    with httpx.Client(timeout=15.0) as cli:
        r = cli.post(FEISHU_WEBHOOK, json=body)
        r.raise_for_status()
        log.info("feishu push: HTTP %s body=%s", r.status_code, r.text[:240])


def post_empty_day() -> None:
    """No new papers — still send a heartbeat so users know the job ran."""
    payload = {
        "msg_type": "interactive",
        "card": {
            "config": {"wide_screen_mode": True},
            "header": {
                "title": {"tag": "plain_text", "content": f"📄 AI Papers Daily · {now_iso_date()}"},
                "subtitle": {"tag": "plain_text", "content": "今天没有新论文进入榜单"},
                "template": "grey",
            },
            "elements": [
                {"tag": "markdown",
                 "content": f"Agent 已运行，但今日没有相关性达标的论文。\n站点: {SITE_BASE}"}
            ],
        },
    }
    post(payload)


def main():
    papers = load_today_papers()
    if not papers:
        log.info("no papers today")
        if os.environ.get("PUSH_EMPTY_DAY", "0") == "1":
            post_empty_day()
        return

    chunks = [papers[i:i + PAPERS_PER_CARD] for i in range(0, len(papers), PAPERS_PER_CARD)]
    for i, chunk in enumerate(chunks):
        post(build_card(chunk, i, len(chunks)))
        if i < len(chunks) - 1:
            time.sleep(1)
    log.info("pushed %d papers in %d card(s)", len(papers), len(chunks))


if __name__ == "__main__":
    main()
