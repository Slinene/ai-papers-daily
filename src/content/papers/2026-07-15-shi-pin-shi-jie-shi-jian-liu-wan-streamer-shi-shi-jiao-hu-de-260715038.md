---
title: Video = World + Event Stream
title_zh: 视频 = 世界 + 事件流：Wan-Streamer 实时交互的预训练视角
authors:
- Lianghua Huang
- Zhi-Fan Wu
- Yupeng Shi
- Wei Wang
- Mengyang Feng
- Cheng Yu
- Chen Liang
- Junjie He
- Chen-Wei Xie
- Yu Liu
affiliations:
- Alibaba Group
arxiv_id: '2607.15038'
url: https://arxiv.org/abs/2607.15038
pdf_url: https://arxiv.org/pdf/2607.15038
published: '2026-07-15'
collected: '2026-07-18'
category: Multimodal
direction: 多模态实时交互 · 世界-事件流分解
tags:
- video-encoding
- world-event-decomposition
- real-time-interaction
- pretraining-task
- audio-visual
- streaming
one_liner: 将视频重新解释为持久世界与事件流之和，提出通用预训练任务，并实现低延迟实时全双工音视频交互
practical_value: '- 世界-事件流分解思想可用于用户行为序列建模：将长期稳定的用户兴趣（世界）与短期刺激（事件流）分离，提升序列推荐模型对上下文变化的鲁棒性。

  - 流式预训练范式可被借鉴到实时推荐 agent：将推荐动作视为事件流，在用户-物品交互的流式数据上预训练，使模型学会在毫秒级延迟下预测用户即时意图。

  - 全双工交互中的端到端联合训练（感知、时机、动作）可启发对话式推荐 agent 设计，避免模块级联导致的延迟累积与损失隔离。

  - 160ms 流单元、200ms 模型延迟的工程实践为实时交互 agent 的部署提供了量化参考，尤其适用于需快速响应的电商直播带货等场景。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：Wan-Streamer 系列从 v0.1 起追求实时全双工音视频交互，但过去将训练目标绑定在特定应用上。v0.3 希望提炼底层能力，提出一个更通用的视角：任何视频都可分解为“世界”（持久的环境、场景、人物、声学条件等）和“事件流”（随时间变化的行为、语音、场景转换等）。基于此可设计一个通用预训练任务——给定世界和当前输入，预测世界的运动、变化与实时响应。该能力可泛化到多种实时任务，尤其被实例化到实时音视频交互中，此时事件流就是 agent 的语音和自由行为。

**方法关键点**：在大量真实视频上执行上述预训练任务，模型学习从多模态输入（文本、音频、视频）直接映射到语言形式的语音和动作行为，形成一种视觉-语言-动作式的理解流程。架构继承 v0.2 的 640×368 分辨率、25 FPS、160ms 流单元，并通过 Ulysses 风格上下文并行保持约 200ms 模型侧延迟。交互过程端到端建模在同一因果时间线上，感知、响应时机、言语、可见倾听、同步视频作为单一行为被联合学习。

**关键结果**：在保持相同操作的条件下，v0.3 验证了该世界-事件流分解的有效性，实现约 200ms 模型延迟、总体约 550ms 交互延迟（含 350ms 双向网络预算）。原论文未直接对比 ablations，核心贡献在于提出新视角与预训练任务的定义。
