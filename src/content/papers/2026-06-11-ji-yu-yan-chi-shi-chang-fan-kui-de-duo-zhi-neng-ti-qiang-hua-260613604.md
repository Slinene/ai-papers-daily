---
title: Multi-Agent Reinforcement Learning from Delayed Marketplace Feedback for Objective-Weight
  Adaptation in Three-Sided Dispatch
title_zh: 基于延迟市场反馈的多智能体强化学习目标权重自适应三方调度
authors:
- Haochen Wu
- Yi Hou
- Shiguang Xie
affiliations:
- DoorDash Inc.
arxiv_id: '2606.13604'
url: https://arxiv.org/abs/2606.13604
pdf_url: https://arxiv.org/pdf/2606.13604
published: '2026-06-11'
collected: '2026-06-13'
category: Other
direction: 多智能体调度优化 · 离线强化学习
tags:
- Multi-Agent RL
- Offline RL
- Dispatch
- Objective-Weight Adaptation
- Delayed Feedback
- Marketplace
one_liner: 离线RL从真实市场延迟反馈中学习调整调度优化器的目标权重，实现效率提升而不损害质量
practical_value: '- 通过低维目标权重接口控制现有优化器，避免直接替换，既保留约束与安全，又实现自适应调节；电商推荐中可类比为调节召回/排序目标权重的外部Agent。

  - 利用离线RL从延迟且耦合的市场反馈中学习，采用 Double DQN 与 Conservative Q-Learning 惩罚未充分支持的动作，减少外推误差，适合业务中无法实时交互的场景。

  - 多智能体完全去中心化执行、集中训练，并利用区域级奖励捕捉网络效应，对电商中多地区/多仓库协同决策具有借鉴意义。

  - 上线前通过离线奖励重加权诊断策略行为的方向灵敏度，确保策略按预期权衡速度与效率，可作为推荐Agent上线前的安全检验方法。'
score: 10
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
外卖调度需在配送质量与批量效率间权衡，传统静态权重无法适应局部时变条件。本文利用DoorDash真实市场延迟反馈，让RL智能体在优化器上游自适应调整目标权重，在不改动生产约束下实现动态优化。

**方法**
- 将问题建模为去中心化多智能体MDP，每个门店视为一个Agent，选择ASAP权重乘子（5个离散值0.8~1.2），控制底层组合优化器的速度-批量化倾向。
- 状态包含待配送订单数、中位快递等待时间及局部供给压力特征（按门店有效快递员数调整区域供给信号）。
- 奖励由延迟的ASAP（顾客侧时效）与XCAT（快递员额外耗时）加权求和并按区域聚合，反映网络效应。
- 训练采用集中离线数据 + Double DQN + Conservative Q-Learning (CQL) 正则化，以抑制未见动作的价值高估，提高离线部署稳定性。
- 数据采集分两轮受控上线：先随机探索，再混合50%利用 + 50%探索的策略；共约346万条转移样本。

**实验结果**
- 生产环境全局切换实验覆盖约4000个地理区域，两小时随机切换。
- 全时段结果：快递活跃时间（CAT）减少1.26秒（p=0.019），快递等待时间（CWT）减少0.86秒（p=0.004），批量化率提升0.495个百分点（p<0.001）；顾客侧ASAP和20分钟迟到率无显著变化。
- 晚餐时段效果更显著，迟到率改善0.037个百分点（p=0.040）。
- 策略行为检查显示，在高积压与低供给压力下倾向于选择更低乘子（鼓励批量化），证实策略依赖状态自适应。

**核心结论**
通过对现有优化器施加低维目标权重接口，并利用离线RL从延迟市场反馈中学习，可以在生产规模安全地提升效率，同时保持顾客体验和操作安全。
