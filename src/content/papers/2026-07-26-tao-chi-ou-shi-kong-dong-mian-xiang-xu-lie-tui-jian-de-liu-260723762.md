---
title: 'Escaping the Euclidean Void: Manifold-Informed Flow Matching for Sequential
  Recommendation'
title_zh: 逃离欧氏空洞：面向序列推荐的流形信息流匹配
authors:
- Dengzhao Fang
- Jingtong Gao
- Yu Li
- Xiangyu Zhao
- Yi Chang
affiliations:
- Jilin University
- City University of Hong Kong
arxiv_id: '2607.23762'
url: https://arxiv.org/abs/2607.23762
pdf_url: https://arxiv.org/pdf/2607.23762
published: '2026-07-26'
collected: '2026-07-28'
category: GenRec
direction: 生成式推荐 · 流形校正与流匹配
tags:
- Flow Matching
- Sequential Recommendation
- Manifold Regularization
- Generative Recommendation
- Embedding Geometry
- Long-tail
one_liner: 指出连续生成推荐中的欧氏空洞问题，提出训练时利用共现图锚点校正路径中间态几何的 MIRAGE 框架
practical_value: '- 在生成式顺序推荐中，中间表征的语义空白(Euclidean void)导致生成性能下降，可通过训练时引入 item 共现图定义的邻居锚点进行路径正则化，重组织
  embedding 空间

  - 关键 trick：硬/软对齐锚点拉近插值态与邻居项，用时间调制 w(t)=4t(1-t) 仅在路径内部施加约束，不污染源分布和目标嵌入

  - 训练时引入图结构，推理时完全图无关（zero graph overhead），可实现一步生成（one-step），效率高且精度好，适合在线服务

  - 长尾物品因训练稀疏，其 embedding 几何不稳健，利用共现图邻居支持可显著提升长尾表现而不牺牲头部，值得在电商推荐中尝试'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：连续生成式推荐（扩散、流匹配）学习从噪声到目标 item embedding 的传输路径。标准流匹配假设的直线概率路径在欧氏空间中会穿过没有有效 item 语义的空白区域，即“欧氏空洞”（Euclidean void）。这导致路径中间状态缺乏语义支撑，向量场预测不准，尤其伤害稀疏（长尾）物品。

**方法关键点**：
- **整体框架 MIRAGE**：基于 target-recovery 流匹配 backbone（直接预测干净目标 embedding），在训练时引入由训练集 item 共现图定义的邻居锚点，施加拓扑正则化项 $\mathcal{L}_{\text{topo}}$。
- **锚点对齐**：对每个路径插值状态 $\bm{x}_t$，将其拉近到目标物品 $i_+$ 的 $K$ 个共现邻居中最近者（硬对齐）或由温度控制的软跨度加权质心（软对齐），从而重构 embedding 空间。
- **时间调制**：采用二次函数 $w(t)=4t(1-t)$ 只在路径内部（$0<t<1$）施加正则化，保证源噪声和目标嵌入不受污染。
- **训练与推理分离**：图结构仅用于训练，推理时无任何图查寻，保留一步生成效率（$q=1$ 即直接预测目标 embedding）。

**关键实验**：
- 数据集：Amazon Beauty, Sports, Toys, CDs（含长尾特性）。
- 基线：传统（SASRec, LightGCN, BERT4Rec 等）、扩散（ADRec, DiffuRec, DimeRec 等）、流匹配（FMRec, FAVE）。
- 主要结果：MIRAGE 在所有数据集和指标上均最优，例如 Sports 上 H@20 比最强基线 FMRec 高 10.70%，Toys 高 11.69%；长尾物品在 Sports 尾部长尾 H@20 提升 14.0%。
- 消融证实拓扑正则化、时间调制、路径内部施加的必要性；一步推理延迟最低。

**金句**：MIRAGE 保留原有概率路径，训练时使用图但推理时完全无图，实现了准确高效的一步生成。
