---
title: 'PerfArena: Ranking LLMs by Code Performance'
title_zh: PerfArena：按代码性能排名大语言模型
authors:
- Rui Rua
- Hailemariam Mersha
- Joao Paulo Fernandes
- Karim Ali
arxiv_id: '2611.18030'
url: https://arxiv.org/abs/2611.18030
pdf_url: https://arxiv.org/pdf/2611.18030
published: '2026-11-13'
collected: '2026-11-16'
category: Other
direction: 代码生成 LLM 性能评估基准
tags:
- LLM
- Code Generation
- Benchmark
- Performance Evaluation
- Energy Consumption
- Open Source
one_liner: 提出可复现的代码性能竞技场，跨语言评测 LLM 生成代码的正确性、延迟、峰值内存与能耗
practical_value: '- 在内部 LLM 应用评测中，除了业务指标（正确性/转化率）还应引入资源成本维度：latency、峰值内存、能耗/成本，构建类似
  leaderboard 按任务和语言选择模型，避免只看准确率或价格。

  - 可插拔评估流水线设计值得借鉴：将评判器（oracle）、性能探针（profiler）、生成工作流解耦，方便替换不同评测后端和度量工具，支持多任务、多语言快速扩展。

  - 统一测量协议（同一任务在每种语言/模型上用相同执行环境、多次执行取稳定值）是保证可比性的关键，做推理成本 benchmark 时要在同一台机器、同一运行时下进行。

  - 对线上 Agent 生成候选 query/文案的场景，可在离线评估中加入延迟和资源消耗排名，提前淘汰慢且贵的模型；gpt-6-astra 的结果说明性能最强的模型在成本上不一定劣化，应把性能指标纳入模型选型。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：行业大量生产代码由 LLM 生成，但正确性不能代表代码适合长期重复使用，时间、内存和能耗成本同样关键。现有代码生成基准大多只评估正确性，性能类基准覆盖语言少、几乎不测能耗。

**方法关键点**：PERFARENA 是一个开源、可复现的竞技场，在 Unix 主机上执行各 LLM 生成的代码，统一报告正确性、延迟、峰值内存和能耗。正确性/性能判定器、profiler 和代码生成工作流均可插拔，便于扩展新评测后端。测量协议在所有语言上保持一致，保证可比性。

**关键结果**：覆盖 CLBGComp 10 个计算密集基准和 LeetCodeComp 99 个 LeetCode 问题，目前持有 13 个 LLM 跨 7 种语言的 9,455 个正确且已测量的解。gpt-6-astra 是唯一在延迟、能耗、峰值内存上没有被其他 LLM 显著超越的模型，解决 99.7% 的 LeetCodeComp 和 100% 的 CLBGComp。其他 LLM 的延迟在 LeetCodeComp 上是 gpt-6-astra 的 1.1–1.6 倍，在 CLBGComp 上是 1.2–3.6 倍；每个正确解最贵的 LLM 成本是 gpt-6-astra 的 2.6–9.3 倍，但代码并不更快。所有 leaderboard 和测量解公开，帮助开发者按语言和指标选择 LLM。
