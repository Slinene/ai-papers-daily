---
title: How to Train a Critic Stably and Efficiently
title_zh: 如何稳定且高效地训练 Critic
authors:
- Penghui Qi
- Xiangxin Zhou
- Wee Sun Lee
affiliations:
- National University of Singapore
- Tencent Hunyuan
arxiv_id: '2608.23566'
url: https://arxiv.org/abs/2608.23566
pdf_url: https://arxiv.org/pdf/2608.23566
published: '2026-08-24'
collected: '2026-08-25'
category: Training
direction: LLM RL 的 Critic 稳定训练
tags:
- RLHF
- Critic Optimization
- DPPO
- GAE
- Advantage Normalization
- LLM Reasoning
one_liner: BPCO 通过值域约束、MC 目标、去标准化等配方稳定单 rollout critic，性能匹配或超过 group 基线
practical_value: '- 若在电商/广告场景用 RL 微调 LLM 生成推荐文案、搜索 query 或导购对话策略，可改用单 rollout critic
  替代 GRPO 多采样，节省采样成本；并采用 BPCO 的 bounded value head（arctan 映射到 reward 范围）和 MC value
  target（λ_V=1），这是稳定性最核心的两项改动。

  - 当 reward 由规则、评分 rubric 或成交标签产生时，让训练期 critic 额外接收这些 reward-defining 信息（如真实成交额、评分细则），policy
  仅使用用户上下文和生成前缀。这样线上推理不增加任何输入，但 critic 拟合更快；小数据量时需注意过拟合。

  - 直接移除 advantage batch normalization，使用 raw GAE advantage 更新 policy；实现成本极低，能避免策略收敛后更新不衰减、噪声被放大导致过拟合。

  - 若生成序列长度差异大（比如长推荐理由 vs 短 query 改写），将 policy 端 GAE 改为 length-adaptive λπ(L)=1-1/(αL)，α
  取 0.4 左右；critic 端保持 λ_V=1 做无偏回归，可稳定长序列上的 credit assignment。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
Critic-based RL 在 LLM 上常不稳定，而 group-based 方法如 GRPO 虽避免 critic 但需要多样本且 token 级 advantage 粗糙。本工作系统定位不稳定来源：PPO 比例 clip 不均匀、bootstrapped value target 自指偏置、固定 GAE 在长序列中 terminal reward 权重衰减、线性 value head 外推超 reward range、batch-wise advantage normalization 放大噪声。

**方法关键点**
- DPPO：以 sampled token 概率绝对变化 |πθ - μ| ≤ ε 作为信任域，替代 PPO 的 ratio clip。
- 值预测限定 reward range：value head 用 scaled arctangent 映射到 (Rmin, Rmax)，防止极端预测。
- 无偏 MC value target：critic 训练目标设为最终 outcome R(x,y)（λ_V=1），避免 bootstrap 偏置；policy 仍可用 λπ<1 降方差。
- 移除 batch-wise advantage normalization：直接使用 raw GAE advantage，避免策略收敛后噪声被放大。
- length-adaptive GAE：policy λπ(L)=1-1/(αL)，α≈0.4，使 terminal reward 权重近似长度不变。
- Privileged critic input：critic 可看 reward-defining 信息（答案、解题、rubric），policy 不接触。

**关键实验**
- 1.5B 模型 sanity test 上，DPPO+λ=1 稳定；逐步加入上述组件在 λ=0.99 压力下稳定。
- DeepScaleR 40.3K 数学题，BPCO 在训练奖励和 AIME 2025 avg@32 上持续优于 critic baseline 与 group baseline；explained variance 更高。
- 30B-A3B MoE 模型上，critic baseline 100 步后停滞，BPCO 显著更好，单 rollout 匹配或超过 group baseline（group size 16）。
- 在 rubric reward 任务上 BPCO 更快收敛，特权 rubric 无额外收益。

**最值得记住的一句话**
Critic 自身不是 LLM RL 的固有弱点；当输出范围、目标、输入与 policy 信号设计一致时，它是 group-relative estimation 的稳定高效替代方案。
