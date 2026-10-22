---
title: Directional Posterior Feedback Fusion for Query Reformulation in Dense Retrieval
title_zh: 稠密检索中方向性后验反馈融合的查询改写
authors:
- Yiteng Tu
- Qingyi Pan
- Weihang Su
- Jiaxin Mao
- Yiqun Liu
- Qingyao Ai
affiliations:
- Tsinghua University
- Renmin University of China
arxiv_id: '2610.29464'
url: https://arxiv.org/abs/2610.29464
pdf_url: https://arxiv.org/pdf/2610.29464
published: '2026-10-21'
collected: '2026-10-22'
category: QueryRec
direction: 查询改写 · 稠密检索向量融合
tags:
- Query Reformulation
- Dense Retrieval
- Pseudo-Relevance Feedback
- Generative Relevance Feedback
- Embedding Space
- Training-free
one_liner: 把反馈向量转为原查询切空间上的方向性约束并做后验融合，训练无关地提升稠密检索查询改写
practical_value: '- 可直接作为线上零训练后处理：对已有 query embedding 和 top-K 召回/LLM 生成反馈 embedding，只做切空间方向提取
  + 闭式融合，不 fine-tune 编码器，也不改文档索引。

  - 反馈置信度用两层控制：局部用 query-feedback similarity 的 MAD 鲁棒归一化再 sigmoid；集合级用证据向量均值强度 S 与方差
  V 算 coherence，并乘以平均局部质量，可避免噪音 PRF 或 LLM 生成反馈带偏改写。

  - 更新幅度用最大转角 θ_up 和集合置信度 g 做 cap：q'' = cosφ q + sinφ δ/||δ||；对电商搜索中短 query、歧义 query，可限制最大转角在
  10-30° 量级，避免改写过于激进。

  - 复杂度 O(K²D+K³)，实际 K=5 较稳；PRF 下 K 太大会噪声变大，GRF 下可适当增大，做实验时按反馈质量分别调 K。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：稠密检索依赖 query embedding，短、歧义或欠约束 query 容易表达不足。PRF 和 LLM 生成反馈能补充证据，但常见 embedding-space 融合把每个反馈向量当完整目标点做平均或插值，会压制互补方向。论文在单位球切空间中指出：点式目标 ∥δ−ℓu∥² 会分解为“支持方向误差”+“对所有正交方向惩罚”，多个反馈方向不同时会被整体置信度各向同性收缩，导致互补证据丢失。

**方法关键点**：
- 方向性证据构造：对每个反馈 f_i，先去除与 query q 平行的分量 r_i = f_i − s_i q，得到切空间方向 u_i 和幅度 ℓ_i = ∥r_i∥ = sin∠(q, f_i)。
- 分层置信度：局部质量 a_i 用 query-feedback similarity 的 MAD 鲁棒归一化后 sigmoid；集合级置信度 g = g_geo × mean(a_i)，其中 g_geo = S/(S+V/K)，S 为平均证据强度，V 为证据方差。
- 后验融合：最小化 λ/2∥δ∥² + 1/2 Σ τ_i (u_i^Tδ − ℓ_i)²，等价 MAP 推断，闭式解 δ* = U^T W (λI + WUU^T W)^{-1} Wℓ，只需解 K×K 系统。
- 球面更新：φ = min(∥δ*∥, g θ_up)，q' = cosφ q + sinφ δ*/∥δ*∥，保持 embedding 归一化。

**关键结果**：在 BEIR 14 个子集、BGE/E5/Qwen 三个 retriever、PRF/HyDE/Q2D/CoT 四类反馈上，DIFF 整体最优。以 BGE 为例，原 NDCG@10 为 0.5492；PRF 下 DIFF 0.5522，HyDE 0.5717，Q2D 0.5723；E5 原 0.5231，HyDE 下 DIFF 0.5489；Qwen 原 0.5492，HyDE 下 DIFF 0.5777。VPRF/Concat 在很多设置下反而下降，DIFF 不依赖额外检索且对 K 更稳定。

**最值得记住的一句话**：反馈不是目标点，而是只约束查询移动方向的方向性证据；控制置信度后融合，比把反馈向量平均或插值更鲁棒。
