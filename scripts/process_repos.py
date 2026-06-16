"""Stage 2c: filter + rank + summarize today's hot AI repos via DeepSeek.

Reads .cache/raw_repos.json -> writes .cache/processed_repos.json:
{
  "date": "...",
  "repos": [
    {name,url,stars,language,topics,one_liner,capability,value,tags}, ...
  ]
}

One LLM call: given repo metadata + README excerpts, pick the ones most
useful to the reader persona (e-commerce / Agent / generative recommendation
practitioner), rank, and for each write 项目能力 + 借鉴价值.
"""
from __future__ import annotations

import json
import os

from openai import OpenAI, OpenAIError
from pydantic import BaseModel, Field, ValidationError

from common import CACHE_DIR, add_usage, env_int, env_str, log, now_iso_date, read_json, write_json

DEEPSEEK_API_KEY = env_str("DEEPSEEK_API_KEY")
if not DEEPSEEK_API_KEY:
    raise SystemExit("DEEPSEEK_API_KEY env var is required")
DEEPSEEK_BASE_URL = env_str("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
DEEPSEEK_MODEL = env_str("DEEPSEEK_MODEL", "deepseek-v4-pro")

MAX_REPOS_OUT = env_int("REPOS_OUT_MAX", 8)
README_IN_CHARS = env_int("REPOS_README_IN_CHARS", 2200)

client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url=DEEPSEEK_BASE_URL,
                timeout=120, max_retries=2)

SYSTEM = """你是一位 AI 工程方向的技术选型分析师。读者是 **专注电商 / 广告 / 搜索推荐系统，
核心关注 Agent 与 LLM 结合搜索推荐系统的 AI 算法从业者**，他想知道今天 GitHub 上比较火的
AI 项目里，哪些对他的工作有借鉴价值。

给你一批仓库（含 star 数、描述、README 摘录）。请：
- 挑出对该读者最有价值的若干个（最多 N 个，N 见 user 消息），按价值排序
- 噪声 / 玩具 / 纯 demo / 跟其方向无关的丢弃
- 每个写：
  * one_liner：一句话这个项目是干嘛的（<= 40 字）
  * capability：项目实现了什么能力（2-4 句，具体到技术栈/架构/支持的场景）
  * value：对电商/Agent/生成式推荐从业者的借鉴价值，markdown '- ' 列表 2-3 条，
    具体到「可以直接用的组件 / 可借鉴的架构 / 能复用的实现思路」
  * tags：2-4 个英文标签

只输出 JSON：
{"repos":[{"name":"<owner/repo，原样照抄输入的 name>","one_liner":"...",
  "capability":"...","value":"<markdown>","tags":["..."]}]}"""


class RepoOut(BaseModel):
    # No hard length/size constraints — LLM length adherence is soft; reject-
    # and-retry on a 130-char one_liner just nukes the whole batch. Clip in
    # the output builder instead.
    name: str
    one_liner: str = ""
    capability: str = ""
    value: str = ""
    tags: list[str] = Field(default_factory=list)


class ReposResult(BaseModel):
    repos: list[RepoOut]


def main():
    raws = read_json(CACHE_DIR / "raw_repos.json") or []
    log.info("processing %d raw repos", len(raws))
    if not raws:
        write_json(CACHE_DIR / "processed_repos.json",
                   {"date": now_iso_date(), "repos": []})
        return

    by_name = {r["name"]: r for r in raws}
    lines = []
    for i, r in enumerate(raws):
        rm = (r.get("readme") or "").replace("\n", " ")[:README_IN_CHARS]
        lines.append(
            f"{i}. {r['name']}  ★{r.get('stars',0)}  "
            f"[{r.get('language','')}|{r.get('heat','')}]  "
            f"{r.get('description','')}\n   README: {rm}"
        )
    user = (
        f"最多挑 {MAX_REPOS_OUT} 个最有价值的。候选 {len(raws)} 个：\n\n"
        + "\n\n".join(lines)
        + "\n\n按要求输出 JSON。name 必须与输入完全一致。"
    )

    messages = [
        {"role": "system", "content": SYSTEM.replace("最多 N 个", f"最多 {MAX_REPOS_OUT} 个")},
        {"role": "user", "content": user.encode("utf-8", "replace").decode("utf-8")},
    ]
    result: ReposResult | None = None
    for attempt in range(2):
        try:
            resp = client.chat.completions.create(
                model=DEEPSEEK_MODEL, messages=messages,
                response_format={"type": "json_object"},
                temperature=0.3, max_tokens=8000,
            )
        except OpenAIError as exc:
            log.warning("repos llm error attempt=%d: %s", attempt, exc)
            break
        add_usage(DEEPSEEK_MODEL, getattr(resp, "usage", None))
        text = (resp.choices[0].message.content or "").strip()
        try:
            result = ReposResult.model_validate_json(text)
            break
        except (ValidationError, json.JSONDecodeError) as exc:
            log.warning("repos parse attempt=%d failed: %s | %.200s", attempt, exc, text)
            messages.append({"role": "assistant", "content": text})
            messages.append({"role": "user", "content": "只返回合法 JSON 对象。"})

    if result is None or not result.repos:
        log.warning("repos clustering failed; writing empty")
        write_json(CACHE_DIR / "processed_repos.json",
                   {"date": now_iso_date(), "repos": []})
        return

    out = []
    for r in result.repos[:MAX_REPOS_OUT]:
        src = by_name.get(r.name)
        if not src:
            continue
        ol = (r.one_liner or "").strip()
        out.append({
            "name": r.name,
            "url": src.get("url", f"https://github.com/{r.name}"),
            "stars": int(src.get("stars") or 0),
            "language": src.get("language", ""),
            "topics": (src.get("topics") or [])[:6],
            "one_liner": ol if len(ol) <= 120 else ol[:117].rstrip() + "…",
            "capability": (r.capability or "").strip(),
            "value": (r.value or "").strip(),
            "tags": [t for t in (r.tags or []) if isinstance(t, str)][:6],
        })
    write_json(CACHE_DIR / "processed_repos.json",
               {"date": now_iso_date(), "repos": out})
    log.info("kept %d repos", len(out))


if __name__ == "__main__":
    main()
