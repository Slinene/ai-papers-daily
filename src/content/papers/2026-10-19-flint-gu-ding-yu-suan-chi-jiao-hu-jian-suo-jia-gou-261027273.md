---
title: 'FLINT: Fixed-budget Late Interaction'
title_zh: FLINT：固定预算迟交互检索架构
authors:
- Himank Handa
- Negar Arabzadeh
- Matei Zaharia
affiliations:
- University of Illinois Urbana-Champaign
- University of California, Berkeley
arxiv_id: '2610.27273'
url: https://arxiv.org/abs/2610.27273
pdf_url: https://arxiv.org/pdf/2610.27273
published: '2026-10-19'
collected: '2026-10-21'
category: RecSys
direction: 多向量检索 · 效率优化
tags:
- multi-vector retrieval
- late interaction
- ColBERT
- attention pooling
- efficiency
one_liner: 通过对称注意力池化，将查询和文档压缩为固定数量向量，大幅减少多向量检索的存储和计算开销
practical_value: '- 商品/内容召回：多向量模型（如 ColBERT）在电商搜索中效果优于单向量，但索引存储巨大。可借鉴 FLINT 的固定预算池化，将商品标题、描述压缩为固定
  \(k\) 个向量，索引大小相对 ColBERTv2 降低 5.3-9.3 倍，适合大规模商品库部署。

  - 查询侧对称池化：不仅池化文档，也池化 query，减少在线 query 编码向量数和匹配计算量。在长查询、对话式搜索或多轮交互生成的查询场景下，端到端检索比
  ConstBERT 快 1.5-2.8 倍，适合 Agent 触发的复杂搜索请求。

  - 架构无关的池化设计：FLINT 在 BERT 和 ModernBERT 上都有效，说明池化策略可以独立于编码器骨干。实际落地时可选用更轻量的 ModernBERT
  等骨干，进一步降低延迟。

  - 若现有系统已使用 ColBERT 风格检索，可将 FLINT 作为召回或粗排组件，在不显著损失效果的前提下降低存储和计算成本，尤其适合索引频繁更新的电商场景。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：多向量检索模型（如 ColBERT）通过 token 级匹配取得优于单向量 bi-encoder 的效果，但每个 token 存一个向量导致索引存储和检索延迟随文档长度线性增长，难以扩展。

**方法关键点**：FLINT 使用注意力池化将 query 和 document 分别压缩为固定数量（fixed budget）的 embedding 向量。与之前仅池化 document、保留 token 级 query 的方法不同，FLINT 对两侧对称池化，同时减少文档存储和查询比较次数。池化基于 attention 聚合 token 表示，保留重要匹配信号，可跨不同编码器骨干（BERT、ModernBERT）使用。

**关键结果**：在 BEIR 上达到与最接近基线可比的效果，在 BrowseComp+、CRUMB、TREC Tip-of-the-Tongue 2025 等长查询、复杂查询基准上超越基线。长查询场景下端到端检索比 ConstBERT 快 1.5-2.8 倍；索引大小相对 ColBERTv2 减少 5.3-9.3 倍。
