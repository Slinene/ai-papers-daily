---
title: World In-Context Learning for Agentic Robot Manipulation
title_zh: 面向智能体机器人操作的世界上下文学习
authors:
- Heng Fang
- Zehui Guo
- Yuehan Zhang
- Mingyang Du
- Dingkang Liang
- Xiang Bai
affiliations:
- Huazhong University of Science and Technology
- ArcheOne AI
arxiv_id: '2611.12885'
url: https://arxiv.org/abs/2611.12885
pdf_url: https://arxiv.org/pdf/2611.12885
published: '2026-11-08'
collected: '2026-11-12'
category: Agent
direction: Agent 世界上下文学习与任务记忆
tags:
- In-Context Learning
- Robot Manipulation
- Simulation Rehearsal
- Task Memory
- Foundation Model
- Agentic System
one_liner: 提出世界上下文学习范式：冻结模型在模拟器中排练并将反馈写入上下文，实现单演示机器人操控
practical_value: '- 用模拟器/环境反馈替代权重更新：在电商推荐 Agent 中，可先构建用户点击或商品检索模拟器，让 Agent 在里面试错，把成功经验写成
  task memory 拼进 prompt，冻结 LLM 权重，大幅降低上线成本。

  - 将 Task Memory 作为可插拔模块跨场景复用：类似论文把一次演示固化成语义步骤与物体角色，推荐系统可把某类活动/场景的策略固化成 prompt 模板或工具调用序列，在新商品/新
  query 上直接复用。

  - 加入反思循环：每次执行后记录失败原因与修正动作，写回上下文，不更新模型参数；这在推荐 Agent 多轮交互中可以持续优化推荐解释、query 改写等决策。

  - 数据隔离与部署一致性：确保推理时所有输入在真实环境可用，避免模拟与现实差距；推荐系统做离线仿真评估时，应限制 Agent 可用的特征和工具与线上一致，防止策略迁移失效。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：传统机器人动作策略将技能写入网络权重，导致学习结果与训练分布强耦合。In-context learning（ICL）冻结权重、从上下文适应任务，但一直不如训练策略，因为其他场景录制的演示缺少当前世界反馈。作者发现 ICL 学到的是语义信息——任务步骤和物体角色，而非视觉外观，因此一个世界的经验可以迁移到另一个世界。

**方法**：提出 World In-Context Learning（WICL），用冻结模型从单条演示出发，在模拟器等世界中排练任务，将环境反馈写入上下文而不是权重。构建 RoboScript 模块化基础设施：从演示通过仿真排练学习每个任务，将学到的知识冻结为 Task Memory，部署到新场景，并通过数据隔离确保每个部署输入在真实机器人上可用。方法支持反思改进、跨视觉分布泛化、随基础模型扩展，以及跨 embodiment 记忆适应。

**结果**：在 RoboTwin 2.0 全部 50 个任务上，每任务仅一条演示、无梯度更新，干净与随机设置平均成功率达 83.4%，超过最强训练动作策略 20 个百分点以上；并成功迁移到物理双臂机器人。
