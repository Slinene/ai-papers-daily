"""Stage 2: filter relevance + summarize using DeepSeek (OpenAI-compatible).

Reads .cache/raw_papers.json -> writes .cache/processed_papers.json.

Pipeline per paper (single model, varying input/output size):
  1. Relevance score (0-10) from title+abstract — cheap, short.
  2. If score >= MIN_SCORE_KEEP, write a card from the abstract.
  3. If score >= MIN_SCORE_DEEP, download the PDF, extract text with pypdf,
     and write a deeper card with the extracted full text in context.

DeepSeek API is OpenAI-compatible; we use the openai SDK with base_url
overridden. PDFs are not natively supported — text is extracted locally.
Structured output uses response_format={"type":"json_object"} plus
Pydantic validation (since strict json_schema isn't guaranteed on
non-OpenAI endpoints).
"""
from __future__ import annotations

import io
import json
import os
import time
from typing import Type, TypeVar

import httpx
from openai import OpenAI, OpenAIError
from pydantic import BaseModel, Field, ValidationError
from pypdf import PdfReader

from common import (
    CACHE_DIR,
    add_usage,
    env_int,
    env_str,
    log,
    read_json,
    reset_usage,
    write_json,
)

DEEPSEEK_API_KEY = env_str("DEEPSEEK_API_KEY")
if not DEEPSEEK_API_KEY:
    raise SystemExit("DEEPSEEK_API_KEY env var is required")

DEEPSEEK_BASE_URL = env_str("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
# Two-tier model strategy:
#   SCORE_MODEL — wide funnel, every candidate scored; use light/fast model
#   SUMMARY_MODEL — narrow output (~MAX_PAPERS_PER_DAY calls); use pro
# Both fall back to DEEPSEEK_MODEL for back-compat.
DEEPSEEK_MODEL = env_str("DEEPSEEK_MODEL", "deepseek-v4-pro")
DEEPSEEK_SCORE_MODEL = env_str("DEEPSEEK_SCORE_MODEL", "deepseek-v4-flash")
DEEPSEEK_SUMMARY_MODEL = env_str("DEEPSEEK_SUMMARY_MODEL", DEEPSEEK_MODEL)

MIN_SCORE_KEEP = env_int("MIN_SCORE_KEEP", 7)
MIN_SCORE_DEEP = env_int("MIN_SCORE_DEEP", 8)
MAX_PAPERS_PER_DAY = env_int("MAX_PAPERS_PER_DAY", 30)
PDF_TEXT_MAX_CHARS = env_int("PDF_TEXT_MAX_CHARS", 60000)

client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL,
    timeout=httpx.Timeout(120.0, connect=15.0),
    max_retries=2,
)

RELEVANCE_SYSTEM = """你是一位 AI 论文领域专家。读者是一名 **AI 算法从业者**，专注：
电商场景 AI / Agent 多智体优化 / 用 Agent 优化电商链路 / 生成式推荐。
他看论文是为了**找能迁移进业务、提升工作效率的方法**，不是学术兴趣。

按对这个读者的实用价值打 0-10 分。

10 分必读（直接命中其业务）：
- 生成式推荐 Generative Recommendation / Semantic ID / RQ-VAE for items / LLM4Rec
- Agentic Recommendation（推荐/搜索/营销场景里的 LLM Agent、planning、tool-use）
- 电商场景 AI（搜推广、用户建模、营销、履约、商品理解）+ LLM/Agent
- Multi-Agent 优化 / 协作 / self-evolution，且方法可迁移到推荐或电商
- LLM-as-Ranker / Reranker / Cold-start / User Simulation 用于推荐

8-9 分核心：
- 通用 Agent / Tool-use / Memory / Planning（方法可借鉴到上面场景）
- 大语言模型核心：训练 / 对齐 / 推理 / Long-context / MoE / Distill / 量化
- RAG / Retrieval / Reasoning（通用）
- 经典推荐 / 排序 / 召回有显著创新

6-7 分：AI/ML 其他主流方向；视觉/语音不结合 LLM 封顶 6
3-5 分：沾边非主流；0-2 分：与读者业务无关

只输出 JSON：
{"score": <0-10 整数>, "reasoning": "<不超过 120 字，点明对电商/Agent/生成式推荐业务的价值>"}"""

