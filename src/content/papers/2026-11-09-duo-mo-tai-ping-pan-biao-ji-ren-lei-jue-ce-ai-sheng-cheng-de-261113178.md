---
title: 'Multimodal Judges Flag, Humans Decide: A Review-and-Edit Framework for AI-Generated
  Product Video Ads'
title_zh: 多模态评判标记，人类决策：AI 生成产品视频广告的审阅-编辑框架
authors:
- Anoubhav Agarwaal
- Sukesh Perla
- Karthikeyan Mohanraj
- Susmita Ghose
affiliations:
- Anoki Inc.
arxiv_id: '2611.13178'
url: https://arxiv.org/abs/2611.13178
pdf_url: https://arxiv.org/pdf/2611.13178
published: '2026-11-09'
collected: '2026-11-11'
category: Eval
direction: 多模态评判 · 人机协同审阅
tags:
- Multimodal Judges
- Human-in-the-loop
- Video Ad Review
- E-commerce
- Vision-Language Models
- Evaluation
one_liner: 用多模态 AI judge 高召回标记问题、人类审阅者决策与补充，形成可扩展的电商视频广告审阅-编辑闭环
practical_value: '- 将生成内容质量评估拆成六个独立轴（产品、场景质量、发音、脚本、声音、字幕），每个轴绑定对应模型 judge，并把 finding
  绑定到具体位置（scene/line/whole ad），使 review 和 edit 可路由、可操作；电商生成式广告/短视频素材审核可直接复用这种结构与路由。

  - AI judge 调高召回，人类做决策：模型 judge 宁可误报也要捕获几乎所有缺陷，人类 reviewer 接受/拒绝每条 finding 并补充遗漏，形成“AI
  flag, human decide”；在业务审核流水线中避免漏检，同时控制误报成本。

  - 盲测显示有 judge findings 时 reviewer 标记缺陷比例从 19% 提升到 57%，说明模型 pre-annotation 能显著提高人工审核敏感度、防止审阅疲劳；可将多模态预标注作为人审
  UI 标配。

  - 六轴问题和 finding-to-fix 路由与具体生成模型解耦，生成模型更换时审核流程不变；工程上可沉淀为独立 review portal 模板，迁移到不同生成管线。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

**动机**：生成式流水线可为电商目录每个产品生成短视频广告，但判断广告是否可用不是简单好坏，需要细粒度审阅和编辑，且审阅编辑速度要跟上生成速度。

**方法关键点**：提出 review-and-edit 框架：reviewer 逐场景回答六个问题（产品、场景质量、发音、脚本、声音、字幕）；judges 基于视觉语言、语音和语言模型将发现归档到对应问题，reviewer 接受/拒绝每条 finding 并补充遗漏；确认问题后打开匹配的编辑工具。六轴和路由不依赖生成模型，生成模型更换时审核流程不变。

**关键结果**：在 120 个广告、562 个场景上，有 judge findings 时 reviewer 标记产品错误占 60% 场景，脚本/字幕/声音问题各低于 10%。60 个广告中，有 judge findings 时产品错误标记 58%，而隐藏 judge 的两个 reviewer 只标记 26%；一位 reviewer 两种方式分别标记 57% 和 19%。120 盲标场景上，产品 judge AUC 0.84，视频质量和照片相似度分数接近随机。产品 judge 召回接近全部缺陷但也误报，需 reviewer 决策；没有 judge findings 时 reviewer 标记随时间衰减。
