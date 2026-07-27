---
title: 'Molt: A Scalable PyTorch-Native Training Framework for Agentic Reinforcement
  Learning'
title_zh: Molt：面向智能体强化学习的可扩展PyTorch原生训练框架
authors:
- Jian Hu
- Huiying Li
- Hao Zhang
- Binfeng Xu
- Yifan Zhang
- Shaokun Zhang
- Hemil Desai
- Michael Demoret
- Pavlo Molchanov
- Jan Kautz
affiliations:
- NVIDIA
arxiv_id: '2607.21653'
url: https://arxiv.org/abs/2607.21653
pdf_url: https://arxiv.org/pdf/2607.21653
published: '2026-07-21'
collected: '2026-07-27'
category: Agent
direction: Agentic RL 训练框架 · 异步流式策略优化
tags:
- AgenticRL
- PyTorch
- TrainingFramework
- MoE
- Asynchronous
- NVIDIA
one_liner: 一个轻量PyTorch原生框架，通过异步循环实现策略训练与展开，代码简洁且性能与Megatron堆栈相当
practical_value: '- **快速算法迭代**：框架设计为单一研究者可完全掌握的代码量，改动新RL算法只需修改Agent Python程序，适合电商/推荐团队频繁实验新的奖励函数、优势估计或过滤逻辑。

  - **异步流式架构**：vLLM rollout引擎通过请求路由器和Ray异步队列与训练actor解耦，确保训练数据完全由当前策略生成（无离线数据泄漏），可复用到对话推荐、搜索
  Agent 的策略训练，避免分布偏移。

  - **MoE与多模态支持**：框架原生支持混合物专家策略和多模态输入，对电商中的多模态商品推荐、广告文案生成等场景，可直接借助此范式训练大型策略模型。

  - **工程实现参考**：提供了完整的配方和容器，业务团队可快速搭建起类似的A2C类训练流水线，降低从论文到系统的转换成本。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：Agentic RL 研究中算法改动频繁，主流框架（如 Megatron 适配层）需要穿透多层次抽象，每次迭代成本高。Molt 旨在提供一个轻量级 PyTorch 原生框架，让研究者能以一个小型、易读的代码库快速实验新想法。

**方法关键点**：
- 用户以普通的 Python 程序定义 Agent，整个系统由三个组件和一个循环构成：单FSDP2策略 actor（基于NeMo AutoModel）、多个 vLLM rollout 引擎、Ray异步队列。
- 通过请求路由器将轨迹流式传输到队列，训练时严格保证只使用当前策略生成的 token，保证 token、策略版本、模型语义一致性。
- 支持多模态和 MoE 策略，全程异步运行，权重更新通过 NCCL 直接返回引擎，绕过路由器。

**关键结果**：在完全异步协议下，Molt 的统计性能与基于 Megatron 的最先进堆栈可比，同时代码库极简（约 2000 行核心逻辑），实现了“无性能损失的简洁”。
