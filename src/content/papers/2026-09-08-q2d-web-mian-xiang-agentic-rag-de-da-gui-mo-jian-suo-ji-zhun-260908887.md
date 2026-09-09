---
title: 'Q2D-Web: A Large-Scale Benchmark for Retrieval in Agentic RAG Systems'
title_zh: Q2D-Web：面向 Agentic RAG 的大规模检索基准
authors:
- Maximilian Schall
- Sedigheh Eslami
- Markus Krimmel
- Antoine Chaffin
- Louis Milliken
- Bo Wang
- Denis Bykov
affiliations:
- Perplexity AI
arxiv_id: '2609.08887'
url: https://arxiv.org/abs/2609.08887
pdf_url: https://arxiv.org/pdf/2609.08887
published: '2026-09-08'
collected: '2026-09-09'
category: Eval
direction: Agentic RAG 首阶段检索评估
tags:
- Agentic RAG
- Retrieval Benchmark
- Relevance Judgment
- Subcorpus Sampling
- Recall@1000
- First-stage Retriever
one_liner: 构建 190M 文档 / 70k agent 改写查询的私有检索基准，发现全量评估排序可用 30% 子语料复现
practical_value: '- **评估检索器必须用改写后的 query**：生产 Agentic RAG 里 first-stage retriever
  接收的是 LLM 改写/分解后的 query，不是用户原始 query。电商/搜索团队如果自建 RAG 或 Agent 搜索，应收集线上改写 query 构建离线评估集，否则会低估或误判检索效果。

  - **多信号 qrels 降低 false negatives**：单一点击或引用标签召回很低，会误伤检索器。可借鉴其做法：组合『曝光点击/成交/加购』『人工标注』『LLM
  judge 对未标注候选再判』成多套 qrels，分别评测并观察排序是否稳定；电商搜索尤其适合用点击、加购、成交、客服负反馈等构造多源 label。

  - **RRF 子语料采样加速评估**：保留所有 positive 文档，用 RRF 融合多个 retriever 的 top-k 结果抽取约 30% 文档，就能保持全量排序，评估成本下降约
  2/3。业务中大规模召回模型快速迭代时可以直接复用这个 trick。

  - **BM25 与 dense 互补明显**：BM25 总 Recall 最低，但 unique positive coverage 最高，说明 lexical
  和 dense 覆盖不同相关文档。电商搜索里 BM25 对品牌型号、精确实体仍是重要召回通路，建议保留 BM25 路并与 dense 结果做 RRF 融合。

  - **分 query 类型/领域/语言看召回**：论文显示 neural retrievers 在 agent 生成的 support queries 上明显弱于
  primary queries，BM25 相反；不同品类/语言差异也大。上线前应按改写 query 类型、类目、语言分片评估，不能只看一个平均 Recall。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
现有 IR 基准无法同时满足生产级 Agentic RAG 对 first-stage retriever 的评估需求：要么 query 数量太少（TREC Web 每年 50 条），要么 corpus 规模不足（MS MARCO v2 12M 文档），要么 relevance label 极浅（MS MARCO Web 每 query 仅 1 个点击 label），且大量基准只测人类原始 query，而生产检索器实际输入的是 agent 改写后的 query。这会系统性低估检索器表现，并引入大量 false negatives。

## 方法关键点
- **数据构建**：从 Perplexity 9 个月生产流量采样 69,721 条 agent 改写 query（17.7% primary / 82.3% support），覆盖 10 种语言；对每个 query 取 top-5000 结果经 MinHash-LSH 去重，得到约 190M 文档的 web corpus。
- **三套 relevance judgments**：① Citation：agent 实际引用即相关；② Web Ranking：内部生产系统 top-50；③ Combined+LLM-Judged：前两者并集，并对未标注候选用 DeepSeek-V4-Flash 做 strict relevance 判断。平均每个 query 有 99.6 个相关文档，大幅降低 false negatives。
- **子语料采样**：用 RRF 融合 9 个 pre-2025 retriever 的 top-1000 结果，保留所有 positives 和挑战性 distractors，抽取约 31.7% 文档作为快速评估集。
- **评测协议**：13 个 open-weight retrievers（BM25、10 个 dense、2 个 late-interaction），主指标 Recall@1000，辅以 Recall@100 和 nDCG@10。

## 关键结果
- **子语料采样有效**：RRF k=1000 保留 31.7% corpus，Kendall's τ_b = 1.00，完全复现全量排序；Recall@1000 平均仅膨胀 5.1 点；4B dense 模型评估成本从 4608 降到约 1500 H200 GPU-hours。
- **模型排序**：pplx-embed-v1-4b 在 Web Ranking 和 Combined 的 Recall@1000 最优；Nemotron-3-Embed-8B 在 Citation 最优，且在 Recall@100 / nDCG@10 上更强，说明不同 retriever 在深召回和前置精度上有不同优势。
- **BM25 的价值**：BM25 总 Recall@1000 最低（44.77），但 unique positive coverage 最大，贡献 14,621 个其他 retriever 都未召回的相关文档，是第二名的近 6 倍。
- **错误分析**：Hard positives 中 51.1% 是 lexical mismatch，17.7% 是长文档 truncation，15.4% 是多语言跨语种。

## 值得记住的一句话
评估生产 RAG 首阶段检索器，必须用 agent 改写后的 query 和多信号 qrels，否则指标会偏乐观；保留全量 positives 的 RRF 子语料采样可以降本 2/3 且不打乱模型排序。
