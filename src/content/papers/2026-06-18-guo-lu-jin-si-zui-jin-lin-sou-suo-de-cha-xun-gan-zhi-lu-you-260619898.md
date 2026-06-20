---
title: Query-aware Routing for Filtered Approximate Nearest Neighbors Search
title_zh: 过滤近似最近邻搜索的查询感知路由框架
authors:
- Qianqian Xiong
- Mengxuan Zhang
affiliations:
- Australian National University
arxiv_id: '2606.19898'
url: https://arxiv.org/abs/2606.19898
pdf_url: https://arxiv.org/pdf/2606.19898
published: '2026-06-18'
collected: '2026-06-20'
category: Other
direction: 向量检索 · 过滤ANN · 查询路由优化
tags:
- filtered ANN
- query-aware routing
- approximate nearest neighbor
- ML-based router
- recall-QPS trade-off
- vector database
one_liner: 提出查询感知路由，用轻量回归模型预测各方法的召回，结合离线基准表动态选择最佳召回-QPS权衡的方法
practical_value: '- 在电商/广告带属性过滤的向量召回场景中，可借鉴查询级路由思想：线上用轻量模型（仅需3个特征）预测各候选ANN方法的召回率，根据实际需要的召回-QPS平衡点动态选择方法。

  - 工程实现：预建离线基准表（方法、参数、召回、QPS），线上查表选择，路由延迟极低。

  - 特征工程简化回归目标：用回归预测召回率比分类方法预测更准，且只需查询向量的简单统计量（如均值、方差）和过滤率等3个特征。

  - 可将该方法集成到推荐系统的多层检索中，对硬过滤（品类、价格区间等）与向量相似度统一优化，避免单一方法全局次优。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：过滤ANN搜索（向量相似性+属性谓词）是推荐系统、语义检索和RAG的关键环节。现有方法（pre-filtering, post-filtering, 融合索引等）没有一种能在不同数据集、不同谓词类型上恒优，甚至在同一个查询集内最优方法也会因查询而异。

**方法**：提出查询感知路由框架。离线阶段：穷举不同ANN方法及其参数组合，在目标数据集上实测召回率和QPS，生成基准表。线上阶段：部署一个轻量级ML模型，接收查询向量和过滤率特征，预测每种候选方法在该查询上的召回率；路由引擎根据用户指定的召回-QPS权衡目标（如最小延迟下召回≥0.95），从基准表中选出满足召回要求且QPS最高的方法。通过消融实验将候选特征从22个精简至仅需3个（查询向量的均值、方差、过滤后候选集大小比例），并采用回归而非分类目标以提升预测精度。模型在6个真实数据集上训练，在5个未见过的数据集上验证。

**结果**：该路由器在5个验证集上均实现了最优的召回-QPS平衡，对比最强基线在所有设定下平均QPS提升可观，而路由延迟开销不到总搜索时间的1%。
