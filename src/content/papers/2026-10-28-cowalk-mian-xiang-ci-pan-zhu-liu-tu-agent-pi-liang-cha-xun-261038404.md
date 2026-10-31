---
title: 'CoWalk: Cooperative Walks for Agentic Batch Queries on Disk-Resident Graphs'
title_zh: CoWalk：面向磁盘驻留图 Agent 批量查询的协作游走
authors:
- Qiao Liang
- Zhiguang Chen
- Yue Yu
- Nong Xiao
affiliations:
- Sun Yat-sen University
- Pengcheng Laboratory
arxiv_id: '2610.38404'
url: https://arxiv.org/abs/2610.38404
pdf_url: https://arxiv.org/pdf/2610.38404
published: '2026-10-28'
collected: '2026-10-31'
category: Other
direction: 向量检索 · 批量协同查询优化
tags:
- ANN
- vector search
- query batching
- disk-resident graph
- cooperative search
- I-O optimization
one_liner: 让批量语义相关向量查询在同一线程协作遍历图索引，每页只读一次、所有查询共享打分，显著减少 I/O 与距离计算
practical_value: '- 如果业务中存在 query 改写、多路并发召回或多 rollout 评测等批量语义相关向量查询，可在服务端把同一 batch
  绑定到同一线程/执行器，共享页读取与打分，直接降低磁盘 ANN 的重复 I/O。

  - 仅加共享 page cache 不一定能加速搜索，因为 walk 不变、距离计算仍是瓶颈；需要让任一 fetched page 被 batch 内所有 query
  同时计算距离，从而改变剪枝与候选扩展过程，才能同时减少距离计算和 I/O。

  - 在电商/广告的 embedding 召回或 RAG 检索服务中，可设计 batch-aware ANN 接口：上游把所有改写 query 一起下发，索引层做协作遍历，而不是逐个查询独立执行，吞吐可提升数倍。

  - GRPO、deep research 等多 rollout/子任务并发的 agentic search 场景，查询生成侧天然产生语义相近 batch，适合用该思路做底层检索加速，降低向量库成本。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：LLM Agent 工作负载（query rewriting、deep research、GRPO）会批量产生语义相关的向量查询。现有磁盘驻留 ANN 系统独立处理每个查询，实测 31%-67% 的 batch I/O 是重复读取同一页。共享 page cache 能消除重复 I/O，但单线程搜索只快 1.1-1.2 倍，因为主要时间在距离计算，且 cache 不改变每个查询的遍历路径。

方法关键点：CoWalk 把 batch 内查询作为单线程上的协作 walk。每个查询维护自己的候选列表；每个 page 每 batch 只读一次；获取到的 full-precision vector 由 batch 内所有 query 依次打分。这样每个查询用更短的候选列表即可达到目标 recall，从而减少距离计算和 I/O。

关键结果：在 recall@10=0.95 时，CoWalk 单线程回答 batch 比最快的逐查询 baseline 快 1.6-1.9 倍，I/O 减少 2.8-6.9 倍；服务端在相似 batch 延迟下吞吐提升 3.0-6.9 倍。
