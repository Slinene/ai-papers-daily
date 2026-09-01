---
title: 'E-SENS: Exclusion-Sensitive Penalization for Negative-Constraint Retrieval'
title_zh: E-SENS：面向负约束检索的排除敏感惩罚方法
authors:
- Yerang Kim
- Jiyoon Myung
- Joohyung Han
affiliations:
- Independent Researchers
arxiv_id: '2608.30130'
url: https://arxiv.org/abs/2608.30130
pdf_url: https://arxiv.org/pdf/2608.30130
published: '2026-08-31'
collected: '2026-09-01'
category: RAG
direction: RAG · 负约束检索优化
tags:
- Negative Constraints
- Dense Retrieval
- Reranking
- Training-free
- RAG
one_liner: 训练无关重排方法 E-SENS，用陷阱查询相似度惩罚排除概念，减少否定敏感检索中的违规召回
practical_value: '- 电商搜索/推荐中用户常含否定词（如“非雪纺”“不含酒精”），现有嵌入召回容易命中否定概念；可借鉴 E-SENS：用 LLM
  抽取否定片段生成 trap query，在召回或重排阶段对候选商品做相似度惩罚，无需训练即可上线。

  - 广告否定关键词可类似处理：为每个否定词构造排除向量，从广告相关性分数中减去，减少 exclusion 流量上的无效曝光。

  - 工程实现上，trap query 应尽量紧凑，避免引入多余语义；惩罚强度作为超参，可在评测集扫描 recall-violation 曲线，取满足召回底线下的最小违规点。

  - 在 Agent/RAG 知识召回中，若用户明确排除某类内容，可由 LLM 先提取排除约束并生成 trap query，对召回结果重排过滤，降低后续生成违规风险。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
检索增强语言模型在用户查询含排除约束时，常因被排除概念仍出现在查询文本中，导致 dense retriever 错误地高分检索到该概念文档，污染生成上下文。例如“language models training excluding reinforcement learning”中，RL 是显著且被排除的术语，但依然可能被检索。

### 方法关键点
E-SENS 是训练无关的重排方法，核心是区分包含语义与排除语义：
1. 从原查询中提取被排除部分，构造紧凑的“陷阱查询”（trap query），专门表示要避免的概念。
2. 分别计算原查询和陷阱查询与候选文档的相似度。
3. 将陷阱查询相似度从原查询分数中减去，得到重排分数。
无需微调嵌入模型即可对排除概念施加惩罚，同时保留原查询相关文档。

### 关键结果
在 ExcluIR 基准上，跨四个嵌入模型，E-SENS 展示出清晰的 recall-violation 权衡：在保持召回率的配置下，显著降低 trap retrieval（检索到被排除概念文档的比例）。
