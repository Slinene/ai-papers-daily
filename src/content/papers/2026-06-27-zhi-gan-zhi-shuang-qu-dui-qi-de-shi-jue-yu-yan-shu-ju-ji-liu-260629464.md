---
title: Rank-Aware Hyperbolic Alignment for Vision-Language Dataset Distillation
title_zh: 秩感知双曲对齐的视觉语言数据集蒸馏
authors:
- Jongoh Jeong
- Sun-Kyung Lee
- Kuk-Jin Yoon
affiliations:
- Korea Advanced Institute of Science and Technology (KAIST)
- Electronics and Telecommunications Research Institute (ETRI)
arxiv_id: '2606.29464'
url: https://arxiv.org/abs/2606.29464
pdf_url: https://arxiv.org/pdf/2606.29464
published: '2026-06-27'
collected: '2026-07-04'
category: Training
direction: 多模态数据集蒸馏 · 双曲对齐与低秩控制
tags:
- dataset distillation
- vision-language
- hyperbolic geometry
- low-rank alignment
- cross-modal retrieval
- contrastive learning
one_liner: 在双曲空间中对齐低秩共享语义并正则化残差子空间，提升多模态蒸馏的检索与迁移鲁棒性
practical_value: '- 电商图文推荐的数据压缩：商品图与描述常呈低秩关联，RAHA 的双曲共享范围对齐与残差正则化可分离核心语义与噪声，用于构建紧凑的蒸馏训练集，降低训练成本。

  - 多模态对齐中的鲁棒性提升：非对称测地线目标可避免强制全维对齐造成的过约束，适合图文匹配任务（如搜索广告素材优选）中对模态私有特征的保留。

  - 联邦学习或隐私受限场景：借鉴蒸馏思想，用少量合成的代表点替代原始数据参与分布式训练，RAHA 的秩感知控制可保证下游模型泛化。

  - 主要适用学术研究，业务迁移需额外适配双曲网络层与矩阵分解的工程实现，短期收益待验证。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：视觉语言数据集蒸馏（VLDD）将大规模图文对压缩为少量合成对以高效训练对比模型。现有方法在欧氏空间强对齐，忽略图文相关性的秩缺陷——共享语义集中在低维子空间，残余维度包含弱相关信息。LoRS 虽用低秩分解松弛对齐，但未显式控制表征空间中的对齐容量与结构。

**方法**：提出秩感知双曲对齐（RAHA），将多模态表征映射到双曲空间以捕捉层次语义，然后将空间分解为共享范围与残差子空间。对共享范围施加测地线对齐损失以保留核心语义，对残差子空间施加正则化以保持模态特有信息。采用非对称目标优化合成图文对，显式控制对齐容量。

**结果**：在多个 VLDD 基准上，固定蒸馏预算下 RAHA 取得有竞争力的跨模态检索性能，并在下游迁移任务中表现出更好的鲁棒性指标。
