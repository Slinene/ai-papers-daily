---
title: 'Reducing Technician Search Burden: A Multimodal RAG for Cessna 172 Maintenance
  Manual'
title_zh: 面向Cessna 172维修手册的多模态RAG降低技师检索负担
authors:
- Seongjun Ha
- Md Rashedul Islam
- Gaurav Nanda
- Damon Lercel
affiliations:
- Purdue University
- Clemson University
arxiv_id: '2608.18465'
url: https://arxiv.org/abs/2608.18465
pdf_url: https://arxiv.org/pdf/2608.18465
published: '2026-08-19'
collected: '2026-08-23'
category: RAG
direction: 多模态RAG垂直领域知识检索
tags:
- Multimodal RAG
- Vision-Language Model
- Aircraft Maintenance
- Retrieval
- Synthetic Queries
- Interpretability
one_liner: 开发多模态手册检索器与MRAG流程，在维修手册上实现93.37% recall@5和87.20%答案语义相似度
practical_value: '- 电商/推荐场景可迁移：将商品文档、规格表、示意图做多模态RAG，让客服或导购Agent同时检索图文页面，而不是只依赖文本切片，提高复杂产品问答质量。

  - 评估方法可直接复用：用合成查询按信息类型（程序、图示、警告/安全、规格）分层构造测试集，能更细粒度定位检索瓶颈，比单一整体指标更利于迭代。

  - 工程实现参考：把检索和生成拆开分别评估 recall@5 和生成相似度，便于定位问题是出现在召回还是生成；同时记录单查询耗时和成本，作为上线前可行性门槛。

  - 多模态可解释性可借鉴：用热力图可视化页面上哪些区域被检索模型关注，可用于排查错误召回、做人工审核，也便于向业务方解释模型为何推荐某张图或某个手册页。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：航空维修手册包含程序、图示、警告与规格等多模态信息，但现有RAG仅做文本检索，技师在紧张排班下很难快速翻到需要的页面；既有工作未覆盖图表等视觉内容。

**方法关键点**：面向通用航空广泛使用的Cessna 172维修手册，构建多模态手册检索器（MMR），对手册页面同时进行文本和视觉编码以支持图文联合检索；用合成查询覆盖程序、图示、警告/安全、规格四类典型信息需求。检索出的页面再输入视觉语言模型生成答案，组成完整多模态RAG流水线（MRAG）。

**关键结果**：MMR在合成查询上达到93.37% recall@5；生成答案与ground-truth语义相似度87.20%。可行性方面，平均检索5页耗时11.93秒，生成耗时4.95秒，单查询成本$0.0091；通过热力图验证了检索注意力区域的可解释性。结果表明该MRAG流水线能显著减少技师检索手册和多模态信息的时间。
