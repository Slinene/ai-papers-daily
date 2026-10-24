---
title: Getting a GRIP on Graph-Based Search for Learned Sparse Retrieval
title_zh: 从图搜索入手改进学习型稀疏检索
authors:
- Vihan Lakshman
- Franco Maria Nardini
- Cosimo Rulli
- Rossano Venturini
affiliations:
- MIT CSAIL
- ISTI-CNR
- Linkup
- University of Pisa
arxiv_id: '2610.30425'
url: https://arxiv.org/abs/2610.30425
pdf_url: https://arxiv.org/pdf/2610.30425
published: '2026-10-21'
collected: '2026-10-24'
category: RecSys
direction: 稀疏检索 · 图索引加速
tags:
- Learned Sparse Retrieval
- Graph-based ANN
- Inverted Index
- SPLADE
- Approximate Nearest Neighbor
- Latency Optimization
one_liner: 提出 GRIP 图索引系统，将倒排启发式融入图搜索，在 MS MARCO v2 上比 Seismic 快 2.5 倍
practical_value: '- 如果业务在用 SPLADE、BGE-M3 sparse 等做大规模召回，不要默认倒排索引最优；可以评估 GRIP 这类图索引在商品/广告库上的
  recall-latency，尤其在线服务对 95% recall@10 敏感时。

  - 三个 trick 可拆开迁移：term-based entry point seeding 可插到 HNSW 等通用图 ANN 的初始节点选择；sparse
  sketching 适合高维稀疏 embedding 的快速距离裁剪；sparse partition-based 构图可适配电商 SKU 或类目聚集的稀疏分布。

  - 如果线上同时维护倒排和图索引，可以用倒排表的高权重 term 作为图入口点或构图先验，降低重构图成本；增量更新时优先围绕高分词、高曝光 item 重建局部图。

  - 注意标准 dense ANN 直接套到 sparse vectors 效果差，迁移前要做小规模 benchmark，关注稀疏度、term 分布和维度差异。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

动机：学习型稀疏检索（LSR）兼具神经表示泛化能力和关键词可解释性，近年来在 IR 中广受关注。现有系统以倒排索引（如 Seismic）为 SOTA，社区普遍认为图 ANN 在 LSR 上劣于倒排。本文挑战这一默认认知。

方法关键点：提出 GRIP，将倒排索引的强项注入图搜索，包含三项加速技术：
- 基于 term 的入口点 seeding：利用文档高权重词选择图遍历入口，类似倒排表定位；
- 通过 sparse sketching 做近似路由，降低高维稀疏距离计算开销；
- 基于稀疏分区的图构建，按稀疏向量结构组织图邻域。

关键结果：在 MS MARCO v2（138M passages）和 SPLADE embeddings 上，GRIP 在 95% recall@10 下比 SOTA 倒排系统 Seismic 延迟快 2.5 倍。结果表明倒排索引不应再被视为 LSR 部署的默认选择。
