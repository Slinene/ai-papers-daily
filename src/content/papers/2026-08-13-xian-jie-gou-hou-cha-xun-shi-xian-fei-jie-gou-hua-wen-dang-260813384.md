---
title: 'Structure then Query: Enabling Precise Analytical Queries over Unstructured
  Documents'
title_zh: 先结构后查询：实现非结构化文档的精确分析查询
authors:
- Teng Lin
- Yuyu Luo
- Nan Tang
affiliations:
- HKUST(GZ)
arxiv_id: '2608.13384'
url: https://arxiv.org/abs/2608.13384
pdf_url: https://arxiv.org/pdf/2608.13384
published: '2026-08-13'
collected: '2026-08-16'
category: RAG
direction: 非结构化文档的结构化查询与分析
tags:
- LLM
- Structured Index
- Query Engine
- Schema Annotation
- SQL Extension
- Document Analytics
one_liner: AnnoIndex 用自动标注模式构建结构化索引，结合 SQL 扩展查询引擎，以 0.87 F1 实现低成本精确文档分析
practical_value: '- 用 annotation index 替代纯向量检索：对商品描述、用户评论、客服工单等非结构化文本，可预先用轻量模型抽取属性（如品牌、价格、功效），构建结构化索引，支持精确过滤，降低在线
  LLM 调用成本。

  - SchemaLoop 自动生成层级 schema：在电商类目/属性挖掘中可借鉴，从语料中自动归纳属性体系，避免手工定义大量标签字典；轻量模型抽取后增量合并，持续丰富知识库。

  - 分层查询执行计划：先低成本过滤（倒排/SQL），再逐步对少量候选调用高成本 LLM 做深层语义分析，适合大规模商品库/内容库上的复杂查询与推理。

  - 查询结果反哺索引：将抽取的新属性写回 annotation index，形成持续增值的文档知识库，类似用户行为/反馈数据不断补充商品标签与属性。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：企业数据以非结构化文档为主，现有方法依赖向量相似度的模糊匹配，难以精确获取信息并做结构化分析与推理，而且在线调用 LLM 成本高。

方法关键点：AnnoIndex 包含两个核心组件。第一是 Annotation Index：SchemaLoop 模块自动从语料生成层级 annotation schema，再用轻量语言模型抽取具体属性值，把散乱文本物化为结构化索引，支持低成本过滤与查询，将属性抽取成本从在线查询分摊到一次性构建。第二是 Structured Query Engine：把用户问题编译为基于 SQL 扩展的执行计划，先用 annotation index 做精确文档过滤，再按成本从低到高逐步应用抽取操作，只有极少量需要深层语义理解的文档才调用 LLM；抽取出的新属性会合并回索引，降低未来查询成本。

关键结果：在三个真实数据集上，AnnoIndex 平均 F1 达到 0.87，优于对比基线，并在复杂多跳 join 和渐进式推理查询上保持稳健性能。
