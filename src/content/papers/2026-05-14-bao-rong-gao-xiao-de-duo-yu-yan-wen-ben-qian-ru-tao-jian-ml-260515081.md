---
title: 'ML-Embed: Inclusive and Efficient Embeddings for a Multilingual World'
title_zh: 包容高效的多语言文本嵌入套件 ML-Embed
authors:
- Ziyin Zhang
- Zihan Liao
- Hang Yu
- Peng Di
- Rui Wang
arxiv_id: '2605.15081'
url: https://arxiv.org/abs/2605.15081
pdf_url: https://arxiv.org/pdf/2605.15081
published: '2026-05-14'
collected: '2026-05-17'
category: LLM
direction: 多语言文本嵌入 · 三维嵌套学习
tags:
- multilingual
- embeddings
- matryoshka
- efficiency
- low-resource
- 3D-ML
one_liner: 通过三维嵌套学习(3D-ML)框架，在存储、推理深度和参数效率上全面优化多语言嵌入，刷新多项 MTEB 基准
practical_value: '- **嵌套维度压缩 (MRL)**：向量维度可按需截断而不显著损失质量，适合电商推荐中的大规模 ANN 检索，可对热门商品用高维、长尾商品用低维，平衡精度与存储成本。

  - **动态推理深度 (MLL)**：允许推理时提前退出浅层网络，Agent 系统可根据对话复杂度或延迟预算灵活选择深度，实现低成本快速响应。

  - **多语言语义一致性**：在低资源语言上表现尤其突出，跨境多语言商品搜索可直接使用同一嵌入空间，统一召回和语义匹配，无需维护多套语言模型。

  - **参数高效嵌入 (MEL)**：通过嵌入层参数共享或分解减少冗余，可借鉴到生成式推荐中的 Semantic ID 映射或 Item Embedding 压缩，在保证表达能力的同时降低参数规模。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：当前文本嵌入发展面临三重壁垒——计算开销过大、语言覆盖极为集中、闭源或半开源模型缺乏透明性，导致大多数非主流语言被忽视，研究难以复现。

**方法**：提出三维嵌套学习 (3D-ML) 框架，从三个维度系统性提升效率与包容性：① 嵌套表示学习 (MRL)，支持向量维度动态截断，减少存储；② 嵌套层学习 (MLL)，允许推理时灵活选择网络深度；③ 首创嵌套嵌入学习 (MEL)，进一步提高参数效率。基于此框架，策划超大规模多语言数据集，训练从 1.4 亿到 80 亿参数的模型套系，并完整开源模型、数据与代码。

**结果**：在覆盖 430 个任务的评测中，ML-Embed 在 17 个 MTEB 基准中的 9 个上创下新纪录，低资源语言表现尤其强劲，为构建全球公平且计算高效的 embedding 系统提供了可复现的技术蓝图。
