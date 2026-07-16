---
title: Personalizing Incremental Video Search with Hybrid Text and ID Embeddings
title_zh: 个性化增量视频搜索：融合文本与ID嵌入
authors:
- Vivek Kanojiya
- Vishalaksh Aggarwal
- Daeho Baek
- Lyndon Kennedy
- Xuetao Yin
affiliations:
- Apple
arxiv_id: '2607.13493'
url: https://arxiv.org/abs/2607.13493
pdf_url: https://arxiv.org/pdf/2607.13493
published: '2026-07-15'
collected: '2026-07-16'
category: RecSys
direction: 搜索排序 · 个性化 · 混合嵌入
tags:
- Personalization
- Incremental Search
- Hybrid Embeddings
- Contrastive Learning
- XGBoost
- Online A-B Test
one_liner: 通过混合语义和协同嵌入为增量搜索提供个性化排序，在意图模糊时收益最大
practical_value: '- 在电商、App搜索等增量搜索场景，可将物品的文本语义嵌入和协同过滤ID嵌入拼接成特征，注入排序模型（如XGBoost或双塔）。文本嵌入可用多语言模型在协同观看/购买三元组上对比学习微调，缓解曝光偏差。

  - 对于意图尚未明确的前缀查询（1-3字符），个性化特征带来的增益远高于完整查询，因此可在前端增加实时用户意图不确定性估计，动态加大个性化权重。

  - 工业场景常面临长尾用户冷启动问题，论文发现长历史用户从个性化中受益更大，但基线指标更低，说明个性化可弥补默认排序不足。可以针对不同活跃度用户设计分级策略。

  - 采用LLM评判物品相似度来评估嵌入质量的方法，可迁移到推荐、搜索中的相关性标注，作为人工标注的补充，降低点击/曝光偏差。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：增量搜索（如Apple TV搜索）中，用户输入前缀字符时意图高度模糊，默认排序难以捕捉个性化偏好，导致结果相关性差。需要引入个性化信号，同时利用物品的语义内容和协同交互模式。

**方法**：离线学习两种物品嵌入——① 基于文本的多语言编码器（TextEmb），在用户共同观看的三元组上通过对比学习微调，捕获语义相似性；② 基于ID的协同嵌入（IdEmb），用用户交互序列训练，编码协同信号。在线推理时，从用户近期观看历史聚合表征，计算用户-物品的余弦相似度，连同其他特征一起输入成对XGBoost排序器，实现个性化重排。

**结果**：离线实验中，对有历史的会话，个性化排序将NDCG@10提升2.99%，MRR提升3.30%。关键切片：在1-3字符的模糊前缀查询上，NDCG@10提升8.63%，比长查询的1.46%提升高近6倍；历史越长提升越大（51-100次历史用户提升4.37%）。线上3周A/B实验中，点击率+1.14%，转化率+1.23%，转化物品排名提升2.91%。消融实验显示语义和协同嵌入互补，且LLM评判的相似度指标能有效评估嵌入质量。
