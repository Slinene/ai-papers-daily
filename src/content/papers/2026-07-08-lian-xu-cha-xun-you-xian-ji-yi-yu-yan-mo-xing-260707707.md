---
title: 'Co-LMLM: Continuous-Query Limited Memory Language Models'
title_zh: 连续查询有限记忆语言模型
authors:
- Yair Feldman
- Linxi Zhao
- Nathan Godey
- Dongyoung Go
- Yilun Hua
- Kilian Q. Weinberger
- Jennifer J. Sun
- Yoav Artzi
affiliations:
- Cornell University
arxiv_id: '2607.07707'
url: https://arxiv.org/abs/2607.07707
pdf_url: https://arxiv.org/pdf/2607.07707
published: '2026-07-08'
collected: '2026-07-09'
category: LLM
direction: 连续向量查询 + 外部可读知识库
tags:
- LMLM
- Continuous Query
- Retrieval Augmented Generation
- Knowledge Base
- Factual Precision
- Perplexity
one_liner: 用连续向量查询替代关系型查询，从可读知识库检索知识，提升语言模型事实精度与数据效率
practical_value: '- 在电商推荐理由生成中，可将商品知识（属性、卖点、用户评价）存入可读知识库，用连续向量查询实时检索，保证生成事实正确且可归因，知识可动态更新无需重训模型。

  - 连续查询方式免去设计结构化查询模板的成本，模型自动学习如何表达信息需求，适配搜索、推荐中的多样化上下文。

  - 提出的自由文本事实标注流程可迁移到业务语料上，自动构建知识库条目，降低人工维护负担。

  - 模型在数据效率上的优势（360M 规模仅用 1/40 数据即超越基线）对资源受限的垂域推荐微调有参考价值，可减少对大规模预训练数据的依赖。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有有限记忆语言模型（LMLM）将事实知识外存于关系型知识库，查询受限于固定模板与 schema，灵活性不足。本文提出连续查询 LMLM，用连续向量作为知识库的键，值保持为可读文本，使模型能生成任意形式的向量查询，低成本集成检索知识。同时设计自动标注 pipeline，从任意文本中识别事实片段，突破此前依赖 Wikipedia 的限制。

**方法关键点**：
- 知识库由 (连续向量键, 文本知识值) 对构成，向量键通过句子编码器从文本片段获得。
- 预训练时，模型基于当前上下文生成连续查询向量，检索 top-k 文本知识，拼接后用于下一 token 预测，训练同时优化查询生成与知识利用。
- 事实标注 pipeline：用大模型先对文档进行事实边界标注，过滤出信息密度高的片段，生成训练语料。

**关键结果**：
- 在 Wikipedia 和 FineWeb-Edu 预训练，多尺度下困惑度全面优于先前 LMLM 和 vanilla LLM。
- 360M 参数模型用 40x 更少数据（约 10B tokens）即达到比更大数据量模型更低的困惑度。
- 在 SimpleQA 事实评测上，与 gpt-4o-mini 持平，高于 Claude Sonnet 4.5。
