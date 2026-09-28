---
title: 'Completed Pairs Hide Capped Failures: A ReVerPi Case Study of Selective Context
  Projection'
title_zh: 已完成配对掩盖被截断失败：选择性上下文投影的 ReVerPi 案例研究
authors:
- Guangzhe Zhang
affiliations:
- Independent AI Researcher
arxiv_id: '2609.31381'
url: https://arxiv.org/abs/2609.31381
pdf_url: https://arxiv.org/pdf/2609.31381
published: '2026-09-25'
collected: '2026-09-28'
category: Agent
direction: Agent 评估方法 · 上下文投影
tags:
- Context Projection
- Agent Evaluation
- Stopping Rules
- Capped Failures
- Resource Aggregation
one_liner: 揭示评估中因仅保留完成配对而掩盖资源受限失败，并给出双臂独立执行的评估方法论
practical_value: '- **A/B 评估必须双臂独立执行**：在 Agent 或推荐策略对比中，不要因一个 arm 先失败/超时而抑制对照 arm；应保留所有干预边界，否则会系统性丢失高成本失败案例，歪曲结论。

  - **报告完成率与资源消耗，而非只看成功样本**：离线评测生成式推荐、query 改写或 RAG 时，同时记录 completion rate、交互轮数、logical
  tokens；仅比较完成样本会掩盖资源耗尽型失败。

  - **Context projection 是双刃剑**：将旧 tool observation 压缩为可寻址摘要可减少 25% 聚合 logical tokens，但可能增加
  29% 中位 tokens 与更多检索请求（35→55）；在构建 agent 记忆或对话压缩模块时，需以完整交互序列评估端到端收益。

  - **分离 fitting 与 evaluation 以避免 selector 偏差**：如果部分数据用于选择/调参，再在同一批数据上统计，会发现虚假 tie；业务中训练/验证/测试须严格隔离，否则资源与成功率结论不可靠。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：Context projection 用紧凑可寻址摘要替代旧工具观察，旨在减少重复输入，但可能增加证据检索轮次与总消耗。若只统计已完成的配对，会隐藏那些因投影导致资源耗尽而失败的情况。

**方法**：在 ReVerPi（Pi 编码 agent 扩展）上进行 86 次 source-reading 实验，共 641 次模型请求，匹配 full/projected 两种 continuation。评估包含完成配对、边界运行（未完成）以及被抑制的 companion。通过恢复边界运行，推导 projected 与 full 的成功率差异界限。

**关键结果**：15 个已完成配对中成功率相同（12/15 per arm）；但 12 个边界运行被停止且 runner 抑制 companion。恢复全部 27 个边界运行后，projected-minus-full 成功率界限为 -9 到 +1。一例被省略的 selector 选定 projected continuation 成功检索归档文本却耗尽 12 次请求，而 full 只需 3 次。在共同正确的 11 对中，projection 减少 25% 聚合 logical tokens，但中位 tokens 增加 29%，suffix 请求从 35 增至 55。分离 fitting 后，selector 的明显平局消失：在 13 个可比较运行中额外产生 1 次失败和 8.6% 更多 logical tokens。结论限于记录 campaign，不构成总体非劣效或优势；评估应保留每个干预边界，独立执行双臂，并同时报告完成率、交互轮数与 token 支出。
