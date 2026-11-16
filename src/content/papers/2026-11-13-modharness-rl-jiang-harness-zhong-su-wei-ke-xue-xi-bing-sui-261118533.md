---
title: 'ModHarness-RL: Recasting Harnesses as Learnable and Evolving Programs for
  Agentic RL'
title_zh: ModHarness-RL：将 Harness 重塑为可学习并随训练演化的程序用于 Agentic RL
authors:
- Zelin He
- Siyu Zhu
- Jacob Helwig
- Yujian Liu
- Li An
- Rohit Jain
- Shiyu Chang
- Alborz Geramifard
affiliations:
- Pennsylvania State University
- LinkedIn
- University of California, Santa Barbara
arxiv_id: '2611.18533'
url: https://arxiv.org/abs/2611.18533
pdf_url: https://arxiv.org/pdf/2611.18533
published: '2026-11-13'
collected: '2026-11-16'
category: Agent
direction: Agentic RL 训练 harness 程序化与演化
tags:
- Agentic RL
- Harness
- Program Synthesis
- Compression
- Steering
- CodeSearch
one_liner: 把 Agentic RL 的固定手写 harness 改为从轨迹学习并随模型演化，显著提升多种智能体任务性能
practical_value: '- 电商/推荐场景中的 shopping agent、搜索 agent 常依赖固定上下文拼装与规则纠偏；可将其重构为可学习的 Compression/Steering
  程序，基于交互轨迹和奖励信号自动调整历史摘要与引导指令，替代人工调规则。

  - 引入 typed blocks 的结构化 State，让压缩和引导逻辑可程序化操作，便于离线日志搜索/验证候选策略，类似 RL 中的经验重放；工程上保持稳定接口，后续策略迭代只改程序不推倒重来。

  - 采用“候选程序从最近轨迹提议，在历史轨迹上重放验证”的更新策略，相当于离线评估 + 在线采纳，可迁移到业务 agent 的迭代优化：离线用日志筛选新策略，灰度上线观察，降低线上风险。

  - 注意该工作面向工具型任务（代码搜索等），奖励定义和轨迹结构与电商/Agent 不同，需自定义 State block 类型与程序搜索空间；但核心思想可复用。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**  
Agentic RL 训练依赖 harness——决定模型看到哪些自身交互、获得何种引导的外部脚手架。现有方法大多采用固定手写 harness，但高效 harness 应随领域、数据、模型变化，且模型训练过程中行为也会漂移。

**方法关键点**  
ModHarness-RL 将交互记录为结构化 State（一组 typed blocks），harness 由两个可学习程序组成：Compression 程序把累积历史组装进模型上下文；Steering 程序在行为偏离时给出引导。RL 训练期间，从最近轨迹提议候选程序，通过执行验证，并在过去轨迹上重放，使 harness 能跟踪模型行为变化，实现与模型共同演化。

**关键结果**  
在 CodeSearch 上深度研究，并在 ALFWorld 和 BIRD SQL 上验证，模型规模从 1.5B 到 8B。所提出的 Compression 和 Steering 机制在多数设定下相对固定 harness 基线提升 held-out 性能，尤其在上下文预算有限（limited）或充足（sufficient）的 SWE-Bench Lite/Verified/Pro 上均观察到改进。结果表明 agentic RL 的 harness 可以从任务数据中学习并随模型训练演化，而非必须保持静态手工设计。
