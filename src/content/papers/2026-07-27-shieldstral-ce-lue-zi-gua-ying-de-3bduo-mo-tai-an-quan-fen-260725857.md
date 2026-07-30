---
title: Shieldstral
title_zh: Shieldstral：策略自适应的3B多模态安全分类器
authors:
- Antonia Calvi
- Avinash Sooriyarachchi
- Giada Pistilli
- Guillaume Lample
- Maarten Buyl
- Maximilian Augustin
- Maximilian Müller
- Pierre Stock
- Tom Bewley
- Wassim Bouaziz
arxiv_id: '2607.25857'
url: https://arxiv.org/abs/2607.25857
pdf_url: https://arxiv.org/pdf/2607.25857
published: '2026-07-27'
collected: '2026-07-30'
category: Multimodal
direction: 多模态安全分类 · 策略自适应
tags:
- safety classifier
- multimodal
- policy-adaptive
- binary QA
- content moderation
- small model
one_liner: 3B小模型通过二元问答统一异构审核任务，文本安全性能比肩7倍大模型，多模态达新SOTA
practical_value: '- **统一二进制问答范式**：将不同审核策略、类别标签统一为自然语言问题是 / 否判断，能融合来源异构的训练数据，降低多业务线接入成本，适合电商、社区同时管理商品描述、买家秀、评论等多模态内容安全。

  - **策略自适应部署**：同一模型可按需输入不同安全政策查询，动态切换审核标准，无需为不同场景（如广告创意审核 vs. 售后评价过滤）分别维护模型，显著降低工程维护复杂度。

  - **小模型高吞吐**：3B参数量支持高并发在线推理，可直接嵌入推荐 / 广告的实时投放链路，对输入素材、生成文案进行轻量级安全预筛，兼顾延迟与精度。

  - **数据配方可复用**：论文公开了54.1M训练样本的构建流程（包含人工标注、合成数据、细粒度评估集），可直接迁移到自建安全审核数据管线，尤其适用于标注成本高的垂类场景。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：主流安全分类器依赖固定危害类别体系，无法应对不同安全政策（如教育平台 vs. 金融工具）的差异化要求，且异构安全数据集难以整合训练。**方法**：提出Shieldstral，基于Ministral-3B，将内容审核重塑为**二元问答**：输入自然语言安全策略描述和待检内容（文本 / 图像），输出连续安全分数；由此可将多源、多标注体系数据统一训练，总样本5410万。**结果**：在文本安全基准上，3B模型**匹配或超越近7倍体量模型**，多模态安全分类设立新SOTA；细粒度评测证实其**策略自适应能力**，同一模型能根据输入策略切换审核标准，为安全审核的统一与灵活部署提供可行路径。
