---
title: 'EviQE: Evidence Selection for LLM-Based Query Expansion'
title_zh: 基于证据选择的 LLM 查询扩展：多改写器互补文档池与相关性筛选
authors:
- Hai Son Le
- Amin Bigdeli
- Shirin Seyedsalehi
- Morteza Zihayat
- Ebrahim Bagheri
affiliations:
- Toronto Metropolitan University
- University of Waterloo
- University of Toronto
arxiv_id: '2609.14875'
url: https://arxiv.org/abs/2609.14875
pdf_url: https://arxiv.org/pdf/2609.14875
published: '2026-09-14'
collected: '2026-09-16'
category: QueryRec
direction: LLM 查询扩展 · 证据选择
tags:
- Query Expansion
- Evidence Selection
- LLM
- Relevance Estimation
- BM25
- BEIR
one_liner: EviQE 将 LLM 查询扩展重构为文档证据选择问题，聚合多改写器检索结果并筛选后单轮生成，显著提升 TREC DL 与 BEIR 检索效果
practical_value: '- 在电商搜索的 query 改写/扩展场景中，不要只依赖单一改写器或单一检索结果作为生成上下文。用多个改写器（如原始 query、LLM
  直改、伪相关反馈、HyDE 等）并行召回文档，合并去重后作为候选池，再让 LLM judge 按与原始 query 的相关性打分选 top-B 篇作为生成 evidence，能显著提升改写
  query 的召回质量。

  - 证据选择比多轮迭代更划算：EviQE 一轮证据选择即可超过多轮 ThinkQE，且增加迭代会引入噪声。实际线上系统可把计算预算从多轮 RAG 改成“并行多路召回
  + 一次性精筛 + 单轮生成”，降低延迟和成本。

  - 用 LLM 做 relevance judge 时，建议采用 graded relevance（0-3）并固定 judge 模型，不要用简单的 agreement
  或 RRF。论文中 LLM-Score 明显优于 frequency/RRF，且跨 generator 骨干稳定；在商品搜索中可复用类似打分来挑选高质量商品详情段落或用户评论作为改写证据。

  - 候选池大小不必盲目扩大：4 个改写源（原始+CSQE+LameR+MuGI）已恢复大部分收益，增加到 11 个提升很小。实际部署可从少量高质量改写器开始。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：LLM-based query expansion 目前大多关注如何生成改写，但 corpus-aware 方法中作为生成条件的 retrieved documents 如何选择被忽视。不同 reformulation 方法检索到的文档可能互补，但现有方法通常只使用单一改写器的检索结果，或每轮同时改变文档和改写，无法区分收益来源。

**方法关键点**：
- EviQE 将 query expansion 定义为文档选择问题：给定 query，用 portfolio of 10+ reformulators（原始 query + CSQE, LameR, MuGI, Query2Doc variants, QA-Expand, GenQR 等）各自检索 top-K，union 成候选池。
- 选择 top-B 文档作为 evidence，输入固定 generator 生成 expansion，拼接原 query 后检索。选择策略包括 Frequency（跨源 agreement）、RRF、LLM-Score（DeepSeek-V3 judge 按 graded relevance 0-3 打分）。
- 所有方法使用相同 BM25 retriever、generator、prompt 和文档预算，隔离证据选择的影响。

**关键实验与结果**：在 TREC DL 2019/2020/DL-Hard 和 5 个 BEIR 数据集上，以 nDCG@10 为指标。
- 改写器在 query 级命中率高（0.96），但文档级覆盖率低（0.07 左右），说明互补性强；pool 的召回增益比最佳单一源高 +0.043 到 +0.153。
- LLM-Score 选择证据优于冷启动 ThinkQE（DL avg 0.5494→0.5760，BEIR 0.5343→0.5513），也优于 Best QR 和 Best Single；比频率/RRF 更有效。
- 候选池从 1 扩到 4 收益明显，再扩到 11 提升很小；多轮迭代下 LLM-Score 第一轮即最优，后续下降。

**最值得记住的一句话**：将 LLM 查询扩展从“生成改写”转向“选择证据”，用多改写器互补检索 + LLM 相关性筛选，单轮即可超过多轮迭代，且效果主要来自证据质量而非生成多样性。
