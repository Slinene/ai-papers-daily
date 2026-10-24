---
title: 'Heartbeat Thinking: Speculative Reasoning and Tool Execution While Listening
  in Realtime Voice Agents'
title_zh: 心跳思考：实时语音代理边听边推测推理与工具执行
authors:
- Zhenyu Zhang
- Kewei Fu
- Yongqi Tong
- Chenzhi Zheng
- Wei Wu
- Jiang-Ming Yang
- Jianshe Li
affiliations:
- Ant International
arxiv_id: '2610.26233'
url: https://arxiv.org/abs/2610.26233
pdf_url: https://arxiv.org/pdf/2610.26233
published: '2026-10-18'
collected: '2026-10-24'
category: Agent
direction: 实时语音 Agent 推测工具执行
tags:
- Voice Agent
- Speculative Reasoning
- Tool Use
- Latency Optimization
- Realtime ASR
- Concurrent LLM
one_liner: 提出 Heartbeat Thinking 机制，在用户说话期间周期性启动 Thinker 并允许已派发工具继续完成，将监听时间转化为可复用的准备，显著提升工具覆盖率并降低最终响应延迟。
practical_value: '- 在实时语音电商客服/导购中，可在 ASR 部分结果上周期性（heartbeat）启动 LLM 推理，不打断已派发工具调用，利用用户说话时间提前完成订单查询、库存检查等工具调用，降低首响延迟。

  - 借鉴“共享推理记录 + 工具结果”的设计，将不同心跳周期内已完成的子任务结果保存下来，后续心跳只需补齐缺失参数或发起依赖调用，避免重复计算，提升并发利用率。

  - 将推测性工具覆盖率和检索复用率作为在线指标，而不仅是最终任务质量；在语音 Agent 工程中监控“说话期间已完成工具调用比例”，用于评估 anticipation
  能力。

  - 如果业务中有长尾复杂请求（如退换货、多条件商品咨询），可采用类似多 Thinker 并发机制，允许部分推理分支自然终止，而不是强杀，减少截断导致的重算。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：工具型语音 Agent 通常在用户说完后才开始推理和工具执行，导致等待延迟；而现有 speculative 方法受 chunk 边界或更新即打断的限制，工具调用常被截断，无法充分利用说话期间已到达的信息。

**方法关键点**：Heartbeat Thinking 在用户说话期间周期性触发新的 Thinker 调用，读取最新部分转录和共享记录（已完成推理与工具结果），同时允许之前派发的工具继续执行而不打断。这样缺失参数可由后续结果补齐，依赖调用可被发起，跨语音更新持续推进准备工作。

**关键结果**：在 SpeechFCEval、FDBench v3、AudioCRAG 三个基准上，相比 SHANKS 风格窗口基线，Heartbeat 在聚合推测工具覆盖率或检索复用率上表现更好。FDBench v3 上工具覆盖率提升 16 个百分点，平均最终响应延迟降低 36.4%。
