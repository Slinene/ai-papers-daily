---
title: 'Miles v0.1: Production-Level Post-Training'
title_zh: Miles v0.1：生产级后训练系统
authors:
- RadixArk
- Tom Chen
- Mao Cheng
- Shi Dong
- Kangrui Du
- Yanbin Jiang
- Jiajun Li
- Yiming Li
- Tao Lin
- Yusheng Su
affiliations:
- RadixArk
arxiv_id: '2609.08368'
url: https://arxiv.org/abs/2609.08368
pdf_url: https://arxiv.org/pdf/2609.08368
published: '2026-09-07'
collected: '2026-09-09'
category: Training
direction: 生产级后训练系统与Agentic RL
tags:
- Post-Training
- Reinforcement Learning
- SGLang
- Megatron-LM
- MoE
- LoRA
one_liner: 一个全栈生产级后训练系统，支持RL、LoRA RL、蒸馏等，在64 GPU上对744B MoE做异步Agentic RL步时263秒
practical_value: '- 借鉴其解耦的 rollout 与 trainer 架构：使用 SGLang 作为独立推理引擎，通过 router 管理多个
  engine，训练器支持 Megatron-LM / FSDP 双后端，可适配电商推荐场景中大规模 LLM 的 RL 训练或在线学习。

  - LoRA RL 支持降低了 RL 微调的资源门槛，适合在电商/广告领域对已有 LLM 做轻量级策略优化，如对话式推荐、搜索 query 改写等业务。

  - true-on-policy rollout-training alignment 机制确保训练数据来自最新策略，避免策略滞后，对推荐系统中的实时反馈学习（如
  bandit / RL 推荐）有参考价值。

  - 异步 Agentic RL 案例（多轮工具调用、外部环境交互）可直接迁移到构建电商导购 / 客服 Agent 的训练 pipeline，缓解 rollout
  与训练间的气泡问题。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：前沿规模 LLM 后训练面临多轮 agentic rollout、工具使用、万亿参数 MoE 等挑战，系统需同时优化延迟敏感的推理与吞吐敏感的训练，易产生 GPU 气泡和数值不一致，需要生产级系统支撑。

**方法关键点**：Miles v0.1 基于 slime 设计，强调组件验证、干净、可定制。系统包含：- rollout 引擎基于 SGLang，支持 router 管理多引擎；
- 训练器可选 NVIDIA Megatron-LM 或 PyTorch FSDP 两种后端；
- 三种权重同步传输方式适配不同部署拓扑；
- 支持全参数 RL、LoRA RL、on-policy 蒸馏、SFT、真 on-policy rollout-训练对齐，并扩展到扩散模型。

**关键结果**：在 GLM-5.2 744B-A40B MoE 模型上执行全异步 Agentic RL 用于终端编码任务，运行在 64 块 NVIDIA GB300 GPU 上，前 30 步中位数步时为 263 秒。
