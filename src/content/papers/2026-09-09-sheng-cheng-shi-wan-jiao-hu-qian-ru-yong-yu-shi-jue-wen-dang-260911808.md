---
title: Generative Late-Interaction Embeddings For Visual Document Retrieval
title_zh: 生成式晚交互嵌入用于视觉文档检索
authors:
- Mohamed Eltahir
- Talal Aloushan
- Rose Khairoalsendi
- Jana Shata
- Mohammed Alhassan
- Leen Alrehaili
- Tanveer Hussain
- Naeemullah Khan
affiliations:
- King Abdullah University of Science and Technology (KAUST)
- Edge Hill University
arxiv_id: '2609.11808'
url: https://arxiv.org/abs/2609.11808
pdf_url: https://arxiv.org/pdf/2609.11808
published: '2026-09-09'
collected: '2026-09-12'
category: Multimodal
direction: 多向量检索压缩与生成式重建
tags:
- Late Interaction
- Embedding Compression
- Generative Decoder
- Vector Index
- MaxSim
- Visual Retrieval
one_liner: GLIE 用 k≪N 个向量存储并生成式重建完整 late-interaction 向量集，在 4 向量/页保留近 80% nDCG@5
practical_value: '- 电商/广告的多向量 late-interaction 索引（如商品图文与 OCR 特征）不要只用随机采样或平均压缩；可以学习极小
  decoder，从少量基向量重建完整向量集，用于召回后精确重排。存储预算可从每商品数千向量降到 4-16 个，仍保留大部分排序精度。

  - 若向量已 L2 归一化，做 k-means/PQ/IVF 聚类时务必把质心重新归一化到球面；本文显示这项免费操作对 MaxSim 有最高 +0.093 nDCG@5
  的收益，电商向量通常也做归一化，可直接迁移。

  - 训练预算非常小：1,000 页 / 415K 参数 / 3 GPU-minutes 即可得到可用的生成式 read-out；在做 embedding index
  压缩时，可以先尝试轻量 decoder，而不是直接微调 large encoder，尤其适合快速适配新类目/新域。

  - 对 Agent/RAG 场景，可借鉴非对称检索流程：粗糙 k 向量索引 -> 生成式重建 top candidates -> 精确 MaxSim，降低长文档/商品详情页检索的
  memory 和 latency。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：Late-interaction retrieval 每个页面约 1,000 个向量，是视觉文档检索 SOTA，但存储成本高；现有压缩方法在激进预算下掉点严重，或需要重训编码器。

**方法关键点**：作者发现跨三个编码器，页面向量严格落在单位球面，且内在维度仅为 5–6。据此提出 GLIE：先对每页 N 个向量做 k-means，并将质心归一化到球面，作为每页 k≪N 个可存储向量；再学习一个 415K 参数 decoder，从这 k 个归一化质心重建整页 N 个向量。查询时只用 k 个存储向量召回，对 top candidates 展开回 N 个向量做精确 MaxSim 重排序。

**关键结果**：在 ViDoRe v1 上，4 个向量/页时 GLIE 保留近 80% 未压缩系统的 nDCG@5，此前最佳 post-hoc 方法约为 70%；仅归一化质心即可带来最高 +0.093 nDCG@5 的免费提升。仅用 1,000 页训练、3 GPU-minutes。同等训练预算下，微调编码器甚至不如 GLIE 未训练阶段；在 ViDoRe v2 和第二编码器上趋势一致。
