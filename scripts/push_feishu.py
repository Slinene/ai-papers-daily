"""Stage 4: push ONE polished Feishu card (news first, then papers) to one or
more groups.

Transports (auto-detected; IM API preferred):
  A. Custom group bot webhook  — FEISHU_WEBHOOK [+ FEISHU_SECRET]
  B. Self-built app via IM API — FEISHU_APP_ID + FEISHU_APP_SECRET + FEISHU_CHAT_ID

Multi-target: FEISHU_CHAT_ID / FEISHU_WEBHOOK may be comma-separated to fan
the same card out to several groups.

Card design goals: single scannable card, news section then papers section,
clean typography, site link footer — newsletter/commercial look.
"""
from __future__ import annotations

import base64
import hashlib
import hmac
import json
import re
import time

import httpx
import yaml

from common import (
    CACHE_DIR,
    PAPERS_DIR,
    env_float,
    env_str,
    log,
    now_iso_date,
    read_json,
)

# Mode A
FEISHU_WEBHOOK = env_str("FEISHU_WEBHOOK")
FEISHU_SECRET = env_str("FEISHU_SECRET")
# Mode B
FEISHU_APP_ID = env_str("FEISHU_APP_ID")
FEISHU_APP_SECRET = env_str("FEISHU_APP_SECRET")
FEISHU_CHAT_ID = env_str("FEISHU_CHAT_ID")
FEISHU_RECEIVE_ID_TYPE = env_str("FEISHU_RECEIVE_ID_TYPE", "chat_id")
FEISHU_OPEN_HOST = env_str("FEISHU_OPEN_HOST", "https://open.feishu.cn").rstrip("/")

SITE_URL = env_str("SITE_URL", "https://slinene.github.io").rstrip("/")
BASE_PATH = env_str("BASE_PATH", "/ai-papers-daily").strip("/")
SITE_BASE = f"{SITE_URL}/{BASE_PATH}" if BASE_PATH else SITE_URL

# How many of each to show in the single card (keeps it scannable)
NEWS_IN_CARD = 8
REPOS_IN_CARD = 6
PAPERS_IN_CARD = 6
NEWS_SUMMARY_MAX = 76
HEADER_TEMPLATE = env_str("FEISHU_CARD_TEMPLATE", "indigo")


def _split(v: str) -> list[str]:
    return [x.strip() for x in (v or "").split(",") if x.strip()]


def have_im_api_creds() -> bool:
    return bool(FEISHU_APP_ID and FEISHU_APP_SECRET and FEISHU_CHAT_ID)


def _clip(s: str, n: int) -> str:
    s = (s or "").strip().replace("\n", " ")
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def _src_label(s: str) -> str:
    if s == "hn":
        return "HN"
    if s.startswith("reddit:"):
        return "r/" + s[7:]
    if s.startswith("cn:"):
        return s[3:]
    if s.startswith("blog:"):
        return s[5:]
    return s


# --------- data loaders ------------------------------------------------------

def estimate_cost_cny() -> tuple[float, int]:
    """Approximate this run's DeepSeek spend in RMB from .cache/usage.json.
    Rates are 元 / 1M tokens, env-configurable (DeepSeek V4 pricing changes;
    tune PRICE_* repo vars to match your real bill). Returns (cny, tokens)."""
    usage = read_json(CACHE_DIR / "usage.json") or {}
    rates = {
        "pro":   (env_float("PRICE_PRO_IN", 2.0),   env_float("PRICE_PRO_OUT", 8.0)),
        "flash": (env_float("PRICE_FLASH_IN", 0.5), env_float("PRICE_FLASH_OUT", 2.0)),
    }
    total = 0.0
    tokens = 0
    for model, u in usage.items():
        tier = "flash" if "flash" in (model or "").lower() else "pro"
        in_rate, out_rate = rates[tier]
        pin = int(u.get("prompt_tokens") or 0)
        pout = int(u.get("completion_tokens") or 0)
        total += pin / 1_000_000 * in_rate
        total += pout / 1_000_000 * out_rate
        tokens += pin + pout
    return total, tokens


def load_today_news() -> list[dict]:
    d = read_json(CACHE_DIR / "processed_news.json") or {}
    return d.get("topics") or []


def load_today_repos() -> list[dict]:
    d = read_json(CACHE_DIR / "processed_repos.json") or {}
    return d.get("repos") or []


def load_today_papers() -> list[dict]:
    summary = read_json(CACHE_DIR / "today_papers.json")
    if not summary:
        return []
    out: list[dict] = []
    for fname in summary.get("wrote", []):
        path = PAPERS_DIR / fname
        if not path.exists():
            continue
        parts = path.read_text(encoding="utf-8").split("---", 2)
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


# --------- the single combined card -----------------------------------------

