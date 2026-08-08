---
title: 'Teaching Nemotron Greek: Mining a Corpus, Adapting Retrieval, and Grounding
  Generation for Modern Greek across Specialist Domains'
title_zh: 教Nemotron希腊语：专业领域现代希腊语RAG全流程构建
authors:
- Ayoub Kirouane
- Christos Petrocheilos
affiliations:
- Sophea AI, KIEFER SA, Athens, Greece
arxiv_id: '2608.05138'
url: https://arxiv.org/abs/2608.05138
pdf_url: https://arxiv.org/pdf/2608.05138
published: '2026-08-04'
collected: '2026-08-08'
category: RAG
direction: 低资源语言RAG全栈适配 · 领域检索增强生成
tags:
- RAG
- Greek NLP
- Dense retrieval
- Reranker
- LoRA
- MoE
one_liner: 为低资源语言从头搭建检索增强生成系统，合成监督、微调嵌入与重排、适配生成，并发布基准HERA。
practical_value: '- **不要迷信多语言密集检索**：在特定领域（如电商商品描述、客服文档），先跑一个BM25作为基线，很可能强过通用多语言嵌入模型，尤其在低资源语言场景。

  - **小规模领域检索对微调有大收益**：仅用6.5万合成希腊语检索对微调1B嵌入模型，nDCG@10从0.362涨到0.835。在电商垂直领域，可以自动构建（query,
  商品/文档）对来微调嵌入模型，成本低但效果显著。

  - **重排器也需要领域适配**：现成跨编码器重排器在不同领域表现不一致，用领域数据微调后能变成稳定增益。构建RAG系统时，别忽略重排环节的定制训练。

  - **LoRA微调MoE阅读器大幅提升答案质量**：仅LoRA调优30B-A3B的MoE模型，答案正确率从29.4%升至66.9%，且忠实性和引用质量显著改善。对于需要从长文档中提取证据的场景（如电商说明书、政策文档），用LoRA高效地让大模型接地气。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**
现代希腊语被主流多语言检索模型忽略，但在法律、能源、金融、医疗等专业领域，长文档、密集术语的RAG需求迫切。

**方法关键点**
1. **语料挖掘与合成监督**：采集希腊语专业文档，用翻译构造检索对和生成训练数据。
2. **检索栈适配**：基于Nemotron嵌入模型，用65,773对希腊语检索对微调；适配交叉编码器重排器；使用LoRA调优Nemotron 30B-A3B MoE模型作为阅读器。
3. **基准构建**：发布首个大规模希腊语RAG基准HERA。

**关键结果**
- 初始时，零参数的BM25击败所有现成多语言密集检索模型。
- 微调后嵌入模型nDCG@10从0.362提升至0.835，并在通用域测试中比未调参版本高出+0.399，但对BM25的优势仅在适配域保持。
- 适配重排器在所有专业域获得一致增益。
- LoRA调优后答案正确率从29.4%升至66.9%，忠实性与引用质量显著提高。
