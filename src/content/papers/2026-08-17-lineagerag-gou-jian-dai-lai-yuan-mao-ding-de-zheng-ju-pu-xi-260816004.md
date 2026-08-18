---
title: 'LineageRAG: Harnessing GraphRAG by Constructing Evidence Lineages with Source
  Grounding'
title_zh: LineageRAG：构建带来源锚定的证据谱系增强 GraphRAG
authors:
- Linyao Zheng
- Xuhang Shi
- Zhifang Mao
- Sai Zhou
- Shuaixian An
- Xiuquan Hou
- Jinze Li
affiliations:
- XiaoLab, Beijing University of Posts and Telecommunications
- Xi'an Jiaotong University
arxiv_id: '2608.16004'
url: https://arxiv.org/abs/2608.16004
pdf_url: https://arxiv.org/pdf/2608.16004
published: '2026-08-17'
collected: '2026-08-18'
category: RAG
direction: GraphRAG 多跳证据溯源与锚定
tags:
- GraphRAG
- Multi-hop QA
- Evidence Grounding
- Provenance
- Retrieval
one_liner: 为每个证据需求构建显式谱系并通过原文字段锚定来源，显著改善多跳检索与生成效果
practical_value: '- 在电商知识图谱/商品属性图上做多跳推理时，可先将用户 query 拆成多个证据需求（如品类、属性、场景约束），并在图谱遍历中保留每个候选与需求的绑定关系，避免最终结果只覆盖部分意图。

  - Agent 做多步检索/推荐解释时，可借鉴 lineage completion：用已检索片段的 provenance 选择互补证据，并强制对每个需求提供原文字段支撑，缺少支撑的需求触发补召回或降低置信度，从而提高可解释性和防幻觉能力。

  - 工程上可把“需求初始化 → 需求条件检索 → 谱系补全 → 来源锚定”拆成独立模块，在电商 RAG pipeline 中输出带有引用来源的结构化证据链，便于
  debug、评估和线上链路追踪。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**
现有 GraphRAG 方法把证据发现与 source grounding 的关系隐式化，导致多跳问题时最终证据集常未完整覆盖 query 中所有证据需求。

**方法关键点**
LineageRAG 先由 query 自动初始化若干 evidence demands；针对每个需求，在结构化语料图上进行 demand-conditioned retrieval，扩展一条 evidence lineage，并在每个候选证据上保留其对应的需求 provenance。随后 lineage completion 利用这些 provenance 选择互补 passages，并在选中证据确实支持某需求时，将其锚定到 verbatim source span，形成从需求到原文片段的显式证据链。

**关键结果**
在 HotpotQA、2WikiMultiHopQA、MuSiQue 三个多跳问答基准上，LineageRAG 相比领先 GraphRAG 基线，平均 R@5 提升 3.51、EM 提升 5.96、F1 提升 5.22。
