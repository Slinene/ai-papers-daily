---
title: 'Think Before You Link: Rarity, Reasoning, and Retrieval in Multilingual Entity
  Linking'
title_zh: 先思后链：多语言实体链接中的稀有性、推理与检索
authors:
- Parinthapat Pengpun
- Simran Khanuja
- Graham Neubig
affiliations:
- Carnegie Mellon University
arxiv_id: '2609.10745'
url: https://arxiv.org/abs/2609.10745
pdf_url: https://arxiv.org/pdf/2609.10745
published: '2026-09-08'
collected: '2026-09-12'
category: RAG
direction: 多模态实体链接 · 推理+检索
tags:
- Entity Linking
- Multimodal
- Reasoning
- Retrieval
- Rare Entities
- Multilingual
one_liner: 提出训练免的视觉-语言模型框架，结合迭代搜索与推理，提升多语言多模态实体链接在稀有实体上的准确率
practical_value: '- 稀有度定义不能只看流行度（如 pageviews），应加入知识图谱结构指标（文档丰富度、连接度），能暴露不同失败模式；在电商长尾商品/实体识别中，可以用类似多维稀有度切片评估模型，避免只优化头部。

  - 训练免框架实用性强：用 reasoning-capable VLM 动态搜索 Wikipedia 并迭代收集证据，无需微调即可部署；适合在业务中快速构建多语言实体链接/消歧模块，尤其处理长尾
  query 或冷启动实体。

  - 推理与检索互补的结论可直接迁移到 RAG/Agent 系统：单独检索能提升稀有实体但可能损害整体，单独推理对稀有实体帮助有限；组合使用时，让模型在推理循环中根据检索反馈调整判断，比一次性生成更稳健。

  - 多模态信息（如图像中的文字、logo）对消歧很有价值；在电商商品匹配、query 到商品实体链接中，可以利用商品图片中的文字信息辅助文本匹配，并配合外部知识库检索。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：多模态实体链接在稀有实体上性能显著下降，但现有稀有度度量主要基于流行度（如 pageviews），会遗漏知识图谱结构上稀缺但有一定流行度的实体。论文引入知识图谱结构度量（实体文档丰富度、连接度等），识别出许多流行度指标遗漏的稀有实体，SOTA 模型在这些切片上准确率下降 15.4-39.9%，表明不同稀有度定义暴露不同失败模式。

**方法关键点**：提出一个简单的训练免框架，由具备推理能力的视觉-语言模型（VLM）在 Wikipedia 上迭代搜索和推理，动态收集证据。模型先根据文本和图像生成查询，搜索相关页面，阅读候选实体片段并推理判断，可多轮迭代。控制实验对比了仅推理、仅检索和两者组合：推理单独使用对稀有实体提升不显著；检索单独使用提升稀有实体但可能损害整体准确率；组合效果最好。

**关键结果**：在 MERLIN 多语言多模态实体链接基准（涵盖印地语、印尼语、日语、泰米尔语、越南语）上，最佳系统较 SOTA 整体提升 6.9%，在稀有实体切片上最高提升 23.3%。同时发布 MERLIN-Rare 稀有实体测试切片，供针对性评估。
