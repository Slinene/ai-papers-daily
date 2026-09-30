---
title: Effective Dense Retrieval using Only In-Context Examples
title_zh: 仅用 In-Context 示例实现无需训练的 Dense Retrieval
authors:
- Nour Jedidi
- Abdul Basit Ali
- Hang Li
- Jimmy Lin
affiliations:
- University of Waterloo
- The University of Queensland
arxiv_id: '2609.38099'
url: https://arxiv.org/abs/2609.38099
pdf_url: https://arxiv.org/pdf/2609.38099
published: '2026-09-29'
collected: '2026-09-30'
category: RAG
direction: LLM 免训练 dense retrieval
tags:
- Dense Retrieval
- LLM
- In-Context Learning
- PromptReps
- Zero-Shot
- BEIR
one_liner: RICE 用少量 in-context query-document 示例直接提示 LLM 生成 dense 表示，免训练，在 BEIR 上显著超越同类零样本检索方法
practical_value: '- 电商搜索/召回可直接复用：用少量人工标注 query-商品对作为 in-context examples，prompt 自有
  LLM 生成 query 侧向量和商品侧向量，再接入 FAISS 做 ANN 召回，省去微调检索模型；商品侧离线预计算，query 侧实时生成，工程上可用 vLLM
  加速。

  - 动态 exemplar selection 值得落地：查询时先用 BM25 从示例池检索与当前 query 最相似的示例，能进一步提升召回（FiQA/NFCorpus/SciFact
  上均有增益），适合电商 query 改写或召回场景。

  - 通过换更大/更强的 LLM 可直接提升检索效果，无需重新训练，RICE 用 Qwen3.5-9B 比 Qwen3-8B 平均高 1.6 点，说明 LLM 能力提升能直接迁移到检索表示。

  - 示例标签不必精准：同域 query-doc 对（甚至 random / non-relevant 对）都能带来提升，shuffled/blank 代表词影响很小；因此收集少量同域语料即可，不必精细标注相关性，但要避免跨域示例。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
Decoder-only LLM 直接当 dense retriever 通常需要额外训练。PromptReps 虽能零样本让 LLM 生成表示，但 query 和 document 各自独立编码，缺乏共享任务语境，内积难以准确反映相关性。RICE 想回答：是否只用少量 in-context examples，就能让 LLM 产生可用的 dense 表示，省去训练并快速适配新领域。

**方法关键点**  
- 基于 PromptReps-Dense：prompt LLM 生成一个代表词，取最后一个 hidden state 作为 query/document embedding。
- RICE 构造 in-context exemplars：从任务中取少量 query-document 对，先用 PromptReps 文档 prompt 为每个文档生成代表词 w_i，形成 (q_i, d_i, w_i) 示例。
- 编码时将这些示例前置到 prompt：query 侧示例要求想象相关 passage 并用一个词代表，document 侧示例要求想象相关 query 并用一个词代表；query 和 document 共享同一组示例语境。
- 文档 embedding 离线预计算存 ANN 索引，query embedding 实时生成；若示例包含当前 query/doc，推理时替换为不涉及该样本的其他示例。

**关键实验与结果**  
在 10 个 BEIR 数据集上，用 Qwen3-8B 和 Qwen3.5-9B 评估 Recall@100。相比 PromptReps-Dense，RICE 分别提升平均 3.6 和 2.4 点；Qwen3.5-9B 上 RICE 平均 0.558，超过 HyDE(0.488)、PRF-UMBRELA(0.485) 和 CSQE(0.513)。与自监督训练的 LLM2Vec-Gen(0.542) 相比，RICE 高 1.6 点；但仍低于有监督 Qwen3-Embedding-8B(0.645) 和 BGE-base(0.578)。消融显示：同域 in-context examples 是关键，示例标签准确性不重要；shuffled/blank 代表词影响很小，但随机无关词显著降低效果；动态选择相似示例可进一步提升。  

**最值得记住的一句话**：In-context examples 可以替代 retriever 训练，前提是示例来自目标语料，且示例标签未必需要精准。
