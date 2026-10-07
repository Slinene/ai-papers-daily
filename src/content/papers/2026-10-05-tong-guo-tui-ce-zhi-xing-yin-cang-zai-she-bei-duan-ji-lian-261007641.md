---
title: Hiding Tool Latency in On-Device Cascaded Voice Agent through Speculative Execution
title_zh: 通过推测执行隐藏在设备端级联语音代理中的工具延迟
authors:
- Kyudan Jung
- Hyunsin Park
- Yoonhyung Lee
- Jinhwan Park
- Jinhyeok Yang
- KiHyun Nam
- Jaegul Choo
- Jinkyu Lee
affiliations:
- Qualcomm AI Research
- KAIST AI
arxiv_id: '2610.07641'
url: https://arxiv.org/abs/2610.07641
pdf_url: https://arxiv.org/pdf/2610.07641
published: '2026-10-05'
collected: '2026-10-07'
category: Agent
direction: 语音 Agent 推测执行与工具缓存
tags:
- speculative execution
- tool calling
- voice assistant
- ASR
- latency optimization
- on-device LLM
one_liner: 在流式 ASR 部分假设上预测工具调用并推测执行缓存结果，将首音频中位延迟从 5.79s 降至 4.60s
practical_value: '- 对搜索/推荐 Agent，可在流式 query 或用户输入未完成时，先用轻量 Predictor 预测意图并预取工具结果（商品搜索、广告召回、知识库查询），LLM
  确认后直接注入缓存，隐藏工具延迟。

  - 规则化校验机制可借鉴：对用户自我纠正/改写场景，只注入与最终意图匹配的缓存结果，避免错误工具调用污染下游，且保留 LLM 直接调用工具能力作为兜底，保证最差延迟不超过串行基线。

  - 工程实现上，Predictor 独立于 LLM、基于部分 ASR 假设或部分 query 做预测，便于回滚和验证，比直接微调 LLM 做推测调用风险更低，适合在线
  A/B。

  - 结果不仅降低中位延迟，还降低标准差，说明响应更可预测；这对强调 P99 延迟的电商搜索/广告 Agent 尤其有价值。'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
工具增强语音助手通常串行执行 ASR、LLM 推理和外部工具调用，工具延迟在用户说完且 LLM 识别完工具需求后才发生，端到端响应慢且波动大。

### 方法关键点
提出在设备端级联语音代理中做推测执行：新增 Predictor 模块，在流式 ASR 产出部分假设时预测可能的工具调用，提前执行工具并缓存结果；缓存结果注入后续 LLM prompt，从而隐藏工具延迟。为缓解用户说话中的自我纠正导致预测错误，采用规则化校验机制，只注入有效的缓存结果。同时 LLM 仍保留直接发起工具调用的能力，使框架最差情况延迟不超过串行执行基线。

### 关键结果
在完全实现的 Android 语音助手上实测：首音频中位延迟从 5.79s 降至 4.60s，标准差从 3.49s 降至 2.81s，响应延迟更低且更可预测。
