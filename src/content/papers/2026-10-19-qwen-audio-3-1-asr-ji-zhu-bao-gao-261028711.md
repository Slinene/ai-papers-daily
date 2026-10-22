---
title: Qwen-Audio-3.1-ASR Technical Report
title_zh: Qwen-Audio-3.1-ASR 技术报告
authors:
- Chuanmeng Bian
- Daren Chen
- Peixin Chen
- Zhigao Chen
- Chong Deng
- Zhiyun Fan
- Zhifu Gao
- Bo Gong
- Qing Gu
- Jiajun He
affiliations:
- Alibaba Token Foundry, Alibaba Group
arxiv_id: '2610.28711'
url: https://arxiv.org/abs/2610.28711
pdf_url: https://arxiv.org/pdf/2610.28711
published: '2026-10-19'
collected: '2026-10-22'
category: Multimodal
direction: 音频语言模型 · ASR 与说话人分离
tags:
- ASR
- Speaker Diarization
- Audio Understanding
- Multimodal
- Low-latency Streaming
- Instruction-controlled
one_liner: 在 Qwen-Audio-3.0-ASR 基础上扩展说话人分离与通用音频理解，覆盖多语言、多方言及流式/非流式部署
practical_value: '- 统一音频语言模型可替代「ASR + 说话人分离 + 音频事件检测」多系统拼接，适合电商直播、客服会话等需结构化语音理解的场景；其输出
  speaker labels + timestamps + text 可直接用于下游 Agent 做意图识别、摘要或推荐线索提取。

  - 指令可控的历史上下文、分层热词定制、原生转录润色，对电商/搜索领域专有名词（品牌、商品名、黑话）识别有直接借鉴：把行业词表分层注入 ASR，可显著降低专有词错误率。

  - 异步文件、低延迟流式、交互语音输入、非流式等变体展示了「按延迟/成本选择不同模型」的工程思路，适合在语音购物助手、实时直播字幕、离线质检等业务中做差异化部署。

  - 说话人分离与重叠语音处理能力可用于多人客服对话、直播连麦分析，为后续推荐/搜索的用户建模提供更干净、带说话人标识的文本特征。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：把语音识别从「转文字」扩展到「谁在说、说了什么、伴随什么声音/音乐」，并适配流式与文件场景，减少独立 ASR、说话人分离、音频理解系统拼接。

**方法**：基于 Qwen-Audio-3.0-ASR 升级，保留 30 语言、16 种中文方言；指令控制支持历史上下文、分层热词定制、原生转录润色。说话人分离 ASR 输出 speaker labels、时间戳、文本，支持跨轮一致的 speaker 标签与重叠语音。通用音频理解覆盖 captioning、temporal grounding、sound event detection、audio QA 等。提供异步文件、低延迟流式、交互语音输入、非流式识别变体。

**结果**：多语言 ASR macro-average error 15.09%，相对 Qwen-Audio-3.0-ASR 降低 32.9%；speaker-diarized ASR 最低 mean cpWER 12.93%；音频理解 MMAU 81.60、MMSU 82.24。
