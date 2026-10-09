---
title: Compact and Efficient Indexes for Learned Sparse Retrieval
title_zh: 面向学习型稀疏检索的紧凑高效索引
authors:
- Franco Maria Nardini
- Luca Rizzo
- Cosimo Rulli
- Rossano Venturini
affiliations:
- ISTI-CNR
- University of Pisa
- Linkup
arxiv_id: '2610.12300'
url: https://arxiv.org/abs/2610.12300
pdf_url: https://arxiv.org/pdf/2610.12300
published: '2026-10-08'
collected: '2026-10-09'
category: RecSys
direction: 稀疏检索索引压缩 · SEISMIC
tags:
- Learned Sparse Retrieval
- Index Compression
- SIMD
- Quantization
- SEISMIC
- Forward Index
one_liner: 用 medoid 替代 block summary，并压缩前向索引组件与值，实现同等精度下最多 5.3× 提速、约 3× 省内存
practical_value: '- SEISMIC 类两段式检索可直接把 block summary 换成 medoid：块元数据从几百字节稀疏向量缩到一个 8
  字节 doc id，省下的空间可用于更细分块；召回下降通过调低 heap_factor（如 0.9→0.7）补偿，适合内存敏感场景。

  - 前向索引压缩与 selector 解耦，可单独接入 KANNOLO/HNSW 等已有系统：先用递归图二分重排 vocabulary，再对 delta-gap
  做 8 整数块 SIMD bit-packing，配合 gather/FMA 融合 decode 与点积，避免 decompress-then-process
  的内存墙；在 SPLADE-v3 上可近半减前向索引内存。

  - 值量化优先考虑 per-component 4-bit：SPLADE 类非负权重可近似 v≈w*k 去掉 offset，每条匹配仅保留一次 FMA；k-means
  centroid 量化在低 bit 下比 scalar 更稳，可用一半 8-bit 内存恢复大部分精度。

  - 若业务有“短 query、长 document”的 inference-free retriever 或 push 选词场景，可用 JUMPDOT：固定 16
  entry/块，按 query component 与 block max 跳过不匹配块，获得约 2.1–2.4× 加速，额外内存开销 <2%。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
Learned sparse retrieval 在 SPLADE 等模型上效果强、可解释、OOD 扩展好，但索引内存已成为比延迟更尖锐的瓶颈。SEISMIC 的 block summary 约占总索引近一半，前向索引又常不压缩或只用全局量化，导致 RAM 成本高。

**方法关键点**
- Selector：用 block 内已有文档作为 medoid 替代合成 summary，把每个 block 元数据从稀疏向量缩成一个 doc id；可用更细分块换空间，并用 heap_factor 补偿召回下降。
- 前向索引组件压缩：先对 vocabulary 做 RGB 重排让共现 term 聚集，再对 delta-gap 做 8 整数块 SIMD bit-packing，DOTPACKING8 将解压与 gather/FMA 点积融合；DP 变体自适应块宽，clustered reference 版用 double gather。
- 前向索引值压缩：按 component 独立做 4-bit 标量或 k-means 量化；非负分量可省略 offset，4-bit 恢复大部分 8-bit 精度。
- JUMPDOT：固定 16 个 entry/块，按 query component 与块最大值跳过不匹配块，适合短 query、长 doc 的 inference-free retriever。

**关键实验**
在 MSMARCO dev 上覆盖 SPLADE、LILSR、SPLADE-v3，对比 SINDI、KANNOLO、原始 SEISMIC、Qdrant。同等精度下新 SEISMIC 比 SINDI 快最多 5.3× 且省约 3× 内存；最紧内存预算仍快 1.9×、省最高 3.9×；DOTPACKING8 让 KANNOLO 在 SPLADE-v3 上内存近减半。

**值得记住**
Learned sparse 索引要同时压 selector metadata 与 forward index，编码不能只看 BPI，必须把 decode 和 dot-product 放进 SIMD 管道里融合，否则内存墙会吃掉压缩收益。
