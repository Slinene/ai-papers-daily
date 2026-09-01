---
title: 'RSLM: Training-Free Vector Quantization for Approximate Nearest Neighbor Search'
title_zh: RSLM：面向近似最近邻搜索的训练自由向量量化
authors:
- Rastislav Lenhardt
- Teodora Dobos
- Thomas Vecchiato
- Jiri Isa
- Igor Ginzburg
affiliations:
- Google Zurich
- Technical University of Munich
- University of Copenhagen
- Google San Jose
arxiv_id: '2608.30384'
url: https://arxiv.org/abs/2608.30384
pdf_url: https://arxiv.org/pdf/2608.30384
published: '2026-08-31'
collected: '2026-09-01'
category: Other
direction: 向量检索 · ANN索引量化
tags:
- ANN
- Vector Quantization
- Training-Free
- FWHT
- MIPS
- Residual Quantization
one_liner: 训练自由的分块旋转量化方案，在1-4bit/维下保持召回，降低ANN索引内存与带宽
practical_value: '- 在 IVF/树型索引的 rescoring 阶段，用训练自由旋转量化（尤其相对残差量化）替代 trained PQ/SQ，可省去离线
  k-means 训练，快速接入新 embedding 版本或新业务数据集；4-bit RelApproxGlobal 在多个数据集达到 100% recall@20@30，2-bit
  达 99%+ recall@20@40，适合 RAG/推荐候选召回的大候选池。

  - 采用 block-wise FWHT（块大小 128）实现 O(D) 旋转复杂度，避免 dense rotation O(D^2) 和全局 FWHT 的维度
  pad 问题；在非标准维度如 2049 时，编码吞吐比 TurboQuant 快约 36 倍（128k vs 3.5k items/s），适合线上实时 query
  预计算。

  - 显式校正最终重建向量的 L2 norm（而非只校正残差）对 MIPS 排名很重要，能替代 ScaNN anisotropic loss 的调参；实现时用 2
  字节自定义浮点 UE7M9 存 scale，Rslm4Lite 把 scale 隐写到前 16 维的最高 bit，实现零额外元数据，内存对齐更优，吞吐显著提升。

  - 在低 bit 场景（1-2 bit）Rslm_Global 超过 Faiss PQ 和 ScaNN AVQ，说明固定 codebook + 旋转 + 全局
  norm 校正是一个可复用的低带宽候选评分方案；但注意低维数据增加 scale 存储占比（如 glove 100d 1-bit 增加 15%），更适合高维 embedding。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
高维向量检索在搜索、推荐、RAG 系统中受 DRAM 容量和内存带宽约束，IVF 两阶段检索中 rescoring 向量的量化压缩直接影响成本与吞吐。传统数据依赖量化需要离线 k-means 训练，数据无关量化在低 bit 下召回下降明显；且通用量化器忽略 ANN 特性：残差空间分布、MIPS 对向量 norm 敏感、维度非 2 幂、硬件 cache line 对齐。

**方法关键点**
- Rslm 家族提供 1-4 bit/维训练自由量化：采用 block-wise cascaded FWHT，块大小 128，将旋转复杂度降到 O(D)；配合 sign flip 和 permutation 均匀化坐标分布，支持任意维度（重叠块处理尾部）。
- 使用固定的 Lloyd-Max codebook（最多 16 个 centroids，贴合 SIMD shuffle 限制），对旋转后的近高斯坐标量化。
- 核心创新：校正最终重建向量的 L2 norm（global scaling），而非只校正残差；scale 使用自定义 2 字节 UE7M9；Rslm4Lite 将 scale 隐写进前 16 维的最高 bit，实现零额外元数据，完美 cache line 对齐。
- 相对量化模式：对残差 r=x-a 量化，支持 local / global scaling；global 模式对最终重建向量 a+r 恢复 norm，显著提升 MIPS 排名质量。

**关键实验**
在 glove（100d, 1M）、bigann（128d, 100M）、openai（1536d, 2M）、wiki_full（3072d）、wiki_pca（384d）五个数据集评测。全向量量化：Rslm4 在 wiki_full/openai >99% recall@20@30；相对量化：RelApproxGlobal-Rslm4 全部 100% recall@20@30，RelApproxGlobal-Rslm2 在 4/5 数据集 recall@20@40 ≥99.3%，高维 1-bit openai 99.4%。端到端对比 Faiss/ScaNN：低 bit（1/2 bit）下 Rslm_Global 显著优于 ScaNN AVQ 和 Faiss PQ；例如 glove 上 Rslm1_Global 54.0% vs ScaNN AVQ 45.6% vs Faiss PQ 42.1%，且无需 k-means 训练。吞吐方面，block FWHT 在 D=2049 时压缩吞吐 128k items/s vs TurboQuant 3.5k，提升约 36 倍。

**最值得记住的一句话**
用固定 codebook + 块旋转 + 最终向量 norm 校正，可以在无训练情况下把 ANN rescoring 从 8bit 压到 2-4bit 而不掉召回。
