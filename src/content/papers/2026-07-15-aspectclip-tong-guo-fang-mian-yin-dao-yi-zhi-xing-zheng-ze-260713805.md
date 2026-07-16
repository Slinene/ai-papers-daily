---
title: 'AspectCLIP: Optimizing CLIP Representation Space via Aspect-Guided Consistency
  Regularization'
title_zh: AspectCLIP：通过方面引导一致性正则化优化CLIP表示空间
authors:
- Yiyang Yao
- Shanglin Liu
- Jianming Lv
- Chengjun Wang
- Jinyi Li
- Yuchan Jie
- Zhihua Jin
affiliations:
- South China University of Technology
arxiv_id: '2607.13805'
url: https://arxiv.org/abs/2607.13805
pdf_url: https://arxiv.org/pdf/2607.13805
published: '2026-07-15'
collected: '2026-07-16'
category: Multimodal
direction: 多模态预训练 · 方面感知对齐
tags:
- CLIP
- Consistency Regularization
- Image-Text Mismatch
- Attribute Clustering
- Representation Space
one_liner: 提出方面引导的一致性正则化，解决图像-文本对信息不对称导致的全局对齐扭曲
practical_value: '- 电商商品图文理解中，图片多属性而标题片面，可借鉴按文本属性聚类，簇内严格对齐、簇间原型对齐，提升多模态检索与推荐的语义一致性

  - 循环一致性策略可用于商品图像-文本-图像的自监督增强，自动挖掘细粒度正负样本，提高表示鲁棒性

  - 广告创意或Agent多模态调用时，采用方面感知表示，避免文本描述片面导致的语义误解，支持基于图像不同方面生成多样化文案

  - 工程实现容易集成：属性聚类可用轻量文本编码器在线完成，循环一致性损失可直接插入现有对比学习框架，计算开销小'
score: 7
source: arxiv-cs.CV
depth: abstract
---

**动机**：CLIP类方法使用全局一致性正则化，忽略图像与文本之间的信息不对称——文本通常只描述图像的单一属性，导致视觉相似但文本描述不同的样本被错误拉近，污染表示空间。

**方法**：AspectCLIP将训练样本依据文本相似度划分为属性簇，在簇内施加完整的图像↔文本↔图像循环一致性，强制同一方面严格对齐；跨簇仅进行原型级比较，避免将不同方面的表示强行拉近。这种方面引导的正则化在共享方面上实现紧致几何结构，在分歧方面上保留灵活性。

**结果**：多个下游基准上一致超越传统CLIP变体，学得语义更结构化的表示空间，显著缓解了全局对齐带来的扭曲问题。
