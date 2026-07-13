---
title: Scalable Visual Pretraining for Language Intelligence
title_zh: 可扩展的视觉预训练用于语言智能
authors:
- Yiming Zhang
- Zhonghan Zhao
- Wenwei Zhang
- Haiteng Zhao
- Tianyang Lin
- Yunhua Zhou
- Demin Song
- Kuikun Liu
- Haochen Ye
- Haian Huang
affiliations:
- Shanghai Artificial Intelligence Laboratory
- University of Science and Technology of China
- Zhejiang University
- Shanghai Jiao Tong University
arxiv_id: '2607.09657'
url: https://arxiv.org/abs/2607.09657
pdf_url: https://arxiv.org/pdf/2607.09657
published: '2026-07-09'
collected: '2026-07-13'
category: Training
direction: 视觉文档预训练提升语言智能
tags:
- visual pretraining
- language model
- document understanding
- unsupervised learning
- multimodal pretraining
one_liner: 直接在视觉文档上预训练可超越纯文本预训练，为语言智能提供高效可扩展路径
practical_value: '- **商品详情页理解**：电商场景中大量信息以布局、表格、图片形式存在，传统 OCR→文本 流程丢失空间关系。可借鉴视觉预训练，直接对详情页截图编码，提升对结构化信息（如规格参数、对比图表）的理解，改善搜索与推荐相关性。

  - **Agent UI 理解**：在购物助手、广告投放等 Agent 任务中，直接对操作界面截图进行视觉预训练，能让模型学会从像素推断可点击元素与交互逻辑，减少对
  DOM 或渲染文本的依赖，提升自动化决策鲁棒性。

  - **落地页质量评估**：广告落地页通常包含大量视觉元素，视觉预训练后的模型可从整体布局、美学设计角度评估页面转化潜力，用于素材优选或创意生成前的质量过滤。

  - **跨模态语义对齐**：视觉预训练获得的表征可与商品标题、用户行为序列联合微调，形成更强的跨模态语义空间，有助于冷启动商品或图文不匹配问题的解决。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：大语言模型预训练长期依赖纯文本语料，但现实中的文档、网页等知识大量以视觉形式存在（排版、公式、图表），转换为文本过程会丢弃空间、样式等关键信息。本文挑战“语言模型必须用文本训练”的默认假设，探索能否直接利用视觉文档提升预训练模型的语言智能。

**方法**：系统对比了多种无监督视觉预训练范式，直接以页面截图为输入，不进行 OCR 或文本提取，与同源纯文本预训练在相同语料下公平对比。采用多种骨干架构（如 ViT、CNN）和下游语言理解基准测试。

**关键结果**：视觉预训练在多个模型和任务上一致超越纯文本预训练，证明视觉文档中的布局、格式等暗含知识对语言智能训练有效且可扩展，提供了一条不依赖图文配对监督的高效预训练路径。
