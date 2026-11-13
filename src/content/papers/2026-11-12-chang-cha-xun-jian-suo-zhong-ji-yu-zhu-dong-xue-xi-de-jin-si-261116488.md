---
title: Active Learning of Approximate LLM Ranking for Energy-Efficient Retrieval of
  Long Queries
title_zh: 长查询检索中基于主动学习的近似 LLM 排序节能框架
authors:
- Ohad Porat
- Elad Yom-Tov
affiliations:
- Department of Computer Science and Artificial Intelligence, Bar Ilan University
arxiv_id: '2611.16488'
url: https://arxiv.org/abs/2611.16488
pdf_url: https://arxiv.org/pdf/2611.16488
published: '2026-11-12'
collected: '2026-11-13'
category: LLM
direction: LLM 排序近似与主动学习
tags:
- LLM ranking
- active learning
- energy efficiency
- BM25
- hybrid retrieval
one_liner: 用主动学习少量标注文档训练轻量排序器，代替大量 LLM 重排，在长查询上以 3.3% 能耗达到 87% P@10
practical_value: '- 对需要 LLM 精排的搜索/推荐场景，不必对全部候选做 LLM 重排；先用 BM25 或双塔召回，再用主动学习挑出最不确定或最具代表性的候选让
  LLM 打分，训练一个小型评分器在线服务，可大幅降低 GPU/能耗成本。

  - 长查询、上下文丰富的 query 是 LLM 语义能力的最大收益区；线上可按 query 长度/复杂度路由：冗长 query 走“LLM 标注 + 轻量近似”路径，短查询直接用
  BM25 或现有召回，避免浪费算力。

  - 能量-精度是可调预算：设置 per-query LLM 调用预算（例如只标注 top-K 个不确定文档），形成连续 trade-off 曲线；在电商搜索或推荐线上可根据商业价值、高峰负载动态调整。

  - 主动学习选择策略可复用：不确定性采样、多样性采样或两者结合，用于构建轻量模型逼近 LLM 偏好，降低人工/标注成本。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：检索中 BM25 等词法匹配速度快、能耗低，但处理长查询时语义理解弱；LLM 重排能提升长查询效果，但推理成本与能耗过高，难以在线部署。

**方法关键点**：LAAM 在 BM25 召回与 LLM 重排之间引入轻量学习评分器；主动学习循环中，由 LLM 只标注少量信息量最大的文档，逐步更新该评分器；将 LLM 计算集中在高不确定或高收益样本。

**关键结果**：TREC Robust 2004 上以 DeepSeek v3 为 LLM；verbose queries 下，LAAM P@10 达 0.459（DeepSeek 为 0.526），保留约 87% 精度，但每查询能耗仅 3.3%；平均精度与 DeepSeek 无显著差异，显著优于 BM25；MAP 仍低于 DeepSeek；能量-精度曲线呈明显边际递减。
