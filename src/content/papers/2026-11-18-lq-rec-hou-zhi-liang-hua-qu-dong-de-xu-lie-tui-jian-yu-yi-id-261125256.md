---
title: 'LQ-Rec: Late Quantization for Sequential Recommendation'
title_zh: LQ-Rec：后置量化驱动的序列推荐语义 ID 生成检索
authors:
- Satoshi Koide
- Yueqi Wang
- Julian McAuley
affiliations:
- Toyota Motor North America
- UC San Diego
arxiv_id: '2611.25256'
url: https://arxiv.org/abs/2611.25256
pdf_url: https://arxiv.org/pdf/2611.25256
published: '2026-11-18'
collected: '2026-11-20'
category: GenRec
direction: 生成式推荐 · 后置量化 / Semantic ID
tags:
- Late Quantization
- Semantic ID
- Generative Retrieval
- Sequential Recommendation
- Residual Quantization
- Non-autoregressive
one_liner: 提出后置量化，将离散化限制在 item 侧，实现语义 ID 长度单调提升排序且单模型任意截断推理
practical_value: '- 在语义 ID 召回中采用后置量化：序列 encoder 读连续 item embedding，量化只放候选 item 侧；这样避免
  AR 解码 M 步，推理只需一次 encoder forward + prefix-tree beam search，且召回随 ID 长度单调提升。

  - 训练量化码本不要只用重建 MSE 或 post-hoc k-means；用 ranking loss 联合训练 codebook。可复用两阶段：Stage1
  STE + soft-to-hard CE 从连续到量化退火；Stage2 冻结 encoder，对所有 prefix L 联合 CE 微调（Prefix-MQA），得到单
  checkpoint 任意截断的 anytime compression。

  - 完全 content-based item encoder（冻结 text encoder + MLP）去掉 item ID embedding，冷启动/新品友好；配合残差码本存储
  O(NM+MKd) 比稠密表轻，适合电商大 catalog。

  - 残差量化前缀树做高效 beam search：每个 beam 携带 partial score，扩展时只查 K 个 centroid 内积 + trie prune，不要每步重跑
  transformer；可迁移到离散索引/工具检索场景。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
自回归生成式检索（TIGER 等）把 item 压缩为 semantic ID 后自回归解码，但序列编码器读取量化 token，导致预测与量化耦合：ID 长度 M 越大，编码器注意力为 O((MN)^2)，自回归解码还需 O(bM) 次额外 forward，且长 ID 不保证排序提升。

### 方法关键点
- **Late Quantization（后置量化）**：量化只放在输出侧（item 侧）；序列编码器 T 和打分始终在连续空间，item 经残差量化器 Q 生成 semantic ID 和重构向量。推理只跑一次 encoder，通过 prefix tree beam search 按内积打分，无额外 transformer forward。
- **可加误差分解与排序界**：量化分数 = 连续分数 + ⟨u,δ_i⟩；成对排序在 margin > ε_i+ε_j 时保持，Recall@K 下界由 per-item 量化误差和 margin 控制。训练目标可分离：encoder 用连续 loss，codebook 用量化 loss。
- **两阶段训练 LQ-Rec**：Stage1 S2H-QA 用 STE 混合连续/量化 CE 从软到硬退火 + commitment；Stage2 Prefix-MQA 冻结 encoder，对所有前缀 L=1..M 联合 CE 微调 codebook，实现单 checkpoint 任意截断。
- **Content-based item encoder**：冻结 text encoder + MLP，不学 item ID embedding，冷启动友好。

### 关键结果
在 Amazon Toys/Beauty/Sports + Yelp 上对比 TIGER/LC-Rec/LETTER/VQ-Rec/RPG 等：LQ-Rec M=16 多数指标最优；Recall@10 比 RPG 在 Toys +19%、Sports +31%、Yelp +57%。单个 M=16 checkpoint 在 L=4/8/16 单调递增，并超过单独训练 baseline。Mem/Gen 泛化显著领先，Gen NDCG@10 全数据集最优；推理 latency 和 catalog memory 均 Pareto 最优。消融显示 joint ranking-codebook 训练、Prefix-MQA、量化感知训练都是关键。

### 一句话
量化器的位置决定检索误差是否可分离：把离散化留在 item 侧，编码器永远读连续表示，就能获得可加分解、排序界限和任意截断。
