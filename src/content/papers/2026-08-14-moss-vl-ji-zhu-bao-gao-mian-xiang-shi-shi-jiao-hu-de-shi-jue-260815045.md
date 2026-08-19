---
title: MOSS-VL Technical Report
title_zh: MOSS-VL 技术报告：面向实时交互的视觉语言模型
authors:
- Pengyu Wang
- Chenkun Tan
- Shaojun Zhou
- Qirui Zhou
- Yanxin Chen
- Xingyang He
- Huazheng Zeng
- Jijun Cheng
- Chenghao Wang
- Xiaomeng Qian
affiliations:
- Fudan University
arxiv_id: '2608.15045'
url: https://arxiv.org/abs/2608.15045
pdf_url: https://arxiv.org/pdf/2608.15045
published: '2026-08-14'
collected: '2026-08-19'
category: Multimodal
direction: 多模态实时交互模型
tags:
- Vision-Language Model
- Real-Time Interaction
- Streaming Video
- Cross-Attention
- Curriculum Learning
one_liner: 开源视觉语言模型 MOSS-VL 通过门控交叉注意力实现边看边说，实时主动交互能力领先
practical_value: '- 架构借鉴：将视觉 token 移出解码序列，仅通过门控交叉注意力注入视觉信息，可显著降低首 token 延迟，适合电商直播助手的实时交互场景

  - 训练策略：合成交互语料库显式监督模型何时发言、何时沉默、何时修正，可借鉴用于训练主动提醒型电商客服或直播导购 Agent

  - 课程学习：实时特定训练集中在轻量最终阶段，避免破坏离线基础能力，可用于多模态模型增量训练，降低工程成本

  - 主动行为：在 OmniMMI Proactive Alerting 上 66.0 vs 37.5 的性能表明模型能主动捕捉关键事件，可应用于商品状态监控、用户行为异常提醒等场景'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有开源视觉语言模型多为离线视频理解，但实时场景（如直播助手、交互式监控）要求模型边看边说，能主动发言、沉默或根据新证据修正。

**方法关键点**：
- 语言解码器仅通过门控交叉注意力关注视觉信息，生成时仍能接收新帧，实现“感知同时生成”；视觉 token 不进入解码序列，降低序列长度，提升首 token 速度。
- 合成交互语料库监督模型何时说话、何时保持沉默、何时修正之前的回复。
- 分阶段课程：在强大离线基础之上，将实时特定训练集中在轻量的最终阶段。

**关键结果**：
- 离线 MOSS-VL-Instruct 在可比规模上有竞争力，并在时序推理视频数据集上领先。
- 在四个流式基准上，MOSS-VL-Realtime 在三个上取得开源流式模型最佳平均（第四个第二）；在 OmniMMI Proactive Alerting 子集上 66.0 vs 最佳基线 37.5，大幅领先。
- 11.3B 参数，视觉 token 在解码序列外，相比同骨架 Qwen3-VL-8B，首 token 时间优势从 2.8x 扩大到 5.1x（视觉上下文增长时）。
- 已发布全部五个 checkpoint、训练课程和实时推理代码。
