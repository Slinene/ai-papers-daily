---
title: 'Candidate-Constrained Retrieval-Augmented Generation for LongEval-RAG: System
  Design and Empirical Analysis'
title_zh: 候选约束检索增强生成系统：LongEval-RAG 的设计与实证
authors:
- Yingdong Yang
- Haijian Wu
arxiv_id: '2607.04008'
url: https://arxiv.org/abs/2607.04008
pdf_url: https://arxiv.org/pdf/2607.04008
published: '2026-07-04'
collected: '2026-07-07'
category: RAG
direction: 候选约束 RAG 流水线设计与多指标评估
tags:
- RAG
- candidate constraint
- LongEval-RAG
- evidence ranking
- sentence reranking
- evaluation
one_liner: 在候选约束 RAG 中，规则分块配合句子级神经选择优于复杂语义分块，获得多项指标最优
practical_value: '- 在候选集受限的检索任务（如给定商品列表的搜索或推荐理由生成）中，分块策略优先采用简单规则（固定句子/段落切分），将语义理解后置到句子级神经重排，避免复杂分块带来的不稳定性。

  - 伪相关反馈（PRF）和倒数秩融合（RRF）可作为轻量级召回增强手段，在不明显增加延迟的情况下提升检索精度，适合线上服务。

  - 需要引用证据的生成场景（如推荐解释或搜索摘要），可引入引用先验（citation prior），强制生成模型关注已选证据的来源，提高生成内容的可信度。

  - 离线评估应采用多指标（如 BERTScore、检索精度、nugget 覆盖、平均等级）和多评判方式（金标准、LLM judge），避免单一指标产生的误导，指导系统迭代。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：LongEval-RAG 任务要求为每个查询在组织者提供的候选文档集合内检索证据并生成答案，所有引用必须限于候选集，这与开放域 RAG 不同。高效地从受限候选集中筛选证据并保证引用准确性是核心挑战。

**方法**：系统设计了确定性来源追踪与基于段落的检索流水线，融合了查询扩展、伪相关反馈（PRF）、倒数秩融合（RRF）、轻量级证据重排序、引用感知证据聚合（citation prior），以及可选的 MiniLM 句子级神经重排。对比了十种流水线变体，包括不同分块策略（规则分块、语义话题分块）和是否启用最终句子选择。

**结果**：在组织方主评估中，最优变体 `rule-minilm`（规则分块 + MiniLM 句子选择）在 BERTScore、检索精度、nugget 覆盖率和平均等级上均最高。关键发现是：主要增益并非来自更复杂的语义或话题偏移分块，而是来自稳定的规则化证据单元与生成前的句子级神经选择相结合。辅助的 LLM-judge 评估倾向于不同的系统，表明多指标 RAG 评估的必要性。
