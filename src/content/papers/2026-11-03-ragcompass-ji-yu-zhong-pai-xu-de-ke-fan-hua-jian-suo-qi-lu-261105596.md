---
title: 'RAGCompass: Generalizable Retriever Routing via Reranking'
title_zh: RAGCompass：基于重排序的可泛化检索器路由
authors:
- Valentin Six
- Mufei Li
- Dongqi Fu
- Yinglong Xia
- Hong Li
- Pan Li
affiliations:
- University of Virginia
- Georgia Institute of Technology
- Meta
arxiv_id: '2611.05596'
url: https://arxiv.org/abs/2611.05596
pdf_url: https://arxiv.org/pdf/2611.05596
published: '2026-11-03'
collected: '2026-11-05'
category: RAG
direction: RAG 检索器路由 · 证据重排序
tags:
- retriever routing
- reranker
- RAG
- generalization
- utility supervision
- comparison head
one_liner: 将检索器路由重构为对证据集的重排序，用效用监督微调reranker，实现跨语料/检索器/reader泛化
practical_value: '- 电商搜索多路召回（BM25/向量/图等）场景下，可借鉴用小型reranker读取每个召回通道的top-k文档并打分，选择最优通道供LLM生成答案或推荐理由；监督信号用下游答案质量而非文档相关性，因为nDCG与答案F1在43%的query上选择不同。

  - 无retriever特定参数的comparison head设计支持新召回源即插即用，无需重训路由器；这对线上频繁迭代（新增embedding模型、调整语料）非常友好，避免高成本重训。

  - 训练目标用KL散度对齐分数分布与效用分布，通过共享归一化制造候选间竞争，实现端到端选择；实现简单，可替代复杂的listwise损失。

  - 推理开销约0.2s/query（占5-6s管道的3.9%），检索可并发，适合对延迟敏感但允许并行调用的搜索推荐系统。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
多个retriever在RAG中的平均性能接近，但oracle选择最佳retriever可达3倍F1（0.751 vs 0.278），说明提升空间在于按query选择而非设计新retriever。现有router大多仅基于query特征或固定retriever池，无法适应新语料、新检索器或reader升级，且缺乏泛化测试。核心问题：如何根据query和每个retriever返回的证据集选择最适合的retriever。

**方法关键点**
- 将路由定义为对证据集的重排序：给定query q和R个retriever返回的top-k passage集Di，排序准则为答案效用 yi = F1(A(q, Di), a*)，其中A为固定reader。
- 使用Qwen3-Reranker-0.6B作为共享backbone，每个retriever的passages单独编码，输出yes-logit作为分数；再加两层transformer comparison head对R个隐藏表征联合比较，输出最终选择。
- 训练目标为KL散度对齐分数分布与效用分布（温度τ），共享归一化制造候选间竞争；两阶段训练：先微调backbone，再冻结backbone训练head；backbone和head均无retriever特定参数，支持新检索器即插即用。
- 监督信号采用答案效用而非文档相关性，因为nDCG与答案F1在约43%的query上选择不同retriever。

**关键实验**
在四个QA数据集（NQ, MuSiQue, HotpotQA, 2WikiMultihopQA）上，从五种异构retriever（dense, BM25, SPLADE-v3, ColBERTv2, HippoRAG2）中路由。RAGCompass比最佳固定retriever提高+7.7pp（相对28%），比最强baseline MoR高+3.5pp；同时提高recall@5 +5.0、nDCG@5 +1.3。泛化测试：未见语料（留一数据集）保留80%以上增益；未见检索器（留一retriever）损失仅0.16–1.17pp；未见reader（换用Qwen2.5-7B）保留71%增益。而三个query-only路由器在分布内均无法超过最佳固定retriever，泛化时全部跌破。

**核心结论**
路由信号应来自检索到的证据本身，并用下游答案效用（而非文档相关性）监督；无retriever特定参数的设计赋予了跨语料、跨检索器、跨reader的泛化能力。
