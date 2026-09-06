---
title: VibeVoice-ASR-Streaming Technical Report
title_zh: VibeVoice-ASR-Streaming：LLM 流式说话人归因语音识别
authors:
- Yujie Tu
- Zhiliang Peng
- Jianwei Yu
- Li Dong
- Songchen Xu
- Yaoyao Chang
- Wenhui Wang
- Zilong Wang
- Zehua Wang
- Yan Xia
affiliations:
- Microsoft Research
- University of Chinese Academy of Sciences
- Shanghai Jiao Tong University
arxiv_id: '2609.02812'
url: https://arxiv.org/abs/2609.02812
pdf_url: https://arxiv.org/pdf/2609.02812
published: '2026-09-01'
collected: '2026-09-06'
category: LLM
direction: LLM 流式说话人归因 ASR
tags:
- ASR
- Speaker Diarization
- Streaming
- LLM
- Speech
- Low-latency
one_liner: 首个 LLM 端到端流式说话人归因 ASR 之一，交错音频块与少量前瞻音频实现低延迟“谁说了什么”输出
practical_value: '- 面向实时语音 Agent/客服：统一 LLM 直接生成“说话人+转写”，省去独立说话人日志模块，降低级联错误与延迟；输入设计可参考
  fixed-size audio chunks + 少量 lookahead audio + previous text 的拼接策略，在语音点单、售后沟通等场景实现流式结构化记录。

  - 自托管替代商业 API：在电商/广告会议转录等数据敏感场景，7B/1.5B 开源模型在五个评测集 WER/CER 上平均最低，且 speaker attribution
  在 12/13 设置最优或并列，可作为内部服务，避免数据外传并控制成本。

  - 工程架构上，用少量前瞻音频而非整句缓存，能显著降低流式延迟；在 Agent 中可类似设计“当前 chunk + 短 lookahead + 上一轮文本”的上下文，减少重复识别和说话人切换丢失。

  - 中文电商场景需注意：论文里的中文会议集 AISHELL-4、AliMeeting 上 CER 仍较高（约 30-50%），落地前应基于国内电商/客服语音数据做领域微调，尤其提升中文说话人归因和电商术语识别。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：传统 speaker-attributed ASR 将 ASR 和 speaker diarization 作为两个独立任务；统一端到端模型如 VibeVoice-ASR 主要支持离线，无法满足实时语音助手和 Agent 的低延迟需求。

**方法关键点**：VibeVoice-ASR-Streaming 是较早的基于 LLM 的端到端流式说话人归因 ASR。它将固定大小音频块、少量前瞻音频和已生成文本交错输入，在语音到达时直接输出“谁在何时说了什么”，无需独立 diarization 阶段。模型提供 1.5B 和 7B 两个规模，并开源权重和推理代码。

**关键结果**：在 AliMeeting、AISHELL-4、AMI-SDM、AMI-IHM 和 MLC-Challenge 五个评测集上，7B 模型取得最低平均 WER/CER；说话人归因在 13 个评测设置中 12 个达到最优或并列最优。与 Gemini 3.5 Transcribe Live、GPT Realtime Whisper、GPT Live Transcribe、ElevenLabs Scribe v2 Realtime 等部署流式系统相比，在会议转录和实时语音识别精度上具有竞争力。
