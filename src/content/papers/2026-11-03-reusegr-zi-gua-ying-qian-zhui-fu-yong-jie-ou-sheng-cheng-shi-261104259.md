---
title: 'ReuseGR: Offline--Online Decoupled Generative Retrieval via Adaptive Prefix
  Reuse'
title_zh: ReuseGR：自适应前缀复用解耦生成式检索
authors:
- Xujing Wang
- Yufeng Chen
- Boxuan Zhang
- Chao Wei
- Cai Xu
- Jie Zhao
- Weiru Zhang
- Wei Zhao
- Ziyu Guan
affiliations:
- Xidian University
- Alibaba International Digital Commerce Group
arxiv_id: '2611.04259'
url: https://arxiv.org/abs/2611.04259
pdf_url: https://arxiv.org/pdf/2611.04259
published: '2026-11-03'
collected: '2026-11-04'
category: GenRec
direction: 生成式检索 · 自适应前缀缓存
tags:
- Generative Retrieval
- Semantic ID
- Prefix Caching
- Knowledge Distillation
- Search Advertising
- Offline-Online Decoupling
one_liner: 7B离线规划共享SID前缀，0.5B在线个性化补全，以38.9%更低延迟达到与7B相当HR@100
practical_value: '- **离线在线解耦的查询缓存**：对高频 query，用大模型离线生成 SID 前缀，在线小模型仅完成剩余 token，平均延迟降低近
  40%，适合电商搜索广告海量请求。

  - **ReuseCut 自适应深度选择**：基于历史点击覆盖率用 Wilson 下限确定缓存深度，而非固定深度，可提升 HR@100 约 3.17 个百分点，可借鉴到
  query 缓存策略。

  - **Path KD 路径级蒸馏**：用 7B 教师的后缀 token 分布 KL 蒸馏 0.5B 学生，只训练 LoRA，提升在线补全质量且训练成本低。

  - **BudgetCut 分支选择**：将 beam 搜索的分支选择建模为策略优化，用边际召回增益作为 OPD teacher 初始化，再用 GRPO 优化整组选择，比简单分数裁剪更有效，可直接用于生成式推荐的
  beam pruning。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
生成式检索（GR）中，大模型质量更好但解码成本高。同一 query 的不同用户请求会重复生成完整 Semantic ID，浪费计算；但不同用户历史又需要个性化结果。如何复用大模型计算同时保持个性化，成为工业部署的关键挑战。

## 方法关键点
- **系统架构**：分离离线 query 级候选规划与在线请求级个性化补全。离线 7B CellPlan 生成共享的 SID 前缀集，在线 0.5B LeafFill 根据用户历史选择前缀并生成剩余 token。
- **ReuseCut**：从 query 文本预测缓存深度（0~3），基于历史点击覆盖率标签（Wilson 下限）训练分类器，平衡计算复用与候选覆盖。
- **Path KD**：用 7B 教师的后缀 token 分布蒸馏 0.5B 学生（LoRA），提升在线后缀打分。
- **BudgetCut**：在固定分支预算下，将分支选择建模为策略优化，先用 OPD 基于边际召回增益初始化，再用 GRPO 优化整组召回，避免高分分支引入非目标叶子。

## 关键结果
在 AE-PV 工业搜索广告数据集（3.38M items，44,225 测试 queries）上：
- 对比全在线 0.5B baseline：HR@100 提高 3.83 个百分点（85.82 vs 81.99），平均在线延迟降低 38.9%（71.45ms vs 117ms）。
- 对比全在线 7B baseline：HR@100 相当（85.82 vs 85.71），延迟降低 57.7%。
- 14 天在线 A/B 测试：CTR +0.93%，RPM +1.05%。
- 真实历史个性化：real-history HR@100 达 88.95%，且以 256 字节/query 前缀负载优于 complete-result caching 和 reranking。

**最值得记住**：自适应前缀复用让 7B 模型离线做粗粒度候选规划，0.5B 模型在线做个性化补全，用小模型达到大模型效果且延迟大幅下降。
