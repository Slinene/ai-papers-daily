---
title: Second-Order Multi-Level Variance Correction for Modality Competition in Multimodal
  Models
title_zh: 多模态模型中模态竞争的二阶多层级方差校正
authors:
- Yishun Lu
- Wes Armour
affiliations:
- University of Oxford
arxiv_id: '2605.16165'
url: https://arxiv.org/abs/2605.16165
pdf_url: https://arxiv.org/pdf/2605.16165
published: '2026-05-15'
collected: '2026-05-18'
category: Training
direction: 多模态训练优化 · 二阶方差校正
tags:
- Multimodal Training
- Second-Order Optimization
- Modality Competition
- Variance Correction
- SOAP
- Large Batch
one_liner: 提出ML-FOP-SOAP，通过Fisher正交投影和层级方差校正抑制模态冲突，稳定大batch训练并提速
practical_value: '- 电商多模态模型（商品图文联合训练）可替换AdamW为ML-FOP-SOAP，缓解视觉生成与文本理解间的梯度冲突，提升训练稳定性与样本效率（1.4×）。

  - 层级折叠策略降低梯度累积时二阶统计量的微步开销，适合大规模分布式训练中通信受限的场景，可直接复用于类似EMA方差跟踪的工程实现。

  - 该方法在batch size 8192下仍能稳定训练，对需要大batch加速预训练的业务有直接价值，可尝试引入到现有大模型训练框架中。

  - Fisher正交投影的模态解耦思想可推广至多任务或推荐系统中的多目标优化，通过正交化投影抑制不同目标间的梯度干扰。'
score: 7
source: arxiv-cs.CV
depth: abstract
---

多模态自回归训练（统一图文生成与理解）存在严重的模态竞争，导致优化不稳定且难以扩展大batch。现有方案多从架构或损失权重入手，本文则从优化器角度出发，提出ML-FOP-SOAP框架。

关键方法：以二阶优化SOAP为基础，引入Fisher正交投影，将梯度投影到各模态方差的正交补空间，显式抑制方差驱动的模态冲突；同时设计多层级方差校正，通过层级折叠策略在梯度累积中低开销捕获细粒度方差，使二阶预条件更精确。

在Janus和Emu3两个多模态模型上，视觉生成与文本理解指标均有提升，batch size 8192下训练稳定。相比AdamW，样本效率最高提升1.4倍，墙钟训练加速最高1.5倍。
