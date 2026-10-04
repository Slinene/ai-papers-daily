---
title: 'Where-OPD: Spatially Guided On-Policy Self-Distillation of MLLMs with Synthetic
  Scenes'
title_zh: Where-OPD：合成场景下空间引导的 MLLM 在线自蒸馏
authors:
- Sophia Sirko-Galouchenko
- Monika Wysoczanska
- Andrei Bursuc
- Nicolas Thome
- Spyros Gidaris
affiliations:
- Valeo.ai
- Sorbonne Université, CNRS, ISIR
- Institut universitaire de France (IUF)
- ILLS, CNRS, Montreal
arxiv_id: '2610.02117'
url: https://arxiv.org/abs/2610.02117
pdf_url: https://arxiv.org/pdf/2610.02117
published: '2026-09-30'
collected: '2026-10-04'
category: Multimodal
direction: 多模态自蒸馏 · 空间感知提升
tags:
- On-policy self-distillation
- Spatial guidance
- MLLM
- Synthetic data
- Visual perception
- Self-training
one_liner: 提出用文本空间引导作为特权信息，通过在线策略自蒸馏提升 MLLM 空间感知，合成训练可迁移真实基准
practical_value: '- 电商/商品视觉问答：可用程序化生成商品布局图、货架图或广告素材，自动获得物体身份与坐标，构造带空间提示（如『在 (x,y)
  附近发现绿色标签』）的 QA 数据做自蒸馏，提升模型对商品计数、空间关系（前后/遮挡/相邻）和属性识别，无需人工标注。

  - 文档/图表理解：对详情页、数据报表、广告资质图生成合成文档并注入 layout 坐标信息，蒸馏出能定位关键区域并整合多区域证据的学生模型，可用于 RAG 中的视觉证据定位、广告合规审核和图表指标抽取。

  - 推理成本不增加：教师仅在训练时使用空间 hint，学生推理时只依赖图像和问题，适合与 LoRA/Adapter 结合部署；且 on-policy self-distillation
  无需外部大模型或人工标注，工程接入成本低。

  - 合成到真实迁移结论：该工作验证了合成场景训练可提升真实感知基准（平均 +3.23 点），可作为低成本增强长尾视觉任务（如稀有商品、复杂陈列）的先验，但需注意合成场景的分布覆盖范围。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：MLLM 在细粒度视觉感知（计数、文档/图表理解）上仍较弱；现有改进方案通常依赖图像裁剪特权信息，收益局限于需要 zoom 的任务，且需要人工标注 grounding 数据或外部教师模型。

**方法关键点**：
- 采用 on-policy self-distillation，教师为 frozen/EMA 版本，接收文本形式的、与 query 相关的空间引导信息（如物体身份和坐标），定位并整合多个相关图像区域证据。
- 训练数据使用程序化生成的合成场景，自动获得物体身份与空间坐标，实现 scalable、annotation-free 的后训练。
- 学生仅从图像和问题中学习模仿教师行为，推理时无额外视觉分支或裁剪。

**关键结果**：
- 在 counting、document 和 chart understanding 基准上多模型（不同 MLLM）稳定提升。
- 仅用合成场景后训练，迁移到真实感知基准 CVBench、V*、ZoomBench、BLINK、HR-Bench、MME-RealWorld，平均性能提升 3.23 点。
- 说明空间引导特权信息可通过自蒸馏激发更广泛的感知能力，实现明显的合成到真实迁移。
