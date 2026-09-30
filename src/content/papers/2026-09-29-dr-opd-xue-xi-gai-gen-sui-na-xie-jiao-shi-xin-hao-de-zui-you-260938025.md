---
title: 'Dr. OPD: Learning What to Follow for Optimal On-Policy Distillation of Large
  Language Models'
title_zh: Dr. OPD：学习该跟随哪些教师信号的最优在线蒸馏
authors:
- Zhenyu Wang
- Tianze Wang
- Linjun Zhang
- Yifan Hu
affiliations:
- Rutgers University
arxiv_id: '2609.38025'
url: https://arxiv.org/abs/2609.38025
pdf_url: https://arxiv.org/pdf/2609.38025
published: '2026-09-29'
collected: '2026-09-30'
category: Training
direction: On-policy distillation 自适应 token 加权
tags:
- On-Policy Distillation
- Token Weighting
- Bilevel Optimization
- LLM
- Outcome Reward
- JVP
one_liner: 通过双层优化学习 token 级教师信号权重，使学生在在线蒸馏中以 outcome reward 为准则超越教师
practical_value: '- 在蒸馏生成式物品/query 模型时，不要平均地模仿 teacher 的所有 token，可以用 outcome reward（如点击、转化、生成质量分）与
  teacher correction 的梯度对齐来给 token 加权。闭式更新 `weight = clip(1 + λ * credit, w_min, w_max)`
  实现简单，λ 在 0.2-0.6 内不敏感，适合线上快速调参。

  - 工程上，credit 的计算不需要为每个 token 显式保存参数梯度，用一次 JVP 即可得到所有 token 的方向导数，开销很小；可直接在现有 GRPO/PPO
  框架里加一个 JVP + 权重重算步骤，且可以复用 actor optimizer 的二阶矩做 scaling，稳定训练。

  - 在业务 LLM 微调中，当 teacher 比 student 强但 reward 信号存在（如 search 中用户点击、query 改写后的检索指标），可先蒸馏后加
  reward 加权，可能让 1.7B 小模型超过 4B 教师；对于 base 模型冷启动，若 reward 成功样本太少，提升有限，需要先保证一定的成功 rollout
  比例或使用更简单训练子集。

  - 可复用的结论：不是所有教师监督都有用，遵循“有利于 reward 的教师信号”才提升业务指标；在 OPD 基础上融合 outcome reward 的方式很重要，简单加
  GRPO 或 gate 可能只带来 marginal gains，梯度对齐的 token-level 加权是关键。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
Vanilla OPD 将 teacher 的 token-level 监督同等看待，忽略不同 token 对最终结果的影响差异。例如纠正关键推理步骤 vs 替换同义措辞，两者对答案正确性的作用完全不同。因此需要选择哪些教师信号值得跟随，且应以学生最终 task reward 为准，而非仅匹配教师分布。

**方法关键点**
- 定义 weighted OPD：在 reverse KL 中引入 token 权重 w(s,v)>0，保持蒸馏目标有效性。
- 将最优权重选择形式化为双层优化：上层最大化学生的 outcome reward，下层给定权重训练学生。
- 迭代求解：每轮从当前学生采样，计算 teacher correction g_t（将 token 概率推向教师）和 reward gradient 的 credit c_t = g_t^T ∇R(θ+vani)，判断跟随教师是否提升 reward。
- 通过对 reward 的下界近似，得到闭式权重更新：w+ = clip(1 + λ c_t, wmin, wmax)，无需额外训练权重模型。
- 高效计算：credit 需要每个 token 的参数梯度与 reward gradient 内积，作者用一次 Jacobian-vector product (JVP) 求出所有 token 的方向导数，避免显式构造大参数梯度。
- 实现细节：credit 使用 GRPO 的 group-relative advantage 估计 reward gradient，并对 credit 做 RMS 归一化和 clip，复用 actor optimizer 二阶矩稳定训练。

**关键实验结果**
在 Qwen3 系列上做 strong-to-weak（4B teacher → 1.7B student）和 same-size（4B RL teacher → 4B student）蒸馏，数学用 DeepMath-103K，代码用 Eurus-RL-Code，评估 AIME24/25、AMC、Minerva、OlympiadBench 及 HumanEval+、MBPP+、LiveCodeBench。与 OPD、ExOPD、OPD+GRPO、GRPD 对比。
- Strong-to-weak：Qwen3-1.7B Instruct 上 Dr. OPD 数学平均 +9.7 分（25.3→35.0），超过 4B teacher 的 34.1；代码平均 +5.0 分。
- Base 学生冷启动下，代码提升 +6.4，数学提升 +1.8，收益受成功 rollout 数量影响。
- Same-size：Dr. OPD 分别比 OPD 提升 +2.3 和 +3.0，且均超过 RL-trained teacher。
- 消融：λ>0 均优于 OPD，λ=0.4 最佳，说明方法对 λ 不敏感。

**最值得记住的一句话**
不是每个教师 token 信号都同等重要，应根据其对 outcome reward 的梯度对齐来加权；正确加权后，1.7B 学生可以在数学上超过 4B 教师。
