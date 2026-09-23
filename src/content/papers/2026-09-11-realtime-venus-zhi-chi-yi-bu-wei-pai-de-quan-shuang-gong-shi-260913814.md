---
title: 'Realtime-Venus: A full-duplex interaction system with asynchronous delegation'
title_zh: Realtime-Venus：支持异步委派的全双工实时交互系统
authors:
- Ruixiang Zhao
- Hualei Wang
- Renhe Sun
- Enzhi Zhou
- Jincenzi Wu
- Xujie Song
- Kexin Shi
- Zihang Liu
- Pengcheng Zhu
- Jiayi Zhou
affiliations:
- Venus Team, Ant Group
- Tsinghua University
arxiv_id: '2609.13814'
url: https://arxiv.org/abs/2609.13814
pdf_url: https://arxiv.org/pdf/2609.13814
published: '2026-09-11'
collected: '2026-09-23'
category: Agent
direction: 全双工语音/多模态 Agent 异步委派
tags:
- full-duplex
- multimodal
- speech interaction
- asynchronous delegation
- realtime agent
- tool use
one_liner: 双 9B 模型全双工交互系统，前台实时对话与后台异步工具执行协同，音频/视频基准超越 GPT-4o 等在线模型
practical_value: '- 双循环异步委派架构值得借鉴：将前台低延迟语音/视觉交互与后台工具执行（如订单查询、库存检查、推荐 API 调用）解耦，高响应实时对话不因长尾任务阻塞，适合电商导购
  Agent。

  - 共享因果时间线统一用户输入、模型输出与委派事件，能有效管理多轮对话中的打断/重叠语音，提升全双工体验；可迁移到实时语音推荐场景，避免状态错乱。

  - 后训练阶段加入主动全双工轨迹和委派工作流，可提高模型在真实对话中的主动性和工具调用协同；对于需主动推送商品/优惠信息的对话式推荐系统有参考价值。

  - 两个 9B 模型分别优化音视频与纯语音，按场景拆分部署，减少模态冗余并降低推理成本；可借鉴为电商视频/语音客服分别训练轻量前端模型。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：自然交互要求持续感知与及时响应，语音对话依赖声学与语言线索，视频交互还需将对话锚定在动态视觉语境中。现有系统难以同时支持流畅的全双工对话与后台工具调用。

方法关键点：Realtime-Venus 为主动式全双工系统，训练两个 9B 模型：Realtime-Venus-Omni 处理音视频，Realtime-Venus-Audio 处理纯语音。每个模型作为完整对话前端，集成持续感知、对话控制与原生语音生成，并共享统一因果时间线管理用户输入、模型输出与委派事件。双循环运行时将前台实时交互与后台推理/工具执行解耦：前台继续对话，Harness 异步执行任务并在完成后将结果融入对话。后训练配方融合离线理解、主动全双工轨迹与委派工作流。

关键结果：在 8 个视频基准中，Realtime-Venus-Omni 在 6 项上最优，包括 StreamingBench 70.2%、OVO-Bench 64.7%、Daily-Omni 81.3%。音频方面，Realtime-Venus-Audio 在 8 个基准中的 MMAU 78.0%、MMAU-Pro 63.2%、Llama Questions 83.8%、Speech CMMLU 67.8% 领先，VoiceBench AlpacaEval 达到最优 4.81。Full-Duplex-Bench v1.5 显示，模型响应 75% 用户打断，并在回传信道、他人导向语音、背景语音条件下保持 97%、88%、86% 的持续率，超过 Gemini 3.1 Live 与 GPT-4o。
