---
title: 'Mind the Heads: Topological Representation Alignment for Multimodal LLMs'
title_zh: 留心注意力头：多模态LLM的拓扑表示对齐
authors:
- Davide Caffagni
- Alberto Compagnoni
- Federico Melis
- Sara Sarto
- Pier Luigi Dovesi
- Mark Granroth-Wilding
- Marcella Cornia
- Lorenzo Baraldi
affiliations:
- University of Modena and Reggio Emilia
- University of Pisa
- AMD Silo AI
arxiv_id: '2606.23885'
url: https://arxiv.org/abs/2606.23885
pdf_url: https://arxiv.org/pdf/2606.23885
published: '2026-06-22'
collected: '2026-06-27'
category: Multimodal
direction: 多模态LLM · 头对齐与拓扑表示
tags:
- Multimodal LLM
- Representation Alignment
- Attention Head
- Topological Structure
- Visual Hallucination
- Contrastive Learning
one_liner: 提出头级表示对齐 HeRA，通过拓扑邻居保持提升多模态LLM视觉任务并抑制幻觉
practical_value: '- 多模态特征对齐可借鉴头级别选择：不在整个层做对齐，而是针对特定注意力头，用拓扑保持目标（如 MKNN 对比代理）约束局部邻域结构，适用于电商图文匹配、商品视频理解等场景。

  - 反直觉发现：对齐最差的头收益最大，暗示在初始跨模态鸿沟大的位置施加约束更有效，可在自有多模态模型中选择对齐差的位置优先优化。

  - HeRA 可作为正则化器，抑制模型过度依赖语言先验而忽视视觉输入，对需要精准视觉识别的任务（如商品属性提取、广告素材合规审核）有帮助。

  - 训练中可引入 MKNN 度量的可微分代理，以对比损失形式端到端优化，工程实现成本低，可直接插入现有 MLLM 训练流程。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：现有多模态LLM的表示对齐通常固定对齐某个语言骨干层，忽略了Transformer内部注意力头的细粒度结构，导致视觉推理（如物体计数、空间关系）仍薄弱，并常产生视觉幻觉。

**方法**：提出头级表示对齐 HeRA，基于柏拉图表示假说，强调保留表示拓扑结构（局部邻域关系）。采用互K近邻（MKNN）度量跨模态对齐，并设计对比目标作为其可微分代理。训练时，依据各注意力头的MKNN分数动态选择特定头进行对齐；出人意料的是，对齐分数最低的头收益最大。

**结果**：在多个MLLM和18个基准上，HeRA 一致提升视觉中心任务性能，并有效降低视觉幻觉，自然抑制了对语言先验的过度依赖。
