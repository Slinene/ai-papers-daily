---
title: 'DecQ: Detail-Condensing Queries for Enhanced Reconstruction and Generation
  in Representation Autoencoders'
title_zh: DecQ：细节压缩查询增强表示自编码器的重建与生成
authors:
- Tianhang Wang
- Yitong Chen
- Wei Song
- Zuxuan Wu
- Min Li
- Jiaqi Wang
affiliations:
- Zhejiang University
- Shanghai Innovation Institute
- Fudan University
- Westlake University
- JD.COM
arxiv_id: '2605.22777'
url: https://arxiv.org/abs/2605.22777
pdf_url: https://arxiv.org/pdf/2605.22777
published: '2026-05-20'
collected: '2026-05-24'
category: Training
direction: 视觉表示自编码器 · 细节压缩查询
tags:
- Representation Autoencoder
- Detail-Condensing Queries
- Reconstruction-Generation Trade-off
- Vision Foundation Model
- Feature Condensation
- Latent Diffusion Model
one_liner: 引入轻量细节压缩查询，从冻结视觉基础模型中间层提取细粒度信息，显著提升重建PSNR与生成FID，收敛加速3.3倍
practical_value: '- 推荐系统使用冻结预训练模型作为编码器时，可插入类似detail-condensing queries的可学习模块，从中间层提取细节，既保持语义空间稳定又缓解细节丢失，仅增加极低计算开销。

  - 生成式推荐中的tokenizer（如Semantic ID的VAE）常面临重建质量与生成保真度的权衡，参考DecQ在解码侧加入轻量细节查询，可同时提升重建精度和下游生成质量。

  - 方法收敛速度3.3倍提升，适合工业界快速迭代实验，尤其在大规模商品图像或内容表征学习场景。

  - 对待不同层级特征的聚合方式（浅层细节+深层语义）可迁移至多模态推荐模型的特征融合，增强商品细节理解能力。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：表示自编码器（RAE）使用冻结视觉基础模型（如DINOv2）作为编码器，虽能加速扩散模型收敛，但冻结约束了空间重建能力，影响细粒度生成和图像编辑；微调则会破坏预训练语义空间，降低生成保真度。如何平衡重建与生成是核心挑战。

**方法关键**：提出DecQ，引入少量可学习的**细节压缩查询**（detail-condensing queries），配合**冷凝器**模块从VFM中间层特征中提取细粒度信息。这些查询与patch tokens一同输入解码器支持重建，并在扩散生成时联合预测。通过门控机制融合浅层细节和深层语义，有效缓解重建-生成权衡。

**关键结果**：仅增加8个查询、3.9%计算量，PSNR从19.13dB提升至22.76dB；生成建模收敛速度提升3.3倍，无引导FID 1.41，有引导FID 1.05，均显著优于基线RAE。
