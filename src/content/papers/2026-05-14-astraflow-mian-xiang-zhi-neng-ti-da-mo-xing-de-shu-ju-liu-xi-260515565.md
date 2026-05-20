---
title: 'AstraFlow: Dataflow-Oriented Reinforcement Learning for Agentic LLMs'
title_zh: AstraFlow：面向智能体大模型的数据流导向强化学习系统
authors:
- Haizhong Zheng
- Yizhuo Di
- Jiahui Wang
- Shuowei Jin
- Xueshen Liu
- Yongji Wu
- Z. Morley Mao
- Ion Stoica
- Jiawei Zhao
- Beidi Chen
affiliations:
- Carnegie Mellon University
- University of Michigan
- UC Berkeley
- Meta
arxiv_id: '2605.15565'
url: https://arxiv.org/abs/2605.15565
pdf_url: https://arxiv.org/pdf/2605.15565
published: '2026-05-14'
collected: '2026-05-20'
category: Training
direction: Agent RL 训练系统 · 数据流架构
tags:
- Reinforcement Learning
- Agent
- Dataflow
- Multi-Policy
- LLM
- System
one_liner: 以数据流架构解耦训练、数据供给与 rollout，原生支持多策略协作训练并提速 2.7 倍
practical_value: '- **训练与 rollout 解耦的架构**：将 rollout 服务化为独立、可替换的组件（Rollout-as-a-Service），可借鉴到推荐模型的在线
  RL 训练中，实现策略模型与交互环境分离，便于弹性扩展和资源优化。

  - **数据流驱动的异步数据管线**：通过数据流层实现完全异步的样本供给，避免训练器等待 rollout，可应用于大规模分布式训练场景，提升 GPU 利用率。

  - **多策略协作训练机制**：支持多个策略模型（如不同推荐策略或不同 Agent 策略）在同一框架下协同训练，适合多目标推荐或多 Agent 协作优化，可直接复用其稀疏权重更新、选择性
  rollout 等设计。

  - **异构、跨区域资源的弹性利用**：支持不同 GPU 类型、跨地域的 rollout 资源池，对需要动态调度算力（如大促弹性扩容）的业务有参考价值，能降低成本。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：强化学习提升 Agent 型 LLM 的推理和工具使用能力，但系统实现昂贵且复杂。现有 RL 系统以训练器为中心，每增加新功能（如多策略训练、弹性资源）就需要专门工程改造，缺乏统一的组件抽象，阻碍了规模化应用。

**方法**：提出 AstraFlow，一个数据流导向的 RL 系统。它将 rollout 服务、数据流管理和模型训练解耦为自治组件：rollout 服务封装环境交互与推理，训练器专注模型更新，中间由数据流层异步供给样本。这种设计原生支持多策略协作训练、弹性 rollout、异构及跨区域资源调度，并且数据算法可组合，无需修改系统代码。

**结果**：在数学、代码、搜索和 AgentBench 等任务上，AstraFlow 无需系统级改动即可支持多策略训练，训练速度比现有系统快 2.7 倍，且精度相当或更好，证明了架构的通用性和高效性。
