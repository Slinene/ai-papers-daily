---
title: 'StaleBench: Isolating Stale Retrieval in Agent Memory, and Pricing the Fix'
title_zh: StaleBench：隔离 Agent 记忆中的过期检索并评估修复成本
authors:
- S M Mahbub Murshed
affiliations:
- Causal Dynamics Lab
arxiv_id: '2611.19752'
url: https://arxiv.org/abs/2611.19752
pdf_url: https://arxiv.org/pdf/2611.19752
published: '2026-11-15'
collected: '2026-11-17'
category: Agent
direction: Agent 记忆过期检索基准与评估
tags:
- Agent Memory
- Stale Retrieval
- Benchmark
- Entity Resolution
- Temporal Facts
- Contamination@5
one_liner: 构建 892 条真实更新事实基准，揭示相似度检索无法区分事实新旧版本，提出 Contamination@5 正确评估记忆策略。
practical_value: '- 在电商/购物助手等 Agent 记忆场景中，时间敏感事实（价格、库存、会员等级、地址）必须采用实体解析+版本覆盖策略，不能仅靠相似度检索，否则过时语句与当前语句同时进入上下文会显著拉低下游回答准确率。

  - 评测记忆策略时不要只看 current@k：即使当前版本在 top-k 中，过时版本“污染”上下文也会损伤 reader 效果。可引入类似 Contamination@5
  的指标，衡量 top-k 中过时语句占比。

  - 简单的“按时间戳重排 top-k”可能适得其反：论文显示把新旧两条都交给 reader，某些 reader 准确率反而下降。建议在写路径做实体解析覆盖旧版本，或读路径只返回当前版本，避免多版本并存。

  - 外部记忆产品（Mem0、Graphiti、LangMem）处理 supersession 的机制差异很大，接入业务前需用更新事实基准验证其过期处理策略，不能依赖默认行为。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：Agent 随时间存储同一事实的多个版本，相似度检索无法区分“当前值”，因为所有版本都与查询中的实体匹配，导致过期版本被返回的概率高达 0.53。简单的按时间戳重排 top-k 反而可能让 reader 同时看到新旧版本，准确率下降。

**方法**：构建 StaleBench，包含 892 条真实更新事实（来自 Wikidata 有效性年份，通过 TempLAMA），提供来源侧的 currency labels，不依赖检索分数。引入 Contamination@5 指标，衡量 top-5 中过时语句的污染程度。评估多种记忆策略：retain-everything、保留策略、实体解析（写路径和查询路径），以及三个部署系统（Mem0、Graphiti、LangMem）和 ERASE。

**关键结果**：保留策略与 retain-everything 在 current@1 和 current@5 上完全相同，但 reader 准确率相差 29.5 和 65.6 个点（不显示日期时）；Contamination@5 能正确区分二者。去除语句携带的 lexical anchor 使 freshness 下降数十个点，而在写路径和查询路径都做实体解析能恢复大部分损失。四个系统对 supersession 的处理各不相同，无单一评分惯例能统一描述。
