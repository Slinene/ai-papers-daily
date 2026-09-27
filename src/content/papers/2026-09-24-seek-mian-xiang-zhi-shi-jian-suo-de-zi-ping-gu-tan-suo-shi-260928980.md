---
title: 'Seek: Self-Evaluative Exploration for Knowledge Retrieval'
title_zh: Seek：面向知识检索的自评估探索式迭代检索框架
authors:
- Amin Bigdeli
- Radin Hamidi Rad
- Negar Arabzadeh
- Sajad Ebrahimi
- Hai Son Le
- Charles L. A. Clarke
- Ebrahim Bagheri
affiliations:
- University of Waterloo
- Mila – Quebec AI Institute
- University of California, Berkeley
- University of Toronto
- Toronto Metropolitan University
arxiv_id: '2609.28980'
url: https://arxiv.org/abs/2609.28980
pdf_url: https://arxiv.org/pdf/2609.28980
published: '2026-09-24'
collected: '2026-09-27'
category: RAG
direction: LLM 迭代式检索与相关性反馈
tags:
- Iterative Retrieval
- Relevance Feedback
- LLM Assessor
- Query Expansion
- Training-free
- Reasoning-Intensive Retrieval
one_liner: 训练无关的迭代检索框架，用 LLM 生成伪段落扩展 query 并分级评估反馈，突破单次检索 recall 上限
practical_value: '- 用「LLM 生成 pseudo-passage 扩展 query → 重新召回 → LLM 分级标注」的测试时循环替代固定候选池
  rerank，能在不训练排序模型的情况下找回 BM25 漏掉的商品/内容；电商搜索中可让 LLM 根据 query 生成伪商品描述、属性组合或场景描述来提升长尾和复杂约束
  query 的 recall。

  - 显式利用正负反馈：高分结果强化有效 facet（风格、价格带、使用场景），低分结果作为 drift 在下一轮 prompt 中抑制，而不是只做简单二值相关；可借鉴
  UMBRELA 0-3 分级判断，使后续 query 扩展更精准。

  - 成本控制设计可直接复用：每轮只评估 top-K 未见文档、最多 T 轮、top-K 全为最高分或连续两轮 top-K 不变时早停；工程上不需要全库 dense
  embedding，适合快速接入已有搜索链路。

  - 最终排序采用两阶段：assessor 打过分文档按 grade 优先、未评估文档按 retriever 分数补位；对 Agent 检索工具友好，因为输出的是已评估的可解释候选池，比原始
  BM25 更适合下游推理或商品推荐生成。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

动机：
现有 LLM retriever/reranker 与语料基本都是一次交互：reranker 只能重排固定 top-100 候选，初排漏掉的相关文档永远无法恢复。对 reasoning-intensive query，lexical mismatch 和隐式约束使单次 BM25 的 recall 尤其不足。Seek 的思路是不训练排序器，而在测试时通过多轮检索、评估和反馈来逐步扩大候选池。

方法关键：
- 每轮由 LLM generator 根据原 query 和累计 feedback pool 生成 n=5 个 pseudo-passages；第一轮只用原 query，后续轮强化高分的相关模式、抑制低分带来的 retrieval drift。
- 扩展后的 query 交给 retriever 从全库重新检索，而不是重排固定候选，因此每一轮都能发现新文档。
- LLM assessor 用 UMBRELA 对 top-K=10 的未见文档按原 query 做 0-3 分级，加入 feedback pool；评估不依赖扩展 query，保证与用户信息需求锚定。
- 终止条件包括 quality saturation、coverage saturation 或最大 5 轮；最终排序以 assessor 打分优先，未评估文档用 retriever 分数补位。

关键实验：
在 TREC DL19/DL20 和 BRIGHT 的 7 个推理密集子域上，Seek 与 dense retriever 和 trained reranker 比较。用 Qwen2.5 时 TREC DL 为 71.6/65.1，与训练过的 Qwen2.5 reranker 相当；BRIGHT 平均 nDCG@10 为 30.9，超过同 backbone 的所有训练 baseline。Qwen3 提升到 33.3，超过 ERank-4B 约 22%；GPT-4.1 达到 37.4，在 6/7 子域最高。Recall@100 上，Biology 从 42 提升到 82，Psychology 从 38 提升到 72。更换 backbone retriever 后，Seek+BM25 的 30.9 接近 Seek+ReasonIR 的 32.3，说明迭代反馈是主要收益来源。

最值得记住的一句话：测试时的自评估迭代检索，比继续堆训练好的 reranker 更能突破单次检索的 recall 上限。
