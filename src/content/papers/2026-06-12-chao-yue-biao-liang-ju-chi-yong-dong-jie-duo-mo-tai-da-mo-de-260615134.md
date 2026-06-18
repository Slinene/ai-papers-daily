---
title: 'Beyond Scalar Distances: Semantic Attribute Gradients from Frozen MLLMs for
  Visual Embeddings'
title_zh: 超越标量距离：用冻结多模态大模型的语义属性梯度训练视觉嵌入
authors:
- Shubhang Bhatnagar
- Dheeraj Baiju
- Narendra Ahuja
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2606.15134'
url: https://arxiv.org/abs/2606.15134
pdf_url: https://arxiv.org/pdf/2606.15134
published: '2026-06-12'
collected: '2026-06-18'
category: RecSys
direction: 利用 MLLM 提供属性级监督改善视觉嵌入
tags:
- Attribute-aware Learning
- Metric Learning
- MLLM
- GRPO
- Embedding Distillation
- Zero-shot Retrieval
one_liner: 将冻结 MLLM 的属性感知预测转化为细粒度梯度，替代传统的类别标量监督，提升细粒度零样本检索
practical_value: '- 电商商品检索中，可用多模态 LLM 生成商品属性描述，通过 GRPO 将属性感知信号注入视觉编码器，使嵌入对细微款式差异更敏感，无需额外推理成本。

  - 注意力蒸馏 loss 可将 LLM 关注的属性 token 对齐到图像嵌入，提升模型对关键属性的聚焦能力，适用于细粒度商品识别和冷启动场景。

  - 冻结大模型仅充当训练时的“属性教师”，线上部署时丢弃，保持轻量级编码器的推理效率，适合高流量推荐系统。

  - 该方法不依赖类别标签即可实现属性级监督，可迁移到长尾或零样本推荐场景，利用 LLM 的开放知识增强检索能力。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：传统度量学习训练视觉编码器时，仅使用类别标签的一维标量距离信号，将所有属性等同对待，无法捕获细粒度差异（如鸟类的喙形、羽毛纹理），导致零样本检索在细粒度场景中性能受限。

**方法**：提出 SAGA 框架，引入冻结的多模态大语言模型（MLLM）作为属性感知教师。对于每个图像对，编码器输出 token 给 MLLM，MLLM 预测两图是否属于同一类别；采用 Group Relative Policy Optimization (GRPO) 以正确预测为奖励，梯度反向传播迫使编码器生成暴露关键区分属性的 token，从而将属性级别的细粒度监督注入编码器。同时，用注意力蒸馏损失将 MLLM 的注意力分布迁移到编码器嵌入，并用标准度量学习损失保持嵌入空间结构。MLLM 仅用于训练，推理时丢弃。

**结果**：在 CUB-200-2011、Cars-196、FGVC-Aircraft 和 iNaturalist Aves 等细粒度数据集上，零样本图像检索 Recall@1 较最优基线提升 3~6 个百分点，且推理成本与基础度量学习模型完全一致。
