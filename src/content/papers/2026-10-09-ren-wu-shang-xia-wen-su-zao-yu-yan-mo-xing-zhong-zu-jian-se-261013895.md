---
title: Task Context Shapes Component Roles in Language Models
title_zh: 任务上下文塑造语言模型中组件角色
authors:
- Sovesh Mohapatra
- Dani S Bassett
affiliations:
- University of Pennsylvania
- Yale University
arxiv_id: '2610.13895'
url: https://arxiv.org/abs/2610.13895
pdf_url: https://arxiv.org/pdf/2610.13895
published: '2026-10-09'
collected: '2026-10-13'
category: LLM
direction: 语言模型组件角色的任务上下文依赖性
tags:
- mechanistic interpretability
- attention heads
- linear response maps
- activation editing
- task context
- LLM
one_liner: 任务上下文改变共享注意力头响应的事实及其对后续计算的影响，线性响应图可预测干预效果
practical_value: '- 在多任务电商/搜索 LLM 中，共享注意力头的角色随任务 Prompt 改变：可测量不同业务任务（query 改写 vs 推荐理由生成）下各头的影响分布，识别任务关键头，指导稀疏微调或任务特定低秩适配，避免全参更新。

  - 线性响应图可作为轻量任务行为代理：为不同业务 Prompt 构建组件间线性映射，用早期激活变化预测后续层响应，降低线上任务切换时的行为漂移监控成本。

  - 激活编辑切换行为而不改指令：在可控生成或 Agent 风格切换场景，只编辑早期内部激活即可让模型读取不同事实/知识，无需重写 Prompt，可用于无感干预或
  A/B 隔离测试。

  - 但整体属于机制可解释性研究，业务直接收益有限；其干预测量与影响分数方法可迁移到诊断推荐/搜索任务间泛化失败原因，但需自行设计干预目标。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：LLM 在不同任务中复用同一批参数和注意力头，但共享头在不同任务中的具体作用差异尚不清楚。借鉴脑网络的任务依赖交互，用网络视角理解模型计算。

方法：在五个开放权重模型（覆盖四个家族、1.5B–14B）上比较固定组件跨任务表现。使用相同的图事实（有向连接陈述）作为输入，测量干预对注意力头和后续层激活的影响，以及对答案的重要性。在 Gemma-2-9B 和 Qwen3-14B 中，编辑早期内部激活向量，在指令不变下切换模型读取的事实。对每个 Prompt 构建两套线性响应图（编辑前后），用早期头的变化预测后续头响应。

结果：任务变化重新分配五个模型中的影响。相同头对不同图事实响应，且对后续组件影响不同。对独立事实干预，对应条件的线性响应图相比两图平均，在 Gemma 上 MSE 降低 53.6%，在 Qwen 上降低 5.0%。说明任务上下文既改变共享组件响应的事实，也改变其输出对后续计算的影响，支持用网络视角解释模型如何用共享参数执行不同计算。
