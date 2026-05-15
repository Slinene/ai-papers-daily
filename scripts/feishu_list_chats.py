"""Diagnostic: list the Feishu groups the bot (app) is a member of, with their
real OpenAPI chat_id (oc_xxx). Run this ONCE locally to discover the value to
put in the FEISHU_CHAT_ID GitHub secret.

The IM API's receive_id_type=chat_id expects the `oc_...` open_chat_id, NOT
the numeric id you see in a group's link/UI. This script fetches the correct
one for every chat the bot can see.

Usage (from ai-papers-daily/, with .env containing FEISHU_APP_ID/SECRET):
  .venv/bin/python scripts/feishu_list_chats.py

Prereq: the app must be added to the target group first
(群设置 → 群机器人 → 添加机器人 → 选你的应用).
"""
from __future__ import annotations

import httpx

from common import env_str

APP_ID = env_str("FEISHU_APP_ID")
APP_SECRET = env_str("FEISHU_APP_SECRET")
HOST = env_str("FEISHU_OPEN_HOST", "https://open.feishu.cn").rstrip("/")

if not (APP_ID and APP_SECRET):
    raise SystemExit("need FEISHU_APP_ID + FEISHU_APP_SECRET in env/.env")


def token() -> str:
    r = httpx.post(f"{HOST}/open-apis/auth/v3/tenant_access_token/internal",
                   json={"app_id": APP_ID, "app_secret": APP_SECRET}, timeout=15)
    r.raise_for_status()
    d = r.json()
    if d.get("code") != 0:
        raise SystemExit(f"token error: {d}")
    return d["tenant_access_token"]


def main():
    tok = token()
    page = ""
    found = 0
    print("groups the bot is in (use the chat_id column for FEISHU_CHAT_ID):\n")
    print(f"{'chat_id (oc_...)':<40}  name")
    print("-" * 70)
    while True:
        params = {"page_size": 100}
        if page:
            params["page_token"] = page
        r = httpx.get(f"{HOST}/open-apis/im/v1/chats", params=params,
                      headers={"Authorization": f"Bearer {tok}"}, timeout=15)
        r.raise_for_status()
        d = r.json()
        if d.get("code") != 0:
            raise SystemExit(f"list chats error: {d}")
        data = d.get("data") or {}
        for c in data.get("items", []):
            found += 1
            print(f"{c.get('chat_id',''):<40}  {c.get('name','(no name)')}")
        if data.get("has_more") and data.get("page_token"):
            page = data["page_token"]
        else:
            break
    if found == 0:
        print("(none — the app is not in any group. "
              "Add it: 群设置 → 群机器人 → 添加机器人 → 选你的应用)")
    print(f"\ntotal: {found} group(s)")


if __name__ == "__main__":
    main()
