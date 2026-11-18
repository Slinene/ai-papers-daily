---
title: Regularized Score Centering
title_zh: 正则化分数中心化
authors:
- Hao Bai
- Chenlu Ye
- Xuanchang Zhang
- Aviral Kumar
- Tong Zhang
affiliations:
- University of Illinois Urbana-Champaign
- Carnegie Mellon University
arxiv_id: '2611.21791'
url: https://arxiv.org/abs/2611.21791
pdf_url: https://arxiv.org/pdf/2611.21791
published: '2026-11-15'
collected: '2026-11-18'
category: Training
direction: LLM Agent 异步 RL 训练稳定性
tags:
- score centering
- reverse KL
- off-policy RL
- LLM agents
- sample efficiency
- asynchronous training
one_liner: 提出 RSC，在 score centering 基础上加反向 KL 正则，提升异步 LLM Agent 强化学习的稳定性与样本效率
practical_value: '- 在异步 LLM Agent 训练中（如电商购物 agent、工具调用 agent），若 rollout 数据来自旧策略，避免直接用
  full importance sampling；改用 score centering 或 SC+TIS 可明显降低梯度尖峰，训练更稳。

  - 给 loss 增加 token-level reverse KL 正则项，约束 learner 的 next-token 分布向 behavior policy
  靠拢，能防止策略漂移；这比只对 final reward 加 KL 更细粒度，也兼容截断 importance sampling。

  - 多 worker 异步采样导致策略滞后时，RSC+TIS 可用相同交互样本量换更高训练 reward，适合降低在线探索成本，例如 WebShop 这类电商
  agentic 任务。

  - 该方法对 dense 和 MoE 模型均有效，可作为 LLM 推荐/Agent 策略 RLHF 训练的默认稳定组件。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
异步 RL 提升训练吞吐，但陈旧策略数据和训练/推理数值不匹配会破坏学习稳定性。Score centering (SC) 能移除 reward baseline 对期望更新的影响，相比 full importance sampling (IS) 梯度更温和；但当 learner 偏离生成数据的 behavior policy 太远时，SC 仍可能失败。

**方法关键点**  
引入 Regularized Score Centering (RSC)，在 SC 或 SC+TIS 基础上加入反向 KL 惩罚：\(-\beta \mathrm{KL}(\pi_\theta \| \mu)\)，鼓励 learner 的 next-token 分布贴近 behavior policy 的 next-token 分布，从而限制策略不匹配。可与 truncated importance sampling (TIS) 结合，截断 token 重要性权重。理论分析表明 KL 正则化能改善收敛保证。

**结果**  
在数学推理和六个 agentic benchmark（在线购物、工具使用、游戏、完全异步软件工程）上，用 dense 和 MoE 模型评估。RSC+TIS 在所有 agentic 任务上显著提升样本效率，相同采样响应数下获得更高训练 reward；最终评估六个任务全部最优，AppWorld 提升 14.3%，BabyAI 达到最强基线分数的 9.9 倍。
