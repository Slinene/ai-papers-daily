---
title: 'Persistent Identity Preservation in Generative Image Models: A Benchmark and
  Evaluation System'
title_zh: 生成图像模型中的持久身份保持：基准与评估系统
authors:
- Mengwei Ren
- Xuaner Zhang
- Zhihao Xia
affiliations:
- Phota Labs
arxiv_id: '2609.04151'
url: https://arxiv.org/abs/2609.04151
pdf_url: https://arxiv.org/pdf/2609.04151
published: '2026-09-03'
collected: '2026-09-06'
category: Eval
direction: 生成式图像身份保持基准与评估
tags:
- Identity Preservation
- Generative Image Models
- Benchmark
- Subject-driven Generation
- LoRA
- Persistent Identity
one_liner: 系统对比三种身份表示范式，证明持久身份层显著降低身份漂移且独立于基础模型
practical_value: '- 在电商商品图生成、虚拟试穿、广告素材合成中，商品/虚拟人身份一致性是核心痛点；可借鉴将主体身份作为独立的 persistent
  embedding 层，与基础生成模型解耦，替代每个主体一个 LoRA 的架构，既降低训练成本又支持跨模型复用。

  - 评估生成结果时不要只看 FID/CLIP 等整体质量指标，应专门构建身份保持压力测试：迭代编辑（模拟多轮对话修改）、小尺寸主体（远距离商品）、严重退化（用户上传低质量图）、多商品组合（bundle
  展示），否则身份漂移容易被掩盖。

  - 多主体组合场景中身份退化显著，直接用于广告多商品合成时建议为每个主体引入独立身份表示并显式组合，避免将多个主体简单塞进同一 prompt 或共享 LoRA。

  - 持久身份层与基础模型解耦的设计，与推荐系统中 embedding 表解耦思路一致，便于业务快速扩展大量 SKU/用户身份，并在更换或 A/B 测试不同生成基座时保持身份不变。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：生成图像模型在主体身份保持上仍不可靠，现有方法在身份表示位置上有根本不同选择——输入上下文（GPT-Image-2/NB2）、可训练参数（LoRA）、或持久身份层（Phota Identity），缺乏系统基准对比。

**方法关键点**：构建覆盖主体驱动生成、编辑、恢复、多主体设置的基准，任务逐步加大身份保持压力；对比三种范式的身份保真度、指令遵循与感知质量。

**关键结果**：身份保持是当前生成基础模型的独立局限，图像质量和指令遵循强并不意味着身份保真强；迭代编辑、小主体尺度、严重图像退化、多主体组合下身份退化更严重；持久身份层显著降低各场景下的身份漂移，在不同基础模型上均能提升身份保持，同时保持指令遵循和感知图像质量。结论：身份不会随模型规模增大自动涌现，应作为持久主体知识与基础模型独立组合。
