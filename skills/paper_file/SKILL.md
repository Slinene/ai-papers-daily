---
name: paper_file
description: 把一篇 arXiv 论文加进「论文沉淀」存档（agent_rl_papers.html）。使用场景：用户给一个 arXiv ID / URL（或同时指定主题），希望把这篇论文加入到沉淀里、自动生成详细解读字段（核心贡献 / 背景 / 方法 / 实验 / 优点 / 局限 / 启发 / 一句话总结）、同步写入 ai-papers-daily/src/content/archive_papers 并推到 GitHub。触发关键词：「加论文到沉淀」「paper_file」「归入沉淀」「加进 agent_rl_papers」。
---

# paper_file

把一篇 arXiv 论文加进 `agent_rl_papers.html` 主题档案 + `ai-papers-daily` 站点的 `archive_papers` 内容集。

## 资源

- HTML 档案：`/Users/bytedance/Documents/Claude/Projects/字节工作/agent_rl_papers.html`
- 网站项目：`~/ai-papers-daily/` (GitHub: `Slinene/ai-papers-daily`)
- 当前已有主题：`agent-rl`（Agent RL 🤖）/ `user-simulation`（User Simulation 👥）/ `gen-rec`（生成式推荐 🎯）
- 绑定 LLM：DeepSeek（OpenAI 兼容，配置在 `~/ai-papers-daily/.env` 里）

## 处理流程

用户给一个 arXiv 输入（ID 如 `2510.18821` 或完整 URL）后：

1. **解析主题**。如果用户没指定，从论文摘要里自动推断 `agent-rl` / `user-simulation` / `gen-rec` 哪个最贴。无把握就向用户问一次。
2. **运行 `add_paper.py`**，路径见下面 `## 用法`。脚本会：
   - 拉 arXiv 元数据（title / authors / abstract / pdf url / 发表日期）
   - 调 DeepSeek 用论文风格生成 `idea` + `detail.{contribution,background,method,experiments,pros,cons,inspiration,takeaway}` 这 9 个字段
   - 注入到 HTML 对应主题 `papers: [...]` 数组的开头（保持最新在前）
   - 写一份 markdown 到 `~/ai-papers-daily/src/content/archive_papers/{topic}/{slug}.md`
   - 如果传 `--commit`，自动 `git add + commit + push` ai-papers-daily
3. **告诉用户结果**：HTML 已更新（diff 大致 +60 行）、site markdown 已写入、是否已推到 GitHub。

## 用法

```bash
# 1) 自动模式：完整一键
python ~/.claude/skills/paper_file/add_paper.py <arxiv_id_or_url> \
  --topic <agent-rl|user-simulation|gen-rec> \
  --commit

# 2) 不 push，只更新本地
python ~/.claude/skills/paper_file/add_paper.py <arxiv_id_or_url> --topic agent-rl

# 3) 也可以直接 URL：
python ~/.claude/skills/paper_file/add_paper.py https://arxiv.org/abs/2510.18821 --topic agent-rl --commit
```

## 重要规则

- **永远先把 ai-papers-daily 切到干净状态再 commit**。如果有未提交的本地修改，先确认是否一并带上 / stash。
- **不要修改 HTML 的样式/JS 代码段**。脚本只在 `papers: [` 后插入新对象。
- **若 DeepSeek 调用失败**，脚本会退出非 0；不会留下半成品 HTML（写入是原子的：先在内存里 build 完整 HTML 再覆盖落盘）。
- **避免重复添加**：脚本在动手前会检查目标主题 `papers[]` 里是否已有同名 paperUrl / arxivId，若已存在就跳过并提醒用户。
- **HTML 不在 Git 仓库里**（在 `~/Documents/Claude/Projects/字节工作/`），所以脚本不会动它的 git 状态；只 push ai-papers-daily。如果用户也希望把 HTML 纳入版本控制，那是另一项工作。
- **slug**：用 title 做 kebab-case，长度限 70 字符。与 ai-papers-daily 现有 `import_archive.py` 的 slug 规则保持一致。

## 失败兜底

- arXiv API 拉取失败 → 重试 1 次，仍失败就让用户手动确认是否输错了 ID。
- DeepSeek 拉取失败 / 解析失败 → 脚本退出非 0；用户可以重试或换网络。
- HTML 注入定位失败（找不到目标 topic）→ 列出可用 topic ID 让用户确认。
- git push 冲突 → 不强推，提示用户手工处理。
