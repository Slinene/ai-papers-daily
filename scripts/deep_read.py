"""One-click deep-read: triggered by a GitHub issue, reads a paper's full text,
generates a 5-section reproducible deep analysis via DeepSeek, extracts best-effort
figures, and writes src/content/archive_papers/<topic>/<slug>.md (+ figures).

Inputs via env (set by the GitHub Action from the issue form):
  PAPER_URL        arxiv abs/pdf url (required)
  TOPIC            existing topic id, or "__new__"
  NEW_TOPIC_NAME   display name (if TOPIC == __new__)
  NEW_TOPIC_ICON   emoji (optional)

Writes the .md + figures. Prints a JSON line {slug, topic, ok} for the workflow.
Does NOT git. Reuses the DeepSeek (OpenAI-compatible) client like process.py.
"""
from __future__ import annotations
import io, json, os, re, subprocess, sys
from pathlib import Path

import feedparser
import httpx
from openai import OpenAI
from pypdf import PdfReader
from slugify import slugify as _slugify

ROOT = Path(__file__).resolve().parent.parent
ARCHIVE = ROOT / "src" / "content" / "archive_papers"
FIGROOT = ROOT / "public" / "figures"
FIG_BASE = "/ai-papers-daily/figures"  # GitHub Pages base prefix

# Canonical topics (id -> name, icon). New topics handled via env.
TOPICS = {
    "gen-rec": ("生成式推荐", "🎯"),
    "gen-search": ("生成式搜索", "🔎"),
    "agentic-rec": ("Agent推荐", "🧭"),
    "user-simulation": ("User Simulator", "👥"),
    "llm-general": ("LLM通用", "🧠"),
    "agent-general": ("Agent通用", "🤖"),
    "agent-auto-research": ("Agent Auto-Research", "🔬"),
}

DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "").strip()
DEEPSEEK_BASE_URL = os.environ.get("DEEPSEEK_BASE_URL", "").strip() or "https://api.deepseek.com"
DEEPSEEK_MODEL = os.environ.get("DEEPSEEK_MODEL", "").strip() or "deepseek-v4-pro"
PDF_MAX_CHARS = int(os.environ.get("DEEP_PDF_MAX_CHARS", "80000"))

client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url=DEEPSEEK_BASE_URL,
                timeout=httpx.Timeout(300.0, connect=15.0), max_retries=2)

SYSTEM = """你是论文深度解读专家，读者是 AI 算法工程师。读完整篇论文，产出「可复现细节级」的中文深度解读。
目标不是摘要，而是让工程师读完就能理解到能复现的程度：每个子模块的输入/输出、关键公式（带符号含义）、张量维度、训练目标/loss、关键超参、数据构造。

只输出一个 JSON 对象：
{
  "title_zh": "<中文标题，<=50字>",
  "idea": "<2-3 句卡片摘要，点明核心 idea/范式>",
  "tags": ["<3-5 个英文标签，CamelCase+空格>"],
  "body_md": "<markdown 正文，严格按五大块，用 ## 标题>"
}

body_md 的五大块（标题必须完全一致）：
## 核心思路
一句话讲清解决什么问题、用什么关键 idea。
## 整体实现思路
端到端 pipeline：输入→各阶段→输出（可用代码块画 ASCII 流程）。
## 子模块实现（可复现细节）
逐个子模块用 ### 小标题，写 输入/输出、关键公式（带符号含义）、维度/超参/loss、数据构造。宁可长、带公式。
## 实验设置与结果
数据集/baseline/指标定义/**关键数字用 markdown 表格**/消融结论。
## 思考与可参考价值
批判性看局限 + 对电商/搜索推荐/Agent 方向的可借鉴点。

要求：信息密度高、不要套话；术语保留英文；公式用行内 `...` 或 $$ 块；数字结果用 markdown 表格。"""


def log(*a):
    print(*a, file=sys.stderr, flush=True)


def arxiv_id(url: str) -> str:
    m = re.search(r"(\d{4}\.\d{4,5})", url or "")
    if not m:
        raise SystemExit(f"无法从 URL 解析 arxiv id: {url}")
    return m.group(1)


def fetch_meta(aid: str) -> dict:
    feed = feedparser.parse(f"http://export.arxiv.org/api/query?id_list={aid}")
    if not feed.entries:
        return {"title": aid, "authors": [], "published": "", "summary": ""}
    e = feed.entries[0]
    authors = [a.name for a in getattr(e, "authors", [])]
    return {
        "title": re.sub(r"\s+", " ", e.title).strip(),
        "authors": authors,
        "published": getattr(e, "published", "")[:7],  # YYYY-MM
        "summary": getattr(e, "summary", ""),
    }


