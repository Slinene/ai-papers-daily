---
title: Task-Focused Memorization for Multimodal Agents
title_zh: 面向多模态Agent的任务聚焦记忆
authors:
- Tao Zou
- Yichen He
- Tian Qiu
- Yuan Lin
- Hang Li
affiliations:
- ByteDance Seed
- Fudan University
arxiv_id: '2605.31075'
url: https://arxiv.org/abs/2605.31075
pdf_url: https://arxiv.org/pdf/2605.31075
published: '2026-05-28'
collected: '2026-06-01'
category: Agent
direction: 多模态Agent长期记忆 · Task-focused Memorization
tags:
- Multimodal Agent
- Memory Policy
- Reinforcement Learning
- Streaming VQA
- Adapter Tuning
one_liner: 提出基于强化学习的记忆策略学习框架，使多模态Agent动态选择任务相关记忆内容，提升流式VQA准确率
practical_value: '- **Agent记忆选择策略可复用**：在电商客服或购物助手中，可将用户交互日志视为连续流，借鉴TaskMem的二阶段训练：先预训练记忆编码器保证信息压缩质量，上线后根据任务奖励（如回复满意度）在线微调Adapter，让记忆聚焦于用户偏好、未解决诉求等关键信号。

  - **RL奖励设计思路**：用近期线上任务自动构建奖励模型，避免人工标注，适合电商Agent动态变化的场景。可将此思路用于对话状态追踪或推荐解释生成中，引导记忆模块捕捉高价值上下文。

  - **Adapter隔离基座模型**：仅在基座MLLM上训练轻量Adapter来调整记忆策略，保持原模型能力不变，利于快速迭代和A/B测试。在电商推荐系统中，类似做法可用于微调序列模型以选择性保留关键用户行为，而不破坏预训练表示。

  - **评估范式可迁移**：将静态数据集改造为流式、仅依赖记忆的问答基准，能更真实反映记忆模块有效性，可用于评估用户长期兴趣建模中序列压缩/记忆模块的效果。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：多模态Agent（如具身智能）需要从连续的多模态观测中选择性记忆与未来任务相关的内容，但信息爆炸导致记忆策略难以设计，现有方法多关注存储结构而忽略“记什么”。

**方法**：提出TaskMem，将记忆生成建模为可学习的策略。采用两阶段训练：阶段一用基础保真度约束预训练记忆模块，学会如何压缩和记录；阶段二部署后，收集近期线上任务构建奖励模型（自动评估记忆对任务的价值），通过强化学习微调基座MLLM上的Adapter，使记忆策略向任务相关内容倾斜，记住“该记的”。

**结果**：在流式化改造的VideoMME、EgoLife、EgoTempo基准上，基于Qwen3-VL-30B-A3B，TaskMem使VQA准确率分别提升6.3%、7.0%、5.3%，且任务相关记忆质量显著提高。
