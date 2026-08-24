---
title: 'EnSI-RAG: Entity-Structure-Indexed Retrieval-Augmented Generation for Long-Document
  Question Answering'
title_zh: EnSI-RAG：实体结构索引的长文档问答检索增强框架
authors:
- Xuanyu Meng
- Jiashuo Sun
- Jash Rajesh Parekh
- Jiawei Han
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2608.21252'
url: https://arxiv.org/abs/2608.21252
pdf_url: https://arxiv.org/pdf/2608.21252
published: '2026-08-21'
collected: '2026-08-24'
category: RAG
direction: 长文档 RAG · 实体结构索引
tags:
- RAG
- Entity-Structure Index
- Long-Document QA
- Multi-hop Reasoning
- Knowledge Graph
- LLM
one_liner: 用实体中心 passage 和 entity-structure index 做检索句柄，把证据定位与答案生成解耦，提升长文档 QA 精度
practical_value: '- 商品/店铺知识库构建：不要用固定 chunking；对每个商品/SKU/商家建实体中心 passage，抽取 type +
  property/relation/aspect（如价格、规格参数、店铺关系），用 [entity][type][field:value]→psg_id 建离线索引。线上从原始
  passage 生成答案，避免表格拆散、属性与值分离。

  - 多跳对比/选购问答：把同类商品对比、品牌关系、优惠条件建模为 relation 或双向 relation（如替代品、配件、belongs_to），保留一对多
  set-valued 映射而不是折叠成唯一记录；LLM 只做证据合成，不负责搜索。

  - 工程实现：offline LLM 抽取成本高但可摊销；online 只需 1 次 retrieval planning + 1 次 generation，适合高
  QPS 场景。对商品 spec 表使用 row-level 而非 table-level 粒度；检索深度未必越大越好，可先从小 k 开始调。

  - 属性粒度按域选择：标准化粗粒度属性能减少稀疏性，但法律/精确规格类需保留细粒度；电商可对标准品类用粗粒度类目属性，对参数敏感品类保留原始参数名。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
长文档 QA 中，固定长度 chunking 会把实体和支撑证据切碎，表格行与表头分离，embedding 相似度还可能漏掉词面不相似但语义关键的证据；多跳聚合、跨文档比较更难。需要把检索单元从机械切分改为语义组织，并用查询无关的实体结构索引提升证据定位。

## 方法关键点
- 离线先做 Passage Construction：以主实体为中心构造语义自包含 passage，保留原文和 psg_id；不套固定长度。
- Information Extraction：从每个 passage 抽取记录 r=⟨e,t,M,psg_id⟩，字段分 property / relation / aspect；只做面向检索的 access path，不替代原文。
- Index Entry Building：建成 [entity][entity type][category:field=value]→{psg_id} 的索引；保留 set-valued 映射，不折叠为单一 canonical 值；对 cites/cited-by 等关系建双向 entry。
- 在线 Retrieval：先把 query 转为结构化 retrieval plan H(q)，多跳可依赖前一步中间实体；用 symbolic + semantic 匹配 keys，再取对应 passage set；最终 Generation 只基于原始 passage 生成答案。

## 关键实验与结果
在 Loong 和 Oolong 上对比 RAG、LongRAG、GraphRAG、DocETL、SLIDERS 等。EnSI-RAG 平均 accuracy 78.24，比参考文献中 SLIDERS 的 71.62 高 6.62 点；Loong 84.64、Oolong 71.84。消融显示：金融表格 row-level（100）明显优于 table-level（91.5）；属性粒度粗化对金融/论文有益，法律域反而下降；Top-5 精度 94.0 优于 Top-12/15，说明更聚焦的证据可减少干扰。效率上，离线 LLM 抽取成本经摊销后为 157k tokens / 468s / 32.35 次调用，在线 retrieval 仅 656 tokens、generation 5460 tokens。

## 最值得记住的一句话
结构索引用于找到证据，不用于替代证据；原文 passage 始终是生成答案的唯一证据来源。
