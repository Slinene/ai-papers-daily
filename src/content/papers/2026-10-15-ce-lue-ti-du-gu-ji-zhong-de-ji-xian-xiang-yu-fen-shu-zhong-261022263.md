---
title: Baselines and Score Centering in Policy Gradient Estimation
title_zh: 策略梯度估计中的基线项与分数中心化
authors:
- Shuo Han
- Ziqing Hu
affiliations:
- University of Illinois Chicago
- Perplexity AI
arxiv_id: '2610.22263'
url: https://arxiv.org/abs/2610.22263
pdf_url: https://arxiv.org/pdf/2610.22263
published: '2026-10-15'
collected: '2026-10-18'
category: Training
direction: RLHF/策略梯度估计·重要性采样
tags:
- policy gradient
- importance sampling
- RLHF
- score centering
- variance reduction
- LLM post-training
one_liner: 用 reward 与 importance-weighted score 的协方差替代正则化 IS 策略梯度，厘清 group-mean baseline
  与 score centering 的不同作用
practical_value: '- 在电商/Agent 的 LLM RLHF 后训练中，若用 sequence-level PPO/GRPO 且 ratio 被
  clip，直接用 batch 内 mean reward 作为 group-mean baseline 即可，不必再对 importance-weighted
  score 做额外 centering，降低实现复杂度。

  - 若采用 token-level advantage（细粒度 reward/PPO），当 importance ratio 被 truncation/masking/clipping
  时，必须对 importance-weighted score 做 score centering（减去总体均值，可用 moving average 估计），否则策略梯度会带偏置。

  - 建议把梯度写成 Cov(reward, weighted_score) 而非单纯加权 reward；该形式天然对 constant reward shift
  稳健，适合离线异步训练中 stale policy 的纠偏。

  - 序列级 IS 下 score centering 无额外收益，token 级 IS 下则是必要修正；实现前先确认 reward/advantage 的粒度再决定是否引入
  score centering。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLM 后训练常用 off-policy RL，行为策略与目标策略不一致，需 importance sampling (IS) 纠偏。实际中 IS ratio 常被 truncation/masking/clipping 正则化，此时 importance-weighted policy gradient 不再对 reward 的常数平移保持不变。

**方法**：改用 Cov(reward, importance-weighted score) 作为 estimand；当 ratio 未正则化时，它与标准 policy gradient 等价。该协方差视角统一处理 sequence-level 与 token-level IS，区分 group-mean baseline（减样本均值）与 score centering（减总体均值）：两者都是协方差估计中的中心化，但减去的均值不同，得到不同的无偏协方差估计量，方差也不同。

**结果**：序列级 IS 下，使用 group-mean baseline 后 score centering 没有额外收益；token 级 IS 下，当 importance ratio 被正则化时，只用 group-mean baseline 而不做 score centering 通常会引入偏置。论文为两类 IS 粒度给出了明确的中心化选择依据。
