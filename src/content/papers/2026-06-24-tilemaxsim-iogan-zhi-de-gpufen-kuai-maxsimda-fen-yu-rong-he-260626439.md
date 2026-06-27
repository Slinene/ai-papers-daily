---
title: 'TileMaxSim: IO-Aware GPU MaxSim Scoring with Dimension Tiling and Fused Product
  Quantization'
title_zh: TileMaxSim：IO感知的GPU分块MaxSim打分与融合量化
authors:
- Ashutosh Sharma
affiliations:
- MIT-IBM Watson AI Lab
arxiv_id: '2606.26439'
url: https://arxiv.org/abs/2606.26439
pdf_url: https://arxiv.org/pdf/2606.26439
published: '2026-06-24'
collected: '2026-06-27'
category: RAG
direction: 多向量检索GPU加速 · IO-aware kernel
tags:
- MaxSim
- ColBERT
- GPU Kernel
- IO-aware
- Triton
- Product Quantization
one_liner: 通过维度分块与融合PQ解压缩，将GPU上MaxSim峰值带宽利用率提升至80.2%，打分吞吐提升220倍
practical_value: '- 搜索/推荐系统中若使用ColBERT等多向量模型做召回或排序，可将TileMaxSim作为即插即用的GPU算子，将候选评分延迟从百毫秒降至毫秒级，显著降低端到端延迟。

  - 在实现自定义的打分/聚合CUDA kernel时，可借鉴其IO-aware SRAM分块策略：流式加载文档嵌入并在寄存器中累积最大值，避免实例化庞大的相似度矩阵，最大化带宽利用率。

  - 融合PQ解压缩与scoring的思路可迁移至在线检索中压缩嵌入的快速还原计算，通过共享内存查找表减少HBM读取量，适用于存储压缩的电商商品或广告嵌入。

  - 维度分块技术解决了嵌入维度超过共享内存容量的问题，可推广至高维推荐模型（如d>128）的打分加速，保持恒定吞吐。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：多向量检索模型（如ColBERT）的MaxSim打分在GPU上带宽利用率极低（5–18%），主要因为显式物化Nq×Nd相似度矩阵，造成大量冗余HBM读写。

**方法关键点**：TileMaxSim通过三个Triton kernel技术突破瓶颈：(1) 多查询SRAM分块，流式加载文档嵌入到共享内存，每个query token在寄存器中即时累加最大值，每个嵌入仅读一次HBM；(2) 维度分块，将嵌入维度切为128宽的chunk，解决d>128时共享内存溢出问题；(3) 融合PQ解压缩，利用共享内存查找表直接在压缩文档上计算内积，HBM I/O最高减少31倍。

**关键结果**：在H100上，TileMaxSim达到峰值带宽的80.2%（2687 GB/s），打分吞吐达82M docs/s（真实MS MARCO数据71.6M/s），比循环基线快220倍，比torch.compile快6.6–8.5倍，比WARP CPU引擎快469倍；精度无损失，在ColBERTv2/PLAID中将100K候选评分延迟从268ms降至1.2ms（端到端延迟降低98%），且吞吐从100K到500K文档保持恒定，支持多GPU线性扩展。
