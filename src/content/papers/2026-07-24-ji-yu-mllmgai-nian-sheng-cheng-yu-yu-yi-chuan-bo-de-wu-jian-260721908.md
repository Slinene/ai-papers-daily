---
title: Unsupervised Multimodal Intent Discovery via MLLM-Guided Concept Generation
  and Semantic Propagation
title_zh: 基于MLLM概念生成与语义传播的无监督多模态意图发现
authors:
- Yunjin Gu
- Qianrui Zhou
- Hua Xu
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- Tsinghua University
arxiv_id: '2607.21908'
url: https://arxiv.org/abs/2607.21908
pdf_url: https://arxiv.org/pdf/2607.21908
published: '2026-07-24'
collected: '2026-07-28'
category: Multimodal
direction: 多模态意图发现 · MLLM语义引导
tags:
- Unsupervised Learning
- Multimodal
- Intent Discovery
- MLLM
- Semantic Propagation
- Contrastive Reasoning
one_liner: 用MLLM生成高层语义概念并通过图传播产生伪标签，实现可解释的无监督多模态意图聚类。
practical_value: '- 电商对话/客服场景下，可利用 MLLM 对比邻近簇生成可解释的意图标签（如“退货咨询”、“物流查询”），替代人工标注，适用于无监督意图发现冷启动。

  - 语义加权图传播策略可迁移到用户意图或 item 聚类的伪标签细化，结合局部结构一致性提升聚类质量。

  - 代表样本选择 + 对比推理的思路可用于构建主动学习或弱监督样本筛选，优先标注信息量大的对话。

  - 若有用户点击/浏览等多模态行为数据，可借鉴多模态融合与概念语义传播，实现可解释的用户意图聚类。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

**动机**：无监督多模态意图发现旨在从无标注对话中自动挖掘用户意图，但现有方法仅依赖几何相似性，缺乏高层语义指导，聚类结果可解释性差。本文提出 MCSP，完全无监督，引入基于概念的语义细化。

**方法关键点**：
1. **概念生成**：对每个簇选择高质量代表样本，利用 MLLM（多模态大模型）对比相邻簇进行对比推理，生成描述意图差异的可解释语义概念。
2. **语义传播**：基于生成的语义概念构建语义加权图，在图上传播概念信息并与局部结构一致性对齐，产生可靠的伪标签。
3. **表示细化**：用伪标签微调多模态编码器，迭代优化聚类。

**关键结果**：在三个挑战性多模态意图数据集（如 MIntRec）上，MCSP 在所有指标（NMI、ARI、ACC）上均超越 SOTA，同时输出的簇附带语义概念，显著提升可解释性。
