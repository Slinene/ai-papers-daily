---
title: On the Redundancy of Timestep Embeddings in Diffusion Models
title_zh: 扩散模型中时间步嵌入的冗余性研究
authors:
- José A. Chávez
affiliations:
- Independent Researcher, Lima, Peru
arxiv_id: '2606.20416'
url: https://arxiv.org/abs/2606.20416
pdf_url: https://arxiv.org/pdf/2606.20416
published: '2026-06-18'
collected: '2026-06-21'
category: Other
direction: 生成架构简化与冗余去除
tags:
- Diffusion Models
- Timestep Embeddings
- Generative Models
- Ablation Study
- Efficiency
one_liner: 证明扩散模型可在无显式时间步嵌入下达到最优，输入可隐式推断噪声尺度，实现更高效生成架构
practical_value: '- 在基于扩散的推荐模型（如 DiffRec）中，可尝试移除时间步嵌入，利用用户交互序列或物料特征直接隐式推断噪声尺度，减少额外调制参数

  - 简化时间步调制后，推理阶段无需处理时间编码，降低工程复杂度与延迟，适合在线推荐场景

  - 无时间步嵌入的扩散模型可能更鲁棒，尤其在数据稀疏的冷启动场景，模型会更关注内容结构而非时间信号

  - 注意力可集中于去噪网络本身的结构设计，为序列推荐中利用上下文长度、时间间隔等信息提供新思路'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：扩散模型普遍依赖显式时间步嵌入来调制不同噪声尺度下的去噪；但该条件信号是否绝对必要尚未被充分验证。本文直接挑战这一长期范式，探究移除时间步嵌入对 U-Net 与 DiT 架构的影响。

**方法关键点**：
- 理论推导：证明在特定条件下（如去噪目标为 L2 损失），全局最优解可以在无显式时间步条件下达到——模型能从被破坏的输入中隐式推断噪声尺度。
- 架构修改：直接从 U-Net 和 DiT 的所有注入位置删除时间步嵌入，取消特征图相加或自适应调制，仅保留基于噪声输入的学习。
- 实验：在 CelebA 和 CIFAR-10 上进行消融，比较有无时间步嵌入的生成质量。

**关键结果**：
- 无时间步嵌入的模型在 FID、精度、召回率等指标上持平甚至超越原始条件模型，表现出惊人鲁棒性。
- 结构保真度得以维持，间接验证了输入本身携带的噪声强度信息足以引导去噪过程。
