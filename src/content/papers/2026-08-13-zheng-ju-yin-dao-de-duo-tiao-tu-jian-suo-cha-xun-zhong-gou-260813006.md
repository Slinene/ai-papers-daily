---
title: 'EviReform: Evidence-Guided Query Reformulation for Multi-Hop Graph Retrieval'
title_zh: 证据引导的多跳图检索查询重构
authors:
- Xinlong Xu
- Yoshua Y. Li
affiliations:
- Nanjing University of Information Science and Technology
- Meituan
arxiv_id: '2608.13006'
url: https://arxiv.org/abs/2608.13006
pdf_url: https://arxiv.org/pdf/2608.13006
published: '2026-08-13'
collected: '2026-08-14'
category: RAG
direction: RAG · 多跳图检索查询重构
tags:
- RAG
- Multi-hop retrieval
- GraphRAG
- Query reformulation
- Evidence-guided retrieval
one_liner: 利用已检索证据生成残差查询，分离查询重构与图证据聚合，提升多跳检索 Recall@5 与 F1
practical_value: '- **多跳检索中引入残差查询**：在商品图谱问答或客服 RAG 中，初始 query 往往只指向第一跳实体，后续证据需要新查询补充。可仿照
  EviReform，用已命中的商品/属性片段生成 residual query，针对尚未解决的信息需求定向检索，避免把所有证据混在一个 query 向量里。

  - **分离查询修正与图聚合**：不要每拿到新证据就重新编码整个 query 或图。工程上可以并行计算原始 query 和多个残差 query 的检索分数，分别归一化后加权融合，再在实体/商品关系图上传播。这样既保留原意图，又能灵活吸收中途证据。

  - **利用语义证据引导图遍历**：在商品知识图谱或内容关系图中，边权重可以结合当前已观察到的实体语义相似度，而非仅依赖静态关系。例如用户问“A 品牌手机续航如何”，先用
  A 品牌手机命中节点，再根据该节点生成“电池容量/快充”残差查询，补充商品属性节点。

  - **评估指标与成本意识**：论文中 Recall@5 最高提升 5.59 点，说明少量残差查询即可带来显著收益。在业务中可控制每轮残差查询数量（如 1-3
  个），平衡检索延迟与召回提升。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：多跳检索需要同时找回互补证据，但初始 question 往往只显式描述第一跳实体或关系，后续证据在检索开始前很难刻画。现有 GraphRAG 方法主要用原始 query 作为检索信号，靠图结构传播相关性，无法利用已检索到的 passage 提供的语义线索，导致互补证据仍依赖存储边关系才能触达。

**方法关键点**：EviReform 将“修订检索请求”与“图证据聚合”分离。检索到的 source passages 用于生成 residual queries，针对性描述尚未解决的信息需求；原始 query 和残差 query 的检索信号分别归一化后合并，再在共享实体的 proposition 之间传播。这样图检索不仅能利用静态结构，还能被观察到的证据动态引导。

**关键结果**：在 2WikiMultiHopQA、HotpotQA、MuSiQue 三个多跳 QA 数据集上，EviReform 比最强基线 Recall@5 最多提升 5.59 点，F1 最多提升 4.50 点，证明观察证据能有效引导图检索定位原始问题中未充分指定的支持链。
