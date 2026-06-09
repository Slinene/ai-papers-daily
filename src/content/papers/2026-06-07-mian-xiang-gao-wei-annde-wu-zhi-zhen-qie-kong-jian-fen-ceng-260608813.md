---
title: 'Aperon Technical Report: Hierarchical No-Pointer Tangent-Local Search for
  High-Dimensional Approximate Nearest Neighbors'
title_zh: 面向高维ANN的无指针切空间分层搜索方案
authors:
- Yong Fu
affiliations:
- Substratum Labs
arxiv_id: '2606.08813'
url: https://arxiv.org/abs/2606.08813
pdf_url: https://arxiv.org/pdf/2606.08813
published: '2026-06-07'
collected: '2026-06-09'
category: Other
direction: 近似最近邻搜索 · 向量索引与缓存优化
tags:
- ANN
- VectorSearch
- SIMD
- Block-SoA
- Tangent-Local Projection
one_liner: 用局部切空间降维与无指针Block-SoA布局替代图索引，实现3.6倍提速与近乎零缓存缺失。
practical_value: '- 电商推荐系统的向量检索引擎可借鉴“聚类-局部 PCA-无指针扫描”策略：将物品 embedding 按簇划分，簇内用少数主成分重建，避免全量高维点积，同时利用
  Block-SoA 布局提升 SIMD 效率，减少缓存失败。

  - Agent 需要瞬时零拷贝分支与快照时，可参考 HNTL 将向量数据组织为只读 Block-SoA，配合分层索引实现轻量级版本切换，无需复制大量指针图。

  - 在高并发场景下，无指针的连续内存布局比图遍历更 CPU 流水线友好，可直接迁移到 Rust/C++ 推理服务中减少停顿，实现每向量 < 5ns 的扫描性能。

  - 当新物品增量加入时，只需更新局部 PCA 基即可保持高召回，适合推荐 embedding 频繁更新的环境。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：近似最近邻搜索中，HNSW 等图索引存在严重的“指针税”，占用大量内存且不规则访存导致 CPU 流水线停顿，难以满足高吞吐向量检索需求。

**方法**：提出 HNTL，将高维空间划分为多个局部一致的“颗粒”，每个颗粒内用局部 PCA 将向量降至低维切空间坐标。存储采用无指针的 Block-SoA 布局，便于 SIMD 顺序扫描。查询时依次扫描各颗粒的低维坐标，快速过滤出候选集，再对极小候选集做精确重排。

**结果**：在 d=768、N=10,000 的各向异性流形数据上，局部 PCA 保留 96.3% 方差，仅用 20 个候选即实现 Rerank Recall@10=1.000。Apple kperf PMU 计数器显示，NEON 自动向量化的扫描引擎达到 4.137 ns/向量，相比传统指针跳转图遍历快 3.61 倍，IPC 提升 3.59 倍，L1/L2 数据缓存缺失接近零。
