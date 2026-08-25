---
title: Hypergraph Embedding Indexing for Efficient Dense Vector Retrieval
title_zh: 超图嵌入索引：高效稠密向量检索
authors:
- Kishore Konda
affiliations:
- Sodhana
arxiv_id: '2608.22980'
url: https://arxiv.org/abs/2608.22980
pdf_url: https://arxiv.org/pdf/2608.22980
published: '2026-08-24'
collected: '2026-08-25'
category: Other
direction: 向量检索 · 倒排索引
tags:
- Dense Retrieval
- ANN
- Inverted Index
- Hypergraph
- Embedding Indexing
one_liner: HEI 按高激活潜维度组合组织文档，用倒排索引生成候选并保留语义排序
practical_value: '- 在电商向量召回中，可将商品/用户 embedding 的高激活维度组合构造成倒排索引，替代或混合 HNSW，降低线上粗排阶段延迟与内存占用；适合作为大规模候选生成层。

  - 采用多个互补超图（不同维度子集、不同激活阈值、不同语义簇）做多路召回，再融合重排，能提升长尾商品或冷门内容的覆盖，避免单超图维度增加带来的组合爆炸。

  - 引入 activation diversity 作为诊断指标：评估当前训练出的 embedding 是否适合坐标倒排索引；若 diversity 低，可考虑加稀疏正则、维度解相关或调整训练目标，使向量更可索引。

  - 该框架对 embedding 的稀疏/高激活特性有依赖，在业务中可先对已有向量做激活分布分析，判断是否值得迁移到倒排索引路线。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：现有 ANN 索引把 embedding 当作高维空间中的不可分割点，忽略了维度激活的组合结构。

方法关键点：
- HEI 将文档按照高激活的潜在维度组合映射到超图，利用倒排索引风格生成候选，同时保留稠密向量的语义排序能力。
- 通过构建多个互补超图提升召回覆盖，避免单超图增加维度时出现的组合增长问题。
- 提出 activation diversity 作为诊断指标，衡量 embedding 维度激活的多样性，用于评估坐标倒排框架下的索引效率。

关键结果：论文未提供具体实验数字，重点在于建立索引框架、覆盖扩展方式与可索引性度量。
