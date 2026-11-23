---
title: 'Auditable Financial Knowledge Graphs: Schema-Driven Construction and Intrinsic
  Quality Evaluation'
title_zh: 可审计的时序金融知识图谱：schema 驱动构建与内在质量评估
authors:
- Samarth Sarin
- Lovepreet Singh
- Dhagash Mehta
affiliations:
- BlackRock, Inc.
arxiv_id: '2611.27835'
url: https://arxiv.org/abs/2611.27835
pdf_url: https://arxiv.org/pdf/2611.27835
published: '2026-11-20'
collected: '2026-11-23'
category: RAG
direction: 可审计时序知识图谱构建与评估
tags:
- Knowledge Graph
- GraphRAG
- LLM Extraction
- Entity Resolution
- Provenance
- Evaluation
one_liner: 面向金融文档的可审计时序知识图谱构建与评估方法，采用 schema 约束分阶段 LLM 抽取和实体消解，并将图质量与下游 RAG 评估解耦
practical_value: '- 构建业务知识图谱时，先定义 schema 和实体关系约束，再让 LLM 分阶段抽取，可大幅减少无约束抽取带来的脏节点/脏边；对商品、商户、权益文档尤其适用。

  - 实体消解混合 exact/normalized/fuzzy/embedding/LLM 并按 scope 分区，能低成本实现跨文档实体归一；这套方法可直接迁移到电商商品归一、店铺/品牌对齐等场景。

  - Temporal merge constraints 和 reporting-period validity 的显式建模值得借鉴：对价格、库存、优惠政策等时效性属性，存储层必须区分生效周期，防止旧事实覆盖新事实或跨期推理错误。

  - 图质量 intrinsic 评估与下游任务解耦：先单独考核图本体覆盖率、一致性、溯源完整性，再接入 RAG/Agent，能更准确定位是抽取问题还是检索/生成问题，避免盲目调
  prompt。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

动机：金融文档包含叙述性披露、会计指标、公司结构、管理层评论和时间相关事实，传统 chunk-based RAG 难表达其结构化与时效性。因此需要可审计的时序知识图谱作为检索基底。

方法：页面级文档经通用文档智能服务解析，重叠窗口分段；分阶段 LLM 抽取结构实体、量化观测和领域关系，候选元素用预定义 schema 校验。实体消解采用 scope-aware 的 exact、normalized、fuzzy、embedding、LLM 多策略合并；时间合并约束、确定性边去重、冲突感知属性管理和细粒度 provenance 保证 issuer 身份、报告期有效性和证据可追溯。

结果：构建了 evidence-grounded 时序金融知识图谱；提出 intrinsic 质量评估框架，含七个加权维度、两个硬验证门和结构诊断，将图质量与下游检索问答评估解耦，支持诊断与迭代优化，下游 GraphRAG 在 FinanceBench 上评测。
