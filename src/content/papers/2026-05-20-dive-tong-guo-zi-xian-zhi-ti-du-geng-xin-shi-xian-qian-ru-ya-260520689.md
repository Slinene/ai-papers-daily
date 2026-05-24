---
title: 'DIVE: Embedding Compression via Self-Limiting Gradient Updates'
title_zh: DIVE：通过自限制梯度更新实现嵌入压缩
authors:
- Dongfang Zhao
affiliations:
- University of Washington Tacoma
arxiv_id: '2605.20689'
url: https://arxiv.org/abs/2605.20689
pdf_url: https://arxiv.org/pdf/2605.20689
published: '2026-05-20'
collected: '2026-05-24'
category: RecSys
direction: 嵌入压缩 · 自限制梯度更新
tags:
- embedding compression
- dimensionality reduction
- triplet loss
- contrastive learning
- adapter
- retrieval
one_liner: 通过自限制 hinge triplet 损失和多头对比学习，在小样本下稳定压缩高维嵌入，全面超越现有适配器
practical_value: '- 小样本场景下微调嵌入压缩模型常过拟合，可借鉴自限制 hinge triplet loss：一旦 triplet 满足 margin
  约束即停止梯度，安全地限制对预训练空间的扰动，稳定训练过程。

  - 利用多头投影构造隐式视角，对每个嵌入计算 NT-Xent 对比损失，为稀疏的 triplet 信号提供密集的自监督梯度。在推荐系统标注数据稀少时，此技巧能显著提升压缩表示质量。

  - 采用轻量 residual adapter 实现维度压缩（仅 14M 参数），无需改动预训练 LLM 骨干，可直接嵌入线上向量检索链路，降低存储与计算成本。

  - 在电商搜索或推荐中，当需要将高维商品/用户 embedding 压缩以加速检索时，DIVE 的损失设计可作为微调范式，避免压缩比例增大时性能断崖下跌。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**  
LLM 生成的高维 embedding 给向量检索系统带来巨大存储与计算压力。现有基于 adapter 的压缩方法（如 Matryoshka-Adaptor、Search-Adaptor）在标注数据稀缺时严重过拟合，检索性能甚至低于冻结的基线模型。  
**方法**  
DIVE 提出两个互补机制：① 自限制 hinge‑based triplet loss——当 triplet 已达到 margin 约束时损失为零、梯度停止，从而严格控制对预训练空间的扰动幅度；② 多头隐式视角集成——用多个可学习投影将每个嵌入映射到不同头，再在头间计算 NT‑Xent 对比损失，相当于为每个样本构造多个自监督视角，用密集的对比信号补偿稀疏 triplet 损失在小数据集上的梯度不足。整体采用冻结 LLM 骨干 + 轻量 residual adapter 的架构。  
**关键结果**  
在六个 BEIR 数据集上，DIVE 在所有数据集和所有压缩比（最高压缩至原维度 1/32）下均超越 Matryoshka‑Adaptor、Search‑Adaptor 和 SMEC，且开源实现仅 14M 参数。尤其在低压缩比时优势更显著，验证了自限制与隐式视角集成对小样本鲁棒性的提升。
