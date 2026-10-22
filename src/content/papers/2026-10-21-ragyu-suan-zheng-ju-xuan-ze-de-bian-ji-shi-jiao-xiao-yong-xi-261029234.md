---
title: Learning Marginal Viewpoint Utility for Budgeted Evidence Selection in RAG
title_zh: RAG预算证据选择的边际视角效用学习
authors:
- Yiyang Duan
- Ziqi Yu
- Tiantong Wu
- Yebo Wu
- Wei Yang Bryan Lim
affiliations:
- Nanyang Technological University
- University of Toronto
arxiv_id: '2610.29234'
url: https://arxiv.org/abs/2610.29234
pdf_url: https://arxiv.org/pdf/2610.29234
published: '2026-10-21'
collected: '2026-10-22'
category: RAG
direction: RAG 预算证据选择 · 边际视角覆盖
tags:
- RAG
- Evidence Selection
- Viewpoint Coverage
- Budgeted Retrieval
- Marginal Utility
- Ranker
one_liner: 提出LMVU轻量排序器，按边际视角覆盖增量选择证据，在有限上下文下提升多视角覆盖
practical_value: '- 在电商 RAG 场景（商品问答、评论摘要、多卖点对比）中，上下文预算有限，可借鉴边际视角覆盖思想：优先选择能补充当前已选集合缺失观点的候选，而非单纯按相关性得分截断。

  - 训练数据构造：利用已有的观点/标签标注（如评论情感、产品属性、类目标签）作为伪视角，构造同一选择状态下的候选配对，让 ranker 学习增量覆盖价值；推理时迭代选择，类似贪心式集束搜索，开销低。

  - 评估指标：用 RVC1/RVC2 度量检索结果的视角覆盖度，可作为多样性/覆盖度补充指标，尤其当业务目标要求搜索结果覆盖不同用户意图或品类时。

  - 轻量 ranker 设计可作为在线精排后的二次重排组件，输入包括已选证据集合与候选的交互特征，输出边际增益，适合低延迟的实时检索链路。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：多视角查询下，RAG 需要在固定上下文预算内保留不同答案/立场，但相关性排序易偏向单一视角，导致覆盖不足。

**方法关键点**：LMVU 是一个轻量 ranker，学习候选对当前已选集合的边际视角覆盖增量。训练时用各 benchmark 开发集的观点标注，在同一选择状态内构造候选对比；推理时随着上下文增长，反复对预算可行候选打分，无需观点标注。评估采用两种视角覆盖恢复指标 RVC1（每个视角至少一个来源单元给满分）和 RVC2（一个给半分，两个及以上给满分）。精确 oracle 给出同证据池与预算下的覆盖上限。

**关键结果**：在四个观点标注 benchmark、1024 token 预算下，LMVU 相较最强非 oracle 基线在 RVC1 和 RVC2 上分别最高提升 0.047 和 0.052，并在两个 benchmark 上达到精确视角广度上限。