def fetch_pdf_text(aid: str, dest: Path) -> str:
    url = f"https://arxiv.org/pdf/{aid}"
    with httpx.Client(timeout=120.0, follow_redirects=True) as cli:
        r = cli.get(url, headers={"User-Agent": "ai-papers-daily-deepread/0.1"})
        r.raise_for_status()
        dest.write_bytes(r.content)
    reader = PdfReader(io.BytesIO(dest.read_bytes()))
    parts = []
    for p in reader.pages:
        try:
            parts.append(p.extract_text() or "")
        except Exception:
            continue
    return "\n".join(parts).encode("utf-8", "replace").decode("utf-8")


def gen_deep(meta: dict, full_text: str) -> dict:
    user = (
        f"标题: {meta['title']}\n作者: {', '.join(meta['authors'][:8])}\n\n"
        f"全文(pypdf 抽取, 截断到 {PDF_MAX_CHARS} 字符):\n-----\n{full_text[:PDF_MAX_CHARS]}\n-----\n\n"
        "请按系统要求输出 JSON。body_md 写到可复现细节级。"
    )
    resp = client.chat.completions.create(
        model=DEEPSEEK_MODEL,
        messages=[{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}],
        response_format={"type": "json_object"},
        temperature=0.3, max_tokens=12000,
    )
    return json.loads(resp.choices[0].message.content)


def main():
    paper_url = os.environ.get("PAPER_URL", "").strip()
    topic = os.environ.get("TOPIC", "").strip()
    if not paper_url:
        raise SystemExit("PAPER_URL 必填")
    # resolve topic
    if topic == "__new__" or topic not in TOPICS:
        name = os.environ.get("NEW_TOPIC_NAME", "").strip()
        icon = os.environ.get("NEW_TOPIC_ICON", "").strip() or "🗂"
        if topic == "__new__":
            if not name:
                raise SystemExit("选了新建 topic 但 NEW_TOPIC_NAME 为空")
            tid = _slugify(name) or "misc"
            TOPICS[tid] = (name, icon)
            topic = tid
        else:
            raise SystemExit(f"未知 topic: {topic}")
    tname, ticon = TOPICS[topic]

    aid = arxiv_id(paper_url)
    log(f"arxiv={aid} topic={topic}({tname})")
    meta = fetch_meta(aid)
    pdfpath = Path(f"/tmp/deepread-{aid}.pdf")
    full = fetch_pdf_text(aid, pdfpath)
    log(f"meta title={meta['title'][:60]!r} pages_text_chars={len(full)}")
    deep = gen_deep(meta, full)

    slug = (_slugify(meta["title"], max_length=60) or aid).rstrip("-")
    # dedup: if slug exists, append -rev
    if any((ARCHIVE / t / f"{slug}.md").exists() for t in TOPICS):
        slug = f"{slug}-rev"
    # NOTE: CI 自动抽图不可靠（矢量图 pdfimages 抽到空白、page-render 自动裁切易串栏/截断），
    # 故 CI 深读只产「可复现深度正文」，配图交给本机 /paper-to-pages（Claude 驱动 + 人工核验）。
    figs: list[str] = []
    body = deep["body_md"]

    authors = ", ".join(meta["authors"][:5]) + (
        f", et al. ({len(meta['authors'])} 人)" if len(meta["authors"]) > 5 else "")
    fm = {
        "title": meta["title"], "authors": authors or "—",
        "date": meta["published"] or "", "venue": "arXiv",
        "topic": topic, "topic_name": tname, "topic_icon": ticon,
        "idea": deep.get("idea", ""),
        "paperUrl": f"https://arxiv.org/abs/{aid}", "codeUrl": None,
        "tags": deep.get("tags", []),
        "unverified": True,  # 机器自动生成（DeepSeek），标「未核实」，可在本机用 /paper-to-pages 精修
    }
    import yaml
    fm_yaml = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, default_flow_style=False)
    outdir = ARCHIVE / topic
    outdir.mkdir(parents=True, exist_ok=True)
    outpath = outdir / f"{slug}.md"
    outpath.write_text(f"---\n{fm_yaml}---\n\n{body.strip()}\n", encoding="utf-8")
    log(f"wrote {outpath}")
    print(json.dumps({"slug": slug, "topic": topic, "topic_name": tname,
                      "n_figures": len(figs), "ok": True}, ensure_ascii=False))


if __name__ == "__main__":
    main()
