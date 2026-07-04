---
title: Scaling Laws for Grid-Based Approximate Nearest Neighbor Search in High Dimensions
title_zh: 高维网格近似最近邻搜索的缩放定律
authors:
- Matthew J Liu
- Wei Hang Zheng
- Vidhan Purohit
- Siqi Xie
- Chieh-En Li
- Jerry Li
- Noah Flynn
affiliations:
- University of California, Berkeley
- University of Toronto, St. George
- Independent Researcher
- University of Waterloo
arxiv_id: '2607.01283'
url: https://arxiv.org/abs/2607.01283
pdf_url: https://arxiv.org/pdf/2607.01283
published: '2026-06-30'
collected: '2026-07-04'
category: Other
direction: 高维ANN缩放定律与网格算法
tags:
- approximate nearest neighbor
- scaling laws
- multiprobe grid
- high-dimensional
- vector search
- indexing cost
one_liner: 多探针网格在高维下展现维度不变吞吐，索引成本低，冲击图/树方法的主导地位
practical_value: '- 当推荐系统使用高维嵌入（d≥300）且索引频繁重建（如分钟级更新），可试用多探针网格替代HNSW，利用其近常数维度吞吐和极低索引延迟，避免图索引重建瓶颈。

  - 查询时间随N近线性增长，但在千万级数据集上仍可能满足延迟要求；通过调节probe数量可灵活控制精度/速度折中，适合召回延迟不极端的业务。

  - 若采用ANN近似自注意力优化大模型推理，网格法的维度不变性可提供更平稳的扩展，值得在推理引擎中作为备选ANN后端。

  - 在离线全量索引构建场景（如每日亿级向量重建），网格法的快速索引特性可大幅缩短总耗时，可作为评估向量检索库时的 baseline 方案。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：随着嵌入维度增加（LLM驱动的趋势），常用ANN算法吞吐量退化，而网格法长期被忽视。同时自注意力被形式化为ANN操作，理解ANN的N和d缩放规律对高效Transformer架构至关重要。

**方法**：系统测量多探针网格算法随数据集大小N和维度d变化的查询吞吐量、索引时间和内存，与经典图/树/分区方法对比，聚焦GloVe嵌入族上的d缩放交叉现象。

**关键结果**：多探针网格在d增加时保持近似常数的维度缩放指数，而HNSW、FAISS-IVF等吞吐量显著下降，出现以前未报告的交叉点。查询延迟随N近线性增长，但索引构建速度远快于图方法，内存开销相近。这表明网格法在索引重建频繁或高维场景具有独特竞争力。
