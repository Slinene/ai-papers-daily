---
title: Fast and Efficient Approximate Nearest Neighbor Search for High-Dimensional
  LLM Embeddings
title_zh: 面向高维LLM嵌入的快速近似最近邻搜索
authors:
- Nico Hezel
- Kai Uwe Barthel
- Bruno Schilling
- Konstantin Schall
- Andre Moelle
- Klaus Jung
affiliations:
- Visual Computing Group, HTW Berlin
- vviinn, Berlin
arxiv_id: '2607.20957'
url: https://arxiv.org/abs/2607.20957
pdf_url: https://arxiv.org/pdf/2607.20957
published: '2026-07-23'
collected: '2026-07-24'
category: RecSys
direction: 向量近似最近邻搜索加速
tags:
- ANNS
- EVP
- FLAS
- MIPS
- graph-indexing
- cache-locality
one_liner: 通过EVP量化与1D预排序优化图索引构建，大幅提升LLM嵌入向量搜索的构建速度与缓存效率
practical_value: '- 工业推荐系统向量召回阶段，可借鉴EVP空间划分量化，加速图索引构建，同时配合定向重排序保证召回率。

  - 处理非归一化嵌入（如LLM特征）做MIPS时，使用维度扩充技巧转换为欧氏距离搜索，复用成熟ANN库而不必重新实现内积索引。

  - FLAS一维预排序方法能显著改善图遍历时的内存局部性，适合在线服务低延迟要求，可集成到现有HNSW等图索引构建流程的前置步骤。

  - 资源受限线上环境（如8核CPU、24GB内存）下，本文技术组合提供了一个低开销高性能的ANNS方案参考，便于算法落地。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：大规模推荐与搜索系统依赖高维LLM嵌入的近似最近邻搜索（ANNS），但在严格资源限制下，图索引构建慢、查询缓存命中率低制约效率。SISAP 2026挑战引入10亿级非归一化向量任务，要求兼顾构建速度与查询延迟。

**方法关键点**：
- 利用**Equi-Voronoi Polytopes (EVP)** 进行高效矢量量化加速图构建，辅以定向重排序维持高召回。
- 针对**最大内积搜索（MIPS）**，将非对称内积问题通过维度扩充转化为欧氏空间，统一采用欧氏距离图索引。
- 提出**快速线性分配排序（FLAS）**，在图构建前对向量做一维预排序，极大提升图遍历时的空间局部性与CPU缓存命中率，降低查询延迟。

**关键结果**：在8核CPU、24GB内存约束下，方法在kNNG构建速度与MIPS查询延迟上均取得显著提升（具体数值见原文），实现了高召回下亿级向量的高效搜索。
