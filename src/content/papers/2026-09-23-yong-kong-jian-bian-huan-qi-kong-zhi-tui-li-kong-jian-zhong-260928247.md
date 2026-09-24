---
title: Controlling Collectives of AI Agents in Reasoning Space with Spatial Transformers
title_zh: 用空间变换器控制推理空间中的 AI 智能体群体
authors:
- Frederic Vatnsdal
- Roshan Gopal
- Romina Garcia Camargo
- Vijay Kumar
- Alejandro Ribeiro
arxiv_id: '2609.28247'
url: https://arxiv.org/abs/2609.28247
pdf_url: https://arxiv.org/pdf/2609.28247
published: '2026-09-23'
collected: '2026-09-24'
category: MultiAgent
direction: 多智能体群体控制 · 空间变换器反馈
tags:
- LLM
- Multi-Agent
- Spatial Transformer
- Decentralized Control
- Reasoning Space
one_liner: 提出 COMPASS 分布式架构，用空间变换器生成紧凑反馈 token 控制大型机器人群体，可扩展至 1024 个机器人
practical_value: '- 用紧凑的学习 token 代替原始状态注入 LLM 作为反馈，避免语言通道过载导致性能崩溃，可迁移到多 Agent 对话或推荐系统中的群体协作模块。

  - 输入命令的结构化多样性（如多种措辞组合）可消除 LLM 的固有偏差，提升策略鲁棒性，适用于电商搜索 query 改写或推荐理由生成时的 prompt 设计。

  - 分散式架构每个 Agent 只聚合局部多跳消息，无需全局通信即可实现大规模可扩展，适合构建大规模 Agent 网络进行分布式推理或商品筛选。

  - 空间变换器作为信息聚合器，将邻居状态压缩为低维反馈 token，可借鉴用于推荐系统中用户-物品图上的局部子图信息聚合，替代全量序列输入。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

动机：LLM 在机器人规划中具备零样本潜力，但团队规模增大时简单多机器人任务也会失败，需解决可扩展的多智能体控制问题。

方法：提出 COMPASS，一种分布式反馈控制架构。每个机器人本地由空间变换器聚合多跳邻居消息，生成一个紧凑的学习反馈 token，注入该机器人的 LLM。与集中式 LLM 策略和纯语言通信基线相比，COMPASS 通过推理空间反馈实现协同。

结果：实验发现，对输入命令进行结构化多样性处理可消除 LLM 偏差，且优势随规模保持。COMPASS 能生成凝聚的群集编队并准确执行指令意图，优于集中式前沿 LLM 策略和语言-only 通信。消融表明，手工设计反馈并将原始状态放入语言通道会破坏凝聚力。COMPASS 零样本泛化到未见模糊指令，可控制 16 倍训练规模的群体，最多 1024 个机器人。
