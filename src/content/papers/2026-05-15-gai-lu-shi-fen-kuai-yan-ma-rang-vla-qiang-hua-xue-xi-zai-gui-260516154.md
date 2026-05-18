---
title: 'Learn Where Outcomes Diverge: Efficient VLA RL via Probabilistic Chunk Masking'
title_zh: 概率式分块掩码：让 VLA 强化学习在轨迹发散处高效更新
authors:
- Vaidehi Bagaria
- Nikshep Grampurohit
- Pulkit Verma
affiliations:
- Indian Institute of Technology Madras
arxiv_id: '2605.16154'
url: https://arxiv.org/abs/2605.16154
pdf_url: https://arxiv.org/pdf/2605.16154
published: '2026-05-15'
collected: '2026-05-18'
category: Training
direction: 高效强化学习训练优化
tags:
- GRPO
- VLA
- Efficient Training
- Probabilistic Masking
- RL
one_liner: 用成功-失败动作方差定位学习信号，概率掩码轨迹块，实现 GRPO 梯度计算 4.8 倍加速且成功率无损
practical_value: '- 在序列决策模型（如对话 Agent、推荐序列）的 RL 训练中，可借鉴 PCM 的思路：仅对成功与失败轨迹出现行为分歧的时间步计算梯度，避免在已经学好的区域浪费算力。

  - 利用分组 rollouts（如 GRPO 的对比样本组）的“成功-失败动作方差”作为信息量指标，无需额外价值网络，可低成本筛选出关键决策片段，适合 critic-free
  的 LLM 微调场景。

  - 在线更新阶段级保留概率的机制，可动态适应策略变化，在推荐模型持续训练或在线学习时有借鉴意义，能更高效地利用回放数据。

  - 工程实现上轻量（drop-in 替换 GRPO），无需奖励模型，能同时大幅降低显存（60% 峰值激活）和训练时间，适合资源受限的 VLA 策略或大模型 RL
  微调。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：VLA 策略的 RL 后训练中，梯度计算占每步墙钟时间约 78%，而 rollout 收集仅占 21%。主因是 GRPO 将相同优势分配给轨迹中所有时间步，导致大量梯度计算浪费在策略已掌握的阶段。实际上，学习信号仅来源于成功与失败轨迹出现行为分歧的片段。

**方法**：提出 Probabilistic Chunk Masking (PCM)，一种 GRPO 的即插即用改进。首先将轨迹划分为语义阶段，用成功-失败动作方差度量每个阶段内成功与失败 rollout 的动作差异，作为“梯度方差”的代理；然后根据该指标在线更新各阶段的保留概率，并概率性地采样一个固定预算的 chunk 进行反向传播，跳过其余部分。方法无需奖励模型或额外 critic。

**结果**：在三个 LIBERO 基准上，PCM 达到与标准 GRPO 相同的最终成功率，同时实现 2.38 倍总墙钟加速，梯度更新速度提升 4.8 倍，峰值激活性内存降低 60%，且仅对不到 20% 的轨迹块计算梯度。
