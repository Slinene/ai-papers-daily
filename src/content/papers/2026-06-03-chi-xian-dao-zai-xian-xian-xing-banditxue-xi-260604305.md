---
title: Offline-to-Online Learning in Linear Bandits
title_zh: 离线到在线线性Bandit学习
authors:
- Kushagra Chandak
- Toshinori Kitamura
- Xiaoqi Tan
affiliations:
- University of Alberta
arxiv_id: '2606.04305'
url: https://arxiv.org/abs/2606.04305
pdf_url: https://arxiv.org/pdf/2606.04305
published: '2026-06-03'
collected: '2026-06-04'
category: RecSys
direction: 离线到在线学习·线性Bandit
tags:
- Linear Bandits
- Offline-to-Online
- Regret Minimization
- UCB
- LCB
- Warm-start
one_liner: 通过预算机制切换UCB与LCB，同时实现接近纯在线和纯离线策略的遗憾界
practical_value: '- 推荐系统上线时常有离线日志数据，LinOtO 的「安全基线 + 预算探索」框架可直接用于冷启动阶段：先用离线保守策略（LCB）累积足够预算，再逐步过渡到在线探索，避免早期高遗憾。

  - 预算机制可迁移到 Agent 决策：设定一个可接受的最低收益阈值，只有当累积超额收益（预算）为正时才执行探索动作，否则回退到保守动作，保证系统安全性。

  - 实验表明离线数据是否包含最优动作对最终效果影响显著，这提示在构造离线先验时应尽量覆盖潜在最优选项，例如通过历史 top 动作并加入适量随机探索数据。

  - 线性 Bandit 框架可用于简化版的上下文推荐：将用户-物品交互视为线性奖励，利用最小二乘估计和置信区间进行探索，配合离线协方差矩阵评估覆盖度，计算成本低，易于工程实现。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

## 动机
在推荐、广告等场景中，在线模型上线前通常拥有离线历史数据，但如何用好这些数据以平衡早期性能与长期探索，仍缺少结构化环境下的理论指导。单纯的离线悲观策略（LCB）在线性增长遗憾，纯在线乐观策略（UCB）在初期探索过度。本工作研究随机线性 Bandit 的离线到在线学习，目标是最小化相对于最优动作的遗憾（Rn）和相对于离线参考策略的遗憾（Roff）。

## 方法关键点
- **预算机制**：维护一个探索预算，由选择保守动作（LCB）积累的安全收益（αS）构成。当预算为正时才选择乐观动作（UCB），否则回退到 LCB 以积累预算。
- **置信区间构造**：离线数据给出固定置信半径 β_off，在线数据增量更新置信半径 β_t，联合构造参数置信集 C_t，用于生成 UCB 和 LCB 值。
- **安全基线**：提议用离线数据的 LCB 动作 L_off 作为安全基线，其期望与 μ_off 的差距被控制在 O(√(d/m))，保证基线保守但不至于太差。
- **切换规则**：每轮计算累计 LCB 值与基线之差作为预算，若预算 > 0 则选 U_t，否则选 L_t。算法称为 LinOtO。

## 关键结果数字
- 理论上，LinOtO 对 Rn 的遗憾界为 Õ(√(nρ_n d_eff) + d^2.5/(αS Δ))，其中 d_eff 是离线数据有效维度。在良好离线覆盖下（λ_min(V0) ∝ m），Rn 为 O(n√(ρ_n d d_eff/m))，与 LinUCB 同阶。对 Roff 的遗憾为 O((α+2)√(d/m) n)，与纯离线 LinLCB 同阶。
- 实验在合成数据上：维度 d=20，动作数 100，离线样本数 m=100，分别变化在线时长 n 和 m。LinOtO 在小 n 下接近 LinLCB，在大 n 下遗憾增长趋缓，最终接近 LinUCB。当离线数据不含最优动作时，LinLCB 线性遗憾，LinOtO 仍能通过探索转为次线性。当离线数据含最优动作时，LinOtO 快速收敛，与 LinUCB 几乎重合。
