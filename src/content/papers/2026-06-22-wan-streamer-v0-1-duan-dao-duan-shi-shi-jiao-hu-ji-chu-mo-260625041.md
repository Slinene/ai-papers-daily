---
title: 'Wan-Streamer v0.1: End-to-end Real-time Interactive Foundation Models'
title_zh: Wan-Streamer v0.1：端到端实时交互基础模型
authors:
- Lianghua Huang
- Zhifan Wu
- Wei Wang
- Yupeng Shi
- Mengyang Feng
- Junjie He
- Chenwei Xie
- Yu Liu
- Jingren Zhou
- Ang Wang
affiliations:
- Alibaba Group
arxiv_id: '2606.25041'
url: https://arxiv.org/abs/2606.25041
pdf_url: https://arxiv.org/pdf/2606.25041
published: '2026-06-22'
collected: '2026-06-25'
category: Multimodal
direction: 端到端多模态流式交互
tags:
- streaming
- multimodal
- transformer
- real-time
- full-duplex
- interactive AI
one_liner: 首个原生流式、端到端全双工多模态交互模型，单Transformer统一语音/视频/文本，模型侧延迟200ms
practical_value: '- 统一多模态 Transformer 架构可简化电商直播、虚拟客服等场景中的感知-决策-生成流水线，消除级联模块间的错误累积和调度延迟。

  - 块因果注意力（block-causal attention）与 160ms 流式单元的设计可直接借鉴到需要低延迟增量推荐的场景（例如直播实时排序、流式反馈更新），保证推理的流式一致性。

  - 全双工交互范式可启发对话式推荐 Agent：让 Agent 在用户说话/行动的同时并行准备响应，实现自然的“边听边想边说”，提升互动流畅度。

  - 低延迟多模态令牌调度策略（audio/video/text token 交错编排）为构建实时多模态搜索与推荐系统提供了工程参考，减少端到端响应时间。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：人类交互是流式、全双工的，但现有 AI 交互系统通常由独立模块（VAD、ASR、LLM、TTS、动画/视频生成）级联而成，导致较高延迟、错误积累和调度复杂。

**方法关键点**：
- 单一 Transformer 直接建模语言、音频、视频的输入与输出，序列由交错的多模态令牌构成，通过 **块因果注意力** 实现增量流式生成，无需外部模块。
- 针对流式重建整个推理栈：因果视觉/音频编码器、因果解码器、低延迟多模态令牌调度，支持最小 160ms 的流式单元（25 fps）。
- 训练时联合学习感知、推理、生成、响应时机、跨模态同步，实现真正的端到端全双工交互。

**关键结果**：
- 模型侧响应延迟约 200ms，结合 350ms 双向网络延迟总交互延迟约 550ms，实现子秒级全双工音视频通信。
- 消除了级联系统中的流水线延迟和错误传播，为实时数字人、直播互动、具身助手等场景提供了统一基础模型。
