---
title: 'Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon
  Real-Time Game Agent'
title_zh: Gamer：面向长时程实时游戏智能体的通用视觉-语言-动作基础模型
authors:
- Run Luo
- Kuan Zhang
- Qi Deng
- Yukun Chen
- Zhihao Yang
- Yufei Zhang
- Renrong Hu
- Yi Zhang
- Guiyu Ma
- Tianyu Fan
affiliations:
- miHoYo Honkai AI R&D Team
arxiv_id: '2611.18397'
url: https://arxiv.org/abs/2611.18397
pdf_url: https://arxiv.org/pdf/2611.18397
published: '2026-11-12'
collected: '2026-11-16'
category: Agent
direction: 游戏 Agent · VLA 基础模型
tags:
- VLA
- Game Agent
- Reinforcement Learning
- Sparse-Thinking
- Cloud-Edge Inference
- Long-Horizon
one_liner: 用大规模键盘鼠标轨迹预训练、稀疏思考微调、多轮RL和云边推理，实现长时程实时游戏Agent
practical_value: '- **稀疏思考指令微调**：在需要实时响应的 Agent 业务中（如对话式推荐、智能客服），可筛选关键推理步骤，减少中间 token
  生成，在保持决策质量的同时大幅降低首响延迟和推理成本。

  - **云边协同推理架构**：支持并发模拟环境、无界上下文执行和低在线延迟，可迁移到高并发电商搜索/推荐 Agent 服务，用边缘节点处理短交互、云端处理长会话记忆，实现规模化实时决策。

  - **行为轨迹预训练**：利用大规模键盘鼠标轨迹学习环境动态，类似推荐系统用用户点击/滑动/购买序列预训练交互模型；电商可从埋点行为轨迹中提炼用户意图与操作模式，训练能预测下一步交互的
  Agent。

  - **多轮强化学习稳定训练技巧**：针对有限上下文窗口、累积 rollout 误差和稀疏奖励的解决方法，可借鉴到基于多轮会话的推荐策略优化，例如用重放缓冲、奖励塑形和阶段式训练缓解长序列信用分配问题。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**
复杂交互环境（尤其 3D 开放世界游戏）要求智能体具备长时程规划、实时响应和跨环境泛化能力，但现有 VLA 模型受限于训练数据、推理延迟和稀疏奖励下的策略优化。

**方法关键点**
- 收集数万小时键盘鼠标交互轨迹，覆盖模拟游戏与具身环境，对 VLA 模型继续预训练，学习跨数字与物理世界的环境动态；
- 引入稀疏思考指令微调，在保留复杂决策所需推理的同时大幅减少冗余计算；
- 采用多轮强化学习方法，针对有限上下文窗口、累积 rollout 误差和稀疏奖励进行稳定训练；
- 设计云边协同推理引擎，并发服务多个模拟环境，支持无界上下文执行并保持低延迟。

**关键结果**
在多个高难度 3D 开放世界游戏中，Gamer 展现出接近熟练玩家的操作效率和泛化能力；在多种 2D 游戏基准上也取得有竞争力的结果，验证了大规模行为轨迹和稳定学习算法带来的显著增益。
