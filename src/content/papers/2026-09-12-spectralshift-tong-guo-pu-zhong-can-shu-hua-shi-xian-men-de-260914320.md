---
title: 'SpectralShift: Effective Context Window Extension of Gated DeltaNet via Spectral
  Reparameterization'
title_zh: SpectralShift：通过谱重参数化实现门控 DeltaNet 的高效上下文窗口扩展
authors:
- Zian Liu
- Yiwen Hu
- Zican Dong
- Tian Xie
- Wayne Xin Zhao
- Yucheng Ding
- Ran Tao
- Bryan Dai
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
- IQuest Research
- Microsoft Research Asia
arxiv_id: '2609.14320'
url: https://arxiv.org/abs/2609.14320
pdf_url: https://arxiv.org/pdf/2609.14320
published: '2026-09-12'
collected: '2026-09-17'
category: Training
direction: 线性注意力长上下文扩展训练
tags:
- Spectral Reparameterization
- Gated DeltaNet
- Linear Attention
- Long Context Extension
- Learning Rate Scaling
one_liner: 提出谱重参数化方法，通过重塑衰减谱和学习率缩放，提升门控 DeltaNet 的长上下文扩展能力
practical_value: '- 若业务中采用线性注意力或状态空间模型（如 Gated DeltaNet、Mamba）做用户长期行为序列建模，可借鉴谱分析思路：调整转移矩阵初始化，将衰减率分布设计为“慢谱带为主、快衰减模式保留”，既能捕获数月级别的长期兴趣依赖，又能在会话切换时快速重置状态，避免历史噪声污染当前推荐。

  - 在将通用 LLM/线性注意力模型继续预训练到业务长上下文场景（如超长用户反馈、多轮 Agent 交互记忆）时，不必盲目全局持续预训练：可只对状态转移相关参数（alpha
  投影）做谱重塑初始化，并赋予其更大的学习率，其他层保持常规更新，以更低成本完成上下文窗口扩展。

  - 该方法不增加推理计算或 KV cache，适合线上低延迟的推荐/搜索服务；若团队自研线性注意力序列模型，可直接沿用“初始化谱重塑 + alpha 投影学习率缩放”的工程
  trick，避免修改推理代码。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：线性注意力层逐步替代 softmax attention 用于长上下文建模，但现有上下文扩展方法通常直接进行 continual pretraining，未修改这些层的结构，忽略了线性注意力状态动态的谱特性。针对 Gated DeltaNet（GDN），从转移矩阵的谱视角研究长上下文扩展，发现长程信息检索依赖两个关键因素：（1）足够宽的慢谱带（slow spectral band）与目标依赖长度对齐；（2）保留快衰减模式（fast-decaying modes）用于状态清理与上下文切换。

方法：提出 SpectralShift，一种面向 GDN 长上下文 continual pretraining 的谱重参数化方法。具体包括：重新参数化 alpha 投影的初始化，以重塑衰减谱，增强慢传播容量；引入对 alpha 投影的学习率缩放，促进长上下文训练。该方法仅调整初始化与学习率，不改变前向推理结构。

结果：实验表明，SpectralShift 在训练过程中持续提升长上下文能力，为线性注意力模型上下文窗口扩展提供有效且高效的方案，且不增加推理开销。代码已开源。
