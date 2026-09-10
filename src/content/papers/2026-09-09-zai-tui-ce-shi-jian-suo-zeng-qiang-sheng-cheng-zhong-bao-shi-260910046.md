---
title: Guaranteeing Faithful Evidence Extraction in Speculative Retrieval-Augmented
  Generation
title_zh: 在推测式检索增强生成中保证忠实证据提取
authors:
- Quentin Signé
- Mohand Boughanem
- Jose Moreno
- Thiziri Belkacem
affiliations:
- Université de Toulouse - IRIT UMR 5505
- Airbus Protect
arxiv_id: '2609.10046'
url: https://arxiv.org/abs/2609.10046
pdf_url: https://arxiv.org/pdf/2609.10046
published: '2026-09-09'
collected: '2026-09-10'
category: RAG
direction: RAG 忠实证据提取与解码约束
tags:
- RAG
- Faithfulness
- Speculative Decoding
- Constrained Decoding
- Hallucination
- Verbatim Extraction
one_liner: 提出CHyD，将投机解码改造为强制约束解码，保证引用片段逐字来自检索文档，技术领域准确率接近完美
practical_value: '- 在电商/广告合规文案、商品政策解释、客服问答等场景，需要引用原文保证信息准确时，可以使用硬约束解码限制生成内容必须来自检索到的商品详情、条款或文档
  span，从机制上避免幻觉。

  - 将 speculative decoding 的目标从加速改为 faithfulness 验证，思路可迁移：用草稿模型提出候选 span，再用约束目标模型验证是否逐字匹配，既保留一定效率又保证忠实。

  - 对于需要精确抽取的任务（如商品属性提取、广告审核依据、搜索中的摘要引用），优先选择 constrained decoding 而非依赖模型自觉引用，能把抽取准确率从低于
  40% 提升到接近 100%，代价是牺牲部分流畅性，适合准确性优先场景。

  - 该思路可以用于 Agent 的检索增强工具：当 Agent 需要引用外部知识回答时，约束其输出为检索结果的连续片段，可显著降低事实性错误和不可验证引用。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：LLM 作为信息检索接口时容易产生幻觉和忠实性错误，即使使用 RAG 或半抽取式方法，也无法保证输出中的引用或抽取片段逐字来自检索上下文。在安全关键领域，回答必须与认证文档完全一致，现有 speculative decoding 方法又主要关注推理速度而非忠实性。

**方法关键点**：提出 Constrained Hybrid Decoding (CHyD)，一种忠实优先的 speculative RAG 范式。CHyD 复用投机解码架构，但目标转向保证逐字证据提取：通过强制硬解码约束，将生成限制为检索文档中出现的连续 span。这样任何显式引用的片段都必须在提供的上下文中逐字出现。与 SEMQA、NEST 等半抽取或投机 RAG 方法不同，CHyD 将抽取正确性作为首要目标。

**关键结果**：在多个抽象式、抽取式、半抽取式 QA 基准及飞机维护技术数据集上，现有混合方法频繁幻觉引用，技术领域精确抽取准确率低于 40%；CHyD 在不同 SOTA LLM 上均达到接近完美的抽取忠实性。硬约束带来了与流畅度指标的权衡，但提高了精确答案正确性，整体竞争力保持，适合安全关键信息检索应用。
