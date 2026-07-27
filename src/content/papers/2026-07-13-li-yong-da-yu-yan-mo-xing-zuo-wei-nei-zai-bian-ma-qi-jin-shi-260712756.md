---
title: 'VisCo: Leveraging Large Language Models as Intrinsic Encoders for Visual Token
  Compression'
title_zh: 利用大语言模型作为内在编码器进行视觉令牌压缩
authors:
- Yupeng Zheng
- Kai Zou
- Bin Liu
- Nenghai Yu
affiliations:
- Anhui Province Key Laboratory of Digital Security, University of Science and Technology
  of China
arxiv_id: '2607.12756'
url: https://arxiv.org/abs/2607.12756
pdf_url: https://arxiv.org/pdf/2607.12756
published: '2026-07-13'
collected: '2026-07-27'
category: Multimodal
direction: 视觉令牌压缩 · VLM推理效率
tags:
- Visual Token Compression
- Vision Language Models
- Autoencoder
- Parameter Sharing
- Memory Tokens
one_liner: 提出 VisCo，把预训练 VLM 重用为内在视觉令牌压缩器，用参数共享自编码器和记忆令牌实现高压缩比下的领先性能。
practical_value: '- 在电商多模态商品理解中，可复用已部署的 VLM 作为视觉特征压缩器，避免引入外部模块和重训练成本，直接降低推理延迟。

  - 记忆令牌（memory tokens）的压缩方式类似推荐系统中的语义 ID 压缩，可将高维视觉特征蒸馏为少量可学习令牌，适合大量商品图片的在线编码。

  - 层级信息传递机制可用于多尺度商品视觉特征提取，在不增加额外参数的前提下保留细粒度信息，提升下游检索或推荐质量。

  - 极端压缩（如单令牌）下性能稳定，适合对实时性要求高的推荐场景，如首页商品卡片渲染、搜索结果的首图压缩。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：VLMs 处理大量视觉令牌，带来高推理延迟与内存开销。现有免训练方法用启发式指标，高压缩比下性能骤降；训练式方法引入外部压缩模块，需重新训练 VLM 骨干，成本高且破坏预训练先验。VLM 本身具备强信息编码能力，但未被现有压缩方法充分利用。

**方法**：提出 VisCo，一个训练高效的自压缩框架，将预训练 VLM 自身作为内在压缩器（intrinsic compressor）。核心是参数共享的自编码器：使用一小部分可学习的“记忆令牌”（memory tokens）把原始视觉令牌压缩成紧凑表示；编码器与解码器共享 VLM 的 Transformer 层，通过层级信息传递（hierarchical information transfer）从编码端向解码端注入多尺度信息，保证重构质量。整个压缩过程不需要额外模块，仅需少量训练。

**结果**：在所有压缩比下性能超越先前方法，压缩比越高优势越大；在极端单令牌设置下仍稳定，甚至结合原始令牌后能进一步提升基线 VLM 的性能，表明记忆令牌学到了原始令牌未覆盖的互补表示。
