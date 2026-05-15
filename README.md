# AI Papers Daily

Agent-curated, daily-refreshed AI paper digest. arXiv + HuggingFace Daily
Papers → DeepSeek (OpenAI 兼容协议) → Markdown → Astro static site →
GitHub Pages + 飞书消息卡片推送。

Inspired by [recsys-frontier](https://blog.recsys-frontier.com/) (NotionNext),
but content production is fully automated by an LLM agent.

## How it works

```
[GitHub Actions cron 09:00 BJT]
        │
        ▼
 fetch  → arXiv (cs.IR/cs.LG/cs.CL/cs.AI) + HuggingFace Daily Papers
        │   dedupe by arxiv_id against src/content/papers/
        ▼
 process → DeepSeek scores relevance (0-10)
        │   keep score >= MIN_SCORE_KEEP
        │   DeepSeek writes card from abstract
        │   score >= MIN_SCORE_DEEP → pypdf 抽 PDF 文本 → DeepSeek 写深度卡
        ▼
 write_md → render frontmatter + body to src/content/papers/{date}-{slug}.md
        ▼
 commit + push                          → triggers deploy.yml (Astro build)
 push_feishu → 飞书自定义机器人交互式消息卡片
```

## Repo layout

```
.
├── .github/workflows/
│   ├── daily-digest.yml   # cron: agent pipeline + commit + 飞书 push
│   └── deploy.yml         # content change: build Astro & deploy Pages
├── src/
│   ├── content/
│   │   ├── config.ts      # Astro content collection schema
│   │   └── papers/        # auto-generated .md cards (one per paper)
│   ├── layouts/, components/, pages/, styles/
├── scripts/
│   ├── common.py          # shared paths, slug, dedupe helpers
│   ├── fetch.py           # stage 1: arXiv + HF Daily Papers
│   ├── process.py         # stage 2: relevance filter + summarize
│   ├── write_md.py        # stage 3: JSON → markdown frontmatter
│   ├── push_feishu.py     # stage 4: 飞书 interactive card
│   └── run_all.py         # orchestrator
├── astro.config.mjs
├── package.json
└── requirements.txt
```

## Setup

### 1. Create the GitHub repo

```bash
cd ~/ai-papers-daily
git init -b main
git add .
git commit -m "init: ai-papers-daily skeleton"
# create a public repo on github.com, then:
git remote add origin git@github.com:<you>/ai-papers-daily.git
git push -u origin main
```

### 2. Enable GitHub Pages

Repo → **Settings → Pages → Build and deployment → Source: GitHub Actions**.

First build runs after the first content commit (i.e. after the daily-digest job
makes at least one commit, or after you trigger `deploy.yml` manually).

### 3. Set repo secrets and variables

Repo → **Settings → Secrets and variables → Actions**:

**Secrets** (encrypted, used by `daily-digest.yml`):

| Name | Value |
|---|---|
| `DEEPSEEK_API_KEY` | `sk-...` from <https://platform.deepseek.com/> → API Keys |
| `FEISHU_WEBHOOK` | 群设置 → 群机器人 → 添加自定义机器人，复制 webhook URL |
| `FEISHU_SECRET` | Optional. Only if you enabled「签名校验」when adding the bot |

**Variables** (plain, can be edited inline):

| Name | Example | Purpose |
|---|---|---|
| `SITE_URL` | `https://<you>.github.io` | Used in canonical links + 飞书 card buttons |
| `BASE_PATH` | `/ai-papers-daily` | URL path prefix (empty for user-site repo) |
| `DEEPSEEK_BASE_URL` | `https://api.deepseek.com` | OpenAI 兼容 endpoint，留空走默认官方 |
| `DEEPSEEK_MODEL` | `DeepSeek-V4-Pro` | 模型 id；改成你账号能用的型号 |
| `MAX_PAPERS_PER_DAY` | `30` | Hard cap after relevance filter |
| `MIN_SCORE_KEEP` | `7` | Minimum relevance score to keep |
| `MIN_SCORE_DEEP` | `8` | Score above which the agent reads the full PDF |
| `PDF_TEXT_MAX_CHARS` | `60000` | PDF 抽取后送给模型的最大字符数（防止炸 context）|

### 4. Local dev

```bash
# Python env
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # fill in DEEPSEEK_API_KEY + FEISHU_WEBHOOK

# Run the full agent pipeline locally
python scripts/run_all.py

# Or one stage at a time
python scripts/fetch.py        # writes .cache/raw_papers.json
python scripts/process.py      # writes .cache/processed_papers.json
python scripts/write_md.py     # writes src/content/papers/*.md
python scripts/push_feishu.py  # POSTs to 飞书

# Node / Astro
npm install
npm run dev      # http://localhost:4321/ai-papers-daily
npm run build    # ./dist
```

## Tuning

- **What to fetch**: edit `ARXIV_CATEGORIES` in `scripts/fetch.py`.
- **What counts as "relevant"**: edit the `RELEVANCE_SYSTEM` prompt in
  `scripts/process.py`. The scoring rubric is in there in Chinese.
- **Card style / depth**: `SUMMARY_SYSTEM` in `scripts/process.py`.
- **Frequency**: `cron` line in `.github/workflows/daily-digest.yml`. Note
  GitHub schedules can be delayed 5-15 min — they're not real-time.
- **Cost**: Haiku is cheap (every paper); Sonnet only runs on
  `score >= MIN_SCORE_DEEP`. Raise `MIN_SCORE_DEEP` to spend less on PDFs.

## Cost ballpark

With defaults (~50 papers fetched/day, ~10 kept, ~3 deep-read), all calls on
DeepSeek。具体单价以 DeepSeek 当前定价为准 — V 系列模型 input/output 通常都比
Claude Haiku 还便宜，所以总成本一般在 **$1-3/月** 量级。

主要花费分布：
- ~50 次 relevance scoring（每次 ~1k 输入 + 0.1k 输出）
- ~10 次 abstract summary（每次 ~2k 输入 + 1k 输出）
- ~3 次 PDF deep read（每次 ~20k 输入 + 2k 输出）

调参降本：调高 `MIN_SCORE_KEEP` / `MIN_SCORE_DEEP`，或调低 `MAX_PAPERS_PER_DAY`
和 `PDF_TEXT_MAX_CHARS`。

## Troubleshooting

- **No 飞书 push in dry run**: `FEISHU_WEBHOOK` not set. The script logs a
  warning and exits 0 (not a failure — useful for first-time setup).
- **`401 unauthorized` from arXiv**: their export server occasionally rate-limits;
  retry the workflow.
- **Pages build fails on first deploy**: enable Pages with **Source: GitHub Actions**
  first, then re-run `deploy.yml` from the Actions tab.
- **Card looks empty in 飞书**: check the bot's signature setting matches
  `FEISHU_SECRET` — mismatched signature returns 200 but the card never renders.
