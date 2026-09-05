---
title: 'LLaDA-Image: Building Strong Image Generators with Fully Open Training Recipes'
title_zh: LLaDA-Image：全开放训练配方构建强大图像生成器
authors:
- Chuyan Chen
- Haoxing Chen
- Kun Chen
- Zhenglin Cheng
- Long Cui
- Ruishan Fang
- Zhangxuan Gu
- Zhicheng Huang
- Zhenzhong Lan
- Yuanting Lei
affiliations:
- AGI Research Center, Inclusion AI
arxiv_id: '2609.03796'
url: https://arxiv.org/abs/2609.03796
pdf_url: https://arxiv.org/pdf/2609.03796
published: '2026-09-02'
collected: '2026-09-05'
category: Multimodal
direction: 图像生成 · 开放训练配方
tags:
- Diffusion Transformer
- Image Generation
- Training Recipe
- Muon Optimizer
- RMSNorm
- Open Source
one_liner: 从零训练6B DiT图像生成模型，开源权重与代码，在Qwen-Image-Bench双榜达到开源SOTA
practical_value: '- 电商商品图/广告素材生成：可借鉴其 image-only pre-training 策略，先利用海量无标注商品图构建视觉生成先验，再做文本对齐，降低对配对图文数据的依赖。

  - 训练效率优化：parameter-free RMSNorm 搭配 Muon optimizer 替换 LayerNorm/Adam，可减少显存占用并提升大模型收敛稳定性，适合在自研
  DiT 或生成式推荐模型中试验。

  - 推理加速：TwinFlow 蒸馏至 2-4 步采样，可用于实时商品素材生成、Agent 内图像生成模块的低延迟部署。

  - 数据配方参考：220M 训练样本中 98% 为真实图像，说明高质量真实数据是生成质量的关键，电商可加强商品图质量治理并充分利用 UGC 素材。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**
现有开源图像生成模型很少公开完整训练流程与配方，导致从零复现强生成器困难。本文提供一套可复用的全套训练方案，目标是让设计权衡可检查、配方可复用。

**方法关键点**
模型采用 6B Diffusion Transformer（DiT）从零训练，视觉-语言理解模块基于 LLaDA2.0-Mini 扩散语言模型主干并冻结。训练先做 image-only pre-training 和 mid-training 建立视觉生成先验，再进入语言对齐与联合生成-编辑阶段。数据规模 220M 样本，其中 98% 为真实图像。优化上使用 parameter-free RMSNorm 贯穿 DiT，配合 Muon optimizer 提升效率与扩展性。进一步通过 TwinFlow 蒸馏得到 LLaDA-Image-Turbo，可在 2-4 步采样内快速推理。

**关键结果**
在 Qwen-Image-Bench 上，LLaDA-Image 英文与中文 track 总分分别为 53.53 和 53.38，均创开源模型新 SOTA。模型权重、训练代码与详细配方全部开放。
