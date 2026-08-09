---
title: 'WorldCycle: Self-Verifiable Reinforcement Learning for Long-Horizon Video
  World Models'
title_zh: 世界循环：面向长时视频世界模型的自验证强化学习
authors:
- Bohai Gu
- Yueyang Yuan
- Taiyi Wu
- Dazhao Du
- Jian Liu
- Xiaoyi Pang
- Jie Zhang
- Xiaocheng Lu
- Haobin Zhong
- Xiaotong Zhao
affiliations:
- The Hong Kong University of Science and Technology
- Wuhan University
- AI Technology Center, Tencent Video, Tencent
arxiv_id: '2608.04964'
url: https://arxiv.org/abs/2608.04964
pdf_url: https://arxiv.org/pdf/2608.04964
published: '2026-08-04'
collected: '2026-08-09'
category: Other
direction: 视频世界模型 · 自验证强化学习
tags:
- Video World Model
- Reinforcement Learning
- Cycle Consistency
- Long-Horizon Dynamics
- Self-Supervision
- CycleBench
one_liner: 利用可逆动作循环构造无标注长期监督，通过空间闭合与时间一致性奖励降低状态漂移并提升组合动作泛化
practical_value: '- 循环自验证思路可迁移至序列推荐模型：设计用户行为序列的“逆操作”（如浏览后返回），要求模型预测回到历史状态，以无标签方式监督长期一致性，缓解漂移问题。

  - 复合动作泛化测试（CycleBench）可类比推荐中的组合条件推荐评估，用于检测模型对多步关联操作的鲁棒性。

  - RL 中基于对称性的奖励设计可启发对话推荐策略训练中的一致性约束，减少来回对话的崩溃。

  - 主要面向视频生成，迁移至推荐需额外适配，但长序列建模的自监督循环思想可直接参考。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机：** 交互式视频世界模型在长时推演中累积误差，传统 RL 缺乏长期真实状态验证信号，无法有效训练。

**方法关键点：** 提出自验证 RL 框架 WorldCycle，核心洞察是：可逆动作循环（序列与其逆序列组合）必须返回初始状态，从而提供无标注的长期正确性监督。具体做法：从普通动作序列中构造闭合循环及重复执行，优化两种奖励——空间闭合奖励（强制前向与反向段预测状态对称）和时间一致性奖励（对齐同一循环多次重复产生的状态）。最终迫使模型学会将动作视为一致的状态变换算子，而非记忆时序模式，并自然泛化到未见过的复合动作循环。

**关键结果：** 在专用基准 CycleBench 上，WorldCycle 将状态返回漂移降低最多 44%，复合动作准确度相对基线模型提升近 4 倍，为物理一致的世界模型奠定基础。
