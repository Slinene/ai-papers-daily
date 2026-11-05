---
title: Optimal Re-Ranking Depth
title_zh: 最优重排序深度
authors:
- Siqing Huo
- Andrew Parry
- Debasis Ganguly
- Charles L. A. Clarke
affiliations:
- University of Waterloo
- University of Glasgow
arxiv_id: '2611.05908'
url: https://arxiv.org/abs/2611.05908
pdf_url: https://arxiv.org/pdf/2611.05908
published: '2026-11-04'
collected: '2026-11-05'
category: RecSys
direction: 搜索重排序深度 · 效率-效果权衡
tags:
- re-ranking depth
- efficiency-effectiveness trade-off
- query performance prediction
- LLM relevance judgments
- neural rankers
- MS MARCO
one_liner: 用LLM相关性标注证明最优重排深度是query-specific的，提出IR-DCG@10预测器，平均深度可降3倍且效果不降
practical_value: '- 在多级排序/重排的搜索或推荐链路中，先离线用 LLM judge 评估一批 query 的 first-stage top-10
  DCG，再按分位数将 query 分桶、标定 rerank depth；线上按 query 的 LLM-DCG 特征查桶得到深度，不要全局固定深度。论文在 BM25+MonoT5
  上把平均 rerank depth 降 3 倍且 DCG@10 不降。

  - 不要依赖 score variance/WIG/NQC 等传统 QPP 做深度或截断决策，它们在该任务上几乎无效；优先使用 LLM 相关性标注或蒸馏其信号（例如小模型预测
  IR-DCG@10）作为 query 难度特征。

  - 若 retriever 本身较强（如 SPLADE），重排深度只需约 20 就够；可先做 query-specific optimal depth 分析，决定固定浅层还是动态路由，节省大模型
  reranker 成本。

  - Agentic RAG / 多智能体搜索流程中，可以把 depth-effectiveness trajectory 作为早期停止或路由信号：当 LLM 判断
  first-stage top-10 DCG 低，或重排收益曲线已 plateau，转向 query reformulation 或 clarification，而不是继续深挖。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

动机：
二级神经排序器通常按固定深度 rerank，假设效果随深度增加而饱和。但本文发现很多 query 的最优 rerank depth 是 query-specific 的，继续加深可能 plateau 甚至损害效果。过去受限于人工标注成本，难以大规模研究 per-query 深度；LLM 自动相关性标注让这种分析变得可行，也能为 agentic IR 提供“是否继续重排/是否转去 query 改写或澄清”的诊断信号。

方法关键点：
- 用 GPT-4o-mini + UMBRELA 对 MSMARCO v1 DEV 的 1000 个 query 生成 dense relevance judgments，共 53,936 条；另在 TREC DL 2019 上标注 5,285 条。
- 将 optimal re-ranking depth 定义为达到该 query 最大 DCG@10 所需的最浅 rerank depth d*(q)。
- 提出 IR-DCG@10：用 LLM 评估 first-stage top-10 的 DCG，作为 query 难度/重排收益的预测特征。
- 用 percentile-based calibration 而非直接回归 depth：按 predictor 分桶，用桶内训练 query 的 optimal depth 分位数作为预测 depth，并通过阈值 thr_min 选择效率-效果平衡点。
- 对比 11 种传统 QPP 方法，如 NQC、WIG、RSD、Dense-QPP 等。

关键结果：
- 在 BM25+MonoT5 上，IR-DCG@10 在 thr=0.80 时平均 rerank depth 降到 331，即减少约 3 倍，同时 DCG@10 不低于 full rerank depth 1000。
- Oracle 选择 per-query optimal depth 时，MSMARCO DEV 上平均 depth 可减少 5 倍，效果提升超过 7%；SPLADE retriever 下 oracle 甚至可减少 50 倍。
- 大多数 QPP 方法无法在保持效果的同时有效降低 depth；最好的传统 baseline RSD 仅减少约 2 倍。
- SPLADE 的最优平均 rerank depth 仅约 20，说明强 retriever 不需要深度 rerank。

最值得记住的一句话：
最优 rerank depth 是 query-specific 的，并且可以从 LLM 评估的 first-stage 排名质量中事先预测，这为搜索和 agentic retrieval 提供了低成本的动态深度控制信号。
