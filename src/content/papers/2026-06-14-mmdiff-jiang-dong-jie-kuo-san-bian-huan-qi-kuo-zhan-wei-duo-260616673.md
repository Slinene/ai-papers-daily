---
title: 'MMDiff: Extending Diffusion Transformers for Multi-Modal Generation'
title_zh: MMDiff：将冻结扩散变换器扩展为多模态生成系统
authors:
- Yagmur Akarken
- Orest Kupyn
- Christian Rupprecht
affiliations:
- University of Oxford, Visual Geometry Group
arxiv_id: '2606.16673'
url: https://arxiv.org/abs/2606.16673
pdf_url: https://arxiv.org/pdf/2606.16673
published: '2026-06-14'
collected: '2026-06-17'
category: Multimodal
direction: 生成式模型多模态解码·扩散特征复用
tags:
- Diffusion Transformer
- Multi-modal Generation
- Feature Fusion
- Perceptual Decoding
- Frozen Backbone
- Lightweight Decoder
one_liner: 冻结扩散变换器，通过多时间步特征融合与轻量解码头，同时生成图像及密集感知模态
practical_value: '- **冻结大模型 + 轻量任务头**：可借鉴到推荐系统的多目标学习或内容理解，冻结预训练 LLM/生成式模型，仅训练极少量参数的任务头，大幅降低训练成本，快速产出多模态信号（如物品描述、属性标签、质量分）。

  - **多时间步特征融合**：在推荐或 Agent 场景中，若干任务需要序列或推理步骤的中间状态，可类似地融合不同阶段的隐状态，例如在会话推断中融合多步推理的中间表示，提升预测准确性。

  - **注意力引导的可解释性**：概念驱动的注意力提取可用于生成可解释的推荐理由或搜索解释，通过在生成式推荐模型中提取与特定概念对应的注意力图，提高对用户的理解。

  - **大规模合成数据生成**：在电商商品配图、广告创意图生成中，可利用此类方法同时产出商品分割图、景深图等多模态标注，低成本构造训练数据，提升下游模型性能。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：扩散变换器在生成图像时，其丰富的中间感知表征在渲染完成后即被丢弃，然而这些表征包含语义、几何等密集信息，可被复用。已有方法仅在单时间步提取特征，未能利用扩散过程中时间维度上分布的信息。

**方法关键点**：
- **冻结骨干**：冻结预训练扩散变换器（DiT），不改动任何参数。
- **多时间步特征融合**：从去噪轨迹的多个时间步提取中间特征，使用空间变化的可学习权重进行融合，捕获全局感知信息。
- **轻量解码头**：针对语义分割、显著性检测、深度估计分别设计浅层解码头，直接预测稠密输出。
- **概念驱动注意力提取**：利用跨注意力图提供可解释的空间引导，增强可控性。

**关键结果**：
- 多时间步融合带来显著提升，语义分割 mIoU 相比单时间步提取最高提升 28.7%。
- 冻结的扩散特征与 SOTA 编码器（如 DINOv3）表现相当且互补。
- 仅训练轻量解码头即达到强性能，适用于大规模合成数据生成。
