#!/usr/bin/env python3
"""paper_file skill — add an arXiv paper to the agent_rl_papers archive.

Workflow:
  1. Resolve arxiv id (accept bare id or arxiv URL)
  2. Fetch arxiv metadata (title, authors, abstract, pdf url, published date)
  3. Use DeepSeek to generate idea + detail.{contribution, background, method,
     experiments, pros, cons, inspiration, takeaway} in the existing archive
     style (信息密度高、中文、术语保留英文)
  4. Inject the paper object into agent_rl_papers.html under the right topic
     (papers: [<new>, ...existing])
  5. Also write a markdown file to ai-papers-daily/src/content/archive_papers/
  6. Optionally git commit + push the ai-papers-daily side

Usage:
  python add_paper.py <arxiv_id_or_url> --topic <id> [--commit] [--html PATH] [--site PATH]

Env (loaded from ai-papers-daily/.env if present):
  DEEPSEEK_API_KEY        required
  DEEPSEEK_BASE_URL       default https://api.deepseek.com
  DEEPSEEK_MODEL          default deepseek-v4-pro
  PAPER_FILE_HTML         override HTML path
  PAPER_FILE_SITE         override ai-papers-daily root
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Optional

import feedparser
import httpx
import yaml
from openai import OpenAI, OpenAIError
from pydantic import BaseModel, Field, ValidationError
from slugify import slugify

# ------- Paths & config ------------------------------------------------------

DEFAULT_HTML = Path("/Users/bytedance/Documents/Claude/Projects/字节工作/agent_rl_papers.html")
DEFAULT_SITE = Path.home() / "ai-papers-daily"


def load_env_from(site: Path) -> None:
    """Best-effort .env load. The skill is run outside the project, so we point
    python-dotenv at ai-papers-daily/.env explicitly."""
    env_path = site / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        os.environ.setdefault(k.strip(), v.strip())


# ------- Models --------------------------------------------------------------

class PaperDetail(BaseModel):
    contribution: str
    background: str
    method: str
    experiments: str
    pros: str
    cons: str
    inspiration: str
    takeaway: str


class PaperAdd(BaseModel):
    idea: str = Field(max_length=300)
    tags: list[str] = Field(default_factory=list, max_length=6)
    detail: PaperDetail


# ------- Arxiv ---------------------------------------------------------------

ARXIV_ID_RE = re.compile(r"(\d{4}\.\d{4,5})")


def normalize_arxiv_id(raw: str) -> str:
    m = ARXIV_ID_RE.search(raw or "")
    if not m:
        raise SystemExit(f"could not extract arxiv id from {raw!r}")
    return m.group(1)


def fetch_arxiv(arxiv_id: str) -> dict:
    url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
    with httpx.Client(timeout=30, follow_redirects=True) as cli:
        r = cli.get(url, headers={"User-Agent": "paper-file-skill/0.1"})
        r.raise_for_status()
        feed = feedparser.parse(r.text)
    if not feed.entries:
        raise SystemExit(f"arxiv returned no entry for {arxiv_id}")
    e = feed.entries[0]
    authors = [a.name for a in e.get("authors", [])]
    return {
        "arxiv_id": arxiv_id,
        "title": re.sub(r"\s+", " ", e.title).strip(),
        "abstract": re.sub(r"\s+", " ", e.summary).strip(),
        "authors": authors,
        "published": (e.get("published") or "")[:7],   # YYYY-MM
        "url": f"https://arxiv.org/abs/{arxiv_id}",
        "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}",
    }


# ------- DeepSeek ------------------------------------------------------------

SYSTEM = """你是一位 AI 论文解读专家，要把一篇 arXiv 论文写成「论文沉淀」风格的深度卡片。

