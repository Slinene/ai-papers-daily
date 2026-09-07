---
title: 'MaxKernel: Agentic Kernel Generation for TPUs'
title_zh: MaxKernel：面向 TPU 的智能体内核生成系统
authors:
- Shangkun Wang
- Nina Cai
- Charles Hoong
- Julian Walker
- Gerson Kroiz
- George Vanica
- Deepak Patil
- Andi Gavrilescu
- Hassan Sipra
- Sethu Sankaran
affiliations:
- Google
- Google DeepMind
arxiv_id: '2609.04523'
url: https://arxiv.org/abs/2609.04523
pdf_url: https://arxiv.org/pdf/2609.04523
published: '2026-09-02'
collected: '2026-09-07'
category: MultiAgent
direction: 多智能体 TPU 内核生成
tags:
- Agentic System
- Kernel Generation
- TPU
- LLM
- Compiler Feedback
- Multi-Agent
one_liner: MaxKernel 多智能体系统利用 LLM 与实时编译反馈，在 TPU 上自动生成并优化高性能内核，匹配专家手写调优基线
practical_value: '- **多智能体专业化分工可迁移到推荐 Agent 工作流**：将规划、实现、自调试、测试、profiling 拆成独立子智能体，共享同一套工具和上下文；在搜索推荐场景中，可类似拆分
  query 理解、召回策略、排序模型评估、A/B 实验分析等角色，降低单 Agent 复杂任务失败率。

  - **实时反馈闭环驱动自主优化**：MaxKernel 利用编译错误、性能指标、硬件 trace 作为环境反馈，让 Agent 自动迭代；这对应推荐系统中的在线指标、实验报告、bad
  case 分析等反馈回路，可用作 Agent 自动调参、自动特征工程或 prompt 优化。

  - **按任务复杂度切换三种协作模式**：HITL 适合高风险策略调整，Auto 适合批量优化，Graph-Based Search 用于全局探索设计空间；推荐/广告业务中，低风险自动优化、高风险人工审核的组合策略可直接借鉴。

  - **对纯推荐业务直接价值有限**：核心是底层 kernel 生成，业务可借鉴点主要在 Agent 架构与反馈闭环方法论，而非推荐算法本身。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：为 TPU 等加速器编写高性能自定义内核需要深硬件知识，LLM 结合实时编译反馈可构建智能体内核生成系统，降低人工门槛。

**方法关键点**：MaxKernel 是一个多智能体系统，实现三种 TPU 内核开发范式：(1) 人在回路（HITL）智能体，协作分步设计；(2) 自主（Auto）智能体，执行完全自动化的指标/trace 驱动优化循环；(3) 基于图的自主搜索，将 Auto 智能体扩展为全局探索设计空间。三种范式共享一组专用子智能体，分别负责规划、实现、自调试、测试和硬件性能分析。系统通过 LLM 与实时编译器反馈（编译错误、性能指标、硬件 trace）持续迭代优化内核实现。

**关键结果**：在 JaxBench 的 50 个多样化 TPU 内核任务及真实开源模型负载上评估，MaxKernel 一致生成高度优化实现，匹配专家手写调优基线，带来显著性能提升。代码已开源。
