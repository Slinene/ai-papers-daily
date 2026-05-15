"""Stage 4: push today's new papers to a Feishu group.

Two transport modes, auto-detected by env vars:

  Mode A — Custom group bot webhook (simplest, no app setup)
    Vars: FEISHU_WEBHOOK [+ FEISHU_SECRET if 签名校验 enabled]
    Just POST the card envelope to the webhook URL.

  Mode B — Feishu self-built app via IM API (preferred when set)
    Vars: FEISHU_APP_ID + FEISHU_APP_SECRET + FEISHU_CHAT_ID
    Steps: exchange (app_id, app_secret) for tenant_access_token, then POST
    to im/v1/messages?receive_id_type=chat_id. Content must be the card
    body serialized as a JSON STRING (not a nested object).
    App needs `im:message:send_as_bot` permission.

If both modes' env vars are present, Mode B (IM API) wins.
"""
from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
import time

import httpx
import yaml

from common import CACHE_DIR, PAPERS_DIR, env_str, log, now_iso_date, read_json

# Mode A: webhook
FEISHU_WEBHOOK = env_str("FEISHU_WEBHOOK")
FEISHU_SECRET = env_str("FEISHU_SECRET")

# Mode B: self-built app + IM API
FEISHU_APP_ID = env_str("FEISHU_APP_ID")
FEISHU_APP_SECRET = env_str("FEISHU_APP_SECRET")
FEISHU_CHAT_ID = env_str("FEISHU_CHAT_ID")
FEISHU_RECEIVE_ID_TYPE = env_str("FEISHU_RECEIVE_ID_TYPE", "chat_id")

FEISHU_OPEN_HOST = env_str("FEISHU_OPEN_HOST", "https://open.feishu.cn").rstrip("/")

SITE_URL = env_str("SITE_URL", "https://slinene.github.io").rstrip("/")
BASE_PATH = env_str("BASE_PATH", "/ai-papers-daily").strip("/")
SITE_BASE = f"{SITE_URL}/{BASE_PATH}" if BASE_PATH else SITE_URL

PAPERS_PER_CARD = 8


def have_im_api_creds() -> bool:
    return bool(FEISHU_APP_ID and FEISHU_APP_SECRET and FEISHU_CHAT_ID)


# --------- Card builder (returns the body: config/header/elements) -----------

def build_card_body(papers: list[dict], chunk_idx: int, chunk_total: int) -> dict:
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
        "config": {"wide_screen_mode": True},
        "header": {
            "title": {"tag": "plain_text", "content": f"📄 AI Papers Daily · {today}"},
            "subtitle": {"tag": "plain_text", "content": subtitle},
            "template": "blue",
        },
        "elements": elements,
    }


def build_empty_day_body() -> dict:
    return {
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
    }


# --------- Mode A: custom bot webhook ----------------------------------------

def feishu_sign(secret: str, ts: int) -> str:
    """飞书自定义机器人签名: base64(hmac-sha256("{ts}\n{secret}", "")).
    The key is the salted string itself; the body is empty bytes."""
    key = f"{ts}\n{secret}".encode("utf-8")
    digest = hmac.new(key, b"", digestmod=hashlib.sha256).digest()
    return base64.b64encode(digest).decode("utf-8")


def send_via_webhook(card_body: dict) -> None:
    body: dict = {"msg_type": "interactive", "card": card_body}
    if FEISHU_SECRET:
        ts = int(time.time())
        body["timestamp"] = str(ts)
        body["sign"] = feishu_sign(FEISHU_SECRET, ts)
    with httpx.Client(timeout=15.0) as cli:
        r = cli.post(FEISHU_WEBHOOK, json=body)
        r.raise_for_status()
        log.info("webhook push: HTTP %s body=%s", r.status_code, r.text[:240])


# --------- Mode B: self-built app via IM API ---------------------------------

