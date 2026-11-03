---
title: 'EAGR: Evidence-Guided Adaptive Graph Retrieval'
title_zh: 证据引导的自适应图检索 EAGR
authors:
- Sonam Gupta
- Vignesh P
- Vishwajeet Kumar
- Adnan Qidwai
- Anand Eswaran
- Jaydeep Sen
- Sachindra Joshi
affiliations:
- IBM
arxiv_id: '2611.01910'
url: https://arxiv.org/abs/2611.01910
pdf_url: https://arxiv.org/pdf/2611.01910
published: '2026-11-01'
collected: '2026-11-03'
category: RAG
direction: RAG · 证据引导的隐式图多跳检索
tags:
- RAG
- Multi-hop QA
- Graph Retrieval
- Evidence-Guided
- VectorDB Metadata
- Adaptive Retrieval
one_liner: 用 VectorDB 元数据中的语义描述符构成隐式图，以积累证据动态选择检索方向，无需显式图或查询改写
practical_value: '- 商品/内容知识库可离线用 LLM 抽取商品属性、卖点、适用人群、实体等作为 metadata 存入现有向量库；共享同一 descriptor
  即形成隐式连边，无需构建商品知识图谱或专用 GraphDB。descriptor 必须 grounding 到原文，并做同义/人名归一，能低成本获得图遍历能力。

  - 会话式导购/多跳商品搜索中，用「accumulated evidence」选择下一步要扩展的属性或关系，而不是重写整个 query 或遍历所有关联属性：让
  LLM 基于已确认的用户约束和商品信息，从当前候选 descriptor 里只挑几个最可能补全信息缺口的方向，可显著节省检索预算。

  - 回答/推荐理由生成前增加「充分性校验 + 证据链填空」：让 LLM 写出 (entity, attribute, value) 链，并强制每个 value
  必须出现在已检索内容中，能拦截模型用参数记忆胡编，适合电商 QA、卖点解释和售后理由。

  - 多跳检索结果按证据链重排，而非仅按 query 相似度：通过关系/属性间接命中的商品或内容，应优先展示能支撑最终结论的节点，可提升 RAG 上下文质量和推荐理由的可信度。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

动机：多跳 RAG 需要检索路径随中间证据动态调整。现有方法要么构建显式图/GraphDB，增加离线成本；要么迭代重写 query，增加在线开销。企业向量库通常已存储 passages 与 metadata，缺一种不物化 graph 的轻量图遍历方案。

方法：
- 离线阶段用 LLM 为每个 passage 抽取命名实体和关键概念作为 semantic descriptors，保留原文中出现过的词，经过人名归一后作为 metadata 存入标准 VectorDB；共享 descriptor 的 passages 隐式连边，不建显式图。
- 在线阶段先用 DPR 召回 k=4 seeds 作为初始 frontier；对每个节点用一次 LLM 调用同时做 Node Assessment（判断相关性、抽取 evidence）和 Edge Selection（从该节点 descriptors 中选择最可能补充信息缺口的方向）；通过 Sufficiency Check 写出 (entity, attribute, value) 链，所有 value 必须来自 accumulated evidence 才算充分；不充分则对候选 descriptors 按 query+evidence 重排，再通过 metadata lookup 取邻居，直到充分或达到 budget B=30。
- 最终按最后证据链重排 passages：证据链相关 > 贡献过 evidence 的 > 其余。

结果：在 HotpotQA、2WikiMultiHopQA、MuSiQue 三个多跳 QA 基准上，EAGR 平均 LLM-Acc 67.1，比 vanilla RAG 高 7.3 点，比最强 graph-aware baseline LinearRAG 高 3.9 点；HotpotQA 77.4、2Wiki 78.1、MuSiQue 45.8。Recall@5：HotpotQA 95.4，2Wiki 95.5，MuSiQue 71.5。消融显示 Edge Selection 最关键，移除后平均降 23.3 点；移除 accumulated evidence 降 4.3 点。

最值得记住的一句话：用 LLM 抽取且 grounding 到原文的 descriptor 作为 VectorDB metadata，配合证据驱动的前沿遍历和充分性校验，就能不建图实现 GraphRAG。
