---
title: 'Bridging the Question-Answer Gap in Retrieval-Augmented Generation: Hypothetical
  Prompt Embeddings'
title_zh: 桥接 RAG 中问答鸿沟的假设提示嵌入
authors:
- Domen Vake
- Jernej Vičič
- Aleksandar Tošić
affiliations:
- University of Primorska, Faculty of Mathematics, Natural Sciences and Information
  Technologies
- InnoRenew CoE
- Research Centre of the Slovenian Academy of Sciences and Arts, The Fran Ramovš Institute
arxiv_id: '2607.29402'
url: https://arxiv.org/abs/2607.29402
pdf_url: https://arxiv.org/pdf/2607.29402
published: '2026-07-31'
collected: '2026-08-03'
category: RAG
direction: RAG 检索优化 · 假设嵌入
tags:
- RAG
- Hypothetical Prompt Embeddings
- Dense Retrieval
- Question-Answer Gap
- Index-time Optimization
- Embedding
one_liner: 将假设内容生成从查询时移至索引阶段，用预计算的假设提示嵌入将检索变成问题-问题匹配
practical_value: '- **预计算假设查询嵌入，替换在线 HyDE**：在电商搜索或客服 RAG 中，可将每个商品详情页、政策文档预先用 LLM 生成多个可能用户会问的问题（hypothetical
  prompts），用这些问题嵌入直接建索引，在线时用户查询嵌入直接与问题嵌入匹配，完全消除查询时调用 LLM 的延迟和成本。

  - **多假设覆盖长尾查询**：每个 chunk 生成 5-10 种不同表述的假设问题，能覆盖更广泛的用户表达习惯，尤其适合电商搜索中同义但非规范表达的查询，提升召回率和上下文精度。

  - **与重排序、多向量检索等兼容**：HyPE 仅改变索引构建方式，不影响线上检索架构，可直接叠加现有的粗排-精排流水线、多向量延迟交互模型（如 ColBERT）或查询分解，适合渐进式落地。

  - **监控与质量保障**：生成假设问题时需要控制幻觉，可先用小模型生成再过滤，或结合类目体系约束生成范围，保证问题与文档内容一致，这比 HyDE 在线生成更容易审计和修复。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：RAG 系统中，用户查询与文档文本的风格差异导致检索相关性不足。运行时方案如 HyDE 通过让 LLM 对查询生成假设文档来对齐，但引入高昂的在线延迟与成本。

**方法**：提出 HyPE，将假设内容生成从查询时转移到索引阶段。索引时为每个文档块使用 LLM 预生成多个假设提示（即该块可能回答的问题），然后用这些提示的嵌入作为该块的表示进行索引。在线检索时，用户查询直接与这些预计算的问题嵌入匹配，从而实现问题到问题的快速检索，无需任何运行时生成。

**关键结果**：在六个数据集上，HyPE 将检索上下文精度最高提升 42 个百分点，声明召回率最高提升 45 个百分点，同时与重排序、多向量检索、查询分解等技术正交兼容，无额外在线延迟。
