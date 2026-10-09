---
title: 'H2CE: Modeling Geo-Semantic Interactions for POI Reranking with Heterogeneous
  Two-Stage Cross-Encoders'
title_zh: H2CE：异构两阶段交叉编码器建模地理语义交互用于 POI 重排
authors:
- Zhengwei Bai
- Moreno D'Incà
- Danielle Class
- Alessandro Moschitti
affiliations:
- Amazon
- University of Trento
arxiv_id: '2610.11277'
url: https://arxiv.org/abs/2610.11277
pdf_url: https://arxiv.org/pdf/2610.11277
published: '2026-10-08'
collected: '2026-10-09'
category: RecSys
direction: 异构特征融合 · 两阶段 POI 重排
tags:
- POI Reranking
- Cross-Encoder
- Learning to Rank
- Geospatial
- Heterogeneous Fusion
- Pairwise Ranking
one_liner: 提出 H2CE 异构两阶段交叉编码器，融合 bucketized 数值描述与精确标量 MLP，用 pointwise+pairwise 重排
  POI，NDCG@5 达 67.48%
practical_value: '- 在电商/本地生活精排中，对价格、销量、评分、距离等强数值特征，可采用「bucketized text descriptor
  + 精确标量 MLP」双通道，并把数值 MLP embedding 与 cross-encoder [CLS] 做 latent concat；比 late weighted
  sum 更能学到 query 条件化交互。

  - 两阶段 pointwise→pairwise top-K 架构适合实时重排：Stage1 用经济模型粗排，Stage2 只对 top 10~20 做 pair
  比较，复杂度 O(N+K²)；训练 pair 时只从 Stage1 top-K 采样，避免训练/推理分布不一致。

  - 压延迟可用 half-matrix：只评 unordered pairs，再用概率互补 Mji=1-Mij 重建另一半，比较次数减半、延迟降约 26%，精度几乎不伤。

  - 零样本 LLM 重排不适合大规模候选和实时链路；本文 RankGPT 质量明显低于 fine-tuned cross-encoder，且贵得多，更适合离线标数据或小规模
  judge。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
本地搜索 POI 重排必须在延迟约束下同时处理 query 语义、地理距离、评分/评论量等数值信号。近的 POI 可能只是部分满足意图，远的 POI 语义更强，正确排序不能靠单一特征。传统 XGBoost 对数值特征建模强但语义弱；cross-encoder 语义强但不擅长数值比较；LLM 重排质量尚可但太贵。

### 方法关键点
- **异构特征编码器**：把 distance/rating/review count 做成两路——一路 bucketized 成自然语言描述（如 walkable、outstanding、substantial）拼入 cross-encoder 输入，让 self-attention 做语义-数值交互；另一路用专用 MLP 处理精确标量，保留幅度信息。
- **隐空间融合**：把 cross-encoder 的 [CLS] 与三个数值 MLP embedding 拼接后过 MLP 分类器，替代 weighted sum late fusion，能学到“query 强调 near 时 distance 更重要”的条件化 tradeoff。
- **两阶段 pointwise + pairwise**：Stage 1 对所有候选 pointwise 打分取 top-K（K=10）；Stage 2 对 top-K 做有序 pair 比较，用 Copeland 聚合；复杂度 O(N+K(K-1))，比全量 pair O(N²) 可控。
- **训练对齐**：pairwise 训练样本从 Stage1 top-10 中采样，而不是全候选均匀采样，匹配推理分布；pointwise 用 multi-pair（最多 16 pos/16 neg）提升稳定性。

### 关键结果
在 5,743 query 本地搜索测试集上，H2CE 达到 NDCG@5 67.48%、RDQ@1 67.02%。比 XGBoost LTR 的 NDCG@5 高 +22.82 个点，比零样本 LLM RankGPT 高 +35.89，比 BGE fine-tuned 高 +9.62。Pairwise 阶段单独贡献 NDCG@5 +1.98。Half-matrix 优化让延迟从 163ms 降到 120ms，NDCG@5 相对损失 <0.1%。

### 最值得记住的一句话
POI/本地生活重排的胜负手不在单一绝对分数，而在 top-K 内做相对比较，并让模型同时看到数值的语义桶和精确幅度。
