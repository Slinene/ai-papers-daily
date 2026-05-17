---
title: Learning to Communicate Locally for Large-Scale Multi-Agent Pathfinding
title_zh: 大规模多智能体寻路的局部通信学习
authors:
- Valeriy Vyaltsev
- Alsu Sagirova
- Anton Andreychuk
- Oleg Bulichev
- Yuri Kuratov
- Konstantin Yakovlev
- Aleksandr Panov
- Alexey Skrynnik
arxiv_id: '2605.07637'
url: https://arxiv.org/abs/2605.07637
pdf_url: https://arxiv.org/pdf/2605.07637
published: '2026-05-11'
collected: '2026-05-17'
category: MultiAgent
direction: 多智能体协作 · 局部通信学习
tags:
- multi-agent pathfinding
- decentralized planning
- communication
- imitation learning
- reinforcement learning
one_liner: 提出可学习局部通信模块，通过多轮特征共享增强协作，在不损失可扩展性的前提下大幅提升多智能体寻路性能
practical_value: '- **局部通信机制设计**：仅在邻居智能体间共享特征，大幅降低通信开销，可直接应用于电商仓储机器人调度或配送路径规划，取代全广播式通信。

  - **可扩展的通信架构**：通信模块与决策策略解耦，且不随智能体数量增加而牺牲效率，适合大规模商品分拣或城市级配送场景。

  - **预训练 + 通信模块微调**：先预训练基础策略，再插入可学习通信模块联合微调，该范式可复用到多 Agent 推荐系统中，通过 Agent 间局部交换特征提升协同推荐效果。

  - **多轮通信增强协商**：允许 Agent 在决策前进行多轮信息交换，这一机制可直接借鉴到生成式推荐中的多 Agent 交互，实现商品组合的迭代协商生成。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：多智能体路径规划（MAPF）是物流、救援等应用的基础问题，传统求解器虽最优但不可扩展，学习型方法多采用去中心化部分可观测马尔可夫决策过程（Dec-POMDP），但相邻智能体间缺乏有效协作，导致决策局部次优。  
**方法**：提出 LC-MAPF，在单智能体视角的 Dec-POMDP 框架中加入一个可学习的通信模块。该模块允许每个智能体在每一步决策前，与通信范围内的邻居进行多轮特征交换，并通过预训练使模型泛化能力强。通信模块轻量与任务策略解耦，不影响整体可扩展性。  
**结果**：在多种未见测试场景中，LC-MAPF 在成功率、路径长度等指标上均显著优于现有基于模仿学习（IL）和强化学习（RL）的方法，同时保持了与无通信方法相同的可扩展性，验证了局部通信在大规模多智能体系统中的有效性和实用性。
