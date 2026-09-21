---
title: 'NemotronLabs VoiceChat: An Open Full-duplex Speech-to-Speech Model with Tool
  Calling Capabilities'
title_zh: NemotronLabs VoiceChat：开放全双工语音到语音模型，原生支持工具调用
authors:
- Jagadeesh Balam
- Travis Bartley
- Edresson Casanova
- Sanjay Chauhan
- Chen Chen
- Zhehuai Chen
- Zijia Chen
- Francesco Ciannella
- Slyne Deng
- Mikyas Desta
affiliations:
- NVIDIA
arxiv_id: '2609.21967'
url: https://arxiv.org/abs/2609.21967
pdf_url: https://arxiv.org/pdf/2609.21967
published: '2026-09-18'
collected: '2026-09-21'
category: Agent
direction: 全双工语音 Agent 与工具调用
tags:
- full-duplex speech
- speech-to-speech
- tool calling
- streaming architecture
- voice agent
one_liner: 开源全双工语音模型，统一流式架构实现听、转写、推理、工具调用与说话，打断恢复与工具选择表现强
practical_value: '- 全双工交互可迁移到语音购物助手/智能客服：用户说话时持续监听，支持打断、backchannel 和自然话轮切换，减少 VAD
  等待造成的延迟和误判，提升实时推荐场景的对话体验。

  - 并行输出 agent text 与结构化 function call 的架构值得借鉴：在对话推荐系统中同时生成自然语言回复和调用商品搜索/推荐 API 的指令，避免串行等待，缩短端到端延迟。

  - 辅助 RNN-T 增量转写分支可用于实时 query 感知：在用户说话过程中即提取关键词（商品、价格、属性），触发增量式 query 改写或推荐候选刷新，抢在用户结束前预计算。

  - 工具调用能力已有较好基础（工具选择 F1 82.5%），但参数准确性和端到端执行仍需提升；业务上可先用于简单、结构清晰的工具（如查订单、加购物车），复杂参数场景建议人工兜底或后验证。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：传统级联 ASR-LLM-TTS 语音助手普遍是半双工，依赖 VAD 等用户停止说话后才响应，难以复现人类自然对话中的打断、backchannel 与实时交互。需要一种统一、低延迟的全双工语音模型，并能直接调用外部工具。

**方法关键点**：NemotronLabs VoiceChat 采用流式语音编码器 + decoder-only LM 作为核心，并行输出两条专用流：agent 自然语言文本和结构化 function call；同时引入辅助 RNN-T 分支做增量用户转写，以及流式 TTS 解码器生成语音。模型在统一流式架构内完成听、转写、推理、工具调用和说话，保持对话时序行为。

**关键结果**：在 Full-Duplex-Bench 1.0 上，该模型在开放权重系统中获得最低的暂停处理接管率，用户打断后 100% 接管，打断后响应质量 4.33/5；在 1.5 上，用户 backchannel 后 93% 恢复响应；VoiceBench 归一化平均分 55.1；在 FDB 3.0 上工具选择 F1 82.5%，但参数准确性和端到端工具执行仍有改进空间。
