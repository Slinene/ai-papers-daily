---
title: 'Route Me If You Can: A Benchmark for Query Reformulation Selection'
title_zh: QueryRoute：查询改写选择的标准化评测基准
authors:
- Hai Son Le
- Negar Arabzadeh
- Amin Bigdeli
- Radin Hamidi Rad
- Sajad Ebrahimi
- Charles L. A. Clarke
- Ebrahim Bagheri
affiliations:
- Toronto Metropolitan University
- University of California, Berkeley
- University of Waterloo
- Mila - Quebec AI Institute
- University of Toronto
arxiv_id: '2609.14885'
url: https://arxiv.org/abs/2609.14885
pdf_url: https://arxiv.org/pdf/2609.14885
published: '2026-09-14'
collected: '2026-09-16'
category: QueryRec
direction: 查询改写选择 / Query Routing 基准
tags:
- Query Reformulation
- Benchmark
- Query Routing
- LLM
- QPP
- Information Retrieval
one_liner: 冻结查询改写候选池与检索结果，系统评估改写选择器在跨检索器/领域下的上限与差距
practical_value: '- 线上如果有多个查询改写/扩展策略（LLM prompt 变体、伪文档、关键词扩展），不要只按平均 A/B 选一个固定策略；应按
  query 路由，且先离线构建候选池 + 各改写召回结果，复用 QueryRoute 的 action–outcome matrix 思路，把路由评估变成只读决策问题。

  - LLM-as-judge 在 BM25 稀疏检索上最强，但在 BGE/SPLADE 等更强检索器下，没有任何学习型 selector 超过固定最优改写；说明稠密检索已经吃掉改写收益时，业务应优先投入检索器质量或相关性精排，而不是改写路由。

  - 评估 selector 时，均值 nDCG 会掩盖 query 级路由行为；建议同时加 near-oracle rate、help/hurt rate、regret、selection
  entropy 等决策质量指标，否则两个均值接近的方法可能一个靠少数 query 拉高、另一个稳定性更好。

  - 工程实现可参考：离线落 query 原词、候选改写、多 retriever 召回列表和 retrieval score；用 QPP/embedding similarity
  router 做低成本冷启动，LLM-as-judge 做高成本兜底，按 retriever 类型分别评估。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM 查询改写能提升检索，但没有任何单一改写策略在跨 query、领域、retriever、模型 backbone 上始终最优。实际推理时会遇到一个选择问题：给定原 query 和一池候选改写，应该把哪一个发给 retriever。现有研究难以比较，因为各自的改写池、retriever、相关性信号、训练标签和评估指标都不同。QueryRoute 的核心是冻结这些昂贵中间产物，让 query 改写选择变成一个可复现的有限动作决策问题。

### 方法关键点
- 构建 action–outcome matrix：对每个 query 存储原词、10 种 LLM 改写候选、3 类 retriever（BM25/SPLADE/BGE）下的 ranked list、retrieval score、目标指标 utility，以及 per-query oracle-best 候选集合。
- 数据规模：3,757 个 query，11 个候选系统（原 query + 10 种改写），5 个 LLM backbone（Qwen2.5-7B/72B、Llama-3.1-8B/3.3-70B、GPT-4.1），3 个 retriever，共 619,905 个 query–candidate–retriever 结果。
- 覆盖 TREC DL、BEIR 六个数据集、BRIGHT 七个推理密集子集；改写方法包括 keyword-level（GenQR/Query2E）、document-level（Query2Doc/QA-Expand/MuGI）、corpus-grounded（CSQE/LameR）。
- 评测两类指标：检索效果（nDCG@10 为主）和决策质量（Near-Oracle、Help/Hurt、regret、pairwise accuracy 等）。
- 对比 selector 家族：supervised BERT 分类、similarity-weighted routing、matrix factorization routing、QPP（pre/post/neural）、LLM-as-judge（UMBRELA 风格）。

### 关键实验
在 Qwen2.5-7B-Instruct + BM25 下，TREC DL 上 Original/Best-single/Oracle 分别为 0.424/0.559/0.666，BEIR 为 0.437/0.503/0.604，BRIGHT 为 0.170/0.315/0.399；oracle headroom 明显，但当前 selector 只能部分回收。LLM-as-judge 是 TREC DL 和 BEIR 上最强的非 oracle selector（0.588 / 0.515），在 BRIGHT 上与 Best-single 基本持平。

跨 retriever 结果更关键：在 BGE/SPLADE 下，没有学习型 selector 超过固定最优改写；BEIR/SPLADE 上学习型 selector 掉到 0.22–0.28，而固定基线为 0.525。这说明 retriever 越强，改写路由的收益越容易被抹平。此外，均值 nDCG 会掩盖 query 级行为：LLM-as-judge 在 TREC DL 的 near-oracle rate 最高 60.5%，但 Neural-QPP 的 help/hurt 表现更好。

### 最值得记住
> Query 改写选择不能在单一稀疏检索设置下下结论；更强 retriever 会显著侵蚀自适应改写路由的收益，评估必须同时看 retriever 和决策质量指标。
