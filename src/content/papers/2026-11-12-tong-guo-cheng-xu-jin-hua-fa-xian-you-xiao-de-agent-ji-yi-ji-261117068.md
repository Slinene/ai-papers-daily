---
title: Discovering Effective Agent Memory Designs through Program Evolution
title_zh: 通过程序进化发现有效的 Agent 记忆设计
authors:
- Xinheng Ding
- Seyyed Saeid Cheshmi
- Ziyang Zhang
- Tairan Chen
- Wenya Xie
- Yu Hou
- Rui Zhang
- Zirui Liu
affiliations:
- University of Minnesota
- Stevens Institute of Technology
arxiv_id: '2611.17068'
url: https://arxiv.org/abs/2611.17068
pdf_url: https://arxiv.org/pdf/2611.17068
published: '2026-11-12'
collected: '2026-11-13'
category: Agent
direction: Agent 记忆系统程序进化
tags:
- Agent Memory
- Program Evolution
- LLM Agents
- Retrieval-Augmented
- Multi-Objective Optimization
- Memory Design
one_liner: MAPE 框架从极简种子进化 Agent 记忆程序，发现保留原始对话和按查询意图组合证据等可迁移设计
practical_value: '- 在对话式推荐/客服 Agent 中，除了抽取结构化 memory，保留原始对话日志作为可检索证据，能显著减少细节丢失；可用混合检索（BM25+稠密向量）提升召回完整性。

  - 将 retrieved evidence 的“组合”阶段从检索中独立出来，按查询意图路由到不同处理逻辑（如计数、时间推理、聚合），结合 LLM 提取与 Python
  确定性计算，可有效提升回答准确率，且该模块可移植到现有 RAG/memory 系统。

  - 用程序进化自动搜索 memory pipeline 时，同时优化 accuracy 和 serving cost 会引导搜索偏向 query-time 选择性处理，减少
  build 阶段 LLM 调用，在保持准确率的同时大幅降低成本；适合预算敏感的业务场景。

  - 将 memory 生命周期拆为 build/retrieve/compose/answer 四个标准化接口，便于对不同 memory 方案做统一评测和组件级移植；工程上可作为
  agent memory 模块的参考架构。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
Agent 记忆系统是长期对话助手的核心组件，但现有设计多依赖人工经验，难以系统比较不同设计选择的有效性。程序进化（program evolution）能从极小种子自动发现算法设计，但以往工作多受限于固定组件或只优化准确率。本工作希望借助全程序进化，探索从零开始能涌现出哪些有效的记忆设计，以及不同优化目标（准确率 vs. 准确率+成本）如何影响设计空间和计算分配。

**方法关键点**
- 提出 MAPE 框架，将记忆系统标准化为 build / retrieve / compose / answer 四个生命周期阶段，统一接口和评测协议；进化从极简种子（如无记忆程序）开始，通过 LLM 提议、执行、诊断的迭代循环修改整个 pipeline 代码。
- 支持两种搜索目标：MAPE-A 仅优化准确率；MAPE-P 将准确率和生命周期 serving cost 作为双目标，维护 Pareto 前沿。搜索过程跟踪 token 用量和成本，候选程序在 held-out evaluation set 上最终筛选。
- 进化出的代表性设计展现两个 recurring patterns：保留原始对话作为可检索证据（而非只存抽取后的摘要），以及 Query-Routed Scaffolding（RQS）——按查询类型路由到特定组合 scaffold，结合 LLM 提取与确定性计算（如日期算术、计数）。

**关键实验与结果**
在 LoCoMo 和 LongMemEval 两个长期对话记忆 benchmark 上，使用 GPT-4.1 mini 和 Qwen3-30B-A3B 作为 serving backbone，对比 Full Context、RAG 和五个手工系统（Mem0, A-Mem, LightMem, SimpleMem, Zep）。MAPE-ALCM 在 LoCoMo 上达到 87.94% 准确率，超过所有 baseline；MAPE-PLCM 以约 28% 的成本保持 85.18% 的竞争力。在 LongMemEval 上，MAPE-ALME 比最强 baseline RAG 提升 11 个百分点（77.00% vs 66.00%）。跨 backbone 和跨 benchmark 迁移实验显示发现的设计具有泛化性。消融表明，移除原始对话证据使 LongMemEval 准确率下降 6.50%，移除 RQS 下降 6.25%；将 RQS 移植到五个手工系统，每个系统准确率绝对提升 2.75–9.25%。此外，加入成本目标后，进化出的程序显著减少 build 阶段 LLM 调用，将计算转移到 query-time 选择性处理，在保持准确率的同时大幅降低 serving cost。

**最值得记住的一句话**
保留原始对话作为可检索证据 + 按查询意图路由的组合模块，是程序进化反复发现的有效记忆设计，且可跨模型、跨基准、跨手工系统迁移。
