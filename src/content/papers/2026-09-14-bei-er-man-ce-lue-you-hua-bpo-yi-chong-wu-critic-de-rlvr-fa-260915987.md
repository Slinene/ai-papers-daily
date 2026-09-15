---
title: Bellman Policy Optimization
title_zh: 贝尔曼策略优化（BPO）：一种无 Critic 的 RLVR 方法
authors:
- Zhuoqing Song
- Haotian Xu
- Xikun Zhang
- Lidong Bing
affiliations:
- Apodex US, Inc.
- Princeton University
arxiv_id: '2609.15987'
url: https://arxiv.org/abs/2609.15987
pdf_url: https://arxiv.org/pdf/2609.15987
published: '2026-09-14'
collected: '2026-09-15'
category: Training
direction: RLVR 策略优化 · Critic-free
tags:
- RLVR
- Policy Mirror Descent
- Critic-free
- GRPO
- Mathematical Reasoning
- LLM Training
one_liner: 利用 Bellman 方程将 Policy Mirror Descent 重构为轨迹级目标，避免价值估计，在 AIME 数学推理上显著超过 GRPO
  等基线
practical_value: '- 对用 RLVR 训练对话式推荐、解释生成、query 改写等 LLM 任务的团队，可尝试用 BPO 的 token-level
  权重替代 GRPO 的 importance ratio：仅将 ratio 换成 (1+ε-μ(y_t|s_t))/(1+ε-π(y_t|s_t))，改动小，且论文显示对
  ε、C 超参数不敏感。

  - 如果业务奖励是可验证的 terminal reward（如用户点击/转化、任务完成、代码执行、工具调用成功），BPO 提供了一种无需 value model
  的 critic-free 更新，省去训练 critic 的 GPU/内存成本，避免 value estimation 误差带来的不稳定。

  - 分组归一化 advantage + 互补概率权重 + truncation/masking 的组合，可作为 RLVR 训练中缓解 rollout/training
  policy mismatch 的工程 trick，尤其适合 MoE 或 router 不稳定等场景。

  - 该论文主要在数学推理上验证，直接迁移到推荐/广告文案或 Agent 规划效果需自行验证；但其理论等价性和对超参数的鲁棒性，值得在 reasoning 型推荐
  Agent 或 search query 生成中用 A/B 测试评估。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
RLVR 在提升 LLM 推理能力上效果显著，但现有 GRPO 等基于 PPO 的 critic-free 方法存在不足：outcome reward 下所有 token 共享同一个 advantage，缺乏细粒度 credit assignment，且 rollout 与训练 policy 不一致时 importance ratio 偏差大；训练 value model 又昂贵且不可靠。需要一种无需 critic 但理论上更合理、能保持训练稳定性的策略优化目标。

## 方法关键点
- 起点是 Policy Mirror Descent（PMD），其闭式解给出 token 级优势 A^μ(s,a) 下的最优 policy 更新。
- 利用 terminal reward 下 Bellman 方程：A^μ(s_t,y_t)=V^μ(s_{t+1})-V^μ(s_t)，沿 trajectory 累加得到 token 级优势之和 = R(x,y)-V^μ(x)。因此可将 PMD 重构为 trajectory-level residual：δ(x,y;π,μ)=η(R(x,y)-V^μ(x))-Σ_t[log(π/μ)+D_KL(μ||π)]，避免估计中间状态价值。
- 该轨迹级目标与原始 PMD 有相同唯一最优解（Theorem 1）。
- 实际损失通过近似得到：线性化 residual、用 group 均值/标准差估计 V^μ(x) 和归一化、用 binary KL 替代 full KL，得到梯度 multiplier 为 (1-μ(y_t|s_t))/(1-π(y_t|s_t))，即互补 token 概率的平滑比率；再应用 GRPO-style masking 和 truncation。
- 最终 BPO loss 与 GRPO 形式相似，但把 importance ratio 替换为 ω_i^t=(1+ε-μ)/(1+ε-π)，并有 clip/cap。

## 关键结果
- 在 Qwen3-30B-A3B-Base、DAPO-Math-17k 英文子集上训练，AIME24-26 Avg@32 平均准确率 50.5%，比 GRPO-ClipHigher 高 11.0，比 GSPO 高 7.0，比 CISPO 高 3.1，比 DPPO 高 4.1 个百分点。
- AIME24/25/26 分别为 57.4/41.0/53.0。
- 消融显示 ε∈[0.05,0.2]、C∈[2,4] 结果稳定。

## 最值得记住的一句话
用 Bellman 方程把 PMD 变成轨迹级 residual，避免 critic，并把 GRPO 的 importance ratio 换成互补概率比率。