风格要求：
- 中文，但术语保留英文（如 LoRA、GRPO、DPO、MoE、RAG、KV cache、RLAIF、SFT、PPO）
- 信息密度高，不要"本文提出 / 本研究表明 / 我们认为"等套话
- contribution / background / method / experiments 等字段都要给出**具体的事实和数字**，不要泛泛而谈
- method 字段尤其要写得详细：算法名、关键设计、训练阶段、reward 设计等
- experiments 要带上数据集名 / baseline / 关键 metric 数字
- 整体风格参考 Anthropic Constitutional AI、DeepSeek-R1、Self-Rewarding LM 这一类奠基论文卡片

只输出 JSON，结构：
{
  "idea": "<2-3 句中文 hook，类似营销 hook 但事实导向，<= 200 字>",
  "tags": ["<2-5 个英文标签>"],
  "detail": {
    "contribution":  "<核心贡献，100-300 字>",
    "background":    "<动机/背景，100-300 字>",
    "method":        "<方法详解，200-600 字。可以用 markdown 列表>",
    "experiments":   "<实验结果，100-400 字，要有具体数字>",
    "pros":          "<优点，60-200 字>",
    "cons":          "<局限性，60-200 字>",
    "inspiration":   "<对后续工作的启发，60-200 字>",
    "takeaway":      "<一句话总结，<= 80 字>"
  }
}"""


def call_deepseek(paper: dict) -> PaperAdd:
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        raise SystemExit("DEEPSEEK_API_KEY missing (looked in env and ai-papers-daily/.env)")
    base_url = os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    model = os.environ.get("DEEPSEEK_MODEL", "deepseek-v4-pro")

    client = OpenAI(api_key=api_key, base_url=base_url, timeout=180, max_retries=2)
    authors_str = ", ".join(paper["authors"][:6]) + (" 等" if len(paper["authors"]) > 6 else "")
    user = (
        f"arxiv id: {paper['arxiv_id']}\n"
        f"标题: {paper['title']}\n"
        f"作者: {authors_str}\n"
        f"发表: {paper['published']}\n\n"
        f"摘要:\n{paper['abstract']}\n"
    )

    messages = [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": user},
    ]
    for attempt in range(2):
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=messages,
                response_format={"type": "json_object"},
                temperature=0.3,
                max_tokens=8000,
            )
        except OpenAIError as exc:
            print(f"deepseek api error attempt={attempt}: {exc}", file=sys.stderr)
            continue
        text = (resp.choices[0].message.content or "").strip()
        try:
            return PaperAdd.model_validate_json(text)
        except (ValidationError, json.JSONDecodeError) as exc:
            print(f"deepseek parse failed attempt={attempt}: {exc} | text={text[:200]}",
                  file=sys.stderr)
            messages.append({"role": "assistant", "content": text})
            messages.append({"role": "user",
                             "content": "返回的不是合法 JSON 或字段不符合 schema。只返回一个 JSON 对象。"})
    raise SystemExit("deepseek failed after 2 attempts")


# ------- HTML injection ------------------------------------------------------

TOPIC_BLOCK_RE = re.compile(r'id:\s*"([a-z0-9\-]+)"')


def js_string(s: str) -> str:
    """Serialize a Python string as a JS double-quoted string literal."""
    return json.dumps(s, ensure_ascii=False)


def render_js_paper(paper: dict, gen: PaperAdd) -> str:
    """Render the new paper as a JS object literal matching the existing style.
    Returns a multi-line string suitable for injection after `papers: [`."""
    lines: list[str] = []
    A = "      "   # 6-space indent matching the file
    B = "        "
    C = "          "

    def kv(key: str, value: str, indent: str = B) -> None:
        lines.append(f"{indent}{key}: {js_string(value)},")

    lines.append(f"{A}{{")
    kv("title", paper["title"])
    authors_str = ", ".join(paper["authors"][:6]) + (
        f" 等" if len(paper["authors"]) > 6 else "")
    kv("authors", authors_str or "(unknown)")
    affiliation = ""  # arxiv API doesn't surface affiliation reliably
    kv("affiliation", affiliation or "")
    kv("date", paper.get("published", ""))
    kv("venue", "arXiv")
    kv("idea", gen.idea)
    kv("paperUrl", paper["url"])
    lines.append(f"{B}codeUrl: null,")
    tags_js = ", ".join(js_string(t) for t in gen.tags[:6])
    lines.append(f"{B}tags: [{tags_js}],")
    lines.append(f"{B}detail: {{")
    kv("contribution", gen.detail.contribution, C)
    kv("background",   gen.detail.background, C)
    kv("method",       gen.detail.method, C)
    kv("experiments",  gen.detail.experiments, C)
    kv("pros",         gen.detail.pros, C)
    kv("cons",         gen.detail.cons, C)
    kv("inspiration",  gen.detail.inspiration, C)
    # takeaway is the last field — drop trailing comma
    lines.append(f"{C}takeaway: {js_string(gen.detail.takeaway)}")
    lines.append(f"{B}}}")
    lines.append(f"{A}}},")
    return "\n".join(lines)


def topic_papers_start(html: str, topic_id: str) -> int:
    """Find the byte offset of the `[` opening the papers array for a topic.
    Robust to whitespace; matches `papers:` after the topic's id."""
    # Locate the topic block
    pattern = re.compile(rf'id:\s*"{re.escape(topic_id)}"')
    m = pattern.search(html)
    if not m:
        return -1
    # Find the next `papers:` after that
    p = re.compile(r"papers:\s*\[")
    m2 = p.search(html, m.end())
    return m2.end() if m2 else -1


