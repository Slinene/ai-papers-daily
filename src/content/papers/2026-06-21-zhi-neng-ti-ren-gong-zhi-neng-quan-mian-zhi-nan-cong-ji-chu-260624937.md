---
title: 'The Hitchhiker''s Guide to Agentic AI: From Foundations to Systems'
title_zh: 智能体人工智能全面指南：从基础到系统实现
authors:
- Haggai Roitman
arxiv_id: '2606.24937'
url: https://arxiv.org/abs/2606.24937
pdf_url: https://arxiv.org/pdf/2606.24937
published: '2026-06-21'
collected: '2026-06-25'
category: Agent
direction: Agent 构建 · RL 训练 · RAG 与记忆系统
tags:
- Agentic AI
- LLM
- Reinforcement Learning
- RAG
- Memory
- Agent Training
one_liner: 覆盖 LLM 基础、RL 对齐、Agent 训练、RAG、记忆与推理的工程实践手册
practical_value: '- **Agent 训练完整配方**：第12章提供轨迹缓冲区、多目标奖励设计、课程学习等细节，可直接用于对话式推荐 Agent
  的强化学习训练

  - **GRPO 与 Agent 优化**：详解 GRPO 及其变体（Dr. GRPO、SAPO 等），可迁移到电商 Agent 多轮交互策略的在线优化

  - **Agentic RAG 模式**：查询变换、自我反思、多源路由等模式可直接用于电商搜索中的多步检索与问题解答 Agent

  - **记忆系统设计**：用户建模、会话连续性、层次化记忆管理器等方案，可落地实现个性化推荐 Agent 的长期记忆管理'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM 正从对话工具演进为自主 Agent，但工程落地缺乏系统性指南。本书填补空白，从 LLM 底层架构到 Agent 生产系统，提供端到端的实现手册。

**方法关键点**：
- **LLM 基础**：涵盖 Transformer 结构、LoRA、MoE、量化、推测解码、解码策略（核采样、受限解码）及高效推理（PagedAttention、vLLM）
- **RL 对齐方法**：系统梳理 PPO、DPO、GRPO 及其变体（如 Dr. GRPO、SAPO），给出奖励模型训练技巧、RLHF 与 RLVR 配方
- **Agent 训练**：提出轨迹缓冲区范式（自我修正、离策略探索、非参数 ICL）；详解 STaR、Reflexion、AgentQ、Voyager 等主流算法，并以生产力助手为例给出完整训练流程（动作空间、状态表示、多目标奖励、课程学习、安全护栏）
- **推理与评估**：分析 DeepSeek-R1、o1 等推理模型的 RL 训练策略；提供 LLM 评测指标（ELO、Win Rate、Pass@k）与 Agent 评测基准（SWE-bench、WebArena）
- **Agent 系统工程**：涵盖 RAG（稀疏/稠密检索、Agentic RAG）、记忆系统（工作/情景/语义记忆，层次化记忆管理器）、编排框架（上下文管理、工具集成、MCP 协议、错误恢复）

**关键结论**：
- PPO 训练中，4 模型（actor、critic、reference、reward）的内存瓶颈可通过解耦推理与训练服务器缓解
- GRPO 通过组内相对奖励去除 critic 模型，降低工程复杂度，成为 Agent 训练的当前首选基线
- 成功 Agent 训练依赖高质量 SFT 基础、精细的稀疏奖励设计、轨迹缓冲区管理和稳定的 RL 超参数（如 Adam beta2=0.95）

**最值得记住的一句话**：这是一份从 LLM 预训练到 Agent 生产部署的全栈工程实战手册，为构建自主推荐/搜索 Agent 提供可直接复用的架构与训练方案。
