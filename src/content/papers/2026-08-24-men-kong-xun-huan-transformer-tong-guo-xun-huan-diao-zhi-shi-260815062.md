---
title: 'Gated Recurrent Transformers: Expressive Depth through Recurrent Modulation
  in Transformers'
title_zh: 门控循环Transformer：通过循环调制实现深度表达力
authors:
- Amr Hegazy
- Amr Alanwar
- Mostafa Elhoushi
affiliations:
- The German University in Cairo
- Technical University of Munich
- Cerebras Systems Inc.
arxiv_id: '2608.15062'
url: https://arxiv.org/abs/2608.15062
pdf_url: https://arxiv.org/pdf/2608.15062
published: '2026-08-24'
collected: '2026-08-27'
category: LLM
direction: 高效Transformer架构 · 循环深度共享
tags:
- Transformer
- Recurrent Depth
- Gating
- Efficiency
- Language Modeling
one_liner: 用门控循环共享核心层，在固定算力或参数预算下达到甚至超越稠密Transformer质量，大幅减少参数与解码内存
practical_value: '- 共享核心层 + 固定 prelude/coda 的架构可作为在线大模型推理的轻量化替代：用 3 层共享核心迭代 R 次匹配
  12 层稠密模型精度，峰值解码内存降低约 59%，适合内存受限但延迟容忍度较高的生成式推荐/文案生成服务。

  - 门控循环更新机制（elementwise gate 结合隐藏状态、prelude 输出与每步重采样噪声）能让同一组层在不同循环步动态调制输入，避免深度共享导致的表达坍缩；该
  trick 可迁移到推荐序列建模中的共享 Transformer 层，在参数不变的情况下提升序列多样性建模能力。

  - 采用 isoFLOPS / isoPARAMS 评估方式做架构选型，对实际部署有指导意义：在固定算力或参数预算下，优先考虑增加循环深度而非堆叠唯一层，可以获得更好的
  loss/质量与内存 tradeoff。

  - 对于广告文案生成、搜索 query 推荐等需要大模型但受限于显存和参数规模的场景，GRT 提供了一种可复用的参数高效化路径，且其代码已开源，便于快速验证迁移效果。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：缩放 Transformer 语言模型带来表达能力与内存效率的矛盾。每层使用独立权重可保留从输入基础到抽象提炼的功能特化，但内存开销大；标准深度共享则强制统一变换，导致表示多样性丧失、建模质量下降。

**方法关键点**：提出 Gated Recurrent Transformer（GRT），采用循环深度架构：固定深度的 prelude 和 coda 块包裹一个共享核心，该核心被迭代 R 次。受门控循环网络启发，使用轻量投影和逐元素更新门——该门以隐藏状态、固定 prelude 输出以及每一步重新采样的噪声为条件——调制循环更新。这样同一组少量层在多次循环中能针对不同输入自适应特化，而无需大量唯一层。

**关键结果**：在 isoFLOPS 约束下，3 层 GRT 匹配 12 层 GPT-2 Small 基线的精度，训练和推理 FLOPs 相近，并在全部九个规模预算单元中领先 MoR 和 heavy-tail depth sampling；中规模且预算加倍时超过稠密模型。isoPARAMS 约束下，更深循环达到验证损失 2.76，对比非循环对照的 2.84。大规模场景下参数减少 63%，峰值解码内存降低 59%，编译生成延迟仅增加 10%。
