---
title: 'When to Repair a Graph ANN Index: Navigability-Signal-Triggered Local Repair
  Protects Tail Recall Under Bursty Churn'
title_zh: 何时修复图ANN索引：导航信号触发局部修复保护突发流失下的尾部召回
authors:
- Madhulatha Mandarapu
- Sandeep Kunkunuru
affiliations:
- VaidhyaMegha Private Limited, India
arxiv_id: '2607.00728'
url: https://arxiv.org/abs/2607.00728
pdf_url: https://arxiv.org/pdf/2607.00728
published: '2026-07-01'
collected: '2026-07-04'
category: Other
direction: 图ANN索引 · 导航信号触发局部修复
tags:
- graph ANN index
- navigability signal
- tail recall
- local repair
- bursty churn
- vector search
one_liner: 用廉价探针召回信号触发图ANN局部修复，在固定预算下大幅提升尾部召回，避免盲目周期性修复
practical_value: '- 在电商商品向量索引中，频繁上下架导致图索引退化，可用廉价探针查询的recall作为导航性退化信号，代替固定周期修复，节省算力且保护尾部查询质量。

  - 信号触发修复策略在稀疏、脆弱的图（如低度图）上收益更大，可针对长尾商品或冷门类目的索引子图优先采用。

  - 引入budget-matched评估协议：对比修复策略时必须控制修复总次数相等，避免单纯比较预算不对等产生的虚假优势。

  - 工程实现上，可维护一组固定探针查询，定期计算其recall，当滑动窗口内的recall下降超过阈值时触发局部重连，无需全量重建索引。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：图ANN索引（HNSW、DiskANN）在插入/删除流失下，删除节点会截断贪心搜索路径，导致召回下降。现有系统多采用固定周期修复（如每X次操作consolidate一次），可能浪费修复预算。

**方法关键点**：提出一种基于导航性退化信号的局部边修复触发策略。通过廉价探针查询计算近似recall（与真实recall的Spearman相关系数约0.95），当信号表明导航能力下降时，才在受影响邻域执行局部重连（将删除节点的入邻居连到出邻居并重剪枝）。在SIFT-128和Fashion-MNIST-784数据集上，模拟突发性流失，并以匹配的修复总次数（budget-matched）对比固定节奏修复与信号触发修复。

**关键结果**：在修复预算稀缺（约1次consolidation）时，信号触发修复将最小recall@10（尾部召回）提升0.014（SIFT）至0.050（Fashion-MNIST），提升显著且稳定（95%置信区间不含0）；平均召回增益很小（<0.005）。优势随着图稀疏度增加而扩大，当索引本身鲁棒或预算充裕时差异消失。
