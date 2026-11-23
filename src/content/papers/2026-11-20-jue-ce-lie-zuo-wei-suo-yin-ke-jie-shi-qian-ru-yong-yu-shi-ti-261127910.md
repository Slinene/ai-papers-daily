---
title: 'Decision Columns as an Index: Interpretable Embeddings for Explainable Entity
  Matching and Search'
title_zh: 决策列作为索引：可解释嵌入用于实体匹配与检索
authors:
- Aadharsh Kannan
- Robert Bruckner
- Philip A. Bernstein
affiliations:
- Microsoft
arxiv_id: '2611.27910'
url: https://arxiv.org/abs/2611.27910
pdf_url: https://arxiv.org/pdf/2611.27910
published: '2026-11-20'
collected: '2026-11-23'
category: Other
direction: 可解释嵌入 · 决策列索引
tags:
- interpretable embeddings
- entity matching
- dense retrieval
- decision columns
- question answering
one_liner: 用决策列构建可解释向量，相似度按问题分解，支持审计、过滤与增量扩展，性能可比稠密检索
practical_value: '- 电商商品归一/店铺去重：用决策列（如“是否同一品牌”“标题是否指同款”）构建可解释向量，相似度可精确追溯到每个问题，便于审核匹配结果；新增属性问题只需加一列，无需重嵌全库。

  - 搜索/Agent 可审计检索：在稠密召回外挂问题空间通道，对高风险操作输出“为什么匹配/为什么不匹配”；从 badcase 中挖掘缺失问题，能提升 MRR
  且不用重算已有向量。

  - 低成本回填：已有 dense embedding 的语料，可用几千条标注行训练一个小网络映射到完整可解释向量，成本约 1/200，适合为存量库补解释能力。

  - 查询侧改写：推断“合适结果应有的属性”再转化成问题，比只编码字面 query 更有效；可结合 question-space 与 dense 分数做混合召回。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：业务系统要做实体匹配和检索，Agent 操作需要可审计理由；稠密嵌入效果好但坐标不可解释、不可按语义过滤、新增属性需全量重编码。

方法关键点：每条记录在有序决策列上回答自然语言问题，取值 yes/no/not stated；向量坐标即问题答案，相似度可拆成逐问题贡献；新问题只增加坐标不改旧坐标；可从 retrieval failures 生成新问题；一个小网络从已有 dense embedding 映射到可解释向量，低成本回填。

结果：实体匹配候选生成 question space 与 dense 统计持平，且每个接受匹配可精确解释；失败挖掘问题使 MRR 提升 3 倍；搜索中推断目标产品属性优于只编码字面请求，question-space+dense 混合改善检索（未达预设置信阈值）；回填成本约 1/200。
