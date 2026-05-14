"""Stage 2: filter relevance + summarize.

Reads .cache/raw_papers.json -> writes .cache/processed_papers.json.

Pipeline per paper:
  1. Haiku 4.5 scores relevance (0-10) using a fixed system prompt.
  2. If score >= MIN_SCORE_KEEP, summarize from abstract (Haiku 4.5).
  3. If score >= MIN_SCORE_DEEP, additionally fetch PDF and let Sonnet 4.6
     produce a deeper read; if PDF fetch/parse fails, fall back to the abstract.

Cost model: Haiku for the wide funnel, Sonnet only on the top-scoring shortlist.
"""
from __future__ import annotations

import base64
import os
import time
from pathlib import Path

import anthropic
import httpx
from pydantic import BaseModel, Field

from common import CACHE_DIR, log, read_json, write_json

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
if not ANTHROPIC_API_KEY:
    raise SystemExit("ANTHROPIC_API_KEY env var is required")

MIN_SCORE_KEEP = int(os.environ.get("MIN_SCORE_KEEP", "7"))
MIN_SCORE_DEEP = int(os.environ.get("MIN_SCORE_DEEP", "8"))
MAX_PAPERS_PER_DAY = int(os.environ.get("MAX_PAPERS_PER_DAY", "30"))

HAIKU = "claude-haiku-4-5"
SONNET = "claude-sonnet-4-6"

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

RELEVANCE_SYSTEM = """你是一位 AI 论文领域专家。你需要根据论文标题和摘要对它做相关性打分。

读者关心的方向（从高到低）：
- 推荐系统 / 搜索 / 排序 / 召回 / 用户建模 + LLM 的交叉工作
- 大语言模型核心：训练、对齐、推理、上下文、MoE、Distill
- Agent / Tool-use / RAG / Memory / Planning
- 评估、解释性、可靠性、效率
- 多模态、Reasoning、Coding 等热门 AI 方向

打分标尺：
  10  推荐系统 + LLM 双重命中，或行业里程碑式工作
  8-9 上述方向的代表性 / 高质量工作
  6-7 同方向但偏增量或工程性
  3-5 沾边但非主流方向
  0-2 与读者关心的方向无关
"""


class Relevance(BaseModel):
    score: int = Field(ge=0, le=10)
    reasoning: str = Field(max_length=160)


SUMMARY_SYSTEM = """你是一位 AI 论文解读专家，为读者撰写中文论文卡片。

风格要求：
- 直接、信息密度高，不要套话
- 术语保留英文（如 LoRA、RAG、KV cache、MoE）
- 不重复原标题；不要"本文提出了 / 本研究表明"
- summary_md 用 markdown，结构：动机 → 方法关键点 → 关键结果数字

字段约束：
- title_zh: 论文标题的中文翻译，简洁，<= 50 字
- one_liner: 一句话核心贡献，<= 60 字，不带句号
- category: 单选: LLM | RecSys | Agent | RAG | Eval | Training | Multimodal | Reasoning | Other
- tags: 3-6 个英文标签（如 RecSys, LLM, MoE, RAG, Distill, RLHF, Eval）
"""


class Summary(BaseModel):
    title_zh: str
    one_liner: str = Field(max_length=120)
    category: str
    tags: list[str] = Field(min_length=1, max_length=8)
    summary_md: str


def _short_authors(p: dict) -> str:
    a = p.get("authors") or []
    head = ", ".join(a[:5])
    return head + (" 等" if len(a) > 5 else "")


def score_relevance(paper: dict) -> Relevance | None:
    user = f"标题: {paper['title']}\n\n摘要:\n{paper['abstract'][:2500]}"
    try:
        resp = client.messages.parse(
            model=HAIKU,
            max_tokens=400,
            system=RELEVANCE_SYSTEM,
            messages=[{"role": "user", "content": user}],
            output_format=Relevance,
        )
    except Exception as exc:
        log.warning("relevance failed %s: %s", paper["arxiv_id"], exc)
        return None
    return resp.parsed_output


