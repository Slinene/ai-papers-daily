---
title: 'REWEAVE: Online Learning for Workload-Adaptive HNSW Indexes'
title_zh: REWEAVE：工作负载自适应的 HNSW 索引在线学习
authors:
- Minghao Li
- Nick Koudas
- Raghav Mittal
affiliations:
- University of Toronto
- The University of Texas At Arlington
arxiv_id: '2611.16060'
url: https://arxiv.org/abs/2611.16060
pdf_url: https://arxiv.org/pdf/2611.16060
published: '2026-11-11'
collected: '2026-11-13'
category: Other
direction: 向量检索 · 工作负载自适应索引
tags:
- HNSW
- workload-adaptive
- online learning
- ANN search
- index maintenance
- query feedback
one_liner: 利用查询反馈学习边效用，在固定度数预算内周期性重连 HNSW 底层，偏斜/漂移负载下提升召回与吞吐
practical_value: '- 若线上 HNSW 索引承载商品/内容 embedding 召回，可在固定度数预算内做在线重连：维护候选池（当前出边 + 近邻
  buffer + 漏检 buffer），每 B 个查询按学习到的边分 trim 到 M 条，无需扩大图规模即可提升偏斜 query 的召回。

  - 导航探索建议优先用 UCB（乐观度）配合较宽 beam（如 W=64）；相比 epsilon-greedy 能更有效地暴露有用边。奖励分配选 recall
  reward 优于 binary endpoint，且 MC(0.8) 能把后续成功信用传播到上游边，防止有用路由边被替换。

  - 漏检候选（missed-neighbor buffer）很关键：把查询 true top-k 中未检出的最近邻注入候选池，可以显著补回搜索漏掉的真邻居；在自标注为主时，即使只有
  10% 查询带精确标注也能恢复约一半收益。

  - 工程落地轻量：只改 HNSW 底层边，冻结服务用标准 HNSW 无额外开销；重连操作可并行，单线程耗时主要在距离计算，适合作为实时索引维护模块嵌入现有向量库。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
向量数据库依赖 HNSW 做近似最近邻搜索，但仅基于语料构建的图可能与偏斜或漂移的查询工作负载不匹配。在电商/RAG/推荐等场景，查询可能集中在少数主题，或随时间漂移，导致图边利用率低、召回下降或搜索开销增加。所以需要在不增加每节点出度预算下，利用查询反馈重配边。

**方法关键点**
- 将导航建模为在线学习：每条出边是一个动作，奖励衡量其对查询的作用。
- 五步循环：导航（epsilon-greedy 或 UCB，可选 beam 宽度 W）、奖励分配（binary endpoint、recall reward、MC/TD 信用分配）、价值估计（运行均值或时间折扣）、候选生成（neighbor buffer + missed-neighbor buffer）、每 B 查询重连（从候选池选 top-M 边保留）。
- 只适应 layer 0，冻结服务无学习开销；支持混合 exact/self 反馈，理论保证覆盖 UCB 导航 regret O(log T) 和图稳定条件。

**关键结果数字**
- GIST-1M 和 T2I-10M 上，相同度预算下较 frozen HNSW 提升 held-out recall@100 最多 16.3 和 23.3 个百分点。
- 与 query-aware baselines 相比，GIST-1M 上 recall@100=0.80 时 QPS 为 NGFix 的 3.3×，T2I-10M 上 2.1×，T2I-100M 上约 1.3×。
- Amazon-ESCI 查询漂移实验中，stream recall@100 从 0.745 提升到 0.979，且搜索距离计算减少 34%。
- 两速率反馈中，10% 精确探针可恢复约 55% 的召回增益，50% 恢复约 73%。

**最值得记住的一句话**：在固定 HNSW 度预算内，用查询反馈学习边分并周期性重连，可以在不增加存储和搜索复杂度下大幅提升偏斜/漂移负载的召回与吞吐。
