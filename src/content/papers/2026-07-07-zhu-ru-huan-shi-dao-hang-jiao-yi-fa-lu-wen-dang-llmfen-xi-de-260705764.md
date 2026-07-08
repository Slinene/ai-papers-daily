---
title: Inject or Navigate? Token-Efficient Retrieval for LLM Analysis of Transactional
  Legal Documents
title_zh: 注入还是导航？交易法律文档LLM分析的令牌高效检索
authors:
- Mahmoud Hany
- Mourad ElSheraey
- Mahmoud Said
- Peter Naoum
affiliations:
- Syntheia Pty Ltd
arxiv_id: '2607.05764'
url: https://arxiv.org/abs/2607.05764
pdf_url: https://arxiv.org/pdf/2607.05764
published: '2026-07-07'
collected: '2026-07-08'
category: RAG
direction: RAG检索策略比较与效率优化
tags:
- RAG
- Legal AI
- Token Efficiency
- Embedding Retrieval
- LLM Navigation
- Structured Index
one_liner: 比较全量注入、嵌入检索与LLM导航索引，证明检索可大幅降低token消耗且质量不降
practical_value: '- **结构感知分块（structure-aware chunking）**：对电商中的长文档（商品说明书、合同、政策）进行结构分块，避免全文注入，大幅降低推理成本，可迁移到产品FAQ或合规文档问答。

  - **嵌入检索+重排序管道**：嵌入检索（NAVEMBED）配合重排序能在长文档QA中达到与全量注入几乎相当的质量，同时输入token减少17⁻30倍，适合构建低延迟、低成本的商品知识库检索。

  - **紧凑结构化索引与LLM导航**：对于成本敏感的Query改写或推荐解释生成，借用LLM导航结构化索引（NAVINDEX）的思路，用极轻量的索引替代大段文本，使回答上下文减少约56倍，成本降低25%。

  - **缓存交叉规则**：论文导出的封闭解可用于决策何时缓存全量文档更划算，可借鉴到广告素材库或推荐理由生成等有固定语料的场景，指导缓存策略以优化总成本。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：法律文档分析中，将整个语料注入LLM上下文窗口虽能保证召回，但token开销随语料线性增长，且长上下文退化明显。需要平衡质量与效率的检索方案。

**方法**：提出结构感知分块，并对比三种模式：①全量注入（基线）；②嵌入检索+重排序（NAVEMBED）；③LLM在紧凑结构化索引上自主导航（NAVINDEX）。构建20道题的基准，包含18道文档相关题和2道域外对照题，采用位置偏差控制、参考答案锚定的两两对比裁判。

**关键结果**：NAVEMBED在18题中与注入持平16次，且输入token减少17.3×（GTE配置达29.9×）；NAVINDEX在所有18题上与注入持平，总token减少1.61×，回答上下文缩小约56×，成本降低25%。推导出缓存交叉规则：仅当语料小于检索负载约10倍时，缓存注入才更便宜。
