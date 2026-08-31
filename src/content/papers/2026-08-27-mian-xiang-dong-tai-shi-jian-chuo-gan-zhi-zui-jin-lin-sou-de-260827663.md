---
title: A Versioned Unified Graph Index for Dynamic Timestamp-Aware Nearest Neighbor
  Search
title_zh: 面向动态时间戳感知最近邻搜索的版本化统一图索引
authors:
- Jun Woo Chung
- Weijie Zhao
affiliations:
- Rochester Institute of Technology
arxiv_id: '2608.27663'
url: https://arxiv.org/abs/2608.27663
pdf_url: https://arxiv.org/pdf/2608.27663
published: '2026-08-27'
collected: '2026-08-31'
category: RecSys
direction: 时间感知向量检索加速
tags:
- ANN
- Time-aware
- Graph Index
- Vector Search
- Dynamic Dataset
one_liner: TiGER 用版本化统一图支持任意时间区间 ANN 查询，无需过滤或分段子图，QPS 提升 5 倍
practical_value: '- **时效性召回加速**：电商推荐中经常需要按时间范围过滤商品/内容向量（如近期上新、近 N 天行为），TiGER 的统一图结构可直接查询任意时间区间，避免
  post-filtering 造成的召回缺失或延迟，适合做实时召回层。

  - **动态向量库无需反复重建**：商品 embedding 频繁增删，传统分段子图需维护多张图或重建；TiGER 的版本化连通性支持动态更新，可降低流式更新成本。

  - **RAG/Agent 场景的时间敏感检索**：在 Agent 工作流中，需要检索“最近发生”的文档或事件，TiGER 可作为底层向量索引，提升时间过滤场景下的检索效率，避免先召回再过滤的性能损耗。

  - **工程实现启发**：如果业务中已用 HNSW 等图索引，可以考虑引入版本化边/节点管理，避免为每个时间范围单独建图，减少内存与同步开销。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：时间感知的近似最近邻搜索在实时推荐、日志分析、RAG 等场景中需求强烈，但现有方法要么先做 ANN 再按时间戳过滤（post-filtering），要么为每个时间分段维护子图，导致效率低、内存大或漏召回。

**方法关键点**：TiGER 构建并维护一个统一的图索引，引入“版本化连通性”（integrated versioned connectivity），将时间信息编码到图的边版本中。查询时直接在统一图上进行任意时间区间的 ANN 搜索，无需遍历无效向量，也无需合并多个子图。

**关键结果**：实验表明，与基于过滤或按时间分段子图的基线相比，TiGER 在保持精度的前提下，QPS 最高提升 5 倍。该方法可支持动态数据集上的实时时间分析，适用于推荐系统、日志检索等场景。
