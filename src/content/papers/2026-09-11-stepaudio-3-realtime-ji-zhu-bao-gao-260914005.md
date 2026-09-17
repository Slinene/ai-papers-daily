---
title: StepAudio 3 Realtime Technical Report
title_zh: StepAudio 3 Realtime 技术报告
authors:
- Bin Lin
- Bo Zhao
- Boyang Zhang
- Boyong Wu
- Chao Yan
- Chen Geng
- Chen Wu
- Cheng Yi
- Chengli Feng
- Chenglin Zhu
affiliations:
- StepFun Audio Team
arxiv_id: '2609.14005'
url: https://arxiv.org/abs/2609.14005
pdf_url: https://arxiv.org/pdf/2609.14005
published: '2026-09-11'
collected: '2026-09-17'
category: Multimodal
direction: 实时音频语言模型与语音 Agent
tags:
- Real-time Speech
- Audio LLM
- Think-While-Speaking
- Full-Duplex
- Voice Agent
one_liner: 实时语音基础模型实现边说边想的低延迟深度推理与全双工语音交互
practical_value: '- **边想边说机制低延迟推理**：Think-While-Speaking 将私有推理与音频输出并行，可迁移到对话式推荐/客服系统，在生成用户可见回复的同时后台进行复杂排序、召回或收益计算，避免深度模型引入的延迟。

  - **全双工流式交互建模**：把用户停顿、backchannel、插话作为第一等事件处理，适合电商直播互动、语音导购等场景，避免打断导致上下文丢失，可借鉴其同步音频流状态管理方式。

  - **异步 Voice Agent 工具调用**：工具执行不阻塞语音流，适合需要实时推荐商品、查询优惠、调用后台服务的语音助手架构，前台持续对话，后台完成工具链路，提升体验流畅度。

  - **音频理解与推理统一评估**：MMSU、AA Full-Duplex Bench、τ-Voice 等指标覆盖听、说、工具调用，可作为构建语音推荐/客服评测集的参考维度。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：实时语音交互要求深度推理、快速响应和自然轮流，传统模型难以兼顾低延迟与强推理。

**方法关键点**：StepAudio 3 Realtime 以连续 listen-converse-think-act 循环组织。Deep Perception 捕获丰富声学线索理解用户意图；Seamless Duplex 同步音频流处理停顿、backchannel 和打断；核心的 Think-While-Speaking 机制在语音输出同时执行私有推理，解耦深度思考与响应延迟；集成 Voice Agent 异步执行工具调用，不破坏对话流。

**关键结果**：推理模式下在 StepAudioChat 达 73.0 macro average；启用 Think-While-Speaking 后，实时模式对话与推理表现与专用推理模型相当；音频理解 MMSU 90.6，全双工基准 AA Full-Duplex Bench 98.9 Overall，语音 Agent 基准 τ-Voice 56.0% macro task-success。
