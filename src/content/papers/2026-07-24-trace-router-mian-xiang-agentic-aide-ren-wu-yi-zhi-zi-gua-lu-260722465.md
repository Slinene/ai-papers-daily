---
title: 'TRACE-ROUTER: Task-Consistent and Adaptive Online Routing for Agentic AI'
title_zh: 'TRACE-ROUTER: 面向Agentic AI的任务一致自适应在线路由'
authors:
- Ritik Raj
- Souvik Kundu
- Sarbartha Banerjee
- Dheemanth Joshi
- Ishita Vohra
- Tushar Krishna
affiliations:
- Georgia Institute of Technology
- Intel
- Texas A&M University
arxiv_id: '2607.22465'
url: https://arxiv.org/abs/2607.22465
pdf_url: https://arxiv.org/pdf/2607.22465
published: '2026-07-24'
collected: '2026-07-27'
category: Agent
direction: Agent任务级自适应路由
tags:
- routing
- contextual bandit
- delayed feedback
- agentic AI
- LLM deployment
- cost-quality trade-off
one_liner: 用任务级上下文Bandit路由替代请求级路由，通过延迟奖励统一优化Agent工作流的准确率与延迟。
practical_value: '- **Agent任务内固定模型池**：对电商客服、搜索推荐Agent等多步工具调用场景，可在任务入口用上下文Bandit选择一个LLM，整个任务会话固定使用该模型，避免每步独立路由带来的反馈归因偏差。

  - **利用任务级延迟奖励在线学习**：直接使用最终的任务成功/失败和总延迟作为奖励信号，无需预估单步复杂度，工程实现简单，适合线上持续优化路由策略。

  - **Bandit策略可迁移**：若业务中已有Agent工作流和模型池，可将现有逐请求路由器替换为任务级Bandit，只需在任务结束时收集终端奖励，即可用LinUCB等标准方法更新策略，降低试错成本。

  - **平衡成本与效果**：在预算受限的推荐Agent中（如商品咨询、比价），可自动将复杂任务路由到大模型，简单任务用小模型，在不牺牲最终准确率的前提下显著降低延迟和推理成本。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有LLM路由以单次调用为单位独立决策，但Agent应用由多步组成，最终质量由任务级结果衡量，导致请求级路由难以将奖励正确归因到每个决策，限制策略学习。

**方法**：提出TRACE-Router，一种任务级路由框架。任务到达时，使用上下文Bandit一次性选择一个后端模型，该任务内的所有后续LLM调用均固定使用该模型；任务完成后，根据最终准确率和总延迟计算联合奖励，更新Bandit策略。通过这种方式，路由决策与监督信号对齐，无需显式估计任务复杂度，并能自适应工作负载变化。

**结果**：在三个Agent基准（τ2-Bench、Terminal-Bench等）上，TRACE-Router均获得最优准确率-延迟帕累托前沿。在τ2-Bench上，相比延迟匹配的模型插值基线，准确率高出7-8个点；在Terminal-Bench上，比最强单一模型准确率高7.1个点，同时延迟降低36%。
