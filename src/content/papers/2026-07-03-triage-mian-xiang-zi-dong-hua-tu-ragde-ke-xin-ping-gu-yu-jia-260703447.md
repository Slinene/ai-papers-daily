---
title: 'TRIAGE: Trustworthy Retrieval Instrumentation And Graph Evaluation'
title_zh: TRIAGE：面向自动化图RAG的可信评估与诊断框架
authors:
- Axel TahmasebiMoradi
- Lucas Schott
- Martin Royer
affiliations:
- IRT-SystemX
arxiv_id: '2607.03447'
url: https://arxiv.org/abs/2607.03447
pdf_url: https://arxiv.org/pdf/2607.03447
published: '2026-07-03'
collected: '2026-07-07'
category: Eval
direction: Graph-RAG 多阶段可信评估
tags:
- Graph RAG
- Evaluation
- Knowledge Graphs
- Trustworthiness
- Diagnostic
- Automated KG Construction
one_liner: 提出分阶段、无标注的信任指标链，用于定位自动构建的知识图谱在RAG中的故障阶段
practical_value: '- 电商知识图谱问答（如商品属性问答、政策检索）可借鉴分阶段诊断链：将RAG流程显式拆为抽取、建图、检索三环，部署轻量级必要性指标，线上第一个不达标的指标直接指明故障环节，缩短排障时间。

  - 提出的无标注指标（三元组置信度、源文档覆盖率、检索覆盖率、检索成本）可直接集成到离线评估流水线，用于自动构建商品知识图谱后的质量门禁，无需人工标注。

  - 明确区分在线指标与离线校准指标，借鉴这一设计可以在保持实时监控轻量的同时，周期性使用人工参考做精确的全量校验，适合推荐场景中“先线上快速检、后离线深度纠”的双层评估策略。

  - 对Graph-RAG系统中“图的结构质量”的评估方法，可迁移到基于知识图谱的搜索或推荐中，帮助判断自动构建的图是否因结构化错误而漏召回或错排序。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：Graph-RAG 越来越多依赖LLM自动抽取知识图谱，缺少系统化的分阶段评估，导致最终错误答案难以追溯根因。TRIAGE旨在提供一个无需标注数据的诊断框架，在抽取、建图、检索各环节设置信任指标，实现故障定位。

**方法关键点**：
- **三阶段指标**：① KG实现阶段——三元组置信度、源文档覆盖率、模式与规范化检查；② KG验证阶段——图结构质量（正确性、完备性仅在有参考时离线计算）；③ KG使用阶段——检索覆盖率、忠实度、检索成本。
- **诊断链**：所有部署指标构成必要条件链，第一个断开的链接直接定位故障阶段，并映射到对应的修复手段（抽取、图/模式、检索）。
- **无标注部署**：运行时指标不需要金标注；标注数据只用于离线校准正确性和完备性。

**关键结果**：概念验证展示了框架的可行性和诊断能力，配套可复现评估协议；无具体数值结果，主要贡献为理论框架与评估方法论。
