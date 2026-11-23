---
title: Mixture of Latent Recursions for Low-Rank Adaptation
title_zh: 低秩适配的潜在递归混合框架
authors:
- Weixun Luo
- Ye Mao
- Ranran Huang
- Junpeng Jing
- Krystian Mikolajczyk
affiliations:
- Imperial College London
arxiv_id: '2611.27823'
url: https://arxiv.org/abs/2611.27823
pdf_url: https://arxiv.org/pdf/2611.27823
published: '2026-11-20'
collected: '2026-11-23'
category: Training
direction: 参数高效微调 · LoRA变体
tags:
- LoRA
- Parameter-Efficient Fine-Tuning
- Adaptive Computation
- Recursion
- Router
one_liner: 用共享潜在递归和阈值路由增强LoRA表达性，几乎不增参数且支持推理算力可调
practical_value: '- 业务上微调LLM做query改写、创意生成或Agent规划时，可用MoLR替代增大LoRA rank或堆叠多个低秩模块，保持低参数的同时提升难样本表达性，适合多任务共享底座的场景。

  - 阈值路由器按token动态分配递归深度，等价于难度感知的计算预算；线上生成任务中可通过调节阈值实现latency-quality折中，无需重新训练，方便AB实验和成本控制。

  - 动态阈值平衡不同递归深度利用的训练技巧可迁移到MoE、early-exit等条件计算模块，避免部分路径过载或闲置。

  - 该方法在低维潜在空间做递归细化，与Semantic ID生成、用户行为序列编码等latent-space操作兼容，不增加主模型显存和推理主路径开销。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：LoRA固定低秩架构，表达性提升通常靠增大rank或添加可学习模块，带来参数和计算开销。MoLR旨在不显著增加参数的前提下增强适应表达性。

**方法关键点**：将LoRA视为latent-space mapping，MoLR在低维潜在空间对每个输入的下投影表示进行递归细化，递归使用共享变换，避免新增大量参数。轻量阈值路由器独立判断每个token是否需要继续递归，实现输入依赖的动态深度分配。训练中动态调整阈值，鼓励不同递归深度被均衡利用，防止坍缩到浅层或过深。该设计可看作每个token的条件计算，推理时可通过阈值控制总计算量。

**关键结果**：在多种语言和视觉任务上，MoLR以相对LoRA可忽略不计的参数开销，一致超越代表性LoRA变体。分析显示模型学到输入相关的递归深度分配，且无需重新训练即可实现推理时计算-性能的可控权衡。
