---
title: 'QO-Bench: Diagnosing Query-Operator-Preserving Retrieval over Typed Event
  Tuples'
title_zh: QO-Bench：诊断类型化事件元组检索中的查询操作符保持
authors:
- Mengao Zhang
- Xiang Yang
- Chang Liu
- Tianhui Tan
- Ke-wei Huang
affiliations:
- Asian Institute of Digital Finance, National University of Singapore
arxiv_id: '2606.04646'
url: https://arxiv.org/abs/2606.04646
pdf_url: https://arxiv.org/pdf/2606.04646
published: '2026-06-03'
collected: '2026-06-06'
category: Eval
direction: 检索增强生成 · 操作符保持诊断基准
tags:
- RAG
- benchmark
- query operators
- typed events
- retrieval evaluation
- IE-to-SQL
one_liner: 提出QO-Bench基准，揭示现有RAG系统因丢失类型化值而无法正确执行数据库风格查询操作，核心瓶颈在操作符执行而非检索
practical_value: '- 在电商RAG/Agent中处理“同时满足A和B的商品”等结构化查询时，应向显式抽取-执行管道（IE-to-SQL）倾斜，避免端到端LLM直接输出答案，以可靠支持join、intersection等操作符。

  - 检索评估不能只看语义相关性，需验证答案是否精确命中所要求的全部实体；可借鉴QO-Bench的精确匹配与召回设计，构建离线算子级诊断，尤其对计数、交集场景更有必要。

  - 即使将相关段落全部提供给长上下文模型，操作符执行准确率仍远未饱和，说明不能高估LLM推理能力；复杂结构化操作应卸载到确定性执行引擎，Agent工作流中可将LLM作为抽取器而非执行器。

  - 对于实时性要求高的推荐或搜索场景，索引时预先抽取、存储类型化元组（如事件属性、数值），查询时直接执行算子，可大幅降低在线推理延迟并避免信息丢弃。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：商业、法律等领域的许多自然语言问题本质是数据库查询，但所需记录隐藏在文本中。现有RAG系统侧重语义相关性，检索到相关段落并不保证正确执行查询操作（如过滤、投影、交集、计数）。本文旨在系统诊断RAG在查询操作符保持上的失败模式。

**方法**：构建QO-Bench基准，包含22,984篇新闻文章、614个公司事件，设计18种查询模板生成785个问题，每个答案由类型化事件元组精确计算，评估基于精确匹配的召回率。在相同条件下对比四种范式：标准RAG、ReAct RAG、GraphRAG、信息抽取转SQL（IE-to-SQL），并设置长上下文预言机（给定所有相关段落）作为上限，以隔离检索失败。提出“索引时保持 vs 查询时执行”两轴分析框架。

**结果**：相似检索在过滤/投影类算子中占优，IE-to-SQL在交集和计数上远超其他方法；各范式均检索到相关文本，但丢失了操作符所需的类型化值（如数值、实体标识）。长上下文预言机仍未饱和（计数操作最高仅约60%），表明操作符执行是核心瓶颈。结论呼吁将检索目标从段落相关性转向查询操作符保持。
