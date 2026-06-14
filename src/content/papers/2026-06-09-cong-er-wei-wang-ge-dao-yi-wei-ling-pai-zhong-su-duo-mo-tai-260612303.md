---
title: 'From 2D Grids to 1D Tokens: Reforming Shared Representations for Multimodal
  Image Fusion'
title_zh: 从二维网格到一维令牌：重塑多模态图像融合的共享表示
authors:
- Yuchen Xian
- Yunqiu Xu
- Yang He
- Yi Yang
affiliations:
- Zhejiang University
- National University of Singapore
- A*STAR (CFAR)
- A*STAR (IHPC)
arxiv_id: '2606.12303'
url: https://arxiv.org/abs/2606.12303
pdf_url: https://arxiv.org/pdf/2606.12303
published: '2026-06-09'
collected: '2026-06-14'
category: Other
direction: 多模态图像融合 · 1D token表示
tags:
- Multimodal Image Fusion
- Token Representation
- Selective Token Editing
- Image Tokenizer
- Shared Representation
one_liner: 用冻结图像分词器的1D token作为全局外观载体，结合2D局部路径，通过选择性令牌编辑轻量控制融合一致性。
practical_value: '- 论文用冻结的 VQ-VAE 类图像分词器将全局外观编码为少量 1D token，仅编辑关键 token 就能显著影响融合图像的色调、对比度等全局属性，这种“分离控制”的思路可以迁移到多模态商品图生成（如背景/光影切换）的轻量后处理模块。

  - Selective Token Editing 的稀疏更新策略（只替换 1–5% 的 token）是一种低成本的条件注入方式，类似 Idea 可应用于推荐场景中视觉特征的快速领域自适应（如换季风格迁移），避免全量微调。

  - 2D 与 1D 双路径并行的设计，为多智能体系统里“局部推理+全局规划”提供了一种具象化的架构参考：一个路径保留细粒度结构，另一个路径用 latent token
  进行高层控制，两者解耦但互补。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：多模态图像融合需要同时保持局部细节和全局外观一致性。传统方法在 2D 特征网格上构建共享表示，擅长局部建模但难以调控图像级的全局外观因素（如色调、亮度分布）。

**方法关键点**：
- 引入基于冻结预训练图像分词器（如 VQGAN）的 1D token 接口，将图像全局外观编码为少量离散 token，作为全局外观载体，与保留的 2D 空间路径形成“1D 全局 + 2D 局部”的双支路共享表示。
- 提出 Selective Token Editing (STE)：仅稀疏地更新或替换一小部分最关键的 token（< 5%），即能有效引导融合结果的全局一致性，无需训练额外损失或改变主骨干网络。
- 整个 fusion backbone 不受改动，1D token 路径通过一个简单的 token-to-map 接口（学习到的映射）注入 2D 特征空间，与局部细节图相加得到最终表示。

**关键结果**：在四个通用多模态融合基准上，方法在全局连贯性和局部保真度的多指标上均取得最优，且参数量增加极少，训练代价低。
