---
title: MLLM-Routed Heterogeneous Ensembles for Robust Cross-Dataset Image Classification
title_zh: MLLM路由异构集成用于鲁棒跨数据集图像分类
authors:
- Daniel Perkins
- John Squires
- Janou Milligan
- Chandra Raskoti
- Linda Ungerboeck
affiliations:
- University of Tennessee, Knoxville
- The Bredesen Center for Interdisciplinary Research and Graduate Education
arxiv_id: '2608.13463'
url: https://arxiv.org/abs/2608.13463
pdf_url: https://arxiv.org/pdf/2608.13463
published: '2026-08-13'
collected: '2026-08-15'
category: Multimodal
direction: 多模态LLM路由异构视觉模型
tags:
- MLLM Router
- Ensemble Learning
- Image Classification
- Heterogeneous Models
- Cross-Dataset
one_liner: 用多模态大语言模型agent动态路由每张图像到最合适的视觉骨干，实现跨域集成分类
practical_value: '- **LLM/MLLM 作为轻量级路由决策层**：无需训练专门的路由模型，直接使用通用多模态大模型根据样本特征（如图像、文本描述）动态选择下游专家模型。可迁移到电商推荐中的多路召回/排序集成，比如按商品类目、用户意图或内容复杂度路由到不同精排模型。

  - **异构模型集成 + 统一 label space**：不同架构（CNN、SSL、VLM）共享统一标签空间，各自发挥优势。推荐系统中可以将协同过滤、Transformer、多模态模型统一在相同的候选集空间下，由
  LLM 路由选择，降低集成维护成本。

  - **通过 prompt 快速增加新知识**：路由器只需修改 prompt 就能纳入新领域信息，无需重新训练。适合电商业务中频繁扩展新类目、新活动场景，能大幅缩短模型更新周期。

  - **自然语言推理 trace 增强可解释性**：路由决策附带 reasoning trace，便于线上 badcase 诊断和策略审计。对推荐系统中的模型选路、兜底策略可解释性有直接借鉴价值。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：单一任务数据集上训练的图像分类模型跨域泛化能力差，难以应对医疗影像、农业、自动驾驶等多样视觉场景。需要一种能动态选择最优视觉骨干的集成机制，兼顾准确率、适应性与可解释性。

**方法关键点**：构建异构集成 ARMDIL，包含 CNN（ResNet）、自监督表示学习模型（SSL）和视觉语言模型（VLM），统一在从多个数据集构造的标签空间上训练。使用多模态大语言模型（MLLM）agent 作为路由器，根据输入图像和任务上下文动态选择最合适的视觉骨干。路由器通过 prompt 修改即可纳入新领域信息，无需重训；同时生成自然语言推理 trace，增强决策可解释性。

**关键结果**：在多个不同分布和特性的视觉域上，ARMDIL 能有效权衡各骨干的优势与脆弱性，整体分类性能与专用训练型路由器相当；在适应性和可解释性上显著提升，能通过简单 prompt 修改快速适应新信息。
