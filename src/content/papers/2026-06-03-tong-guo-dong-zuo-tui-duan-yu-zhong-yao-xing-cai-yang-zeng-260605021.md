---
title: Enhancing the MADDPG Algorithm for Multi-Agent Learning via Action Inference
  and Importance Sampling
title_zh: 通过动作推断与重要性采样增强MADDPG多智能体学习
authors:
- Marc Walden
- Jason Liu
- Shaashwath Sivakumar
- Ryan Liu
- Hamza Khan
arxiv_id: '2606.05021'
url: https://arxiv.org/abs/2606.05021
pdf_url: https://arxiv.org/pdf/2606.05021
published: '2026-06-03'
collected: '2026-06-04'
category: MultiAgent
direction: 多智能体深度强化学习算法优化
tags:
- MADDPG
- Action Inference
- Importance Sampling
- Multi-Agent RL
- Non-Stationarity
one_liner: 引入动作推断机制与几何分布重要性采样，提升MADDPG在非平稳多智能体环境中的学习稳定性和探索效率
practical_value: '- 在多智能体协同推荐（如召回-粗排-精排多级联动）中，可借鉴动作推断思想，让各级代理预测上下游的决策意图，减少因独立更新导致的策略震荡。

  - 面对用户兴趣漂移或策略频繁迭代造成的环境非平稳性，可采用几何分布重要性采样对经验回放加权，优先使用近期交互数据，加快对新分布的适应。

  - 若将推荐模块抽象为离散动作的协作代理，本文的离散动作MADDPG变体提供了一个轻量实现起点，工程上易集成到现有Actor-Critic框架。

  - 实验表明动作推断对提升智能体间协作效果显著，可用于优化多代理竞价、多目标排序等存在隐性博弈的场景，稳定联合策略。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：多智能体强化学习面临环境非平稳性——其他智能体策略持续变化，导致独立学习不稳定，标准MADDPG对此应对不足。  
**方法**：提出两项改进：1）**动作推断（Action Inference）**：每个智能体额外学习一个推断网络，预测其他智能体的待执行动作，并将其作为自身策略网络的输入，从而显式建模智能体间依赖，提升协作稳定性；2）**几何分布重要性采样**：在经验回放中，用几何分布对时间步索引加权，使得近期经验被采样到的概率更高，帮助策略快速适应最新的环境动态。两项改进在离散动作版Predator-Prey任务上验证，使用PettingZoo基准。  
**关键结果**：动作推断显著增强了学习的平稳性和智能体间的协作成功率；几何分布重要性采样相较于均匀采样，大幅提高了探索效率，使智能体在更短时间内习得有效合作策略。
