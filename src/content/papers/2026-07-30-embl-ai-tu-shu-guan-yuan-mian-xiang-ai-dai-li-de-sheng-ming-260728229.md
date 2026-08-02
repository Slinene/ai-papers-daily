---
title: 'EMBL AI Librarian: Life-Sciences Knowledge Layer for AI Agents'
title_zh: EMBL AI 图书馆员：面向 AI 代理的生命科学文献知识层
authors:
- Luigi Sigillo
- Matteo Silvestri
- Francesco Tabaro
- Rajat Bhatnagar
- Syed Irtaza Mubashar
- Matt Jeffryes
- Daljit Nijjer
- Vittorio Perera
- Ola Spjuth
- Julio Saez-Rodriguez
affiliations:
- EMBL Rome, European Molecular Biology Laboratory
- European Bioinformatics Institute (EMBL-EBI)
- Sapienza University of Rome
- Uppsala University
- Heidelberg University
arxiv_id: '2607.28229'
url: https://arxiv.org/abs/2607.28229
pdf_url: https://arxiv.org/pdf/2607.28229
published: '2026-07-30'
collected: '2026-08-02'
category: RAG
direction: 面向 AI 代理的文献检索 · 证据提取
tags:
- RAG
- Literature Retrieval
- AI Agents
- Evidence Extraction
- LLM Orchestration
- Life Sciences
one_liner: 将结构化文献搜索升级为自然语言证据检索层，大幅提升科学代理的问答、验证与综合性能
practical_value: '- **领域知识层架构可迁移至电商导购 Agent**：将核心思想——用 LLM 将自然语言问题分解为互补子查询，对接现有搜索引擎
  API，并以“证据”而非整篇文档返回——直接用于构建商品知识检索层，为电商对话推荐 Agent 提供精准的商品属性、评价摘要或政策依据。

  - **子查询规划与合并策略**：借鉴其 LLM 动态生成多个子查询、去重并汇聚证据的方式，可用于复杂推荐解释或多条件检索场景，避免 Agent 硬编码搜索语法，提升召回覆盖率和信息密度。

  - **评估方法启发**：论文使用的 Citation F1 指标可用于推荐系统生成解释时的引用准确率评估，尤其适合需要引用原文（如用户评价）的场景，可设计类似的证据覆盖度与精确度指标。

  - **实时检索与证据定位流水线**：该工作结合了现有搜索引擎的实时检索与 LLM 的精读定位，方案轻量且无需重新索引，电商领域可直接套用此模式，将商品搜索 API
  与 LLM 结合，为 Agent 提供“事实性回答”能力，降低幻觉风险。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：AI 代理访问科学文献的需求剧增，但传统数据库（如 Europe PMC）为人类设计，要求关键词语法且返回全文，代理需多次搜索并通读证明，效率低下。

**方法**：提出 EMBL AI Librarian，一个面向代理的知识层，以自然语言为接口。核心是单个 LLM 统一协调：将用户问题分解为多个互补子查询，通过 Europa PMC 实况搜索执行，获取相关论文后从中精确定位并提取证据片段，最终返回给代理。无需重训检索器，直接利用现有搜索引擎能力。

**结果**：在四个基准上验证：
- 文献综合（ScholarQA-Bench）：Citation F1 达 73.8，比强基线（55.9）提升超 16 点；
- 声明验证（ProClaim-eval）：与专家共识的平均一致性从 75.0 提升至 80.0；
- 开放域问答（LitQA2）：GPT-5.4 代理在 Librarian 上的准确率（78.9）比直接网络搜索（70.3）高出 8.6 点；
- 实验室基础任务（LAB-Bench）：准确率从 50.5 提升至 54.6。
表明该知识层能显著增强生命科学代理的检索与推理能力。
