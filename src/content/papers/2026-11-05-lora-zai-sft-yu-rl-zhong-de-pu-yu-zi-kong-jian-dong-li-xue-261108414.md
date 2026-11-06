---
title: Spectral and Subspace Dynamics of LoRA in Supervised Fine-Tuning and Reinforcement
  Learning
title_zh: LoRA 在 SFT 与 RL 中的谱与子空间动力学分析及定制优化
authors:
- Chenruo Liu
- Zihan Wang
- Yijun Dong
- Qi Lei
affiliations:
- New York University
- Institute of Science and Technology Austria
arxiv_id: '2611.08414'
url: https://arxiv.org/abs/2611.08414
pdf_url: https://arxiv.org/pdf/2611.08414
published: '2026-11-05'
collected: '2026-11-06'
category: Training
direction: LoRA 训练动态分析与阶段定制优化
tags:
- LoRA
- SFT
- Reinforcement Learning
- Spectral Dynamics
- Subspace Rotation
- Fine-tuning
one_liner: 揭示 RL 基线减法导致 LoRA 谱集中与子空间快速旋转，针对 SFT/RL 设计不同平坦化更新提升推理性能
practical_value: '- SFT 阶段不要默认标准 LoRA：可对全更新矩阵的奇异值做平坦化（flatten）处理，放大弱奇异方向，避免只在少数主导方向过拟合，提升下游任务适应与泛化能力。

  - RL 阶段（如 RLHF/GRPO/策略优化）中，group-mean baseline subtraction 自然促进子空间旋转，只需较小学习率即可获得良好探索；因此当计算资源有限时，优先保障基线减法机制，而非单纯调大
  LR。

  - 可以通过监控 LoRA 更新矩阵的奇异谱诊断微调阶段：若 SFT 谱过度集中，可能表征记忆而非泛化；若 RL 谱过度集中但子空间旋转慢，则需检查更新是否局限在初始子空间内。

  - 在推荐/Agent 大模型微调中，区分 SFT 与 RL 阶段设计不同的 LoRA 更新策略（SFT 平坦化全更新，RL 平坦化 LoRA 当前 span
  之外的部分），比统一配置更可能获得更优的在线策略性能。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**
LoRA 在 SFT 与 RL 中广泛使用且优化器设置相似，但两阶段下的低秩增量动力学差异未被理解。

**方法关键点**
在数学推理任务上追踪 LoRA 更新的奇异谱与子空间变化，发现：RL 在所有学习率下都使谱集中，SFT 在中等学习率下谱扩张；RL 在小学习率下旋转奇异子空间远快于 SFT。通过逐个替换 SFT/RL 要素，定位到 group-mean baseline subtraction 是两者差异的根源。进一步利用二次 multi-index 模型分析 LoRA 更新机制：基线减法打破 coherent fitting 与 gradient noise 的平衡，推动谱集中和子空间快速旋转，同时迫使风险有利学习率降低。基于此提出阶段定制策略：SFT 平坦化全更新谱以跨奇异方向铺开适配；RL 平坦化当前 LoRA 增量 span 之外的部分以促进子空间旋转。

**关键结果**
在多个模型和数学推理任务上，SFT 与 RL 各自的定制配置在多数评估设置中达到最优。
