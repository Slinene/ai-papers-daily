---
title: 'XViewRank: Overlap-Conditioned Score Fusion for LLM-Augmented Sparse Retrieval'
title_zh: XViewRank：基于重叠条件的 LLM 增强稀疏检索分数融合
authors:
- Xinxuan Lv
- Minghan Li
- Guodong Zhou
affiliations:
- School of Computer Science and Technology, Soochow University
arxiv_id: '2610.20122'
url: https://arxiv.org/abs/2610.20122
pdf_url: https://arxiv.org/pdf/2610.20122
published: '2026-10-14'
collected: '2026-10-18'
category: QueryRec
direction: 查询扩展与多视图检索排序融合
tags:
- LLM
- Sparse Retrieval
- Rank Fusion
- Query Expansion
- Learning to Rank
- BM25
one_liner: 提出轻量检索端方法，将 BM25 分数与查询级重叠作为上下文，用小型非线性 scorer 条件融合多查询视图结果
practical_value: '- 电商搜索可参考 LLM 生成 hypothesis / step-back 等多视角 query，配合 BM25 多路召回，避免词汇不匹配；无需重建索引，工程成本低。

  - 融合时不要只依赖固定权重的 RRF：可加 query-level overlap 特征（如各路 top-k 结果重合度）和归一化分数据，训练小型非线性 scorer
  做条件融合；特征少、可解释性强，容易在线打分。

  - 收益主要在视图排名一致性低时出现，可设计动态触发策略：先计算 overlap 或一致性指标，只对低一致性的 query 走融合模型/更复杂的改写，控制延迟与成本。

  - 注意论文在 DL20 证据较弱，收益具有数据集敏感性；业务迁移前应做在线 A/B，验证是否比固定融合、单独 LLM 扩展稳定提升。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：稀疏检索（BM25）在短查询上易出现词汇不匹配，LLM 可通过生成多个视角（hypothesis、step-back）的查询来缓解；但各视角独立检索后的排序列表可能互补、冗余或产生语义漂移，固定融合（如 RRF）对每个查询不够灵活。

方法关键：XViewRank 是检索端轻量方法，对原始 query、hypothesis view 和 step-back view 分别执行 BM25；对每个候选文档池化后，保留三个归一化 BM25 分数以及三个查询级重叠（检索结果集两两之间的重叠程度）作为特征；一个小规模非线性 scorer 以重叠度为上下文，条件地重新解释各视角分数，无需对 query 和 passage 做联合编码。

结果：在 matched-input 协议下，TREC DL 2019 和 2020 上 nDCG@10 与 MAP 均数值优于 reciprocal rank fusion；其中 DL19 的 MAP 提升统计显著；分析显示收益最明显发生在视图排名一致性较低时，而 DL20 上的证据相对较弱。
