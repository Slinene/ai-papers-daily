---
title: 'HiDream-O1-Image: A Natively Unified Image Generative Foundation Model with
  Pixel-level Unified Transformer'
title_zh: 'HiDream-O1-Image: 像素级统一Transformer的原生多模态图像生成基础模型'
authors:
- Qi Cai
- Jingwen Chen
- Chengmin Gao
- Zijian Gong
- Yehao Li
- Yingwei Pan
- Yi Peng
- Zhaofan Qiu
- Kai Yu
- Yiheng Zhang
affiliations:
- HiDream.ai
arxiv_id: '2605.11061'
url: https://arxiv.org/abs/2605.11061
pdf_url: https://arxiv.org/pdf/2605.11061
published: '2026-05-11'
collected: '2026-05-17'
category: Multimodal
direction: 像素级统一Transformer的图像生成范式
tags:
- Diffusion Transformer
- Unified Architecture
- Pixel-space Generation
- Multimodal
- In-context Generation
- Scalable Foundation Model
one_liner: 通过像素空间扩散Transformer，消除VAE与独立文本编码器，实现多模态原生统一生成，8B参数媲美27B模型并可扩展至200B+
practical_value: '- 统一token空间设计消除了独立VAE和文本编码器，大幅简化多模态生成pipeline，在电商商品图生成中可降低工程复杂度与延迟。

  - In-context编辑与个性化能力可直接用于商品图片的指令式修改（如背景替换、文案添加），实现快速营销素材生成。

  - 200B+规模的扩展性验证了架构的工业可行性，适合作为商品视觉内容生成与编辑的统一基座模型。

  - 将文本、像素、条件统一视为token进行推理的思路，可迁移至多模态推荐或Agent系统，用单一Transformer统一处理异构输入。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

动机：当前视觉生成模型多依赖独立的VAE和预训练文本编码器，架构碎片化、难以扩展。HiDream-O1-Image旨在通过原生统一的设计消除这些分离模块。

方法：模型采用像素空间扩散Transformer，将原始图像像素、文本token和任务条件映射到共享token空间，利用统一Transformer (UiT) 架构直接在像素层面进行多模态融合与去噪生成。这种原生编码范式无需额外VAE或文本编码器，并将文生图、指令编辑、主体个性化等任务统一为上下文推理过程。数据上通过精心构建的多来源数据集和提示工程进行训练。

结果：仅8B参数的版本在文本到图像生成、编辑、个性化等多种任务上达到或超越27B的Qwen-Image等SOTA模型。进一步缩放至200B+参数的Pro版本展现出前所未有的生成能力，在多个基准上建立了新的最优结果，验证了该架构的超强可扩展性。
