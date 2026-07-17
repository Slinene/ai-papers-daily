---
title: Mask-Aware Policy Gradients for Diffusion Language Models
title_zh: 掩码感知策略梯度：面向扩散语言模型的强化学习
authors:
- Haran Raajesh
- Kulin Shah
- Adam Klivans
- Philipp Krähenbühl
affiliations:
- The University of Texas at Austin
arxiv_id: '2607.15200'
url: https://arxiv.org/abs/2607.15200
pdf_url: https://arxiv.org/pdf/2607.15200
published: '2026-07-16'
collected: '2026-07-17'
category: LLM
direction: 扩散语言模型 · 强化学习训练
tags:
- diffusion language model
- policy gradient
- reinforcement learning
- mask-aware
- masked generation
one_liner: 将扩散语言模型生成分解为“选词”与“选位置”两步，策略梯度自然拆分成两项，联合优化在数学与代码推理上达到SOTA
practical_value: '- 对电商/推荐中使用非自回归生成（如扩散模型生成商品序列或文案）有直接啓发：可将生成过程建模为两阶段 MDP——“生成什么 token”与“在哪些位置生成”，分离梯度后能更稳定地优化序列质量。

  - 在 Agent 多步决策场景，如果动作包含“执行什么操作”和“在哪个目标上执行”，可借鉴本工作的动作空间分解，用对应的 mask 策略网络显式建模顺序决策，提升复杂任务表现。

  - 工程实现上，可对现有 GRPO/PPO 等 RL 训练框架做简单改造：在计算每步 log 概率时，将 token 预测的 log-prob 与 mask 选择的
  log-prob 相加，同时优化两个头，无需大幅改动训练管线。

  - 该方法表明扩散生成的去掩码顺序严重影響效果，在线 RL 训练时联合学习生成顺序，比固定随机顺序有明显的增益（GSM8K 提升+2.5%），这提示我们在生成式推荐中，如果采用逐步生成，也应将生成顺序作为可学习策略，而非预定义。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：扩散语言模型（MDLM）在推理任务上效果强劲，但用强化学习提高推理能力时，面临 log-likelihood 难以准确计算的难题。已有方法（如 D1、GDPO）只对 token 预测建模，完全忽略生成过程中逐位置去掩码（unmask）的顺序，导致估计偏差，优化效果受限。

**方法关键点**：作者将 MDLM 每步生成重新定义为两阶段动作：第一步选择哪些位置放什么 token（token 動作），第二步选择哪些位置重新 mask（mask 動作）。整个生成过程构成一个两级 MDP，推导得出 policy gradient 自然分解为 token 项与 masking 项。基于此，可同时训练 token 预测头和 mask 策略头，用 GRPO 风格算法直接优化。训练时奖励使用 final answer 的正确性，无需 reward model。

**关键结果**：在 LLaDA-8B-Instruct 基座模型上，将本方法用于数学推理（GSM8K、MATH500）与代码生成（HumanEval、MBPP），全部显著超越 D1、GDPO、StepMerge 等基线。GSM8K 达到 **87.1%**（提升 2.5%），MBPP 达到 **53.4%**（提升 2.2%），MATH500 提升 4.0%。消融显示，固定随机去掩码顺序会明显损害性能，证实可学习的 mask 策略至关重要。
