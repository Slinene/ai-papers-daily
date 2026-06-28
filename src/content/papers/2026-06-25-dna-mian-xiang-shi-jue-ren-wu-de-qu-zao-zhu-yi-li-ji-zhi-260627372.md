---
title: 'DnA: Denoising Attention for Visual Tasks'
title_zh: DnA：面向视觉任务的去噪注意力机制
authors:
- Ron Campos
- Subhajit Maity
- Xin Li
- Srijan Das
- Aritra Dutta
affiliations:
- University of Central Florida
- University of North Carolina at Charlotte
arxiv_id: '2606.27372'
url: https://arxiv.org/abs/2606.27372
pdf_url: https://arxiv.org/pdf/2606.27372
published: '2026-06-25'
collected: '2026-06-28'
category: Training
direction: 去噪注意力机制提升模型判别力
tags:
- denoising attention
- softmax
- vision transformer
- subspace separation
- image classification
- video understanding
one_liner: 通过正负查询分离与子空间排斥设计，消除softmax注意力中的噪声模式，提升ViT/B等视觉模型判别力。
practical_value: '- 用户行为序列（点击/购买）常含误触、偶然兴趣等噪声，可借鉴DnA的正/负query思想：设计正query提取目标意图，负query抑制干扰行为，提升序列建模质量。

  - 电商多模态场景（商品图片+文本）中，视觉注意力易被背景、无关细节干扰，可将DnA嵌入ViT backbone，增强物品表征的判别力。

  - 子空间分离增大主角的想法可迁移到embedding层：对不同属性的特征（如类目、品牌）学习相互正交的子空间，避免信息混杂，提升特征区分度。

  - 该方法轻量且即插即用，替换标准softmax无需大幅改动模型结构，适合快速验证能否抑制推荐模型中的注意力噪声问题。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：标准softmax注意力虽然能聚焦高得分位置，但对正负值处理不对称，容易产生噪声注意力图，稀释真正相关特征，尤其在视觉任务中导致判别力下降。
**方法**：提出Denoising Attention (DnA)，核心包含两个组件：1) 引入一对正/负query，正query负责定位正确类别的图像特征，负query识别语义相近但无关的特征；2) 将正负query与key的交互结果分别投影到两个相互正交程度尽可能高的子空间中（即最大化子空间主角），强制正、负特征表征分离，从而强化判别信号，抑制噪声。该模块可直接替换Transformer中的标准softmax多头注意力。
**结果**：以ViT-B为backbone，ImageNet-1K分类绝对提升0.8%；视频理解任务上，Video Transformer提升1.8%，Video-LLM提升0.5%；消融实验证实子空间分离与去噪设计的有效性。
