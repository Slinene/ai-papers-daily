---
title: 'ReflectWorld-MM: An Entity-Oriented Multimodal Memory System for Open-Ended
  Video Streams'
title_zh: 'ReflectWorld-MM: 面向实体的开放视频流多模态记忆系统'
authors:
- Xiaokang Ma
- Yifan Sun
- Zhihong Jin
- Jie Gu
- Yudong Luo
- Shenyi Shao
- Chu Tang
- Jingmin Chen
- Li Pu
affiliations:
- Rightly Robotics
- Hangzhou Institute for Advanced Study, UCAS
- Zhejiang University
arxiv_id: '2607.09759'
url: https://arxiv.org/abs/2607.09759
pdf_url: https://arxiv.org/pdf/2607.09759
published: '2026-07-13'
collected: '2026-07-21'
category: Agent
direction: 面向实体的视频流长期记忆 · Agent 记忆增强
tags:
- Entity-Oriented Memory
- Multimodal
- Long-Term Memory
- Video Stream
- Agent Memory
- Hierarchical Memory
one_liner: 以实体为中心的分层多模态记忆系统，在六个长视频与终身记忆基准中全面超越现有方案
practical_value: '- **用户长期兴趣建模**：借鉴实体为中心的语义记忆，将用户行为序列中的商品、品牌、品类等作为持久实体，动态更新其表示，避免遗忘历史兴趣，适用于电商推荐中的长周期兴趣刻画。

  - **Agent 对话记忆架构**：分层记忆设计（情景记忆、语义记忆、程序记忆）可直接迁移到对话推荐或客服 Agent，使 Agent 能跨会话记住用户提及的实体及其变化，提升连续交互的连贯性。

  - **流式数据处理**：感知前端与短时记忆的边界设计，适合工程化实现流式用户行为输入下的增量更新，可参考其在特征存储和实体解析上的工程权衡，构建实时推荐特征管道。

  - **多模态扩展思路**：若将视频流替换为商品图文流或直播流，实体导向记忆有助于捕捉跨模态的同一商品，为多模态召回或排序提供一致的表征。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有视频助手将记忆存放在模型上下文或扁平特征库中，以帧而非持久实体为中心组织记忆，导致无法有效跟踪长时间跨度中人物与物体的重现，难以胜任开放流任务。

**方法**：提出 ReflectWorld-MM，包含三部分：
- **感知前端**：将音视频流转化为实体解析的观察，受限于短时记忆窗口；
- **分层长期记忆**：借鉴人类记忆理论，组合多尺度情景记忆、以实体为中心的语义记忆和程序记忆，语义记忆随新观察不断演化，实体成为记忆核心；
- **工程实现**：系统可接入任意视频流，并与现成助手模型集成。

**结果**：在 EgoSchema、NExT-QA、ActivityNet-QA、QAEgo4D、MemBench、MileBench 六个长视频和终身记忆基准上均取得最高准确率，超越 MemGPT、ChatDev 等记忆 Agent 以及 GPT-4V 等前沿模型。