def already_has(html: str, topic_id: str, arxiv_id: str) -> bool:
    """Cheap check: does the html already mention this arxiv id?"""
    return arxiv_id in html


def inject_paper(html_path: Path, topic_id: str, paper: dict, gen: PaperAdd) -> None:
    text = html_path.read_text(encoding="utf-8")
    if already_has(text, topic_id, paper["arxiv_id"]):
        raise SystemExit(f"arxiv {paper['arxiv_id']} already present in HTML; skip")
    insert_at = topic_papers_start(text, topic_id)
    if insert_at < 0:
        raise SystemExit(f"topic id {topic_id!r} not found in HTML")
    new_block = "\n" + render_js_paper(paper, gen) + "\n"
    out = text[:insert_at] + new_block + text[insert_at:]
    html_path.write_text(out, encoding="utf-8")


# ------- Site markdown -------------------------------------------------------

def write_site_markdown(site: Path, topic_id: str, topic_meta: dict,
                        paper: dict, gen: PaperAdd) -> Path:
    archive_dir = site / "src" / "content" / "archive_papers" / topic_id
    archive_dir.mkdir(parents=True, exist_ok=True)
    slug = slugify(paper["title"] or "paper", max_length=70, word_boundary=True)
    path = archive_dir / f"{slug}.md"

    fm = {
        "title": paper["title"],
        "authors": ", ".join(paper["authors"][:6]) + (
            f" 等" if len(paper["authors"]) > 6 else ""),
        "date": paper.get("published", ""),
        "venue": "arXiv",
        "topic": topic_id,
        "topic_name": topic_meta["name"],
        "topic_icon": topic_meta.get("icon", ""),
        "idea": gen.idea,
        "paperUrl": paper["url"],
        "tags": gen.tags,
        "unverified": False,
        "detail": gen.detail.model_dump(),
    }
    fm = {k: v for k, v in fm.items() if v}
    fm_yaml = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, default_flow_style=False)

    SECTIONS = [
        ("contribution", "核心贡献"),
        ("background",   "背景"),
        ("method",       "方法"),
        ("experiments",  "实验结果"),
        ("pros",         "优点"),
        ("cons",         "局限"),
        ("inspiration",  "对后续工作的启发"),
        ("takeaway",     "一句话总结"),
    ]
    body_parts = [gen.idea, ""]
    for key, label in SECTIONS:
        val = getattr(gen.detail, key)
        if val:
            body_parts.append(f"## {label}\n")
            body_parts.append(val)
            body_parts.append("")
    body = "\n".join(body_parts).rstrip() + "\n"
    path.write_text(f"---\n{fm_yaml}---\n\n{body}", encoding="utf-8")
    return path


