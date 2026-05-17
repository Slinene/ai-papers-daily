---
title: Policy Optimization in Hybrid Discrete-Continuous Action Spaces via Mixed Gradients
title_zh: 混合离散-连续动作空间的策略优化：基于混合梯度
authors:
- Matias Alvo
- Daniel Russo
- Yash Kanoria
arxiv_id: '2605.14297'
url: https://arxiv.org/abs/2605.14297
pdf_url: https://arxiv.org/pdf/2605.14297
published: '2026-05-14'
collected: '2026-05-17'
category: Other
direction: 强化学习与混合动作空间优化
tags:
- Reinforcement Learning
- Hybrid Action Spaces
- Policy Gradient
- Mixed Gradient Estimator
- Pathwise Gradients
- Score-Function
one_liner: 提出HPO算法，结合路径梯度与分数函数梯度实现混合动作空间的无偏策略优化
practical_value: '- **可借鉴的混合梯度架构**：推荐系统的选品（离散）与出价（连续）等混合动作场景，可将 HP O的混合梯度估计作为 baseline，用路径梯度直接优化连续部分，分数函数梯度处理离散部分，避免单独
  score function 的高方差。

  - **近似分散更新的工程实现**：当离散策略接近最优时，交叉项可忽略，连续部分与离散部分可分散独立更新，降低方差并简化工程实现，适合电商多臂老虎机或分层决策体系。

  - **利用可微分仿真**：若业务中决策环境有可微模型（如用户响应曲线、供给端模型），可用 HP O的路径导数提升连续动作梯度质量，替代纯无梯度或 score
  function 方法。

  - **库存管理、供应调度场景直接复用**：电商库存补货、仓储调度等本质是混合动作空间（选择补货点、连续补货量），HP O可优于标准 PP O，提供更高效优化方案。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：混合离散-连续动作空间在机器人、控制、运营中常见，如离散选择模式、连续参数优化。传统无模型策略梯度依赖分数函数估计量，高维下存在严重信用分配问题；可微分仿真虽能通过路径导数缓解，但含离散动作或非平滑动态时梯度有偏或无信息。

**方法**：提出 Hybrid Policy Optimization (HPO)，在平滑允许处通过仿真反向传播路径导数，与分数函数梯度结合形成无偏混合梯度估计。关键创新在于混合梯度中的交叉项——刻画连续动作如何影响未来离散决策——当逼近离散最佳响应时可忽略，从而支持连续与离散策略近似分散更新，并降低最优解附近的方差。

**结果**：在库存控制和切换线性二次调节器任务上，HPO 大幅优于 PPO，且性能差距随连续动作维度增加而扩大。消融实验验证了混合梯度的无偏性与低方差特性。代码已开源。
