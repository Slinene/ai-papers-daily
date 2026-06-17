---
title: Temporal Preference Optimization for Unsupervised Retrieval
title_zh: 面向无监督检索的时间偏好优化
authors:
- HyunJin Kim
- Jaejun Shim
- Young Jin Kim
- JinYeong Bak
affiliations:
- Sungkyunkwan University
- Microsoft
arxiv_id: '2606.17664'
url: https://arxiv.org/abs/2606.17664
pdf_url: https://arxiv.org/pdf/2606.17664
published: '2026-06-16'
collected: '2026-06-17'
category: RAG
direction: 时间感知检索 · 偏好优化
tags:
- Temporal Retrieval
- Preference Optimization
- Unsupervised Dense Retriever
- TRPO
- Time Embedding
one_liner: 用时间偏好优化（TRPO）训练无监督稠密检索器，使其偏好时间对齐文档
practical_value: '- 在商品搜索/推荐中，可利用商品发布时间、季节性构建时间偏好对，无需人工标注即可训练检索器优先返回时效性强的物品

  - 时间嵌入插值技巧可泛化到未见过的时间段（如未来促销期），解决时间冷启动问题

  - 方法轻量：仅需在双塔模型中加入时间嵌入和偏好损失（类似DPO），容易集成到已有推荐召回模型

  - 对比超大语言模型嵌入，用72.7倍更小模型达到更高nDCG，适合工程部署中的延迟和成本约束'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机** 无监督稠密检索通过对比学习捕获语义相似性，但忽略时间相关性，常返回语义相近但时间错位的文档（如查询“2019年总统”却返回2021年文档）。现有方法依赖显式时间戳监督，不总是可获取。

**方法** 提出TPOUR，核心为时间检索偏好优化（TRPO）：将时间对齐建模为偏好学习问题。给定查询，从正确时间段采样正样本文档，从错误时间段采样负样本，通过成对排序损失引导检索器偏好时间匹配文档。同时学习一个时间嵌入，注入检索器，并通过对训练时间段的嵌入做插值，使模型能泛化到未见时间段（连续时间对齐）。

**关键结果** 在时间信息检索（T-IR）任务上，TPOUR优于无监督和有监督基线。TPOUR-Contriever模型大小仅为Qwen-Embedding-8B的1/72.7，但在显式时间查询上平均nDCG@5提升4.04（+12.15%），隐式查询上提升4.98（+15.21%）。消融实验验证了TRPO损失和时间插值的有效性。
