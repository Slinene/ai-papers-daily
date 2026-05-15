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

from common import CACHE_DIR, env_int, env_str, log, read_json, write_json

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

RELEVANCE_SYSTEM = """你是一位 AI 论文领域专家。根据论文标题和摘要给一个 0-10 的相关性分数。

读者最关心的子方向（10 分必读）：
- 推荐系统 × LLM 交叉：
  * Generative Recommendation（生成式推荐 / next-item generation）
  * Semantic ID / Token-based RecSys / RQ-VAE for items
  * Agentic Recommendation（推荐场景里的 LLM Agent / planning / tool-use）
  * LLM4Rec / LLM-as-Ranker / LLM-as-Reranker / Cold-start with LLM
  * User Simulation 用 LLM 模拟用户 / RL-from-LLM-feedback
  * 多模态 / 多兴趣 / 序列推荐 中用 LLM
- 大语言模型核心：训练 / 对齐 / 推理 / Long-context / MoE / Distill / 量化

8-9 分核心方向：
- Agent / Tool-use / Memory / Planning（通用 Agent，非推荐场景）
- RAG / Retrieval / Reasoning（通用）
- 评估、可靠性、效率（system-level）
- 经典推荐系统 / 排序 / 召回（不含 LLM）但有显著创新

6-7 分相关：
- AI/ML 其他主流方向；视觉/语音如不结合 LLM 通常封顶 6
- 偏工程或增量

3-5 分：沾边但非主流方向
0-2 分：与读者方向无关

只输出 JSON，结构：
{"score": <0-10 整数>, "reasoning": "<不超过 120 字的中文一句话理由>"}"""

SUMMARY_SYSTEM = """你是一位 AI 论文解读专家，为读者撰写中文论文卡片。

风格要求：
- 直接、信息密度高，不要套话
- 术语保留英文（如 LoRA、RAG、KV cache、MoE）
- 不重复原标题；不要"本文提出了 / 本研究表明"
- summary_md 用 markdown，结构：动机 → 方法关键点 → 关键结果数字

只输出 JSON，结构：
{
  "title_zh":     "<论文标题的中文翻译，简洁，<= 50 字>",
  "one_liner":    "<一句话核心贡献，<= 60 字，不带句号>",
  "category":     "<单选: LLM | RecSys | Agent | RAG | Eval | Training | Multimodal | Reasoning | Other>",
  "tags":         ["<3-6 个英文标签，如 RecSys、LLM、MoE、RAG、Distill、RLHF、Eval>"],
  "affiliations": ["<作者所属机构，最多 5 个，例如 MIT、Google DeepMind、Anthropic、清华大学；abstract 模式下若无法确认则留空数组 []>"],
  "summary_md":   "<markdown 正文>"
}"""


class Relevance(BaseModel):
    score: int = Field(ge=0, le=10)
    reasoning: str = Field(max_length=200)


class Summary(BaseModel):
    title_zh: str
    one_liner: str = Field(max_length=120)
    category: str
    tags: list[str] = Field(min_length=1, max_length=8)
    affiliations: list[str] = Field(default_factory=list, max_length=8)
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
            "tags": summary.tags or [],
            "one_liner": summary.one_liner,
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
