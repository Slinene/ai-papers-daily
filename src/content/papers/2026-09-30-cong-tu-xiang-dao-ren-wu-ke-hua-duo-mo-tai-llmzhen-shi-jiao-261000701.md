---
title: 'From Images to Tasks: Characterizing Multimodal LLM Interactions in the Wild'
title_zh: 从图像到任务：刻画多模态LLM真实交互
authors:
- Jinyi Ye
- Scott Counts
- Gaurav Verma
- Kate Lytvynets
- Weiwei Yang
affiliations:
- University of Southern California
- Microsoft
- Microsoft Research
arxiv_id: '2610.00701'
url: https://arxiv.org/abs/2610.00701
pdf_url: https://arxiv.org/pdf/2610.00701
published: '2026-09-30'
collected: '2026-10-03'
category: Multimodal
direction: 多模态LLM真实任务分布分析
tags:
- Multimodal LLM
- User Behavior
- Benchmark
- Task Taxonomy
- Interaction Analysis
one_liner: 分析4万+图像上传对话，揭示多模态LLM真实任务分布及基准错位
practical_value: '- 用户上传图像的意图通常是复合的，如商品图+文字需求（找相似、鉴别、搭配建议），应在多模态助手中构建复合意图理解，而非单一分类。

  - 借鉴其分层能力框架（感知/认知/生成）作为埋点与监控维度，在拍照搜索或多模态客服中统计任务分布，指导模型迭代和资源分配。

  - 真实使用中生成类任务（根据图片生成文案、表格、代码）占比较高但公开基准覆盖不足，业务上应自建生成质量评测集，避免依赖通用 benchmark。

  - 跨模态 grounding 任务（如截图提取数据、图表转代码）在真实场景常见，可针对性加强 OCR+结构化理解+生成的能力链路。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

**动机**：多模态 LLM 日益普及，但用户在自然场景下上传图像的真实任务需求尚缺乏大规模实证分析。

**方法**：作者分析 Microsoft Copilot 中超过 40,000 个去标识化的图像上传对话，构建包含感知、认知、生成三大类共 10 种能力的分层任务框架；并将观察到的能力需求映射到 253 个现有基准，评估基准覆盖与真实使用的对齐程度；最后在独立的 ChatGPT 数据集上验证分类体系。

**关键结果**：
- 大多数图像上传任务涉及多种能力（如先识别再生成），复合性突出；
- 多模态使用场景比纯文本交互更广，出现依赖跨模态 grounding 的新任务类；
- 现有基准过度集中在感知与固定答案推理，而真实用户中常见的文本生成、代码生成、数据生成等工作流测试严重不足。
