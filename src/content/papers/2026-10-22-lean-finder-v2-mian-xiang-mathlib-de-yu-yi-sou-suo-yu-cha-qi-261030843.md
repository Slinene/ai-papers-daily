---
title: 'Lean Finder V2: Semantic Search for Mathlib That Disambiguates User Queries'
title_zh: Lean Finder V2：面向 Mathlib 的语义搜索与查询消歧
authors:
- Jialin Lu
- Xiaoyu Liu
- Hengrui Luo
- Rodrigo Stehling
- Linxi Liu
- Weiran Sun
- Yuepeng Wang
- Wuyang Chen
affiliations:
- Simon Fraser University
- Rice University
- University of Pittsburgh
arxiv_id: '2610.30843'
url: https://arxiv.org/abs/2610.30843
pdf_url: https://arxiv.org/pdf/2610.30843
published: '2026-10-22'
collected: '2026-10-25'
category: QueryRec
direction: 语义搜索 · 查询改写与消歧
tags:
- Semantic Search
- Query Rewriting
- Adversarial Training
- Mathlib
- Lean
- Retrieval
one_liner: 用对抗训练生成大规模短歧义查询，结合模型微调与输入层改写，在 MathlibQR 上至少相对提升 11%
practical_value: '- **用对抗训练补足“短歧义 query”数据**：电商搜索里“苹果”“nike 卫衣”等短查询经常缺 context；可仿照用生成模型
  + 判别器迭代生成大量带标签的歧义 query，而不是只靠真实日志，显著扩充训练集，解决数据稀疏。

  - **模型层 + 输入层双层消歧**：同时 fine-tune 检索模型（增强对短 query 的鲁棒性）并在检索前对 query 做改写/补全（如加类目、属性、别名），两者互补；在商品搜索或
  Agent 工具检索中可分开评估增量，避免只做单一层。

  - **面向真实短查询做人类评估基准**：构建少量人工标注的短 query benchmark，用 unlabeled 真实 human/agent 交互做 ranking
  评估，比离线 dense retrieval 指标更贴近线上体验。

  - **检索质量直接挂钩下游 agent 任务成功率**：与 Claude Code 集成后证明 proof success 提升，说明 Agent 工具检索/商品召回改善能直接转化为任务成功；建议将检索召回作为
  Agent 流程中的关键优化点。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：Mathlib 有 40 万+定理/定义，人类数学家和 coding agent 搜索时通常只输入短属性、符号、别名或假设，缺少上下文，歧义严重；现有语义搜索引擎假设 context-rich query，且短 query 与 ground-truth 配对数据稀缺，本质是数据问题。

**方法**：
- 通过对抗训练规模化生成带标签的短歧义 query，缓解真实数据不足；
- 在模型层 fine-tune retriever 提升对短 query 的鲁棒性，同时在输入层做 query rewriting 显式补全/消歧；
- 两层互补，端到端用于 Mathlib 语义搜索。

**结果**：
- 在人工整理的 MathlibQR 基准上刷新 SOTA，相对此前最佳至少提升 11%；
- 在 SOTA retriever 之上，优化的 query rewriting 进一步提升 MathlibQR；
- 在无标签的人类与 coding-agent 真实查询中被评为最强系统；
- 与 Claude Code 集成后，下游定理证明成功率提升。
