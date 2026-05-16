---
title: Logging Policy Design for Off-Policy Evaluation
title_zh: 面向离策略评估的日志策略设计
authors:
- Connor Douglas
- Joel Persson
- Foster Provost
affiliations:
- New York University
- Spotify
arxiv_id: '2605.15108'
url: https://arxiv.org/abs/2605.15108
pdf_url: https://arxiv.org/pdf/2605.15108
published: '2026-05-14'
collected: '2026-05-16'
category: Eval
tags:
- Off-Policy Evaluation
- Logging Policy
- Inverse Propensity Weighting
- Reward-Coverage Tradeoff
- Experimental Design
one_liner: 在已知/未知目标策略与奖励分布的信息条件下，推导最小化IPW估计均方误差的最优日志策略，揭示奖励-覆盖权衡
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：离线策略评估中，日志策略的选择对IPW估计量的准确性和效率影响极大，但如何系统设计日志策略以最小化估计的均方误差，至今缺乏理论指导。实践中，目标策略和奖励分布往往不完全已知，存在信息约束，直接采用均匀随机或on-policy收集数据可能导致方差过大或偏差严重。本文在不同信息条件下研究日志策略的最优设计，为优化离线评估提供原则性方法。

**方法关键点**：
- 将日志策略设计形式化为最小化IPW估计量的MSE，并分解为偏差与方差，揭示“奖励-覆盖权衡”：将概率质量集中在高奖励动作可降低方差，但需覆盖目标策略可能选择的动作以避免偏差。
- 在目标策略与奖励分布完全已知时，推导出最优日志策略具有Neyman分配形式：π*_l(a|x) ∝ π_t(a|x)·√μ(a,x)，其MSE低于on-policy评价，且预期奖励不低于目标策略。
- 当只有目标策略分布已知时，构造pseudo-target ˜π_t = √(E[π_t²])，结合√μ分配质量，极大化期望MSE。
- 奖励估计含噪声时，提出后验收缩方法：ˆμ_l向上下文均值收缩，收缩权重w = ε²/(ε²+σ²) 可由历史数据中估计的Cov(ˆμ, R)和Var(ˆμ)近似计算。
- 实践中若无法实施最优策略，提出top-k、softmax、power-normalized三类soft-greedy策略族，通过单一贪婪参数在均匀随机与全贪婪之间平滑插值，接近理论最优MSE。

**关键结果**：
- 模拟显示，个性化日志策略在1,000次观测下的MSE即可达到均匀日志策略100,000次观测的精度；当噪声较低时，优化策略的MSE甚至优于on-policy评估，且日志期间奖励更高。
- 使用推导的收缩规则，即使奖励预测噪声较大，优化日志策略的MSE仍可优于on-policy评估，验证了后验收缩的有效性。
- soft-greedy策略族在合适贪婪参数下可接近理论最优MSE，证实仅需调整一个参数即可平衡奖励-覆盖权衡。

**核心洞见**：通过协同利用目标策略结构与奖励估计，优化日志策略可同时实现比直接运行目标策略更高的奖励和更精确的离线评估——这打破了在策略评价中常见的“推断与收益权衡”。