def summarize_abstract(paper: dict) -> Summary | None:
    user = (
        f"标题: {paper['title']}\n"
        f"作者: {_short_authors(paper)}\n\n"
        f"摘要:\n{paper['abstract']}\n\n"
        f"请基于以上信息写卡片。summary_md 200-450 字。"
    )
    try:
        resp = client.messages.parse(
            model=HAIKU,
            max_tokens=2000,
            system=SUMMARY_SYSTEM,
            messages=[{"role": "user", "content": user}],
            output_format=Summary,
        )
    except Exception as exc:
        log.warning("abstract summary failed %s: %s", paper["arxiv_id"], exc)
        return None
    return resp.parsed_output


def _fetch_pdf(url: str) -> bytes | None:
    try:
        with httpx.Client(timeout=60.0, follow_redirects=True) as cli:
            r = cli.get(url, headers={"User-Agent": "ai-papers-daily/0.1"})
            r.raise_for_status()
            return r.content
    except Exception as exc:
        log.warning("pdf fetch failed %s: %s", url, exc)
        return None


def summarize_with_pdf(paper: dict) -> Summary | None:
    pdf_url = paper.get("pdf_url")
    if not pdf_url:
        return None
    pdf_bytes = _fetch_pdf(pdf_url)
    if not pdf_bytes:
        return None
    pdf_b64 = base64.standard_b64encode(pdf_bytes).decode("ascii")
    content = [
        {"type": "document",
         "source": {"type": "base64", "media_type": "application/pdf", "data": pdf_b64}},
        {"type": "text", "text": (
            f"以下是 arXiv 论文 {paper['arxiv_id']} 的 PDF 全文。\n"
            f"标题: {paper['title']}\n"
            f"作者: {_short_authors(paper)}\n\n"
            "请阅读后输出中文卡片。summary_md 写 400-800 字，要求：\n"
            "1) 一段动机：为什么这个问题值得做\n"
            "2) 方法关键点：模型/算法/数据的具体设计，列要点\n"
            "3) 关键实验：数据集、对比 baseline、最关键的几个数字\n"
            "4) 你认为最值得记住的一句话"
        )},
    ]
    try:
        resp = client.messages.parse(
            model=SONNET,
            max_tokens=4000,
            system=SUMMARY_SYSTEM,
            messages=[{"role": "user", "content": content}],
            output_format=Summary,
        )
    except Exception as exc:
        log.warning("pdf summary failed %s: %s", paper["arxiv_id"], exc)
        return None
    return resp.parsed_output


def main():
    raws = read_json(CACHE_DIR / "raw_papers.json") or []
    log.info("processing %d raw papers", len(raws))

    # Step 1: relevance scoring (all candidates)
    scored: list[dict] = []
    for p in raws:
        rel = score_relevance(p)
        if rel is None:
            continue
        if rel.score < MIN_SCORE_KEEP:
            continue
        p["_score"] = rel.score
        p["_score_reason"] = rel.reasoning
        scored.append(p)

    scored.sort(
        key=lambda x: (x["_score"], x.get("hf_upvotes", 0)),
        reverse=True,
    )
    scored = scored[:MAX_PAPERS_PER_DAY]
    log.info("kept %d after relevance filter", len(scored))

    # Step 2: summarize
    processed: list[dict] = []
    for p in scored:
        depth = "abstract"
        summary: Summary | None = None
        if p["_score"] >= MIN_SCORE_DEEP:
            summary = summarize_with_pdf(p)
            if summary is not None:
                depth = "full_pdf"
        if summary is None:
            summary = summarize_abstract(p)
        if summary is None:
            continue

        processed.append({
            "arxiv_id": p["arxiv_id"],
            "title": p["title"],
            "title_zh": summary.title_zh,
            "authors": p.get("authors", []),
            "url": p["url"],
            "pdf_url": p.get("pdf_url"),
            "published": (p.get("published") or "")[:10],
            "category": summary.category or "Other",
            "tags": summary.tags or [],
            "one_liner": summary.one_liner,
            "summary_md": summary.summary_md,
            "score": p["_score"],
            "source": p.get("source", ""),
            "depth": depth,
        })
        # be gentle on rate limits
        time.sleep(0.4)

    write_json(CACHE_DIR / "processed_papers.json", processed)
    log.info("processed %d papers (deep=%d)",
             len(processed), sum(1 for x in processed if x["depth"] == "full_pdf"))


if __name__ == "__main__":
    main()
