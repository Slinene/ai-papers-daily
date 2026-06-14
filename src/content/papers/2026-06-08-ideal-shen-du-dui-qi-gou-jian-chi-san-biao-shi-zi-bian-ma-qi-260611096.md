---
title: 'IDEAL: In-DEpth ALignment Makes A Discrete Representation AutoEncoder'
title_zh: IDEAL：深度对齐构建离散表示自编码器
authors:
- Yitong Chen
- Zijie Diao
- Junke Wang
- Lingyu Kong
- Yixuan Ren
- Bo He
- Yu-Gang Jiang
- Zuxuan Wu
affiliations:
- Fudan University
- Shanghai Innovation Institute
- University of Maryland, College Park
arxiv_id: '2606.11096'
url: https://arxiv.org/abs/2606.11096
pdf_url: https://arxiv.org/pdf/2606.11096
published: '2026-06-08'
collected: '2026-06-14'
category: Multimodal
direction: 视觉生成 · 离散表示对齐
tags:
- Discrete Representation
- Autoencoder
- Vision Foundation Model
- Image Generation
- Feature Alignment
one_liner: 联合对齐浅层与深层视觉特征，使离散视觉标记兼顾保真度与语义，重建与生成双SOTA
practical_value: '- **离散 token 学习借鉴**：若在电商多模态推荐中学习物品的离散 Semantic ID，可引入浅层视觉特征（局部纹理、布局）与高层语义联合对齐，提升视觉
  token 的重建保真度，有助于生成式推荐中 ID 的语义保持。

  - **多层级特征融合范式**：训练视觉 tokenizer 时，利用冻结的预训练视觉模型（如 DINO）提取多层特征，通过深度对齐损失强化 token 的表征能力，该思路可迁移至任何需要离散化视觉输入的推荐或搜索任务。

  - **生成式推荐中视觉生成优化**：若需在 Agent 或推荐流程中根据语义生成商品图像，IDEAL 的 tokenizer 可直接作为图像离散生成的前置工具，提升生成图像细节与语义一致性。

  - 主要贡献在视觉生成领域，存在一定学术借鉴价值，但业务落地需二次适配。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有基于预训练视觉基础模型（VFM）的表示自编码器（RAE）在图像生成中重建质量不理想，深层 VFM 特征缺乏细粒度视觉细节，离散化后损失更严重。观察到浅层 VFM 特征保留丰富的局部外观和结构信息，与深层特征的高层语义互补。

**方法**：提出 IDEAL（In-Depth Alignment），将图像编码为离散 token 后，同时对齐浅层与深层 VFM 特征，通过联合损失使 token 既保持视觉保真度又捕获语义，无需额外解码器设计。

**效果**：在 ImageNet 256x256 上，IDEAL 的重建 rFID 达到 0.61，相较此前最佳方法提升 0.28；在自回归图像生成中，gFID 为 1.89，刷新 SOTA。
