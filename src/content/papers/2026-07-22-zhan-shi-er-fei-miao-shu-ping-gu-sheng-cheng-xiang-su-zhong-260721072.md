---
title: 'Show, Don''t Tell: Evaluating Spatial Cognition in Generative Pixels Rather
  Than LLM Text'
title_zh: 展示而非描述：评估生成像素中的空间认知而非LLM文本
authors:
- Xu Wang
- Kaixiang Yao
- Miao Pan
- Xiaohe Zhou
- Xuanyu Liu
- Wenqi Zhang
- Xuhong Zhang
affiliations:
- Zhejiang University
arxiv_id: '2607.21072'
url: https://arxiv.org/abs/2607.21072
pdf_url: https://arxiv.org/pdf/2607.21072
published: '2026-07-22'
collected: '2026-07-28'
category: Eval
direction: 空间推理评测框架 · 生成式像素评估
tags:
- spatial reasoning
- image generation
- visual evaluation
- benchmark
- agentic protocol
- multimodal
one_liner: 提出ProVisE框架，将图像生成模型的视觉答案解析为结构化预测，实现像素级空间推理的公平评测
practical_value: '- 对电商中需要空间理解的生成任务（如虚拟试穿、商品摆放、AR场景）有评测启发：可借鉴“协议化视觉答案”思想，将模型生成的图像通过规则解析成结构化指标（如物品位置、遮挡关系），从而量化评估生成质量。

  - Agentic protocol builder 能自动为新任务生成评测协议，可迁移到广告创意生成、商品主图优化等场景，降低人工设计评测规则的成本。

  - 揭示了文本推理与像素表达的互补性，在推荐系统多模态交互（如对话式推荐+视觉展示）中，可结合文本VLMs做高层推理、图像生成模型做像素级细粒度表达。

  - 整体方法论对构建统一的多模态推荐评测基准有参考价值，但直接业务应用场景有限，更适合学术评测框架设计。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**  
现有空间推理基准要求模型输出坐标、选项或文本描述，这对擅长在像素空间直接标注位置、区域、路径的图像生成模型形成“答案接口不匹配”，导致其能力被低估。同时，真实世界空间交互更自然的方式是绘图而非报坐标。因此需要一种统一框架，让图像生成模型也能参与同类任务评测。

**方法**  
提出 ProVisE（Protocolized Visual Evaluation）框架，通过定义任务特定的“视觉协议”（如画箭头、打点、绘框），强制图像生成模型以受约束的视觉方式作答，再经解析模块将生成图像中的视觉元素映射回结构化预测，完全兼容原有评价指标。框架内建的 Agentic builder 能自动为新基准构造并验证协议。基于此，构建了诊断性基准 SpatialGen-Bench，包含 14 个子任务、4 个能力层级、470 个样本，覆盖定位、区域判别、路径规划等。

**关键结果**  
在统一设置下比较文本输出 VLMs 和图像生成模型，发现：图像生成模型在可直接用像素表达的任务上性能颇具竞争力，尤其在需要精确空间定位和细粒度区域标注时；但文本输出 VLMs 在组合空间推理上仍有明显优势。将 Agentic 协议构建推广到 6 个外部空间基准，验证了框架的通用性。结论表明像素空间表达与文本推理存在互补优势，为图像生成模型的空间认知研究提供了度量兼容的测试平台。
