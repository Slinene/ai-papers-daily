---
title: Automating the Design of Embodied Agent Architectures
title_zh: 具身智能体架构设计的自动搜索
authors:
- Jian Zhou
- Sihao Lin
- Jin Li
- Shuai Fu
- Gengze Zhou
- Qi Wu
affiliations:
- Australian Institute for Machine Learning, University of Adelaide
arxiv_id: '2606.30111'
url: https://arxiv.org/abs/2606.30111
pdf_url: https://arxiv.org/pdf/2606.30111
published: '2026-07-02'
collected: '2026-07-10'
category: Agent
direction: Agent 自动化架构搜索
tags:
- Architecture Search
- Embodied Agents
- AgentCanvas
- KDLoop
- LLM Agents
- Rollout Noise
one_liner: 首次系统评估在具身模拟环境中用架构搜索自动化设计Agent，揭示噪声与局部最优等局限
practical_value: '- **架构搜索范式可迁移**：将 Agent 设计视为图编辑任务，用“提议-批判-实验-蒸馏”循环自动优化，可用于电商推荐 Agent
  的模块组合（如召回/排序/记忆/工具调用），减少人工试错。

  - **类型化图运行时**：AgentCanvas 把 Agent 表示为可编辑节点-连线程序，支持带类型校验的执行和回滚，类似思路可用于搭建推荐系统 Agent
  的可视化编排与自动搜索。

  - **关注搜索噪声与局部最优**：具身环境中 rollout 噪声会掩盖真实信号，导致搜索陷入局部编辑盆地，提示我们在业务 Agent 架构搜索中需设计鲁棒的评估策略，如多次采样平滑、引入对抗验证。

  - **引入反思机制**：KDLoop 在优化停滞时触发反思，可借鉴到电商 Agent 的持续优化中，当线上指标不再提升时，自动回溯日志、重提假设，防止过早收敛。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：具身智能体通常由感知、记忆、规划、动作模块手工组合，架构设计空间巨大且依赖专家直觉。文本域 Agent 架构搜索（AAS）已出现，但未在具身模拟器环境中通过 rollout 系统评估。本文探索将 AAS 迁移至具身场景。

**方法关键点**：
- **AgentCanvas**：一个类型化图运行时，将具身执行器表示为可编辑的节点-连线程序，支持模拟器感知执行和 episode 级日志记录。
- **KDLoop**：一种编码智能体搜索流程，循环进行**提议**新架构、**批判**弱点、**实验**验证、**蒸馏**知识，并在优化停滞时触发**反思**，重新审视历史假设。
- 在视觉语言导航、具身问答、语言条件操作等四个具身执行器上，测试三种 AAS 变体（手工基线、随机搜索和 KDLoop），形成 3×4 矩阵评估。

**关键结果**：架构级搜索可产生**可部署且成功率方向性提升**的具身 Agent，如将成功率从 34% 提升至 41%（相对提升约 20%）；但发现一个表面高分候选因泄露环境信息被拒绝。实验同时暴露文本域 AAS 中不显著的约束：优化信号被 rollout 噪声掩盖、搜索易陷入局部编辑盆地，以及即便有详细日志，episode 级信用分配仅部分浮现。
