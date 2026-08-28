---
title: 'PUMA: Post-Hoc Sparsification of Universal Multimodal Embeddings for Efficient
  Retrieval'
title_zh: 通用多模态嵌入的事后稀疏化：PUMA 实现高效检索
authors:
- Matteo Attimonelli
- Alessandro De Bellis
- Franco Maria Nardini
- Claudio Pomo
- Cosimo Rulli
- Rossano Venturini
- Tommaso Di Noia
affiliations:
- Politecnico di Bari, Italy
- Sapienza University of Rome, Italy
- ISTI–CNR, Pisa, Italy
- University of Pisa, Italy
arxiv_id: '2608.25780'
url: https://arxiv.org/abs/2608.25780
pdf_url: https://arxiv.org/pdf/2608.25780
published: '2026-08-26'
collected: '2026-08-28'
category: Multimodal
direction: 多模态嵌入事后稀疏化与高效检索
tags:
- sparse retrieval
- multimodal embeddings
- post-hoc sparsification
- efficient retrieval
- autoencoder
- vector compression
one_liner: 用稀疏自编码器将通用多模态嵌入事后转化为紧凑稀疏码，不重训骨干，存储降 8-16 倍、检索最高加速 25 倍
practical_value: '- 电商多模态检索（如商品图搜、文搜图、组合查询）可直接在现有通用 embedder 之后挂接稀疏自编码器，把 dense FP32
  向量压缩为少量非零分量，线上索引存储降低 8-16 倍，大候选池精确打分提速约 25 倍，适合对延迟和内存敏感的召回场景。

  - 预训练阶段先让稀疏编码保持 dense 点积几何（重建内积），再针对检索损失微调，这个两阶段 recipe 可以迁移到商品 embedding 压缩：先用自监督对齐
  dense 相似度，再用业务正负样本微调稀疏表示，避免直接端到端训练导致语义漂移。

  - 注意两个失败模式：pre-TopK 支持不足（稀疏码中没有保留足够多与 query 最相关的维度）和 active support 与检索错位，意味着在业务落地时要监控稀疏化后
  TopK 召回与 dense 的覆盖差异，必要时通过增加预 TopK 约束或检索微调时加入 ranking 损失修正。

  - 若已有稠密 embedding 模型不想重训，PUMA 提供了一种 post-hoc 压缩路径：冻结 backbone，只训练轻量稀疏编码器，对已有电商图文
  embedding 服务可以低成本升级，减少向量数据库存储成本，适合在召回/粗排阶段做候选快速扫描。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：通用多模态嵌入（universal multimodal embedders）统一处理文本、图像和混合查询，但 dense 向量存储和推理成本高，事后稀疏化（post-hoc sparsification）在多模态检索领域尚未充分探索。

**方法关键点**：PUMA 采用稀疏自编码器结构，将通用多模态嵌入映射为紧凑稀疏码，且不重训 backbone。训练分两阶段：预训练阶段保持 dense 点积几何（重建内积），之后针对检索任务微调稀疏编码器。该方法适用于文本到图像、组合图像检索等场景。

**关键结果数字**：在 5 个基准上评估（涵盖 text-to-image 和 composed image retrieval），骨干为 Qwen3-VL-Embedding-2B。PUMA 在 5 个数据集中的 4 个上统计上不劣于或优于 dense retrieval。进一步识别两个事后稀疏化失败模式：pre-TopK 支持不足和 retrieval 错位的 active support。存储上，FP32 向量降低 8-16 倍；在大候选池上，比精确 dense 打分快最多 25 倍。
