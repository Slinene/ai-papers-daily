---
title: Long-Term Agent Memory through Complementary Curation and Consolidation
title_zh: 长时智能体记忆：互补式记忆构建与整合
authors:
- Abhishek Gupta
- Dongge Han
- Daniel Madrigal Diaz
- Wei-Ning Chen
- Mayukh Das
- Victor Rühle
- Saravan Rajmohan
affiliations:
- Microsoft
arxiv_id: '2610.39790'
url: https://arxiv.org/abs/2610.39790
pdf_url: https://arxiv.org/pdf/2610.39790
published: '2026-10-29'
collected: '2026-10-30'
category: Agent
direction: Agent 长程记忆 · 混合存储与整合
tags:
- Agent Memory
- Long-term Memory
- Memory Consolidation
- Episodic Memory
- Relational Memory
- Retrieval
one_liner: 提出情节记忆+结构化关系记忆的混合存储，并通过离线聚类整合压缩16%以上记忆且性能几乎不降
practical_value: '- 会话级记忆构建：电商客服/导购 Agent 可在 session 结束后批量抽取两类记忆，减少逐轮 LLM 调用，同时保留跨轮上下文；关系记忆采用
  (实体, 关系, 客体, 时间戳, 来源上下文) 结构，便于后续查询、更新和溯源。

  - 双存储分离检索：查询时同时检索情节记忆和关系元组，关系条目更短、预算内可多取，适合「用户历史偏好/订单/承诺」等电商 QA 场景；固定 top-k 且 k=10
  已饱和，能省 token 和延迟。

  - 离线 UMAP+HDBSCAN 聚类整合：定期对 embedding 聚类做 merge/delete，可压缩 16–34% 存储，适合长生命周期用户档案；min_cluster_size
  取 5–10 能在压缩率和准确率间取得平衡。

  - 关系记忆的 provenance/timestamp 设计可直接迁移到推荐系统的用户画像：不仅存「用户喜欢什么」，还存「何时为何说」，避免旧偏好覆盖新偏好。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
长程对话智能体需要跨 session 记住事实、事件和关系。纯参数化记忆更新成本高、易幻觉；非参数化记忆若只存一种表示，往往无法同时兼顾时间线和结构化查询。混合表示可能更贴合真实检索需求。

## 方法关键点
- 双存储：Episodic Memory 存 session 级摘要（title/summary/details/timestamp），保留叙事与时间顺序；Relational Memory 存 (实体, 关系, 客体, 时间戳, 来源上下文) 元组，将隐式关系显式化。
- Session 级离线 curation：每个对话 session 结束后各跑一次 LLM 抽取，避免逐轮 CRUD 带来的碎片化和 O(n) LLM 调用。
- 查询阶段分别对两个 store 做 embedding top-k 检索：episodic 取 k 条，relational 取 2k 条；固定 k=10，不在 query-time 做额外 LLM 调用。
- 记忆整合：用 UMAP 降维 + HDBSCAN 对 embedding 聚类，对同簇记忆做 LLM merge/delete，消除冗余、过时和冲突。

## 关键结果
- LoCoMo：gpt-4.1-mini 下 overall 90.2%，gpt-4o-mini 下 83.5%，超过 Mem0/Zep/Nemori 等 SOTA memory 框架；比 FullContext 少 87% token。
- LongMemEval-S：overall 85.5%，超过 FullContext 和 Nemori；其中 multi-session 0.801 vs Nemori 0.556，temporal-reasoning 0.858 vs Nemori 0.722。
- 双存储互补：ablation 中 Multi-Hop +6.3 点、Temporal +6.8 点（gpt-4o-mini）。
- Consolidation：min_cluster_size=10 时压缩 16.3%，LoCoMo 仅降约 1 点；mcs=5–10 是较好权衡区间。检索预算 k=10 后性能饱和。

## 最值得记住的一句话
把记忆拆成「有时间线的叙事摘要」和「可查询的关系元组」两种互补表示，比单一记忆结构更接近长程 Agent 的实际检索需求；再加离线聚类整合，就能用低 token 成本维持高召回。
