---
title: 'Second Thought: Reasoning in Parallel as LLM Agents Act and Observe'
title_zh: 第二思考：LLM Agent 行动与观察期间并行推理
authors:
- Zhensu Sun
- Chengran Yang
- Yunbo Lyu
- Jieke Shi
- David Lo
affiliations:
- Singapore Management University
arxiv_id: '2608.13667'
url: https://arxiv.org/abs/2608.13667
pdf_url: https://arxiv.org/pdf/2608.13667
published: '2026-08-13'
collected: '2026-08-18'
category: Agent
direction: Agent 推理时延优化 · 异步并行思考
tags:
- LLM Agents
- Parallel Reasoning
- ReAct
- Asynchronous Inference
- Idle Window
- Test-time Scaling
one_liner: 在 ReAct 的 Action-Observation 空闲窗口并行分叉四路原子思考，融合回下一轮，降低主线程解码与轮次而不损精度
practical_value: '- 把 ReAct 中 Action–Observation 的等待窗口当成免费并行推理资源：Agent 调用商品搜索、用户模拟器或工具返回期间，分叉
  Check/Recall/Rehearse/Alternative 四路旁路思考，下一轮提示词直接拼接收获的原子思考，可减少无效轮次；工程上可复用主线程前缀 KV
  cache，关闭旁路 thinking mode 以快速产出。

  - 四类推理维度对应电商对话 Agent 常见失败：假设未验证（库存/优惠条件）、长对话约束遗忘（预算/偏好）、工具结果偏离时重新规划、过早锁定单一策略；可按业务裁剪只保留
  1-2 路，例如 Alternative + Rehearse，单分支 API 成本仅增加 16%-35%。

  - 原子思考输出契约值得直接抄：用 `<thought>` 包裹、每条 ≤25 词、无前后引用，中断只丢弃当前单元，适合推送文案生成、搜索 query 改写等任何需要异步生成且可随时截断的场景。

  - 延迟收益主要来自主线程 token 减少而非隐藏工具等待，说明把旁路思考预算转到等待窗口比单纯 force 主模型更长推理更划算；若允许主线程等待分支完成，Pass@1
  还能再涨 4.7 点，但会牺牲关键路径，适合离线批处理或准实时场景。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM agent 在 ReAct 循环中只在 Thought 阶段产出推理，Action 和 Observation 阶段形成连续的“推理空闲窗口”；但 test-time scaling 的额外思考通常都放在主线程关键路径上，直接拉高延迟。这个窗口是未被利用的并行容量：既不影响当前 turn 决策，又受 Observation 到达时刻的硬性截止约束。

### 方法关键点
- 在 Thought 结束瞬间 fork 四个辅助分支：**Check**（审计刚形成计划的脆弱假设）、**Recall**（召回长历史中已淡化的约束）、**Rehearse**（预演可能的工具结果与条件性下一步）、**Alternative**（生成备选策略与触发条件）。
- 所有分支共享主线程前缀 KV cache，用同一个模型继续自己的轨迹，关闭 native thinking 以加快产出。
- 输出格式为**原子思考**：每条用 `<thought>...</thought>` 包裹，单点 ≤25 词，无前后引用；中断只丢当前未闭合单元，已完成的原子思考保持可用。
- Observation 返回时立即截断所有分支，保留最后一个闭合标签，每维度最多 5 条，拼接在 tool message 后，供下一轮 Thought 读取。

### 关键结果
在 SWE-Bench Pro、Terminal-Bench 2.1、τ³-bench 三个 benchmark × DeepSeek-V4-Flash、Qwen3.6-Plus、MiniMax-M3 三个 reasoning LLM 上：全部 9 对的平均 turn count 下降；6/9 对主线程 output tokens 下降最多 43%（平均约 20%）；Pass@1 在 7/9 对无显著变化，Terminal-Bench 2.1 上两对显著提升 +12.4 和 +10.2。与 budget forcing 的 s1 对照中，适用场景下 Pass@1 严格更高且主线程解码少 1.3–3.2 倍。配对 wall-clock replay 显示 median 延迟降低 10.9%。四分支 API 成本增加 66%–181%（主要来自输入 cache 读取），只保留单分支可降至 +16%–35%。

**最值得记住**：把推理从主线程关键路径搬到等待环境返回的空闲窗口，可以同时拿到更多推理和更低延迟。
