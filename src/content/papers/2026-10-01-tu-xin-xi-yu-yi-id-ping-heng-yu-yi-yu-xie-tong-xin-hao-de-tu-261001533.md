---
title: 'Neither Black nor White: Balancing Semantic and Collaborative Signals with
  Graph-Informed Semantic IDs (GrIS)'
title_zh: 图信息语义 ID：平衡语义与协同信号的分层图划分框架
authors:
- Aleksei Medvedev
- Alejandro Ariza-Casabona
- Steven Derby
- Gonzalo Fiz Pontiveros
- Xinyang Shao
- Florian Spiess
affiliations:
- Huawei Ireland Research Centre
arxiv_id: '2610.01533'
url: https://arxiv.org/abs/2610.01533
pdf_url: https://arxiv.org/pdf/2610.01533
published: '2026-10-01'
collected: '2026-10-02'
category: GenRec
direction: 生成式推荐 · 图层次 Semantic ID
tags:
- Semantic ID
- Generative Recommendation
- Graph Partition
- RQ-VAE
- DMoN
- Collaborative Filtering
one_liner: 将 Semantic ID 构建重定义为图上层次划分，统一内容型与协同型 SID 方法，两个实例带来最高 +52% Hit@10
practical_value: '- **把 SID 构建当成分层聚类/图划分，而不是单纯 representation learning**：业务里设计生成式推荐
  item tokenization 时，可以先问“什么图、怎么递归切分”，而不是只选 encoder。内容相似不等于行为相似，协同边能纠正语义聚类的偏差。

  - **RQ-GAE 的图重建正则很值得复用**：在标准 RQ-VAE 目标上加一个 subsampled neighbourhood softmax 项，直接对量化后的
  latent 做邻域预测，不需要重建全邻接矩阵，适合大 item catalog；工程上可低成本给现有 RQ-VAE 管道注入协同信号。

  - **图信息输入和重建 loss 要一起用**：消融显示只把 item embedding 换成图传播表示（APPNP）在部分数据集会掉点，只加图 loss
  更稳；两者组合才最优。如果把 APPNP 的 α 调得过大、太接近原始语义 embedding，也会损失协同增益。

  - **RecDMoN 适合小/中型 catalog，且要关注 SID 空间均衡性**：其 Gini 指数远低于 spectral clustering，说明更均衡的层级前缀对下游生成式推荐更友好；但
  dense adjacency 限制了大规模应用，需要稀疏化/采样后再考虑。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**

生成式推荐中 Semantic ID (SID) 通常被当作 representation learning：把 item 编码进量化隐空间再读码。但 SID 真正要解决的是按推荐目标做粗到细的层级组织，内容相似并不等于行为相似。只看语义 embedding 会得到“语义合理但协同错位”的 ID。已有方法把协同信号当辅助 loss 或 embedding 对齐，本质仍停留在表示学习视角。

**方法关键点**

- 将 SID 构建重定义为**递归图划分**：节点带语义内容、边带协同信号，SID 是 item 在划分树中的路径。
- 框架 GrIS 显式拆出两个可配置轴：**图构建**（窗口共现、相邻转移、会话共现、随机游走等）和**层次划分**（RQ-VAE、微分图池化等）。
- 现有内容型方法（TIGER、RQ-VAE / RQ-KMeans）成为空图特例；LETTER、MMGRec、S2GR 也在同一设计空间中。
- 两个实例：
  - **RecDMoN**：递归可微图池化，逐层用 DMoN 目标切图，最大化局部 modularity，分支路径直接成为 SID。
  - **RQ-GAE**：在图信息 item 表示（APPNP）基础上做标准 RQ-VAE，并加入图重建 loss；为避免重建大邻接矩阵，采用 mini-batch 内 subsampled neighbourhood softmax。

**关键实验与结果**

在 Amazon Beauty / Sports / Toys / Books、MIND、Yelp 六个数据集，下游固定为 TIGER T5 生成式 backbone。

- RecDMoN 在 Toys 上比 LETTER 提升 **+52% Hit@10**，Beauty +28.9%，Sports +38.0%。
- RQ-GAE 在 Books 上比 LETTER 提升 **+34.1% Hit@10**，Yelp 上 +83.5% Hit@10；在 Beauty / Toys / Books / Yelp 稳定居前二。
- SID 空间诊断显示，RecDMoN 的层级 Gini 指数远低于 spectral clustering，说明前缀层级更均衡、SID 空间利用更充分；RQ-GAE 的 codebook 利用率显著高于 LETTER / MMGRec / S2GR。
- 更换更强 sentence embedder（Qwen3-Embedding-0.6B）后，RecDMoN 提升更明显，说明更依赖原始语义空间的划分方法对 embedder 质量更敏感。

**最值得记住的一句话**

SID 构建的本质不是压缩 item 表示，而是对 item 协同图做递归划分；显式分离图构建与划分算法后，语义、协同和结构信号可以像搭积木一样组合评估。
