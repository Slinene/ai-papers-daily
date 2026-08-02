---
title: 'Dynamic Exploration Graph: A Novel Approach for Efficient Nearest Neighbor
  Search in Evolving Multimedia Datasets'
title_zh: 动态探索图：支撑动态多媒体数据集高效近邻搜索的新方法
authors:
- Nico Hezel
- Kai Uwe Barthel
- Bruno Schilling
- Konstantin Schall
- Klaus Jung
affiliations:
- Visual Computing Group, HTW Berlin
arxiv_id: '2607.27640'
url: https://arxiv.org/abs/2607.27640
pdf_url: https://arxiv.org/pdf/2607.27640
published: '2026-07-30'
collected: '2026-08-02'
category: RecSys
direction: 动态向量索引 · 图算法优化
tags:
- ANNS
- Dynamic Graphs
- Graph Index
- Vector Search
- Streaming Data
one_liner: 提出动态图索引 DEG，以连通性保持顶点删除和分布无关扩展实现高效动态 ANNS
practical_value: '- 电商推荐中商品向量索引频繁增删（新品/下架），DEG 的在线动态更新机制可替代全量重建，降低工程复杂度与计算开销。

  - 顶点删除算法保证图连通性，可借鉴到召回索引的结点下线逻辑，避免因删除引发召回缺口。

  - 分布无关的图扩展不依赖数据分布先验，适合电商长尾、冷热不均的嵌入分布，维持索引平衡。

  - 流式场景下构建时间与检索吞吐优于 FreshDiskANN 等方法，适合实时推理服务，可转用到 Agent 动态知识库的向量检索模块。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：多模态数据持续变化，传统的图索引在点增删时需全量重建或损失效率，无法适应实时流式场景。方法：基于持续优化的 Exploration Graph，提出动态探索图 DEG，核心包含两个创新：1）保证连通性的顶点删除算法，通过局部重连避免删除导致图分裂；2）与数据分布无关的图扩展策略，在插入新点时自适应调整边，保持图平衡和连通度。DEG 无需预设参数，可在插入和删除操作中持续维持高效的搜索结构。结果：在 SIFT、GIST 等标准数据集上，流式（streaming）和在线（online）场景下 DEG 的构建速度与搜索 QPS 均显著优于动态图算法 FreshDiskANN，静态数据集上的召回率-速度曲线达到当前静态图 SOTA 水平（如 HNSW、NSG）。