def build_card_body(news: list[dict], repos: list[dict], papers: list[dict]) -> dict:
    today = now_iso_date()
    news = news[:NEWS_IN_CARD]
    repos = repos[:REPOS_IN_CARD]
    papers = papers[:PAPERS_IN_CARD]

    elements: list[dict] = []

    # ---- News section ----
    if news:
        elements.append({
            "tag": "markdown",
            "content": "**🗞️  今日 AI 行业动态**",
        })
        elements.append({"tag": "hr"})
        for i, t in enumerate(news, 1):
            title = t.get("title", "").strip()
            srcs = t.get("sources") or []
            url = srcs[0]["url"] if srcs else ""
            head = f"**{i}. [{title}]({url})**" if url else f"**{i}. {title}**"
            summary = _clip(t.get("summary", ""), NEWS_SUMMARY_MAX)
            tags = t.get("tags") or []
            chips = "  ".join(f"`{x}`" for x in tags[:3])
            srcline = ""
            if srcs:
                s0 = srcs[0]
                pts = f" · {s0['points']}↑" if s0.get("points") else ""
                srcline = f"  ·  {_src_label(s0.get('source',''))}{pts}"
            body = f"{head}\n{summary}\n{chips}{srcline}"
            elements.append({"tag": "markdown", "content": body})

    # ---- Hot repos section ----
    if repos:
        if news:
            elements.append({"tag": "hr"})
        elements.append({"tag": "markdown", "content": "**💻  今日热门 AI 项目**"})
        elements.append({"tag": "hr"})
        for i, r in enumerate(repos, 1):
            name = r.get("name", "").strip()
            url = r.get("url", f"https://github.com/{name}")
            stars = int(r.get("stars") or 0)
            star_s = f"{stars/1000:.1f}".rstrip("0").rstrip(".") + "k" if stars >= 1000 else str(stars)
            one = _clip(r.get("one_liner", ""), 60)
            tags = r.get("tags") or []
            chips = "  ".join(f"`{x}`" for x in tags[:3])
            # top borrow-value point
            val = r.get("value") or ""
            pts = [
                _clip(re.sub(r"^\s*[-*•]\s*", "", ln).replace("**", "").replace("`", ""), 60)
                for ln in val.splitlines() if ln.strip()
            ][:2]
            vblock = ("\n" + "\n".join(f"　▸ {x}" for x in pts)) if pts else ""
            elements.append({
                "tag": "markdown",
                "content": f"**{i}. [{name}]({url})**  ★{star_s}\n{one}{vblock}\n{chips}",
            })

    # ---- Papers section ----
    if papers:
        if news or repos:
            elements.append({"tag": "hr"})
        elements.append({
            "tag": "markdown",
            "content": "**📄  今日精选论文**",
        })
        elements.append({"tag": "hr"})
        for i, p in enumerate(papers, 1):
            title = p.get("title", "").strip()
            slug = p.get("_slug", "")
            site_url = f"{SITE_BASE}/paper/{slug}" if slug else SITE_BASE
            star = " ⭐" if p.get("depth") == "full_pdf" else ""
            cat = p.get("category", "")
            direction = (p.get("direction") or cat).strip()
            score = int(p.get("score", 0))
            tags = p.get("tags") or []
            chips = "  ".join(f"`{x}`" for x in tags[:3])
            one = _clip(p.get("one_liner", ""), 90)
            head = f"**{i}. [{title}]({site_url})**{star}"
            dirline = f"🧭 {direction}  ·  {score}/10"
            # top 2 actionable points, clipped
            pv = p.get("practical_value") or ""
            pv_pts = [
                _clip(re.sub(r"^\s*[-*•]\s*", "", ln).replace("**", "").replace("`", ""), 60)
                for ln in pv.splitlines() if ln.strip()
            ][:2]
            pv_block = ("\n" + "\n".join(f"　▸ {x}" for x in pv_pts)) if pv_pts else ""
            elements.append({
                "tag": "markdown",
                "content": f"{head}\n{dirline}\n{one}{pv_block}\n{chips}",
            })

    if not elements:
        elements.append({
            "tag": "markdown",
            "content": "今日没有新内容进入榜单。",
        })

    # ---- footer: site link + this run's LLM cost ----
    cost_cny, tok = estimate_cost_cny()
    cost_line = ""
    if tok > 0:
        cost_line = f"   ·   💰 本次消息耗费 ≈ ¥{cost_cny:.3f}（{tok:,} tokens，估算）"
    elements.append({"tag": "hr"})
    elements.append({
        "tag": "note",
        "elements": [{
            "tag": "lark_md",
            "content": f"🔗 [打开完整站点 · 论文沉淀 · 历史归档]({SITE_BASE}/)"
                       f"   ·   每日 09:00 自动更新{cost_line}",
        }],
    })

    return {
        "config": {"wide_screen_mode": True},
        "header": {
            "title": {"tag": "plain_text", "content": f"📡 AI Radar Daily · {today}"},
            "subtitle": {"tag": "plain_text",
                         "content": f"{len(news)} 行业动态 · {len(repos)} 热门项目 · {len(papers)} 精选论文"},
            "template": HEADER_TEMPLATE,
        },
        "elements": elements,
    }


