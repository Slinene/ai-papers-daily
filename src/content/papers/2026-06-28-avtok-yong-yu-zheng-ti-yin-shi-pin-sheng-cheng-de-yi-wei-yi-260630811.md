---
title: 'AVTok: 1D Unified Tokenization for Holistic Audio-Video Generation'
title_zh: 'AVTok: 用于整体音视频生成的一维统一分词器'
authors:
- Kien T. Pham
- I Chieh Chen
- Qifeng Chen
- Long Chen
affiliations:
- The Hong Kong University of Science and Technology
arxiv_id: '2606.30811'
url: https://arxiv.org/abs/2606.30811
pdf_url: https://arxiv.org/pdf/2606.30811
published: '2026-06-28'
collected: '2026-07-02'
category: Multimodal
direction: 统一多模态分词器 · 音视频生成
tags:
- Unified Tokenization
- Audio-Video Generation
- Dual-Stream Transformer
- Discrete Representation
- Multimodal Learning
- 1D Latent
one_liner: 提出统一音视频分词器 AVTok，用双流 Transformer 将音视频对编码为共享码本的紧凑一维 token 序列
practical_value: '- 统一码本设计可借鉴：在电商推荐中，将商品图像、描述、甚至短视频音轨等异构模态信息通过统一分词器映射到共享离散空间，便于后续的生成式推荐模型（如基于
  AR 的 item 生成）处理。

  - 双流架构与模态特定可学习查询：可用于处理搜索推荐中用户行为序列（时序流）和内容特征（语义流）的融合，共享主干而保留模态差异，降低计算开销。

  - 分层训练策略：缓解多模态数据的信息不平衡问题，在推荐场景中可逐步引入不同模态特征（先文本后图像），让模型渐进学习对齐表示，避免单一模态主导。

  - 主要是学术贡献，业务可借鉴点有限，但统一多模态 tokenization 的思路对构建商品或内容的全域统一表示有启发性。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有音视频生成方法多采用分离式双分支设计，各模态独立分词和生成，忽略模态间表示鸿沟，且训练成本高昂。受一维视觉分词进展启发，本文旨在设计一个统一分词器，将音视频对编码为紧凑的一维离散表示，为下游生成模型提供高效的全模态 token。

**方法关键点**：
- 提出 AVTok，一种双流 Transformer 架构，共享编码器-解码器，引入模态特定的可学习查询（learnable queries），将音视频对联合编码为统一的 1D latent code。
- 使用统一的离散码本（unified codebook），使音频和视频 token 共享同一个词汇表，消除模态表示 gap。
- 设计分层训练策略（hierarchical training），先分别重建单一模态，再联合训练，缓解音视频信息不平衡问题，逐步提升重建能力。

**关键结果**：
- 在音视频重建质量上达到与单模态 SOTA 分词器（视频 tokenizer 和音频 codec）可比的性能。
- 集成至自回归生成模型后，在音频到视频、视频到音频、类别条件联合生成等下游任务上表现优异，生成结果具有细粒度音画同步和语义对齐。
- 为构建统一的音视频大模型提供了可行的 tokenization 方案。
