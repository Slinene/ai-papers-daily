---
title: Lossless Compression of Proximity Graph Indexes for Efficient Approximate Nearest
  Neighbors Search
title_zh: 面向高效近似最近邻搜索的邻近图索引无损压缩
authors:
- Francesco Benocci
- Leonard Dahlmann
- Francesco Gargiulo
- Tobias Heuer
- Silvio Martinico
- Franco Maria Nardini
- Cosimo Rulli
- Rossano Venturini
affiliations:
- ISTI-CNR
- eBay Inc.
- University of Pisa
arxiv_id: '2610.37176'
url: https://arxiv.org/abs/2610.37176
pdf_url: https://arxiv.org/pdf/2610.37176
published: '2026-10-27'
collected: '2026-10-29'
category: Other
direction: 向量检索 · HNSW 图索引压缩
tags:
- HNSW
- graph compression
- vector search
- SIMD
- Stream VByte
- ANN
one_liner: 通过离线图置换制造结构局部性，用 SIMD 整数压缩器快速解压 HNSW 邻接表，压缩率最高 52.7% 且延迟近零损失
practical_value: '- 电商/广告向量召回中 HNSW 内存吃紧时，先定位边存储占比：若向量已量化、图边成为主要开销，可对邻接表做离线节点重编号，再使用
  Stream VByte 等 SIMD 整数压缩器，在线边解压边遍历，基本不损失延迟。

  - 关键 trick 是离线图置换：人为让邻接表内的 ID 分布更集中，能显著提升整数压缩器的压缩率；业务上可直接对 item/user embedding 的
  HNSW 索引做同样的重编号，无需改召回精度。

  - 如果已经在用 PQ/Scalar quantization，此方法可叠加使用，进一步降低 HNSW 整体内存，缩小索引集群规模或支持更大规模向量库。

  - 工程落地优先选 SIMD 友好的解压器（如 Stream VByte），避免复杂熵编码带来的分支和延迟；上线前需重点验证查询 P99/P999 延迟，并做无损压缩以避免召回质量回退。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：HNSW 等图索引是现代向量搜索的核心，但内存开销巨大；向量量化普及后，图边结构在总内存中的占比越来越高。线上查询时解压发生在图遍历路径上，因此压缩不能牺牲查询延迟。

**方法关键点**：对 HNSW 图进行离线节点重编号/置换，人为制造邻接表内的结构局部性；基于这种局部性，使用 SIMD 加速整数压缩器（如 Stream VByte）压缩邻接表。查询时按需快速解压，属于无损压缩。

**关键结果**：在多个真实负载上，压缩率最高达 52.7%，相比未压缩基线延迟损失可忽略；在 eBay 生产系统部署后边存储最高降低 44.3%，查询延迟无退化。
