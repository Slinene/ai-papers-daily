---
title: Tracing Query Expansion Effects through Sparse Autoencoder Features
title_zh: 通过稀疏自编码器特征追踪查询扩展效应
authors:
- Fangan Dong
- Weiran Shi
- Zhiwei Xu
- Xuri Ge
- Ben He
- Xin Xin
- Zhumin Chen
- Ying Zhou
affiliations:
- Shandong University
- University of Chinese Academy of Sciences
- Institute of Software, Chinese Academy of Sciences
arxiv_id: '2609.06968'
url: https://arxiv.org/abs/2609.06968
pdf_url: https://arxiv.org/pdf/2609.06968
published: '2026-09-07'
collected: '2026-09-09'
category: Other
direction: SAE可解释性 + 查询扩展分析
tags:
- Sparse Autoencoder
- Query Expansion
- Dense Retrieval
- Interpretability
- Activation Steering
one_liner: 用SAE分解dense retriever表示，解释查询扩展引起的内部特征变化，并通过激活引导提升检索性能
practical_value: '- 利用SAE特征分析查询改写/扩展对检索模型内部表示的影响，定位与用户意图、商品属性相关的稀疏维度，可用于电商搜索相关性问题的诊断与归因。

  - 激活引导提供了一种无需重训检索模型或改写查询的轻量干预方式，可能用于实时调整检索行为，例如在电商搜索中提升特定品类或意图的召回。

  - 对于生成式推荐或Agent系统，可借鉴SAE分解中间表示的方法，理解上下文如何影响item或action的生成，增强模型决策的可解释性。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

## 动机
查询扩展（QE）在dense retrieval中效果不可靠，尤其对强预训练检索器。现有研究多关注扩展质量、语义漂移或检索结果，但很少解释QE如何改变检索器内部表示。

## 方法关键点
- 使用配对原始查询与扩展查询，将dense retriever各层表示分解为稀疏自编码器（SAE）特征。
- 从扩展引起的激活偏移中识别QE相关潜在特征，并用自然语言描述和检索案例进行解释。
- 提出基于SAE的激活引导（activation steering），直接调制这些特征以影响检索行为。

## 关键结果
分析显示有效QE诱导的稀疏特征变化集中在特定层，并与检索意图和实体属性对齐，而非仅扰动最终query embedding。在四个基准上，SAE激活引导比随机干预或原始QE更一致地提升检索性能，验证了SAE可解释QE效应，并提供轻量级检索行为调制方案，无需查询改写或检索器微调。