SUMMARY_SYSTEM = """你是一位 AI 论文解读专家。读者是 **专注电商 / Agent 多智体优化 / 生成式推荐的 AI 算法从业者**，
看论文是为了把有用的东西迁移进业务。为他写一张中文论文卡片。

风格要求：
- 直接、信息密度高，不要套话；术语保留英文（LoRA、RAG、KV cache、MoE、Semantic ID）
- 不重复原标题；不要"本文提出了 / 本研究表明"
- summary_md 用 markdown：动机 → 方法关键点 → 关键结果数字
- practical_value 是重点：站在电商/推荐/Agent 从业者角度，写 2-4 条
  「可以怎么借鉴到工作里」——具体到方法 trick、架构选择、工程实现、能复用的结论；
  没有可迁移价值就直说"主要是学术贡献，业务可借鉴点有限"

只输出 JSON，结构：
{
  "title_zh":       "<论文标题的中文翻译，简洁，<= 50 字>",
  "one_liner":      "<一句话核心贡献，<= 60 字，不带句号>",
  "category":       "<单选: GenRec | RecSys | Agent | MultiAgent | LLM | RAG | Eval | Training | Multimodal | Reasoning | Other>",
  "direction":      "<一句话方向归属，<= 24 字，例如 '生成式推荐 · Semantic ID' 或 'Agent 多智体协作优化'>",
  "tags":           ["<3-6 个英文标签>"],
  "affiliations":   ["<作者机构，最多 5 个；abstract 模式无法确认则 []>"],
  "practical_value":"<markdown，2-4 条 '- ' 列表，面向电商/Agent/生成式推荐从业者的可借鉴点>",
  "summary_md":     "<markdown 正文：动机/方法/结果>"
}"""


class Relevance(BaseModel):
    score: int = Field(ge=0, le=10)
    reasoning: str = Field(max_length=200)


class Summary(BaseModel):
    title_zh: str
    one_liner: str = Field(max_length=120)
    category: str
    direction: str = Field(default="", max_length=60)
    tags: list[str] = Field(min_length=1, max_length=8)
    affiliations: list[str] = Field(default_factory=list, max_length=8)
    practical_value: str = Field(default="")
    summary_md: str


T = TypeVar("T", bound=BaseModel)


def _strip_surrogates(s: str) -> str:
    """pypdf can emit lone UTF-16 surrogates (math glyphs like 𝐀 in U+1D400),
    which make json/utf-8 encoding of the API request body raise
    UnicodeEncodeError. Replace any unencodable code points."""
    if not s:
        return s
    return s.encode("utf-8", "replace").decode("utf-8")


def _short_authors(p: dict) -> str:
    a = p.get("authors") or []
    head = ", ".join(a[:5])
    return head + (" 等" if len(a) > 5 else "")


def _call_json(
    system: str,
    user: str,
    schema: Type[T],
    *,
    model: str = "",
    max_tokens: int = 2000,
    label: str = "",
) -> T | None:
    """One round-trip to DeepSeek that demands a JSON object and validates it
    against the given Pydantic schema. Retries once on parse/validation error
    with an explicit "must be JSON only" reminder."""
    model = model or DEEPSEEK_SUMMARY_MODEL
    # Single chokepoint for every LLM call (score / abstract / deep) — strip
    # surrogates so the OpenAI SDK can UTF-8 encode the request body.
    messages = [
        {"role": "system", "content": _strip_surrogates(system)},
        {"role": "user", "content": _strip_surrogates(user)},
    ]
    for attempt in range(2):
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=messages,
                response_format={"type": "json_object"},
                temperature=0.2,
                max_tokens=max_tokens,
            )
        except OpenAIError as exc:
            log.warning("[%s] api error attempt=%d: %s", label, attempt, exc)
            return None
        add_usage(model, getattr(resp, "usage", None))
        text = (resp.choices[0].message.content or "").strip()
        try:
            return schema.model_validate_json(text)
        except (ValidationError, json.JSONDecodeError) as exc:
            log.warning("[%s] parse failed attempt=%d: %s | text=%.200s",
                        label, attempt, exc, text)
            messages.append({"role": "assistant", "content": text})
            messages.append({"role": "user",
                             "content": "上次返回不是有效 JSON 或字段不符合。请只返回一个 JSON 对象，不要加任何前后说明。"})
    return None


def score_relevance(paper: dict) -> Relevance | None:
    user = f"标题: {paper['title']}\n\n摘要:\n{paper['abstract'][:2500]}"
    # Score path uses the cheaper/faster model (flash). Pro's deep reasoning
    # chain made 19 candidates take ~45 min — overkill for a 0-10 score.
    return _call_json(
        RELEVANCE_SYSTEM, user, Relevance,
        model=DEEPSEEK_SCORE_MODEL,
        max_tokens=1500,
        label=f"score:{paper['arxiv_id']}",
    )


