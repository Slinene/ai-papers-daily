---
title: 'AsyncTool: Evaluating the Asynchronous Function Calling Capability under Multi-Task
  Scenarios'
title_zh: 异步工具调用基准：多任务场景下的异步函数调用能力评估
authors:
- Kou Shi
- Ziao Zhang
- Shiting Huang
- Avery Nie
- Zhen Fang
- Qiuchen Wang
- Lin Chen
- Huaian Chen
- Zehui Chen
- Feng Zhao
affiliations:
- University of Science and Technology of China
- University of Toronto
arxiv_id: '2605.27995'
url: https://arxiv.org/abs/2605.27995
pdf_url: https://arxiv.org/pdf/2605.27995
published: '2026-05-26'
collected: '2026-05-29'
category: Agent
direction: Agent异步工具调用评测与多任务协调
tags:
- Asynchronous Tool Calling
- LLM Agents
- Multi-Task
- Benchmark
- Temporal Reasoning
- Function Calling
one_liner: 提出首个交互式多任务环境下含延迟的异步工具调用基准，揭示延迟反馈显著降低LLM代理性能。
practical_value: '- 电商客服或订单处理等多API场景下，可参考异步任务交错策略提升吞吐，利用**Same‑task Streak**指标评估Agent的调度效率。

  - 延迟反馈下模型易因过早继续任务而违反依赖，工程实现中需引入**显式依赖图、任务状态表**防止非法调用。

  - 多任务下小模型常遗忘未完成子任务，可设计**外部任务队列或滑动记忆窗口**避免任务丢失。

  - 工具混淆错误频发，建议按任务类型隔离工具命名空间，并用**工具调用前检验上下文**的提示减少误用。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：现有工具调用评测多忽略工具响应延迟与多任务并发场景。现实应用中，多个任务常需并发执行，Agent能否在等待一个工具返回的同时推进其他任务（即异步工具调用）是效率关键，但缺乏对应基准。

**方法关键点**：
1. **数据集构建**：从BFCLv3和Nestful中提取358个单任务工具调用轨迹，经Gemini 2.5 Pro粗重建后，人工进行轨迹校验、依赖增强和歧义消除，最终生成712个多任务实例（双/三任务，同类/跨类组合）。
2. **交互环境**：模拟真实的工具响应延迟，Agent发出调用后不能立即获得结果，必须决定等待或切换任务；环境返回结果时可能乱序。
3. **三层评估**：步骤级（函数名、参数F1）、子任务级（轨迹完成、环境一致性）、任务级（全部子任务均满足才算成功）；引入**Same‑task Streak**等效率指标量化任务交错程度。

**关键实验**：
- 评估19个主流模型，GPT‑4.1以38.06的总分领先，开源最佳DeepSeek‑V3.1‑Terminus为28.93。
- 异步执行普遍造成性能下降：GPT‑4.1的任务完成率从同步的67.1%降至36.5%（见图3）。
- 效率分析表明，高性能模型并非切换最频繁，而是在正确时机切换并保持依赖正确；频繁但盲目的切换反而降低成功率（图4）。
- 主要失败模式：依赖违反（过早调用后续函数）、任务遗忘（忽略早期任务）、工具混淆（跨任务误用工具）和参数幻觉。

最值得记住的一句话：_异步工具调用的核心不在于频繁切换任务，而在于延迟反馈下精准地跟踪依赖、维护状态，并在正确的时机切换。_
