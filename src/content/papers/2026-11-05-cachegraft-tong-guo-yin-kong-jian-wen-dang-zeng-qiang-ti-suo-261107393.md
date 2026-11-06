---
title: 'CacheGraft: Enhancing Retrieval-Augmented Generation via Latent-Space Document
  Enrichment'
title_zh: CacheGraft：通过隐空间文档增强提升检索增强生成
authors:
- Vihan Lakshman
- Peter Baile Chen
- Zhuohan Gu
- Michael Cafarella
affiliations:
- MIT CSAIL
arxiv_id: '2611.07393'
url: https://arxiv.org/abs/2611.07393
pdf_url: https://arxiv.org/pdf/2611.07393
published: '2026-11-05'
collected: '2026-11-06'
category: RAG
direction: RAG · 离线 KV cache 文档增强
tags:
- RAG
- KV cache
- cache translation
- latent space
- model collaboration
- zero-shot
one_liner: 离线把语料段落编码成大模型与小模型融合的 KV cache，查询时仅注入小模型以增强 RAG 质量
practical_value: '- 可将商品详情页、用户评价、广告文案等长文档离线预编码为 fused KV cache，线上仅用 0.6B 级小模型做 RAG，大幅降低推理成本与延迟；适合电商搜索/推荐中低延迟问答与文案生成场景。

  - 借鉴 cache-to-cache translation：用大模型作为离线知识注入器，小模型作在线执行器，类似知识蒸馏但保留 latent 状态；fuser
  可以零样本迁移到检索数据，降低训练样本收集成本。

  - 在多 Agent 或大小模型协作架构中，可把用户 session、候选集、知识片段编码成 KV cache 传给下游小模型，避免重复拼接长文本、节省显存与重复编码。

  - 落地前需验证：超长商品语料切片策略、缓存存储/更新代价、与文本拼接 RAG 在电商业务指标上的差异；论文只覆盖 QA 基准，推荐/广告收益需小规模 A/B
  测试。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

## 动机
Transformer agent 已展示可以通过 KV cache 在隐空间直接传递状态，而不必经过文本。RAG 系统通常需要较大的 LLM 对检索到的文档进行编码，推理成本高，难以在计算受限场景部署小模型。

## 方法关键点
CacheGraft 基于 Cache-to-Cache (C2C) fusion 框架，离线阶段用大 sharer 模型（4B）和小 receiver 模型（0.6B）共同把每个语料 passage 编码成一个 fused KV cache 表示；该过程学习一个 fuser，完成跨模型 cache 翻译，使小模型能直接消费大模型的隐空间信息。查询时只需将预计算的 cache 注入 receiver，无需再加载大模型。关键点：
- 离线文档增强，在线小模型推理；
- fuser 未在任何检索数据上训练，提升是 zero-shot 的；
- 每个文档只编码一次，可持久化复用。

## 主要结果
在五个 QA 基准、两个独立本地裁判的 30 组对比中，CacheGraft 在 29 组上优于纯文本 receiver baseline，其中 17 组具有统计显著性。结果显示 latent-space document enrichment 可以在不增加在线计算负担的前提下提升小模型 RAG 答案质量。
