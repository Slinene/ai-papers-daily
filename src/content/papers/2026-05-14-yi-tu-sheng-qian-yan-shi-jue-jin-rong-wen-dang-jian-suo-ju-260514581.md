---
title: A Picture is Worth a Thousand Words? An Empirical Study of Aggregation Strategies
  for Visual Financial Document Retrieval
title_zh: 一图胜千言？视觉金融文档检索聚合策略实证研究
authors:
- Ho Hung Lim
- Yi Yang
arxiv_id: '2605.14581'
url: https://arxiv.org/abs/2605.14581
pdf_url: https://arxiv.org/pdf/2605.14581
published: '2026-05-14'
collected: '2026-05-17'
category: RAG
direction: 视觉RAG · 文档嵌入聚合
tags:
- Visual RAG
- Embedding Aggregation
- Financial Documents
- Semantic Shift
- Patch Tokens
one_liner: 实证证明单向量聚合使金融文档区分度崩溃，全局纹理主导是关键原因
practical_value: '- 电商涉及数字敏感文档（价比、标价图）时，避免直接用单向量检索全页图像，应保留 patch 级特征或结合 OCR 文本。

  - 视觉 RAG 检索金融类图像时可改用多向量（如后期交互 ColBERT 风格），仅聚合会丢失细粒度数字变化。

  - 全局纹理主导提示：均值池化洗掉局部关键信号，可试注意力池化、稀疏 patch 选择或区域编码。

  - 商品图搜索若依赖局部细节（LOGO、规格数字），全局向量易误匹配，需强化局部特征权或加 OCR。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：视觉 RAG 将文档作为图像编码，虽保留排版等视觉上下文，但每个文档产生数百个 patch token，在向量库中存储和检索成本过高。实际部署通常聚合成单个向量，然而金融文档中单一数字的微小变化可能导致完全不同的业务含义，这种聚合是否丢失关键信息尚不明确。

**方法**：构建金融文档诊断基准，故意制造仅一位数字不同的文档对，形成语义显著变化的场景。对比单向量聚合（均值池化等）与 patch 级表示在区分上述文档时的表现，通过向量余弦相似度衡量区分度。进一步分析聚合失效的根因，并测试不同模型规模、检索优化嵌入及多种缓解策略（如加权池化、投影）是否改善。

**关键结果**：单向量聚合使原本语义不同的文档获得几乎相同的向量（相似度>0.99），而 patch 级表示能明显区分（相似度约0.3）。根本原因是全局纹理（背景、布局）在单向量中占主导，淹没了重要的局部数字细节。该结论在 ViT-B/310M 到 ViT-L/650M 等不同规模模型、检索微调嵌入及增强局部注意等策略下均稳健成立，表明单向量聚合在金融文档检索中存在系统风险，不应直接用于数字敏感场景。
