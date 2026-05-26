---
title: 'DVAO: Dynamic Variance-adaptive Advantage Optimization for Multi-reward Reinforcement
  Learning'
title_zh: DV AO：面向多奖励强化学习的动态方差自适应优势优化
authors:
- Guochao Jiang
- Jingyi Song
- Guofeng Quan
- Chuzhan Hao
- Guohua Liu
- Yuewei Zhang
affiliations:
- Alibaba Cloud Computing
arxiv_id: '2605.25604'
url: https://arxiv.org/abs/2605.25604
pdf_url: https://arxiv.org/pdf/2605.25604
published: '2026-05-24'
collected: '2026-05-26'
category: Training
direction: 多奖励强化学习 · 优势组合优化
tags:
- GRPO
- multi-reward RL
- variance-adaptive
- Pareto optimization
- LLM alignment
one_liner: 动态按组内奖励方差自适应调整多目标优势权重，解决 GRPO 多奖励标量化的幅度爆炸与目标孤立问题
practical_value: '- **多目标奖励的可学习聚合**：在电商推荐/Agent 多目标优化（如准确率+多样性+延迟）中，现有做法往往直接固定权重标量化奖励或优势，导致某一目标梯度主导。DV
  AO 提供了完全数据驱动的自适应加权方案，无需人工调参，直接基于每个目标的组级方差动态平衡信号强度，可应用于生成式推荐的 multi-reward 对齐。

  - **稳定训练的技巧**：DV AO 从理论上保证了优势幅度低于直接奖励组合，避免策略梯度爆炸。在 RL 微调推荐模型或 Agent 策略时，可直接用于处理准确度、格式合规、长度等冲突目标，防止训练崩溃。

  - **交叉目标正则化机制**：通过优势计算对单一目标梯度的重新缩放，隐式地促进目标间协同优化，避免某个简单目标淹没困难目标。这对 Agent 多轮任务中同时优化任务成功率与工具调用格式很有价值。

  - **轻量实现**：DV AO 不引入额外可学习参数，完全基于组内方差的后计算，易于集成到现有的 GRPO 或 PPO 训练流程中，适合快速实验。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：在实际大模型对齐中，常需同时优化多个奖励（如准确率、长度、格式合规等）。GRPO 的无价值模型特性使其成为高效的 LLM RL 框架，但多奖励适配面临两难：标准标量化方法“奖励组合”会导致优势幅度过大、梯度震荡；“优势组合”虽缓解幅度问题，却采用固定权重且孤立刻画各目标，忽视目标间相关性，难以达到最优帕累托平衡。

**方法**：提出 Dynamic Variance-adaptive Advantage Optimization (DV AO)。核心思想是用每个奖励在 rollout 组内的经验方差动态调整优势组合权重：高方差目标（携带更强学习信号）被放大，低方差目标（可能噪声）被抑制。理论上证明了：(1) DV AO 优势幅度始终不超过奖励组合法，保证训练稳定；(2) 梯度对单目标奖励的敏感性不仅依赖于自身优势，还与全体目标的联合优势乘积相关，从而实现自适应的跨目标正则化。

**实验**：在数学推理（AIME-2024/2025、MATH500 等）和工具使用（BFCL-v4）两个多目标任务上，基于 Qwen3-4B/8B 和 Qwen2.5-3B/7B 模型训练。DV AO 在保持极高标准（长度/格式合规接近 100%）的同时，准确率显著超过 GRPO、RC、AC、GDPO 等基线。例如 Qwen3-8B 在数学推理上平均准确率 47.49%，长度合规 99.92%，而最强的 AC 基线仅 45.42%/98.84%。帕累托前沿分析也确认 DV AO 在整个权重扫描范围中占优。训练动态曲线显示该方法能更快提升准确奖励均值并稳定压低其方差。

**一句话**：DV AO 通过方差自适应权重实现了无需调参、幅度受控且有跨目标协同能力的多奖励 GRPO 优化。
