---
title: Quantum-Inspired Pairwise Ranking Aggregation via Active LLM Feedback
title_zh: 量子启发式成对排序聚合与主动 LLM 反馈用于文档重排
authors:
- Quan Mai
- Susan Gauch
- Gibson Nkhata
affiliations:
- University of Arkansas, Fayetteville
- Walmart Inc. Applied AI
arxiv_id: '2610.38683'
url: https://arxiv.org/abs/2610.38683
pdf_url: https://arxiv.org/pdf/2610.38683
published: '2026-10-28'
collected: '2026-10-30'
category: RAG
direction: 量子启发式排序聚合 · LLM 主动反馈
tags:
- Ranking Aggregation
- LLM-as-Judge
- Reranking
- Quantum-Inspired
- Active Feedback
- BEIR
one_liner: 只用高分歧文档对的少量 LLM 判断学习多路检索融合权重，以约 30 次调用逼近 SOTA 零样本 LLM 重排效果
practical_value: '- 如果线上已有多路检索/召回（BM25、dense、SPLADE）需要融合，可借鉴「只让 LLM 判高分歧 top-r 文档对」的主动采样：每
  query 约 5–30 次 LLM call 即可超过最强无监督融合，成本远低于 listwise/pairwise 全量重排，适合低延迟搜索与 RAG 候选重排。

  - 权重更新公式可直接复用：用 LLM 的 A/B 判断和 logit gap 做置信度过滤，保留高于 τ 的判断；权重 ∝ softmax(β * mean(2*P(winner|ranker)-1))。累积历史
  refit 比 momentum 更稳定更强，推荐 β=3、τ=2.5，无需训练数据或微调。

  - 最终只做线性分数融合，工程上极轻量，可缓存各 ranker 分数与融合权重，毫秒级重排；若原始 BM25 分数缺失，可用 rank-based proxy
  替代。

  - 注意当前二选一判断无法处理“两个文档都不相关”的场景，可能引入噪声；低置信度过滤只能缓解，业务可考虑增加“都不相关”选项或校准置信阈值。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：混合检索中多路排序聚合通常依赖 RRF、CombSUM 等静态无监督方法，缺乏 query 级自适应；全监督 LTR 需要标注，零样本 listwise LLM reranker 单 query 需上百次调用，成本过高。需要一种几乎无训练、极低 LLM 预算、又可在线学习融合权重的方案。

**方法关键点**：
- 把 QI-IRA 从 pointwise 扩展到 pairwise：将文档对建模为二维量子态，基检索器作为观测算子，pairwise 胜出概率为 sigmoid(score_A - score_B)，聚合概率天然是各 ranker 的线性加权。
- 主动 LLM 反馈：从 top-40 候选区中，每轮只挑 cross-ranker 分歧最大的 K=3 对文档，让 LLM 做 A/B 二选一；仅保留 logit gap ≥ τ=2.5 的高置信判断。
- 权重更新：由保留判断计算每个 ranker 的 provisional weight = mean(2*P(correct)-1)，再 softmax 归一化；支持 momentum blending（γ=0.7）和 accumulated-history refit（β=3）两种规则。
- 最终推理退化为 pointwise 线性分数加权，不保留 pairwise 矩阵，也不做 listwise prompting。

**关键结果**：在 TREC DL19/DL20 与 BEIR 的 Covid/SciFact/DBpedia/NFCorpus 上，以 BM25+nomic dense+SPLADE 为基检索器、Llama-3.1-8B-Instruct 为 judge。accumulated refit 在 6 个基准中 3 个显著超过最强无监督聚合（DL20、DBpedia、NFCorpus），且从不显著变差；5 次 LLM call 内即超过最强静态基线。在 Flan-T5-Large 同 judge 成本对比中，LLM-IRA 用 27 次调用、6003 tokens 达到 DL19 NDCG@10 66.43，超过 PRP-Graph 的 65.8（后者 483 次调用），仅比 HeapSort 66.9 低 0.47，成本约其 1/5。

**最值得记住的一句话**：用极少的高分歧 pairwise LLM 判断在线调整融合权重，就能让轻量线性融合逼近昂贵 listwise reranker，且无需任何训练。
