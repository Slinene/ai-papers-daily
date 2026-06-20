---
title: 'Stochastic Linear Contextual Bandits with Bounded Noise: A Set-Membership
  Approach'
title_zh: 有界噪声下的随机线性上下文老虎机：一种集合成员估计方法
authors:
- Haonan Xu
- Yingying Li
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2606.20022'
url: https://arxiv.org/abs/2606.20022
pdf_url: https://arxiv.org/pdf/2606.20022
published: '2026-06-18'
collected: '2026-06-20'
category: Other
direction: 在线决策 · 遗憾界改进
tags:
- bounded noise
- linear contextual bandits
- set-membership estimation
- log regret
- optimism
one_liner: 利用奖励噪声有界性提出 SME-OFU 算法，将遗憾界从 O(√T) 降至 O(log T)
practical_value: '- 推荐系统中点击、转化等反馈天然有界（[0,1]），可假定噪声有界，比次高斯假设更强，理论上能获得更低遗憾。实践中可考虑在置信区间构建时利用边界信息，例如采用截断或基于集合估计的不确定性量化，替代通常的
  Hoedffding 不等式。

  - 集合成员估计（SME）提供一种非概率的置信集构造方式，可尝试替代传统岭回归置信椭球，特别适合对噪声分布缺乏先验但对边界明确的场景（如转化率预测）。工程实现上，SME
  本质上维护一个参数可行集，可通过线性不等式约束求解，复杂度可控。

  - 该算法的 UCB 形式（SME-OFU）求解一个凸优化问题，可通过投影梯度或凸包近似处理。在推荐系统的在线学习模块中，可借鉴其乐观选择策略：在可行参数集中选择最大化奖励且满足信息约束的动作，以加速冷启动收敛。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

## 动机
随机线性上下文老虎机是推荐、广告等在线决策的核心模型，通常假设奖励噪声为次高斯，得到 Ω(√T) 的遗憾下界。然而，许多应用中的奖励本身有界（如点击率 ∈ [0,1]），其噪声自然也有界，这一更强的假设尚未在 SLCB 理论中被充分利用。

## 方法
提出 SME-OFU 算法，结合集合成员估计（SME）与乐观面对不确定性（OFU）原理。SME 利用噪声有界这一事实，维护一个包含真实参数 θ* 的可行多面体：Θ_t = {θ : |X_i^Tθ - r_i| ≤ η_max for i=1..t}，其中 η_max 是已知噪声边界。每步在 Θ_t 中选取能最大化期望奖励（乐观）的 θ，据此选择动作并更新可行集。算法无需任何超参数，仅需噪声边界。

## 关键结果
理论证明 SME-OFU 获得 O(log T) 的伪遗憾界，显著优于次高斯噪声下的 O(√T) 最优界。仿真对比 OFUL 算法，在有界噪声（如均匀、截断高斯）下，SME-OFU 的累积遗憾更低且波动更小，非线性结构的学习速度更快。