# --------- transports --------------------------------------------------------

def feishu_sign(secret: str, ts: int) -> str:
    key = f"{ts}\n{secret}".encode("utf-8")
    digest = hmac.new(key, b"", digestmod=hashlib.sha256).digest()
    return base64.b64encode(digest).decode("utf-8")


def send_via_webhook(card_body: dict, webhook: str) -> None:
    body: dict = {"msg_type": "interactive", "card": card_body}
    if FEISHU_SECRET:
        ts = int(time.time())
        body["timestamp"] = str(ts)
        body["sign"] = feishu_sign(FEISHU_SECRET, ts)
    with httpx.Client(timeout=15.0) as cli:
        r = cli.post(webhook, json=body)
    try:
        data = r.json()
    except Exception:
        data = {"_raw": r.text[:300]}
    if r.status_code >= 400 or data.get("code") not in (0, None):
        raise RuntimeError(f"webhook failed: HTTP {r.status_code} {data}")
    log.info("webhook push ok -> %s", webhook[-12:])


_token_cache: dict = {"token": "", "expire_at": 0.0}


def get_tenant_access_token() -> str:
    now = time.time()
    if _token_cache["token"] and now < _token_cache["expire_at"] - 60:
        return _token_cache["token"]
    url = f"{FEISHU_OPEN_HOST}/open-apis/auth/v3/tenant_access_token/internal"
    with httpx.Client(timeout=15.0) as cli:
        r = cli.post(url, json={"app_id": FEISHU_APP_ID, "app_secret": FEISHU_APP_SECRET})
        r.raise_for_status()
        data = r.json()
    if data.get("code") != 0:
        raise RuntimeError(f"tenant_access_token error: {data}")
    _token_cache["token"] = data["tenant_access_token"]
    _token_cache["expire_at"] = now + int(data.get("expire", 7200))
    return _token_cache["token"]


def send_via_im_api(card_body: dict, chat_id: str) -> None:
    token = get_tenant_access_token()
    url = (f"{FEISHU_OPEN_HOST}/open-apis/im/v1/messages"
           f"?receive_id_type={FEISHU_RECEIVE_ID_TYPE}")
    payload = {
        "receive_id": chat_id,
        "msg_type": "interactive",
        "content": json.dumps(card_body, ensure_ascii=False),
    }
    with httpx.Client(timeout=15.0) as cli:
        r = cli.post(url, json=payload, headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        })
    try:
        data = r.json()
    except Exception:
        data = {"_raw": r.text[:500]}
    if r.status_code >= 400 or data.get("code") not in (0, None):
        raise RuntimeError(
            f"im/v1/messages failed: HTTP {r.status_code} code={data.get('code')} "
            f"msg={data.get('msg')!r} (receive_id={chat_id!r} "
            f"type={FEISHU_RECEIVE_ID_TYPE!r}) full={data}")
    msg_id = (data.get("data") or {}).get("message_id", "?")
    log.info("im-api push ok -> chat=%s msg=%s", chat_id, msg_id)


def dispatch(card_body: dict) -> None:
    """Fan the card out to every configured target. One target failing logs
    but does not stop the others."""
    sent = 0
    errors: list[str] = []

    if have_im_api_creds():
        for cid in _split(FEISHU_CHAT_ID):
            try:
                send_via_im_api(card_body, cid)
                sent += 1
            except Exception as exc:
                errors.append(f"chat {cid}: {exc}")
    elif FEISHU_WEBHOOK:
        for wh in _split(FEISHU_WEBHOOK):
            try:
                send_via_webhook(card_body, wh)
                sent += 1
            except Exception as exc:
                errors.append(f"webhook …{wh[-12:]}: {exc}")
    else:
        log.warning("no feishu transport configured — skipping push")
        return

    log.info("feishu: %d sent, %d failed", sent, len(errors))
    if errors:
        # surface but don't crash the (already non-fatal) step
        for e in errors:
            log.error("feishu target failed: %s", e)
        if sent == 0:
            raise RuntimeError(f"all {len(errors)} feishu target(s) failed; "
                               f"first: {errors[0]}")


def main():
    news = load_today_news()
    repos = load_today_repos()
    papers = load_today_papers()
    if not news and not papers and not repos:
        log.info("no news, repos or papers today")
        if env_str("PUSH_EMPTY_DAY", "0") == "1":
            dispatch(build_card_body([], [], []))
        return
    dispatch(build_card_body(news, repos, papers))
    log.info("pushed combined card: %d news + %d repos + %d papers",
             min(len(news), NEWS_IN_CARD), min(len(repos), REPOS_IN_CARD),
             min(len(papers), PAPERS_IN_CARD))


if __name__ == "__main__":
    main()
