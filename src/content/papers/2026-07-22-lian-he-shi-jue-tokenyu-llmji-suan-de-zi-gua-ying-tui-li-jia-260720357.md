---
title: 'Look Less, Think Faster: Joint Token-Compute Adaptation for Multimodal LLMs'
title_zh: 联合视觉Token与LLM计算的自适应推理框架
authors:
- Pengcheng Wang
- Zhiquan Wang
- Jayoung Lee
- Zhuoyan Xu
- Ran Xu
- Saurabh Bagchi
- Yin Li
- Somali Chaterji
affiliations:
- Purdue University
- University of Wisconsin–Madison
- NVIDIA
arxiv_id: '2607.20357'
url: https://arxiv.org/abs/2607.20357
pdf_url: https://arxiv.org/pdf/2607.20357
published: '2026-07-22'
collected: '2026-07-23'
category: Multimodal
direction: 多模态高效推理 · 联合自适应调度
tags:
- Adaptive Inference
- Multimodal LLM
- Token Pruning
- Dynamic Compute
- Efficiency-Accuracy Trade-off
one_liner: 提出SmartVL，联合动态控制视觉token数量和LLM计算量，实现多模态LLM的精度-效率帕累托最优
practical_value: '- 在电商多模态问答或商品理解Agent中，可借鉴视觉token的动态剪枝，按输入复杂度自适应保留关键视觉信息，减少冗余计算，降低首词延迟。

  - LLM推理时基于预算灵活跳层或关头的思路，可迁移至推荐系统重排或大模型推理阶段，在流量高峰期实现算力的细粒度分配。

  - 共享预算编码+可微分延迟估计器的联合训练范式，可指导将多个自适应模块（如特征选择、模型深度）进行端到端协同优化，避免独立调优的次优解。

  - 对于需要同时处理图片和文本的搜索推荐Agent，可联合调度视觉编码器和LLM的资源消耗，在保证回复质量的前提下最大化吞吐。'
score: 7
source: arxiv-cs.CV
depth: abstract
---

动机：多模态LLM推理瓶颈来自两方面——大量视觉token和LLM本身高计算量。现有方法分别优化视觉token剪枝或LLM计算跳层，忽略两者间的耦合：计算资源需根据输入内容在视觉编码与LLM推理两阶段动态协调。单独的维度优化难以达到全局最优的精度-效率平衡。

方法：提出SmartVL框架，包含两个控制器：视觉端token控制器动态选择信息量高的视觉token，LLM端计算控制器自适应调整层数和注意力头等。控制器通过共享的预算编码进行信息交互，并引入可微延迟估计器，支持端到端训练联合策略。训练时以总推理延迟满足目标预算为约束，使两个控制器协同学习跨阶段分配方案。

关键结果：在多个多模态基准（VQA、Captioning等）上，SmartVL的联合调度一致优于仅优化单一维度的自适应方法，实现明显更优的精度-延迟帕累托前沿，且能根据实时算力预算灵活调整行为。
