---
title: 'Few Channels Draw The Whole Picture: Revealing Massive Activations in Diffusion
  Transformers'
title_zh: 少数通道描绘全貌：揭示扩散Transformer中的大规模激活
authors:
- Evelyn Turri
- Davide Bucciarelli
- Sara Sarto
- Lorenzo Baraldi
- Marcella Cornia
affiliations:
- University of Modena and Reggio Emilia, Italy
- University of Pisa, Italy
arxiv_id: '2605.13974'
url: https://arxiv.org/abs/2605.13974
pdf_url: https://arxiv.org/pdf/2605.13974
published: '2026-05-13'
collected: '2026-05-17'
category: Multimodal
direction: 扩散Transformer · 大规模激活语义分析
tags:
- Diffusion Transformers
- Massive Activations
- Text-to-Image Generation
- Semantic Control
- Feature Interpretation
- Activation Sparsity
one_liner: 扩散Transformer中极稀疏的大规模激活通道是语义信息的载体，控制生成质量、空间布局并支持无训练的语义迁移
practical_value: '- 在电商商品图生成中，可定位大规模激活通道，通过替换这些通道的值实现细粒度属性控制（如颜色、材质、风格），无需重训模型。

  - 生成式推荐场景下，将用户/物品描述作为文本条件，利用大规模激活通道的迁移性，生成跨语义的个性化插值图像或推荐解释。

  - 推理加速：发现仅极少数通道起决定性作用，可设计稀疏计算策略，在推理时跳过低贡献通道，显著降低计算量。

  - 对于Agent系统中的视觉生成模块，借鉴该机制可实现zero-shot的语义技能迁移，即保留画面结构但改变语义内容，增强多模态交互灵活性。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：扩散Transformer（DiT）已成为最强文本到图像生成模型，但其内部如何根据文本控制语义仍不清晰。本文研究一种现象：隐藏状态中存在少量通道响应极大（大规模激活），旨在揭示这些异常值是否承载关键语义信息。

**方法**：在FLUX等DiT模型上，通过三个角度分析大规模激活通道：1）**功能关键性**：消融实验，零化大规模通道（约占通道数1%）导致生成质量急剧崩溃，而零化等量低响应通道几乎无影响；2）**空间组织性**：将图像token仅在大规模通道上聚类，得到的区域与主体和显著物体高度吻合，表明这些通道编码空间语义；3）**可迁移性**：将一个文本条件下生成轨迹中的大规模激活注入另一轨迹，结果图像在保留目标结构的同时趋向源提示语义，实现无训练的语义插值。进一步提出文本条件和图像条件语义传输，前者支持提示插值，后者实现主题驱动生成。

**关键结果**：大规模激活通道虽稀疏但不可或缺，它们形成了一种稀疏的、受提示条件控制的载体子空间，组织并控制DiT中的语义信息。