# ------- Topic registry (kept in sync with the HTML by inspection) ----------

TOPICS = {
    "agent-rl":        {"name": "Agent RL",        "icon": "🤖"},
    "user-simulation": {"name": "User Simulation", "icon": "👥"},
    "gen-rec":         {"name": "生成式推荐",        "icon": "🎯"},
}


# ------- Git -----------------------------------------------------------------

def git_commit_push(site: Path, paper: dict, topic_id: str) -> None:
    rel_md = f"src/content/archive_papers/{topic_id}/"
    commit_msg = (
        f"archive: add {paper['arxiv_id']} {paper['title'][:60]} -> {topic_id}\n\n"
        f"Source: {paper['url']}\n"
        f"Added via paper_file skill."
    )
    subprocess.run(["git", "-C", str(site), "add", rel_md], check=True)
    res = subprocess.run(["git", "-C", str(site), "diff", "--cached", "--quiet"])
    if res.returncode == 0:
        print("git: no changes to commit")
        return
    subprocess.run(["git", "-C", str(site), "commit", "-m", commit_msg], check=True)
    push = subprocess.run(["git", "-C", str(site), "push"])
    if push.returncode != 0:
        print("git push failed — please resolve manually", file=sys.stderr)
        sys.exit(push.returncode)


# ------- CLI -----------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="paper_file: add arxiv paper to archive")
    ap.add_argument("paper", help="arxiv id (e.g. 2510.18821) or arxiv URL")
    ap.add_argument("--topic", required=True, choices=sorted(TOPICS.keys()),
                    help=f"target topic id; one of {', '.join(sorted(TOPICS.keys()))}")
    ap.add_argument("--commit", action="store_true",
                    help="git add + commit + push ai-papers-daily site")
    ap.add_argument("--html", default=os.environ.get("PAPER_FILE_HTML"),
                    help=f"path to agent_rl_papers.html (default: {DEFAULT_HTML})")
    ap.add_argument("--site", default=os.environ.get("PAPER_FILE_SITE"),
                    help=f"path to ai-papers-daily project (default: {DEFAULT_SITE})")
    args = ap.parse_args()

    html_path = Path(args.html) if args.html else DEFAULT_HTML
    site = Path(args.site) if args.site else DEFAULT_SITE
    if not html_path.exists():
        raise SystemExit(f"HTML not found at {html_path}")
    if not site.exists():
        raise SystemExit(f"site not found at {site}")
    load_env_from(site)

    arxiv_id = normalize_arxiv_id(args.paper)
    print(f"[fetch] arxiv {arxiv_id}")
    paper = fetch_arxiv(arxiv_id)
    print(f"[fetch] title: {paper['title'][:90]}")

    print(f"[gen]   asking DeepSeek to write 8 detail sections...")
    gen = call_deepseek(paper)
    print(f"[gen]   ok: {len(gen.detail.method)} chars method · {len(gen.tags)} tags")

    print(f"[html]  injecting into {html_path.name} under topic={args.topic}")
    inject_paper(html_path, args.topic, paper, gen)
    print(f"[html]  done")

    md_path = write_site_markdown(site, args.topic, TOPICS[args.topic], paper, gen)
    print(f"[site]  wrote {md_path.relative_to(site)}")

    if args.commit:
        print(f"[git]   commit + push ai-papers-daily")
        git_commit_push(site, paper, args.topic)
        print(f"[git]   pushed")
    else:
        print("[git]   --commit not set; local-only")
    print("done.")


if __name__ == "__main__":
    main()
