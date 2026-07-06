---
title: 'Learning to Compose: Revisiting Proxy Task Design for Zero-Shot Composed Image
  Retrieval'
title_zh: 重新审视零样本组合图像检索的代理任务设计
authors:
- Jingjing Zhang
- Lei Zhang
- Zheren Fu
- Zhendong Mao
affiliations:
- University of Science and Technology of China
arxiv_id: '2607.00374'
url: https://arxiv.org/abs/2607.00374
pdf_url: https://arxiv.org/pdf/2607.00374
published: '2026-07-01'
collected: '2026-07-06'
category: Multimodal
direction: 零样本组合图像检索 · 代理任务学习
tags:
- Zero-Shot CIR
- Proxy Task
- Multimodal Retrieval
- Vision-Language
- FoCo
one_liner: 提出可学习的二阶段组合模型FoCo，通过文本锚定视觉聚合与上下文补全代理任务，无需三元组监督即达SOTA
practical_value: '- 电商以图搜稿/找同款场景可直接复用：用图片+文字修改（如“袖子更长”）搜索商品，无需昂贵三元组标注，仅靠图像-文本对即可训练组合编码器。

  - 两个代理任务可迁移到多模态搜索模型训练：文本锚定的视觉聚合（让模型学会关注修改相关区域）和上下文补全（保留场景上下文避免语义丢失），能提升模型对细粒度修改的敏感度。

  - 跨实例对比目标（cross-instance contrastive）有意引入类别内变异作为负例，可借鉴到商品搜索中防止模型走捷径（如只靠图片相似度忽略文本修改），让模型更关注文字指令。

  - 整体框架与现有预训练视觉-语言模型（如CLIP）兼容，适合作为轻量插件嵌入现有检索系统，无需重建索引或修改推理流程。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

动机：零样本组合图像检索（ZS-CIR）通过代理任务免去昂贵三元组标注，但现有方法仅增强特征表示以适应预定义的组合方式（如伪词注入或特征代数），组合函数本身未学习，导致难以处理多样、细粒度的语义修改。

方法：提出 FoCo（Focus-then-Complete），将组合过程分为“聚焦修改相关视觉内容”和“补全目标语义”两个阶段。设计两个代理任务：1) **文本锚定的视觉聚合**，利用局部文本语义引导模型从参考图像中选择性地聚合与修改相关的视觉信息；2) **上下文条件的语义补全**，把聚合后的视觉特征与场景上下文融合，生成连贯的组合表示。训练时采用跨实例对比学习，迫使组合表示与目标图像拉近，同时与同批次其他实例的组合表示推远，防止模型利用简单视觉相似性走捷径。

结果：在四个 ZS-CIR 基准（FashionIQ、CIRR、CIRCO、GeneCIS）上取得最优性能，尤其在需要复杂语义组合的测试中优势明显，展现出更强的泛化能力。
