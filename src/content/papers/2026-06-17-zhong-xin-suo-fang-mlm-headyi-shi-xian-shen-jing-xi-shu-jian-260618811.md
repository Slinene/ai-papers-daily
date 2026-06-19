---
title: Rescaling MLM-Head for Neural Sparse Retrieval
title_zh: 重新缩放MLM-Head以实现神经稀疏检索
authors:
- Youngjoon Jang
- Seongtae Hong
- Jonah Turner
- Heuiseok Lim
affiliations:
- Korea University
- Independent
arxiv_id: '2606.18811'
url: https://arxiv.org/abs/2606.18811
pdf_url: https://arxiv.org/pdf/2606.18811
published: '2026-06-17'
collected: '2026-06-19'
category: RecSys
direction: 神经稀疏检索 · MLM-head尺度校正
tags:
- Learned Sparse Retrieval
- SPLADE
- MLM-head rescaling
- training stability
- ModernBERT
one_liner: 发现SPLADE训练中MLM-head尺度不匹配导致训练崩溃，提出初始化时简单缩放修正，稳定训练并提升大骨干检索性能
practical_value: '- 在电商搜索或推荐系统的召回阶段，若使用SPLADE类稀疏检索模型，替换更强预训练骨干时出现训练不稳定，可检查MLM-head的L2范数，并在初始化时进行尺度缩放（如除以范数均值），零成本、不改架构，即可恢复稳定训练。

  - 该发现提示：对于依赖预训练MLM-head输出构造稀疏表示的模型，模型升级时不能只看编码器能力，还要注意输出头的尺度校准；类似问题可能存在于其他用MLM-head
  logits构建匹配分数的检索或排序模型中。

  - 广告搜索场景中，稀疏词项表示能提供可解释的召回结果，此技巧可帮助团队更放心地将现代预训练模型（如ModernBERT）应用于生产级稀疏检索，提升召回率而无需担心训练崩溃。

  - 在Agent系统中若用稀疏检索作为记忆或知识召回模块，更换更强的语言模型时，推荐先检查并校正MLM-head尺度，避免对比训练不稳定导致性能下降。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：Learned Sparse Retrieval (LSR) 如 SPLADE 通常以 BERT 为骨干，直觉上换用更强的预训练编码器应提升检索效果。但作者发现，在标准 SPLADE 训练流程下，某些现代骨干（如 ModernBERT）的 MLM-head L2 范数过大，会导致训练不稳定甚至崩溃。根因是 SPLADE 直接使用 MLM-head 的输出构造稀疏词项权重，并利用未归一化的点积计算查询-文档相关性；MLM-head 尺度过大会放大稀疏激活，扭曲匹配分数，破坏对比学习。

**方法关键点**：提出一种零成本的初始化修正——在 SPLADE 训练前，将 MLM-head 投影矩阵除以一个常数缩放因子（如 backbone 的 MLM-head 权重初始 L2 范数的均值），从而校准输出尺度。该操作不改变模型架构或训练目标，仅调整初始状态。

**关键结果**：在 MS MARCO 域内检索及 BEIR 域外零样本检索等基准上，经尺度校正后，原先不稳定的大范数骨干（ModernBERT、Ettin）不仅训练稳定，而且检索指标大幅提升，部分设置下匹配甚至超越经典 BERT-SPLADE 基线。例如，ModernBERT-base 未经校正时 MRR@10 仅 0.281，校正后升至 0.387（域外数据上也有类似增益），验证了 MLM-head 尺度校准是迁移预训练编码器的关键瓶颈。
