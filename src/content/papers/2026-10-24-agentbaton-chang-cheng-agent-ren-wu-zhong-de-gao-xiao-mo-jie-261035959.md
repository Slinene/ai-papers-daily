---
title: 'AgentBaton: Efficient Model Collaboration in Agentic Tasks'
title_zh: AgentBaton：长程 Agent 任务中的高效模型交接检测
authors:
- Junlong Li
- Jindong Jiang
- Yonggan Fu
- Jiarui Yao
- Hanrong Ye
- Wonmin Byeon
- Peter Belcak
- Hao Zhang
- Pavlo Molchanov
affiliations:
- The Hong Kong University of Science and Technology
- University of Illinois Urbana-Champaign
- NVIDIA
arxiv_id: '2610.35959'
url: https://arxiv.org/abs/2610.35959
pdf_url: https://arxiv.org/pdf/2610.35959
published: '2026-10-24'
collected: '2026-11-09'
category: Agent
direction: Agent 模型交接与成本优化
tags:
- Model Handoff
- LLM Agent
- Cost Optimization
- Routing
- AgentBaton
- DeepSWE
one_liner: 提出轻量检测器 AgentBaton，在 capable→efficient 一次性交接点切换模型，11 组模型对平均 API 成本降 65.9%
  且精度基本保持
practical_value: '- 在长程 agent 流程（导购助手、售后 agent、数据分析 agent）中，优先采用“强模型打前段、弱模型收尾”的一次性交接，而不是
  query 级路由或逐轮路由；逐轮路由可能带来频繁纠错与协调开销。

  - 交接时机看“任务进展”而非轮数：当强模型已产出可用实现/方案、已获得执行反馈、剩余工作变为局部修复或验证时交接。可抽取这些信号训练轻量判断模型（论文用 2B，P50
  338ms），每轮后做低延迟 gating。

  - 上下文传递方式影响精度：强→弱多用 in-context transfer；弱→强或多模型不明时用 logfile transfer，让接手模型用 cat/grep/sed
  按需查历史，降低 prefill 和上下文污染。

  - 评估协作策略要用 accuracy–cost Pareto frontier，而非只看 accuracy；业务上可结合 API 价格和本地部署模型成本做动态预算分配。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
长程 agentic 任务中，可靠表现常依赖昂贵的 capable 模型，而高效模型成本低但独立完成率不足。传统 query 级路由只在初始请求上分配模型，无法适应 agent 执行中 workspace 和反馈动态变化。因此需要研究：能否在一个长程任务内部，让 capable 与 efficient 模型通过一次性 handoff 协作，大幅降本而不牺牲精度。

## 方法关键点
- 系统分析两个关键因素：交接方向与上下文传递方式。用 GPT-5.6 Sol、Kimi K3、GLM-5.3 作为 capable 模型，Qwen3.8-27B 作为 efficient 模型。
- 发现 efficient→capable 交接通常精度低于 capable-only，且未必省成本；capable→efficient 在合适的任务进展阶段能保持甚至提升精度，并大幅降低成本。
- 归纳交接就绪的三种重复模式：已有实质实现/原型；已获得执行、测试或检查反馈；剩余工作已收敛为局部诊断、修复、验证或最终产出。
- 基于这些模式训练 AgentBaton：从 Qwen3.5-2B 初始化，输入系统指令、任务描述、capable 模型的 action/tool observation 及历史决策，输出 HANDOFF_READY/NOT_READY。数据来自 SWE-rebench V2 的 2000 个任务、4000 条轨迹，由 Codex 回溯标注最早合适交接点。
- 推理时 capable 模型先跑，每轮后 AgentBaton 判定是否交接；收到 READY 则 efficient 模型接管 workspace 和上下文继续到结束。P50 延迟 338ms，P95 1.11s。

## 关键实验
在 DeepSWE v1.1 与 Terminal-Bench 2.1 上，11 组模型对评估。AgentBaton 平均降低 API 成本 65.9%，12/22 个设置精度损失小于 5% 或反超；最高比 capable-only 提升 8.8 pp。例如 Kimi K3→Qwen 在 DeepSWE 精度 72.6% vs 73.5%，成本降 72.9%；Claude Opus 5→GPT-5.6 Luna 精度从 67.3% 升至 76.1%，成本降 70.5%。对比 MTRouter 逐轮路由，AgentBaton 在精度持平或更优的情况下成本低 46.7–86.6%。Prompt 让模型自己交接不可靠：Kimi K3 从不交接，GLM 仅 6/113 任务交接。

## 最值得记住的一句话
一次性、时机合适的强→弱交接几乎就是最优协作策略；关键不是路由，而是判断任务进展是否已经足以让弱模型接手。
