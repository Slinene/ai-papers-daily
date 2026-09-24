---
title: 'WhatWorkedBench: Benchmarking Experimental Understanding in AI Agents'
title_zh: WhatWorkedBench：评测 AI Agent 实验理解能力
authors:
- Jingjie Ning
- Xueqi Li
- Yibo Kong
- Dongting Li
affiliations:
- Carnegie Mellon University
- Tsinghua University
arxiv_id: '2609.27490'
url: https://arxiv.org/abs/2609.27490
pdf_url: https://arxiv.org/pdf/2609.27490
published: '2026-09-22'
collected: '2026-09-24'
category: Eval
direction: AI Agent 实验理解与自适应实验设计评测
tags:
- AI Agents
- Benchmark
- Experiment Design
- Gaussian Process
- Code Equivalence
- Numerical Inference
one_liner: 构建 WhatWorkedBench 基准，衡量 Agent 在预算内实验后预测组件组合效果的准确性
practical_value: '- 在业务 Agent 做离线调参/工作流组合优化时，不要依赖完整网格搜索，可让 Agent 在预算内主动选择少量配置测量，再用
  GP 或 pair-effect ridge 推断全配置响应面，直接降低实验成本。

  - 静态分析代码等价性，把行为完全相同的配置合并成同一组，作为先验约束注入 GP；论文中该 trick 将小样本恢复从 0.248 提到 0.462，适合推荐/广告流程中大量冗余开关或等价组件组合。

  - 多组件组合实验（如召回/粗排/精排策略开关）优先建模主效应 + 成对交互，用 pair-effect ridge 在少量新测量下选优并控制误差，避免全阶交互带来的样本需求爆炸。

  - 内部评估 Agent 实验推断能力时，可借鉴该 benchmark 方式：用穷举离线结果构建数值控制记录，让 Agent 提交预测表，再对照完整参考效果算
  recovery，而非只看最终推荐指标。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：研究型 AI Agent 需要可靠预测实验改动对结果的影响，但缺少系统性 benchmark 衡量其“实验理解”能力。

**方法关键点**：WhatWorkedBench 让 Agent 阅读代码、在测量预算内选择配置，最终提交一张响应面表，预测所有组件配置组合的分数。穷举 CPU 执行全部合法配置生成参考效果，覆盖 36 个任务、30 个数据源、8 类 workflow，共 1248 条配置记录。核心评价包含 4206 条数值控制记录和 108 个 agent episodes。

**关键结果**：在 8 次新测量下，pair-effect ridge 在 15/22 个数据源上选到最优配置，并在 3 个数据源上把每个 effect error 控制在分数范围的 10% 以内；用同一组 agent 观测拟合 Gaussian process，effect recovery 从 0.632 提升到 0.698（原始 Flash cohort），另一个 cohort 从 0.621 提升到 0.720；在 6 个六选项 workflow 上编码代码等价性后，GP recovery 从 0.248 提升到 0.462。
