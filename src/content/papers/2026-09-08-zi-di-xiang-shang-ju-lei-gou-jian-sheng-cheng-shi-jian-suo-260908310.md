---
title: Exploring Bottom-Up Clustering for Creating Semantic IDs
title_zh: 自底向上聚类构建生成式检索 Semantic IDs
authors:
- Leah Woldemariam
- Sudhanshu Garg
- Taha Belkhouja
- Charles Kim-Yip
- Ali Sahami
affiliations:
- Cornell Tech, Cornell University
- PayPal
arxiv_id: '2609.08310'
url: https://arxiv.org/abs/2609.08310
pdf_url: https://arxiv.org/pdf/2609.08310
published: '2026-09-08'
collected: '2026-09-09'
category: GenRec
direction: 生成式推荐 · 自底向上 Semantic ID
tags:
- Semantic IDs
- Generative Retrieval
- Bottom-Up Clustering
- RQ-VAE
- Recommendation
- Codebook Utilization
one_liner: 提出自底向上层次聚类生成 Semantic IDs，保证唯一性并保留嵌入局部结构，提升下游生成式检索效果
practical_value: '- 电商生成式推荐中，可直接用自底向上聚类对商品文本 embedding 生成 Semantic IDs，避免 RQ-VAE 训练和
  codebook collapse 调参；唯一性由构造保证，不再需要追加去重码，简化线上 ID 映射。

  - 冷启动上新：新商品只需找最近邻已有商品，继承前几层码字并分配唯一末位码即可纳入生成式检索，无需重建整个 ID 空间，适合频繁上新的电商场景。

  - 层级设计中可通过 cluster size cap 控制每个簇的商品数量，避免头部类目簇过大导致解码搜索空间不均；同时监控 silhouette score、avg
  rows per ID、簇内类目纯度等指标。

  - 注意自底向上聚类簇数通常少于典型 RQ-VAE codebook，粗粒度簇的类目纯度可能下降；在强类目体系场景可结合类目树约束或增加层级来改善。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式检索（Generative Retrieval）依赖 Semantic IDs 作为 item 的离散化表示，但现有 RQ-VAE / R-KMeans 采用自上而下的 residual quantization，存在 codebook collapse 和 item collision；为去重往往追加额外码字，但 ad hoc 去重会破坏语义结构。需要在保证唯一性的同时保留 embedding 空间的局部近邻关系，以便冷启动泛化和下游检索利用。

### 方法关键点
- 用 bottom-up hierarchical clustering 替代 top-down：先在原始 item embedding 上做 MiniBatch K-Means，得到最细粒度簇；簇内对每个 item 枚举一个唯一末位码，从构造上保证无碰撞。
- 向上逐层合并：对当前簇质心按簇内 item 数加权，进行 MiniBatch K-Means / Agglomerative Clustering，得到粗粒度码字；可设 cluster size cap 强制分裂超大簇。
- 新 item 通过最近邻继承前 L-1 个码字，再在所选簇内分配唯一第 L 位码；簇过大时可再分裂，无需重建整个 SID 空间。
- 嵌入来自文本属性（title、caption、category、brand）经 Qwen 编码，适用于多模态/文本侧。

### 关键结果
- 数据集：Amazon Beauty、Sports & Outdoors，以及约 580 万 item 的自定义商品数据集。
- Baseline：RQ-VAE（3 个 codebook，每个 256，追加去重码）。
- Bottom-up 在所有数据集上 Avg. Rows per ID = 1，完全唯一；Custom 数据集 silhouette score 0.29 vs RQ-VAE 0.00，Beauty 0.07 vs -0.07，Sports 0.07 vs 0.02。
- Recall@10：Custom 0.036 vs 0.020，Beauty 0.0567 vs 0.0509，Sports 0.0327 vs 0.0328 基本持平；NDCG@10 也整体略优。
- 簇平均唯一类目数更高，因为层级簇数少于 RQ-VAE codebook，但不影响下游指标改善。

最值得记住的一句话：自底向上构造 Semantic IDs 能在不追加额外去重码的前提下同时满足唯一性和局部语义保持，且实现轻量，适合作为生成式推荐中替换 RQ-VAE 的默认 ID 构建方案。
