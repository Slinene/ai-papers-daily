---
title: 'ViSAR: Training-Free Adaptive-$k$ Retrieval for Visual Document Question Answering'
title_zh: ViSAR：面向视觉文档问答的无训练自适应-k检索
authors:
- Adrien Mialland
- Marc Plantevit
- Julien Gallois
- Céline Robardet
affiliations:
- INSA Lyon, CNRS, LIRIS UMR 5205
- EPITA Research Laboratory (LRE)
- Lowit
arxiv_id: '2609.02486'
url: https://arxiv.org/abs/2609.02486
pdf_url: https://arxiv.org/pdf/2609.02486
published: '2026-09-02'
collected: '2026-09-06'
category: RAG
direction: 视觉文档RAG·自适应k检索
tags:
- DocVQA
- RAG
- Adaptive-k Retrieval
- Late Interaction
- LVLM
- Training-Free
one_liner: 在嵌入空间构造查询条件页面级相似度矩阵，动态决定检索页数，降低RAG延迟并保持或提升准确率
practical_value: '- 可借鉴动态 top-k 思想：在电商/广告场景中，为商品详情页、广告落地页或用户评价做 RAG 时，不再固定召回条数，而是根据查询复杂度动态截断，能显著减少输入
  LVLM 的 token 数和首字延迟。

  - 利用 late-interaction 编码器产生的 page-level 相似度矩阵作为查询语义激活图：该方法无需训练，直接基于 embedding 空间的
  MaxSim 等运算，可在现有向量检索链路上快速实现，适合业务侧低成本验证。

  - 将相似度矩阵的统计结构（如激活分布、峰值集中度）作为检索质量信号，用于重排或决定是否触发多跳检索/补充上下文，类似于推荐中 uncertainty-aware
  的截断策略。

  - 论文结果显示自适应检索在多个编码器与 LVLM 组合下最高降低 58.7% 延迟且准确率不降，证明“检索质量感知的上下文裁剪”在视觉富文档问答中有效，对多模态商品理解、店铺资质审核等
  RAG 任务有直接迁移价值。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：DocVQA 通常采用 RAG 流程，先用 late-interaction 编码器检索与用户问题相关的文档页面，再交给大视觉语言模型（LVLM）生成答案。现有方法固定检索 top-k 页面，不考虑查询复杂度，导致简单查询也传入过多页面，增加 LVLM 延迟，并可能引入噪声降低准确率。

**方法关键点**：ViSAR 是一种训练自由的自适应 k 检索方法，直接在嵌入空间构造查询条件下的页面级相似度矩阵。它利用 late-interaction 编码器对 query 和 page 的 token/region 嵌入进行 MaxSim 等运算，得到 page-page 语义相似度图，突出查询相关语义的局部激活模式；然后基于该矩阵结构动态确定需要检索的页面数量，而不是固定 k。整个过程无需微调编码器或 LVLM。

**关键结果**：在多个 late-interaction 编码器和 LVLM 上，ViSAR 检索出更紧凑、查询自适应的页面集合，相比固定 top-k 和已有自适应启发式，RAG 延迟最高降低 58.7%，同时答案准确率保持或提升。此外，相似度矩阵结构与最终答案准确率存在相关性，提示未来可将检索质量信号用于文档理解。
