---
title: 'TRAJDEBUG: Tracing Error Lifecycle to Identify Critical Failures in Long-Horizon
  Agent Trajectories'
title_zh: TrajDebug：通过错误生命周期追踪定位长程Agent关键失败
authors:
- Yunjia Qi
- Zehua Yin
- Xintong Shi
- Hao Peng
- Songyuanyi Lu
- Yixian Liu
- Richeng Xuan
- Yuhong Liu
- Zhichao Hu
- Xiaozhi Wang
affiliations:
- Tsinghua University (BNRist)
- Shenzhen International Graduate School, Tsinghua University
- Tencent Hunyuan
arxiv_id: '2608.06346'
url: https://arxiv.org/abs/2608.06346
pdf_url: https://arxiv.org/pdf/2608.06346
published: '2026-08-06'
collected: '2026-08-07'
category: Agent
direction: Agent错误调试与关键失败定位
tags:
- Agent Debugging
- Error Lifecycle
- Critical Error Detection
- Multi-granularity Compression
- Trajectory Analysis
- LLM Agents
one_liner: 提出TrajDebug，以多粒度历史压缩和证据驱动错误识别追踪错误生命周期，定位关键失败步骤
practical_value: '- 在电商客服或推荐Agent开发中，借鉴多粒度历史压缩，对长对话轨迹进行层次化摘要（如将交互划分为任务、子步骤），降低人工调试成本。

  - 错误生命周期追踪（判断错误是被修复、无影响还是导致最终失败）帮助锁定真正关键的错误步骤，避免在多轮Agent调试中浪费时间在无关错误上。

  - 证据驱动的错误识别方法可迁移至推荐系统策略校验，例如检测推荐结果是否违反库存、价格等业务规则，并定位第一个违规步骤。

  - 构造内部失败轨迹数据集并持续评估，将关键错误诊断信息作为Agent自我反思或自动修复的输入，提升系统成功率。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM Agent在长程任务中易发生级联错误，手动从长轨迹中定位导致最终失败的关键步骤十分困难。主要原因：（1）证据分散在远隔的指令、观察和历史中；（2）轨迹中常包含多个局部错误，仅部分对最终失败负责。

**方法关键点**：TrajDebug框架通过三个机制实现关键错误检测。①多粒度历史压缩：将长轨迹压缩为层次化表示（如按任务、子步骤），减少无关信息干扰。②证据驱动错误识别：基于任务目标和约束，检验每一步是否违背预期，从而发现局部错误。③错误生命周期追踪：追踪每个错误的解决状态及是否产生终端影响，区分被修复/无害/关键错误，定位最早导致失败的关键步骤。同时构建了TrajErrBench，包含486条人工标注的失败轨迹，来自τ²-Bench和SWE-Bench Pro，覆盖工具使用与代码场景。

**关键结果**：跨多个Agent基准测试，TrajDebug在关键错误检测上综合性能最优；应用研究证实其诊断能生成可操作反馈，重试后下游Agent成功率提升。
