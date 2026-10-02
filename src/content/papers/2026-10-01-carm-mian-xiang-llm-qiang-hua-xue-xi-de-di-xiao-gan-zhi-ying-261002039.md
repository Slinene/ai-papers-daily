---
title: 'CARM: Cancellation-Aware Response Masking for LLM Reinforcement Learning'
title_zh: CARM：面向 LLM 强化学习的抵消感知响应掩码
authors:
- Yafei Zhang
- Songshuo Lu
- Sicong Liao
- Zhi Chen
- Yaohua Tang
affiliations:
- Moore Threads AI
arxiv_id: '2610.02039'
url: https://arxiv.org/abs/2610.02039
pdf_url: https://arxiv.org/pdf/2610.02039
published: '2026-10-01'
collected: '2026-10-02'
category: Training
direction: LLM RL 离策略响应掩码
tags:
- LLM RL
- off-policy
- GRPO
- sequence masking
- trust region
- response filtering
one_liner: 用绝对 log-ratio 均值替代带符号 geometric mean，防止双向策略漂移相互抵消，提升 GRPO 训练稳定性与推理/代码效果
practical_value: '- 在做 LLM 推荐/Agent reasoner 的 GRPO/PPO 训练时，可直接把现有 GeoMean 离策略 mask
  换成 CARM：只改聚合方式为 mean absolute log-ratio，复用 rollout logprobs，工程成本低，且不改变 token 级 surrogate。

  - 阈值可直接当策略漂移监控：对 token ratio band [0.8,1.28]，tau=1.02 意味着最多约 8.88% token 越界；tau=1.04
  约 17.58%。可据此设置离线训练过滤阈值和预警线。

  - 不要只 mask negative-advantage 样本：CARM 消融显示标准全量 mask 在数学和代码任务上都明显好于 negative-only；正
  advantage 样本同样可能离策略，推荐/Agent 任务中奖励稀疏时更建议全量掩码。

  - 过滤比例不是越高越好：accuracy 与 masked fraction 非单调，调试时不要只盯 mask rate，应结合验证集准确率、保留样本质量或
  best-of-k 一致性来调 tau。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机

LLM 后训练中的 PPO/GRPO 通常假设采样策略和当前优化策略一致，但 actor–learner 延迟、mini-batch 带来的策略陈旧、rollout 引擎与训练后端差异都会引入 off-policy。序列级掩码用于决定整条 response 是否参与更新，常见做法是用长度归一化的 token 概率比的 geometric mean，等价于对带符号 log-ratio 求均值。关键问题是：正负 log-ratio 会相互抵消，一条 response 可能每个 token 都产生了 10 倍概率变化，但几何均值得分仍接近 1，从而被错误接受。

## 方法关键点

- **CARM score**：先取绝对值再平均，`d_CARM = (1/T) Σ |log r_t|`，`s_CARM = exp(d_CARM)`，当 `s_CARM ≤ τ` 时保留 response。
- **对称性**：每个 token 等价于 `max(r_t, 1/r_t)` 的 mismatch，reciprocal 变化不被抵消。
- **可解释阈值**：若设 token ratio band `[ℓ,u]`，CARM 接受条件给出越界 token 比例 `p_out` 与平均越界严重度 `δ_out` 的联合预算：`p_out ≤ min(1, log τ / (b_min + δ_out)) ≤ log τ / b_min`。
- **实现**：mask 在损失评估时用当前 policy forward 和 rollout 存储 logprobs 计算，`stopgrad` 后作为二值 gate；保留 token 级 PPO/GRPO clip，不替代 clip。
- **与 GeoMean 的关系**：三角形不等式保证 `s_CARM ≥ s_GeoMean`，同一阈值下 CARM 接受集是 GeoMean 的子集。

## 关键实验

在 Qwen3.5-4B/9B 上，用 verl/GRPO 训练 DAPO Math，数学评估 AIME 2024/2025/2026 + BeyondAIME；代码用 TACO 训练，评估 TACO test、LiveCodeBench-v6、HumanEval+、MBPP+。对比 Null、IcePop、TRM、GeoMean。

- 数学：Qwen3.5-4B 四数据集平均 63.45 vs GeoMean 61.59；Qwen3.5-9B 平均 70.42 vs 67.29，相对 GeoMean 提升最高约 3.13 个点。
- 代码：平均 pass@1 从 GeoMean 65.28 提升到 68.31，比最强 baseline 高 2.88 个点；LiveCodeBench-v6 从 44.50 提升到 51.20。
- 消融：标准 CARM mask 明显优于 negative-only mask；mask rate 相似时 CARM 仍更优，且 accuracy 不随 masked fraction 单调上升。

最值得记住的一句话：**off-policy 序列掩码不能只看净位移，正负概率漂移会抵消；改成平均绝对 log-ratio，既防抵消又给「越界 token 比例 × 越界严重度」一个确定的预算。**
