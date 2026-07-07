---
title: 'Relevance-Based Embeddings: Lightweight Candidate Retrieval via Heavy-Ranker
  Calls'
title_zh: 基于相关性的嵌入：用重排序器调用实现轻量级候选检索
authors:
- Kirill Shevkunov
- Andrey Ploskonosov
- Liudmila Prokhorenkova
affiliations:
- Yandex
arxiv_id: '2607.03515'
url: https://arxiv.org/abs/2607.03515
pdf_url: https://arxiv.org/pdf/2607.03515
published: '2026-07-03'
collected: '2026-07-07'
category: RecSys
direction: 轻量级候选召回 · 相关性嵌入
tags:
- relevance-based embeddings
- candidate retrieval
- heavy ranker
- support set selection
- CUR decomposition
- lightweight retrieval
one_liner: 利用重排序器评分构造查询与物品的相关性向量，通过神经网络映射为嵌入，可近似任意复杂相关函数且参数极少。
practical_value: '- **直接复用重排序器分数作为特征**：如果业务中已有性能很强的重排序模型（如 CatBoost 或大型 CE），可将其对少量「支持集」的打分向量作为查询和物品的表示，无需额外特征工程，就能训练一个超轻量召回模型（参数量可低至
  50K，而基线双塔有 300M+）。

  - **支持集选择策略是核心杠杆**：实验表明，简单的 KMeans 聚类中心或 l2-greedy 贪婪选点比随机选支持集提效显著（HitRate@100 相对提升
  10~20 个百分点）。在电商推荐中，可直接按一级类目聚类、或用高频交互物品作为支持集，零额外成本提升召回质量。

  - **训练时组合 CUR 近似与可学习残差**：将初始化嵌入设为 CUR 分解得到的系数，再用浅层 MLP 学习残差，能稳定训练并进一步提点，这一技巧可迁移到任何用评分向量构建序列表征的场景。

  - **灵活应对物品冷启与动态库**：对新物品只需计算其与固定支持查询的相关性向量，立即获得嵌入，无需重训嵌入表；在物品集固定的情形下，也可以直接用可训练 embedding
  代替 f_I，大幅减少线上重排调用次数。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
在搜索、推荐等大规模检索场景，最终排序模型（重排序器）精准但昂贵，无法对全量物品打分。常用方案是把双塔模型（DE）的嵌入做近似最近邻检索，再用重排器 rerank，但 DE 无法利用仅存在于 query-item 对上的重要特征，且通常需要巨大参数量和训练数据。已有 AnnCUR 利用 CUR 分解用随机选择的支持集来近似重排分数，但随机选支持集远非最优。

**方法关键点**
- **相关性向量表示**：将查询 q 表示为它对固定支持物品集 S_I 的重排分数向量 R(S_I, q)，将物品 i 表示为它对固定支持查询集 S_Q 的重排分数向量 R(i, S_Q)。用定理 3.2 证明只需含少量支持项的这种向量，通过 MLP 映射为嵌入后做点积，就能以任意精度逼近任意连续相关函数（包括含 pairwise 特征的重排器）。
- **支持集选择策略**：对比多种策略：随机、热门、KMeans/凝聚聚类中心、最大多样性、以及理论驱动的 l2-greedy（贪婪地最小化 CUR 近似的全局 MSE）。l2-greedy 几乎在所有数据集上最优；简单的 KMeans 聚类中心也能带来显著提升。
- **训练与推理**：训练时将嵌入分解为 CUR 近似部分 + 可训练的 MLP 残差，用 listwise 损失优化。推理时先查询对 m 个支持物品打分得到查询向量，再通过 ANN 检索预计算的物品向量，候选重排时可将省下的 m 次重排调用用于更多候选。

**关键结果**
在 ZESHEL 实体链接、MS MARCO 问答、以及 Yandex Games/Music 生产推荐数据上实验。对比 AnnCUR、强生产级双塔和 AXN。以 HitRate 衡量：
- 支持集选择：l2-greedy 的 HitRate@100 在多个数据集上比随机提升 10-29 个百分点（如 Military: 0.3357 vs 0.2455）；KMeans 也有类似提升。
- 神经网络映射：RBE+l2-greedy 在 QA 上达到 0.6022，显著优于 AnnCUR 的 0.5700；RecMusic 上从 DE 的 0.3792 提升到 0.3964（HitRate@100）。
- 与生产双塔对比：给定相同重排调用预算，RBE 在较大候选集时明显超越双塔和 AXN DE。例如 RecGames1 上召回 100 个最佳物品时，DE 的 HitRate@100 为 0.7048，RBE 为 0.6682，但重排调用仅 100 次；当预算提升到 900 次重排时，RBE 的 HitRate@100 达 0.9799，远超同预算的 DE（0.9561）。且 RBE 模型参数仅 ~50K，远小于 DE 的 300M+。