_token_cache: dict = {"token": "", "expire_at": 0.0}


def get_tenant_access_token() -> str:
    """Exchange app credentials for a 2h tenant_access_token. Cached in-process."""
    now = time.time()
    if _token_cache["token"] and now < _token_cache["expire_at"] - 60:
        return _token_cache["token"]

    url = f"{FEISHU_OPEN_HOST}/open-apis/auth/v3/tenant_access_token/internal"
    with httpx.Client(timeout=15.0) as cli:
        r = cli.post(url, json={
            "app_id": FEISHU_APP_ID,
            "app_secret": FEISHU_APP_SECRET,
        })
        r.raise_for_status()
        data = r.json()
    if data.get("code") != 0:
        raise RuntimeError(f"tenant_access_token error: {data}")
    _token_cache["token"] = data["tenant_access_token"]
    _token_cache["expire_at"] = now + int(data.get("expire", 7200))
    return _token_cache["token"]


def send_via_im_api(card_body: dict) -> None:
    """POST to im/v1/messages with the card body JSON-stringified into `content`.

    receive_id_type defaults to chat_id; override via FEISHU_RECEIVE_ID_TYPE
    (open_id / user_id / union_id / email / chat_id).
    """
    token = get_tenant_access_token()
    url = (f"{FEISHU_OPEN_HOST}/open-apis/im/v1/messages"
           f"?receive_id_type={FEISHU_RECEIVE_ID_TYPE}")
    payload = {
        "receive_id": FEISHU_CHAT_ID,
        "msg_type": "interactive",
        "content": json.dumps(card_body, ensure_ascii=False),  # MUST be a string
    }
    with httpx.Client(timeout=15.0) as cli:
        r = cli.post(url, json=payload, headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        })
    # Feishu returns a useful {code,msg} body even on HTTP 400 — read it before
    # raising so the failure is diagnosable (wrong chat_id / bot not in chat /
    # missing permission all surface here with distinct codes).
    try:
        data = r.json()
    except Exception:
        data = {"_raw": r.text[:500]}
    if r.status_code >= 400 or data.get("code") not in (0, None):
        raise RuntimeError(
            f"im/v1/messages failed: HTTP {r.status_code} "
            f"code={data.get('code')} msg={data.get('msg')!r} "
            f"(receive_id={FEISHU_CHAT_ID!r} type={FEISHU_RECEIVE_ID_TYPE!r}) "
            f"full={data}"
        )
    msg_id = (data.get("data") or {}).get("message_id", "?")
    log.info("im-api push: message_id=%s", msg_id)


# --------- Dispatch ----------------------------------------------------------

def dispatch(card_body: dict) -> None:
    """Pick a transport based on which env vars are populated.
    Order of preference: IM API (more reliable for app integrations) > webhook."""
    if have_im_api_creds():
        send_via_im_api(card_body)
        return
    if FEISHU_WEBHOOK:
        send_via_webhook(card_body)
        return
    log.warning("no feishu transport configured (set FEISHU_APP_ID+SECRET+CHAT_ID "
                "or FEISHU_WEBHOOK) — skipping push")


# --------- Existing helpers --------------------------------------------------

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


def main():
    papers = load_today_papers()
    if not papers:
        log.info("no papers today")
        if env_str("PUSH_EMPTY_DAY", "0") == "1":
            dispatch(build_empty_day_body())
        return

    chunks = [papers[i:i + PAPERS_PER_CARD] for i in range(0, len(papers), PAPERS_PER_CARD)]
    for i, chunk in enumerate(chunks):
        dispatch(build_card_body(chunk, i, len(chunks)))
        if i < len(chunks) - 1:
            time.sleep(1)
    log.info("pushed %d papers in %d card(s) via %s",
             len(papers), len(chunks),
             "im-api" if have_im_api_creds() else "webhook" if FEISHU_WEBHOOK else "none")


if __name__ == "__main__":
    main()