def summarize_abstract(paper: dict) -> Summary | None:
    user = (
        f"标题: {paper['title']}\n"
        f"作者: {_short_authors(paper)}\n\n"
        f"摘要:\n{paper['abstract']}\n\n"
        f"请基于以上信息写卡片。summary_md 200-450 字。"
    )
    return _call_json(
        SUMMARY_SYSTEM, user, Summary,
        max_tokens=4000, label=f"abs:{paper['arxiv_id']}",
    )


def _fetch_pdf(url: str) -> bytes | None:
    try:
        with httpx.Client(timeout=60.0, follow_redirects=True) as cli:
            r = cli.get(url, headers={"User-Agent": "ai-papers-daily/0.1"})
            r.raise_for_status()
            return r.content
    except Exception as exc:
        log.warning("pdf fetch failed %s: %s", url, exc)
        return None


def _extract_pdf_text(pdf_bytes: bytes, max_chars: int) -> str:
    """Pull plain text out of an arXiv PDF page by page until max_chars hit.
    Returns empty string if the PDF is unreadable or scanned-only."""
    try:
        reader = PdfReader(io.BytesIO(pdf_bytes))
    except Exception as exc:
        log.warning("pdf parse failed: %s", exc)
        return ""
    parts: list[str] = []
    used = 0
    for page in reader.pages:
        try:
            t = page.extract_text() or ""
        except Exception:
            continue
        if not t:
            continue
        parts.append(t)
        used += len(t)
        if used >= max_chars:
            break
    text = "\n\n".join(parts)
    return _strip_surrogates(text[:max_chars])


def summarize_with_pdf(paper: dict) -> Summary | None:
    pdf_url = paper.get("pdf_url")
    if not pdf_url:
        return None
    pdf_bytes = _fetch_pdf(pdf_url)
    if not pdf_bytes:
        return None
    text = _extract_pdf_text(pdf_bytes, PDF_TEXT_MAX_CHARS)
    if not text or len(text) < 500:
        log.info("pdf text too short or empty for %s, skip deep read",
                 paper["arxiv_id"])
        return None
    user = (
        f"以下是 arXiv 论文 {paper['arxiv_id']} 的正文文本（pypdf 抽取）。\n"
        f"标题: {paper['title']}\n"
        f"作者: {_short_authors(paper)}\n\n"
        f"正文（截断到 {PDF_TEXT_MAX_CHARS} 字符）:\n"
        f"-----\n{text}\n-----\n\n"
        "请基于以上正文输出中文卡片。summary_md 写 400-800 字，要求：\n"
        "1) 一段动机：为什么这个问题值得做\n"
        "2) 方法关键点：模型/算法/数据的具体设计，列要点\n"
        "3) 关键实验：数据集、对比 baseline、最关键的几个数字\n"
        "4) 你认为最值得记住的一句话"
    )
    return _call_json(
        SUMMARY_SYSTEM, user, Summary,
        max_tokens=8000, label=f"deep:{paper['arxiv_id']}",
    )


def main():
    reset_usage()  # first LLM stage of the pipeline — start the cost tally fresh
    raws = read_json(CACHE_DIR / "raw_papers.json") or []
    log.info("processing %d raw papers via %s @ %s",
             len(raws), DEEPSEEK_MODEL, DEEPSEEK_BASE_URL)

    # Step 1: relevance scoring
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

    # Step 2: summarize. One bad paper must never abort the whole batch.
    processed: list[dict] = []
    for p in scored:
        depth = "abstract"
        summary: Summary | None = None
        try:
            if p["_score"] >= MIN_SCORE_DEEP:
                summary = summarize_with_pdf(p)
                if summary is not None:
                    depth = "full_pdf"
            if summary is None:
                summary = summarize_abstract(p)
        except Exception as exc:
            log.warning("summarize crashed for %s: %s — skipping",
                        p.get("arxiv_id"), exc)
            continue
        if summary is None:
            continue

        processed.append({
            "arxiv_id": p["arxiv_id"],
            "title": p["title"],                    # English original
            "title_zh": summary.title_zh,
            "authors": p.get("authors", []),
            "affiliations": summary.affiliations or [],
            "url": p["url"],
            "pdf_url": p.get("pdf_url"),
            "published": (p.get("published") or "")[:10],
            "category": summary.category or "Other",
            "direction": summary.direction or "",
            "tags": summary.tags or [],
            "one_liner": summary.one_liner,
            "practical_value": summary.practical_value or "",
            "summary_md": summary.summary_md,
            "score": p["_score"],
            "source": p.get("source", ""),
            "depth": depth,
        })
        time.sleep(0.3)

    write_json(CACHE_DIR / "processed_papers.json", processed)
    log.info("processed %d papers (deep=%d)",
             len(processed), sum(1 for x in processed if x["depth"] == "full_pdf"))


if __name__ == "__main__":
    main()
