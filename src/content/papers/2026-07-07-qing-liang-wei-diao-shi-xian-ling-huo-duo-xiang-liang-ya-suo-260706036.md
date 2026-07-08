---
title: 'Learn to Pool: Lightweight Fine-Tuning for Flexible Multi-Vector Compression'
title_zh: 轻量微调实现灵活多向量压缩的池化学习
authors:
- Stefan Josef
affiliations:
- Independent Researcher
arxiv_id: '2607.06036'
url: https://arxiv.org/abs/2607.06036
pdf_url: https://arxiv.org/pdf/2607.06036
published: '2026-07-07'
collected: '2026-07-08'
category: RecSys
direction: 多向量检索模型轻量压缩微调
tags:
- late interaction
- multi-vector
- token pooling
- vector compression
- lightweight fine-tuning
- ColBERT
one_liner: 用轻量微调与k-means池化让ColBERT压缩83%向量而不损失检索精度
practical_value: '- 在电商搜索或推荐的多向量模型（如 ColBERT）中，直接用 k-means 聚类池化加轻量微调，可将文档向量压缩 80%+，大幅降低线上存储与召回延迟。

  - 多因子训练让单一模型同时适配不同压缩级别，可根据业务场景灵活切换（粗排高压缩，精排低压缩），无需维护多套模型。

  - 只需少量目标域数据微调（而非全量对比学习），适合在业务中快速迭代，将通用检索能力迁移到垂直领域。

  - 池化策略具备跨数据集迁移能力，可用通用数据预训练池化头，再在电商 query-doc 对上调优，减少冷启动成本。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：late interaction 模型如 ColBERT 将文档编码为多个 token 向量，检索效果好但存储和内存开销巨大。推理时使用池化可以减少向量数，但精度会下降；池化感知的大规模训练能维持精度却成本高昂，不适用于多数业务场景。  
**方法**：作者提出在预训练 ColBERT 上做轻量微调来学习池化。具体使用 k-means 聚类对 token 向量进行分组，并通过少量参数（如聚类中心）的微调使模型适应池化。进一步提出多因子训练，让同一个模型同时面对多个池化因子（向量压缩率）进行学习，训练后可根据需求随意切换压缩级别。  
**结果**：在 BEIR SciFact 上，最强模型在池化因子 1–6（即 83% 压缩率）下均超越未池化基线，做到无精度损失的压缩。轻量微调在所有池化设置下均优于仅推理时池化，且池化能力能跨方法、跨数据集迁移，为实际部署提供了低成本、高弹性的压缩方案。
