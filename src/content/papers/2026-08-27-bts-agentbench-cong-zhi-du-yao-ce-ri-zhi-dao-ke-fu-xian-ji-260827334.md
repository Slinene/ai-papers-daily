---
title: 'BTS-AgentBench: A Deterministic, Replayable Pipeline from Read-Only Telemetry
  Logs to Agent Benchmarks'
title_zh: BTS-AgentBench：从只读遥测日志到可复现 Agent 基准的确定性管线
authors:
- Jeong-Yoon Kim
arxiv_id: '2608.27334'
url: https://arxiv.org/abs/2608.27334
pdf_url: https://arxiv.org/pdf/2608.27334
published: '2026-08-27'
collected: '2026-08-30'
category: Eval
direction: Agent 基准构建与确定性重放
tags:
- Agent Benchmark
- Telemetry
- Replay
- Deterministic Pipeline
- Evaluation
- Tool Store
one_liner: 从工业遥测日志构建可重放、零泄漏多轮 Agent 基准，精确复现 356/87/89 划分
practical_value: '- 用业务日志构造 agent 评估集时，先将原始日志规范化为 read-only tool store，再生成任务，保证工具视图与实际一致，避免评测数据污染。

  - 采用 deterministic pipeline + replay report + construction-exclusion controller，确保
  train/dev/test 可重建且无答案泄漏；这在电商/客服 agent 评测中可复用到多轮任务生成。

  - 对多轮 agent 任务显式添加 clarification、goal revision、timestamp policy、quality-gated reporting、evidence
  attribution 等类型和边界，能在业务上定义更可操作的 agent 评估维度。

  - 对 benchmark 引入 coded contract preflight 和 double build matching，提升构建质量；工程上可以用类似契约测试保障
  pipeline 一致性。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：工业现场积累大量只读遥测日志，但缺少从这些日志编译为可执行多轮 agent 任务的基准方法；BTS 原始数据可诱导约 219 万 day-window 候选和 599 万 pairwise 候选，手工构造不现实。

**方法关键点**：BTS-AgentBench 将 BTS 元数据和原始历史规范化为只读工具存储；编译静态任务并用工具派生金答案和证据；再升为带类型的、有边界的 operator-facing episodes。发布 532 行数据，增加 clarification、goal revision、timestamp policy、quality-gated reporting 和 evidence attribution，同时保留源计算和划分。构建质量通过 coded contract preflight 和 construction-exclusion controller 保证。

**关键结果数字**：contract preflight 零发现；construction-exclusion controller 完成 0/532 行，即无泄漏。两次独立 raw-to-episode 构建匹配全部 11 个逻辑工具存储导出，并精确复现发布版 356/87/89 train/dev/test。将共享构建路径迁移到 XAI4HEAT 得到 204 episodes；在其 41 行 held-out test 上，控制器完成 0 行，GPT-5.5 执行完成全部 41 行。
