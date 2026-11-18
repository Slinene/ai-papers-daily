---
title: 'Deal With It: On Better Schedules for Listwise Reranking'
title_zh: Listwise 重排的调度优化：发牌式切分
authors:
- Benjamin Clavié
- Herumb Shandilya
- Hanna Lichtenberg
- Aamir Shakir
- Makoto P. Kato
affiliations:
- Mixedbread
- National Institute of Informatics (NII)
- University of Tsukuba
arxiv_id: '2611.22392'
url: https://arxiv.org/abs/2611.22392
pdf_url: https://arxiv.org/pdf/2611.22392
published: '2026-11-17'
collected: '2026-11-18'
category: RecSys
direction: LLM listwise 重排调度优化
tags:
- Listwise Reranking
- LLM
- Scheduling
- Dealing
- Latency
- Retriever Rank
one_liner: 证明在配额会截断时按 retriever 排名发牌切分最优，提出 DealRank：固定两轮、质量不减且延迟显著更低
practical_value: '- 在 LLM 重排或生成式 item 排序中，若并行分组每组保留固定 top-q，不要用 retriever 输出的连续块（1-20,21-40...），改为按
  retriever rank 轮询发牌（第i组取 i, i+H, i+2H...）。这能把 BlitzRank 的认证调用从 59% 降到 14%，nDCG@10
  无显著损失，可以直接作为 scheduling 组件的输入切分 patch。

  - 如果第一阶段 retriever 质量较强，连续分块损失更大（BM25 差 2.7 nDCG@10，dense 差 4.4）。在电商搜索/广告中，召回模型越准，越应使用轮询切分；该做法零额外成本，只改变分组顺序。

  - 线上 latency 需要可预测时，参考 DealRank：top100 两轮 6 calls，top1000 三轮，固定轮数不依赖认证 call；1000
  候选下比 sliding window 快 11 倍、比并发 BlitzRank 快 1.26 倍。适合有严格 SLA 的 search/ads 重排。

  - 避免直接随机分组：q=4 时随机和发牌接近，但结果依赖 seed；q≤2 时随机明显变差（dense retriever q=1 差 1.3 nDCG@10）。若每组配额小或需要可复现性，采用确定性发牌。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

动机：
Listwise LLM reranker 难以一次可靠排序上百文档，依赖调度。并行调度按组切分并每组固定配额，当某组含有多于配额的 top-k 文档时会截断好结果，迫使额外认证轮。现有工作偏重 token 成本，忽视延迟轮次和切分方式的影响。

方法关键点：
- 把候选按第一阶段 retriever rank 发牌（round-robin）到 H 组，而非连续分块；第 i 组拿 ranks i, i+H, i+2H...。
- 提出 DealRank：top100 时发成 5 组各 20 文档，并行排序每组 top4 进入最终合并 call；top1000 层次化：50 组各保留 2，再发牌成 5 组各保留 4，最终一轮，共 3 轮。
- 证明发牌在期望截断数上最优；连续块随 retriever 变好损失增大；随机切分只是平均平衡，不逐 query 稳定。

关键实验：
- 在 TREC-DL19/DL20 和 BEIR 8 个子集共 1622 queries 上，主评测用 Gemini 3 Flash，并在 6 个 LLM 上验证。
- DealRank nDCG@10 为 57.6，与 sliding window 57.9、BlitzRank 57.8 无显著差异，但只需 2 轮 6 calls、31k tokens；API 中位延迟 3.4s，对比并发 BlitzRank 4.0s、sliding window 13.4s。
- 连续块 vs 发牌：BM25 下差 2.7 nDCG@10，dense retriever 差 4.4；BlitzRank 换上发牌后认证调用从 59% 降至 14%，质量不显著变化。

最值得记住的一句话：
在配额会截断的并行 listwise 重排中，按第一阶段 retriever rank 发牌分组是最优且几乎无代价的调度优化——不要连续分块，发牌。
