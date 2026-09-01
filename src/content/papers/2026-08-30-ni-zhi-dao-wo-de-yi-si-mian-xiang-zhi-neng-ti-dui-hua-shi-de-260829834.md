---
title: 'You Know What I Mean: A Benchmark for Agentic Conversational Reference Grounding'
title_zh: 《你知道我的意思：面向智能体对话式引用消解的基准》
authors:
- Karen Fuchs
- Uri Katz
- Yoav Goldberg
affiliations:
- Bar-Ilan University
- Allen Institute for AI
arxiv_id: '2608.29834'
url: https://arxiv.org/abs/2608.29834
pdf_url: https://arxiv.org/pdf/2608.29834
published: '2026-08-30'
collected: '2026-09-01'
category: Agent
direction: Agent 多工具引用消解基准
tags:
- Agentic Benchmark
- Tool Use
- Conversational Grounding
- GitHub
- LLM Evaluation
- Reference Resolution
one_liner: 提出 CoRG 对话引用消解任务和 REPOREF 基准，最优 LLM 智能体仅 67% 成功率
practical_value: '- 对客服/导购 Agent：把“用户说昨天看的那款”“活动页那个券”这类间接指代建模为多步工具搜索，而不是直接 embedding
  召回；把候选发现和最终选择分开诊断。论文显示 70–92% 失败发生在候选没被 surface，所以优先投入查询改写、时间/作者/类目过滤等探索策略，而不是只优化
  ranking 模型。

  - 数据构建可复用 natural masking：从含商品 ID/URL 的真实会话中，用 LLM 把显式链接改写成自然间接表达，再用 identifiability/ambiguity
  filter 筛出可唯一定位样本；适合低成本构造测试集或训练数据。

  - 工具/API 设计：保留只读、按平台对象组织的搜索与元数据工具，支持按时间/作者/类型过滤；给 agent 预算 B≈6 可能获得大部分收益（B=1→B=6
  从 23% 到 64%），再往上成本高但增益有限。生产环境可设 6–10 次调用上限。

  - 诊断 bucket 值得迁移：区分 surface mismatch、competitive alternatives、sparse evidence、commit-level（或
  SKU/SPU/活动商品级）等，定位自己 Agent 的失败集中区；对低文本显著性的目标（commit 或具体 SKU 变体），需额外文件/属性/历史 diff
  校验。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：协作会话中高频出现间接引用，例如“昨天那个 PR”“我开的那个 issue”，人类能结合上下文和外部系统定位，但 AI 助手通常只会做表层检索。论文把该问题形式化为对话式引用消解（CoRG），要求智能体在给定工具集下从外部 API 可访问的空间中找到唯一目标资源。

**方法关键点**：
- 数据：REPOREF 从 Gitter 开发者聊天中含 GitHub 链接的消息出发，做 reference-centered segmentation、natural masking，将直接 URL/ID 改写为自然间接表达；再用 identifiability 与 ambiguity filtering 保留可唯一消解样本。
- 规模：400 个对话片段、7,781 条消息、92 个仓库、23 个社区，覆盖 issue/PR/commit 三类目标。
- 任务环境：22 个只读 GitHub API，支持多种搜索、评论/代码 diff/commit 历史/文件内容查看；智能体采用 ReAct 循环或 Claude Code MCP，预算 B=10。
- 指标：exact-match accuracy、工具调用次数、token 成本、超额调用。

**关键结果**：
- 最优 Gemini-3-Flash 67.0% 成功率；DeepSeek-V4-Pro 60.25%；Claude Code Opus 4.7 63.25%；轻量模型仅 1.5–4.0%。
- 预算从 B=1 到 B=16，Gemini-3-Flash 准确率 23.21%→73.93%，主要提升发生在 B=6 前。
- 70–92% 的失败是 gold 候选未被探索到；一旦被 surfacing，选取正确率 87–91%。
- 最难的 bucket 是 commit 级引用，最好模型仅 46.8%。

**最值得记住的一句话**：CoRG 失败主要不是最后选错，而是没把正确候选找出来；先提高探索召回，再优化排序决策。
