---
title: 'Negligible in Size, Significant in Effect: On Scale Vectors in Large Language
  Models'
title_zh: 被忽视的尺度向量：对LLM训练的巨大影响与优化改进
authors:
- Mingze Wang
- Shuchen Zhu
- Yuxin Fang
- Binghui Li
- Kai Shen
- Shu Zhong
affiliations:
- ByteDance Seed
- Peking University
arxiv_id: '2605.26895'
url: https://arxiv.org/abs/2605.26895
pdf_url: https://arxiv.org/pdf/2605.26895
published: '2026-05-25'
collected: '2026-05-27'
category: Training
direction: LLM优化 · 尺度向量重设计与预条件
tags:
- scale-vector
- preconditioning
- RMSNorm
- LLM pretraining
- weight decay
- reparameterization
one_liner: 理论证明Pre-Norm中尺度向量虽参数极少但通过自加速预条件效应关键加速训练，并据此提出分支异构、双端放置与幅度方向重参数化三种改进，在密集和MoE模型上一致提升预训练损失。
practical_value: '- **尺度向量设计可视为免费优化加速器**：在推荐模型（如生成式推荐、CTR DNN）的RMSNorm/LayerNorm中，可引入分支特定的尺度向量，为Q/K/V或不同特征交叉分支提供独立的自适应预条件，几乎不增加参数。

  - **权重衰减策略直接可复用**：对紧接线性层的RMSNorm（Input-Norm）施加weight decay以稳定Hessian、加速收敛；而对不接线性层的（Output-Norm，如Q/K-Norm或最终输出前的归一化）应避免weight
  decay，防止限制表达能力。这一规则在MoE专家网络或Agent多模块网络中也适用。

  - **双端放置与幅度方向解耦提升优化效率**：在Transformer类推荐模型（如SASRec、BST）中，对注意力投影矩阵同时加输入侧和输出侧尺度向量（DP），或对FFN的gate/up分支采用
  \( \gamma_a \odot \text{Norm}(W(\gamma_b \odot x)) \) 的归一化双端放置，可进一步加速收敛。幅度方向重参数化（OR/ER）在低参数增量下带来更各向异性的预条件机制，适合大规模训练。

  - **实验表明，这些trick组合可取得约1.2×-1.25× 的scaler效率提升**，在工业级token预算下保持优势，且与Muon优化器、warmup-stable-decay调度兼容，可直接集成到已有训推框架中。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机：** 现代LLM中的RMSNorm包括确定性归一化操作和可学习的尺度向量γ。归一化操作已被广泛研究，而尺度向量虽仅占参数总量的十万分之几，却是训练稳定的关键组件。现有工作对尺度向量的作用机制、权重衰减策略以及设计空间均缺乏系统认知，许多实践中是否对γ施加weight decay甚至相互矛盾。本文旨在揭示尺度向量在Pre-Norm架构中的本质作用，并利用新的理论理解提出轻量优化设计。

**方法关键点：**
- **理论分析**：在Pre-Norm架构中，尺度向量不增加模型表达能力（可被吸收到后续线性映射），但通过引入状态依赖的自放大预条件器 \( P_{f,j}(t) = \gamma_j(t)^2 I + w_{f,j}(t) w_{f,j}(t)^\top \)，加速梯度下降。证明即使从相同损失出发，带尺度向量的模型始终拥有更快的损失下降。
- **权重衰减原则**：将RMSNorm分为Input-Norm（后接线性映射）和Output-Norm（不接线性映射）两类，理论证明对Input-Norm尺度向量加weight decay可控制Hessian尖锐度、加速训练；对Output-Norm尺度向量加weight decay则会限制表达性，应禁用。
- **三种改进设计**：(1) **分支异构 (HG)**：对注意力中的Q/K/V和FFN中的gate/up分支分配独立的尺度向量，以匹配不同分支的训练动态；(2) **放置优化 (DP/DNP)**：在 Pre-Norm 线性映射的输出侧增加尺度向量，或采用带归一化的双端放置，使预条件同时作用于行和列方向，进一步加速优化；(3) **幅度方向重参数化 (OR/ER)**：将γ分解为幅度β和方向单位向量，在原始空间或指数空间中参数化，诱导各向异性的预条件器，让幅度方向获得d倍的学习率放大。
- **统一观点**：这些设计都可视为对有效权重矩阵的轻量重参数化 \( W_c \mapsto \text{diag}(u_c)W_c\text{diag}(v_c) \)，其诱导的预条件器与优化器自适应预条件互补。

**关键结果：**
- 在0.12B Llama上，移除全部尺度向量导致验证损失增加约0.028（1.4× token差距），调大学习率后仍差0.015。
- 综合采用HG+DNP+OR+IWD的统一策略，在0.12B~2B的密集Llama和MoE模型上，均在100 tokens/param的训练预算下一致降低终端损失，拟合的缩放定律显示约1.22-1.25×的算力效率提升。
- 与Muon优化器和wsd学习率调度兼容，在0.5B密集和MoE上额外降低损失0.016-0.019，且优势在学习率平稳阶段持续扩大。
- 计算开销仅增加4%的wall-clock time和1%的内存，参数增量最多7.85×10⁻⁵。

**最值得记住的一句话：** 尺度向量是Pre-Norm Transformer中几乎无代价的优化加速器，其功能可通过分支独立、双端放置和幅度方向解耦被进一步放大，且对Input-Norm和Output-Norm应执行不同的weight decay策略。
