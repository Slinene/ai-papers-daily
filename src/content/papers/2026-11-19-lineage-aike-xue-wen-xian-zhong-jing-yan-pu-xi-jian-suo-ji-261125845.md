---
title: 'LINEAGE: A Benchmark for Empirical Lineage Retrieval in AI Scientific Literature'
title_zh: LINEAGE：AI科学文献中经验谱系检索基准
authors:
- Pangjing Wu
- Xu Yuan
- Wenqi Fan
- Qing Li
affiliations:
- The Hong Kong Polytechnic University
arxiv_id: '2611.25845'
url: https://arxiv.org/abs/2611.25845
pdf_url: https://arxiv.org/pdf/2611.25845
published: '2026-11-19'
collected: '2026-11-23'
category: Eval
direction: 科研文献检索基准 · 多跳关系图
tags:
- Benchmark
- Literature Retrieval
- Empirical Lineage
- Graph
- Research Agents
- Evaluation
one_liner: 提出首个面向AI文献的经验谱系检索基准，用基线对比关系构建多跳谱系图评估检索系统
practical_value: '- 构建带关系类型的知识图谱作为检索 ground truth 的思路可迁移到电商场景：例如用“商品作为对比/替代/搭配”关系构建图谱，评估搜索或推荐系统是否召回关联邻域而非单点命中。

  - 多跳结构评估指标值得借鉴：不只衡量 top-k 命中，还评估召回集合是否形成紧密连接的关系子图，可用于推荐系统的多样性/连通性评估。

  - 检索系统在长距离关系上性能下降明显的结论提示：实际 Agent 检索中需要针对多跳关系设计专门的索引、查询扩展或图 traversal 策略。

  - 从非结构化论文文本提取“基线对比”证据的 pipeline 思路可复用于构建商品评价、竞品对比等结构化数据，但整体业务可借鉴点有限，主要是学术贡献。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有科学文献检索基准主要用主题相关性或引用链接作为监督信号，无法捕捉哪些先前方法被后续论文用作实证对比基线。而研究 Agent 在文献综合与实验规划中需要检索这类经验谱系关系。

**方法关键点**：定义 empirical lineage relation，将一篇先前论文链接到明确使用其方法作为实证对比基线的源论文。这些关系构成 lineage graphs，其多跳邻域提供结构化检索 ground truth。开发 LINEAGE-Constructor，从异构论文记录和全论文实证基线证据中自动构建校准的谱系图。

**数据与结果**：基于 2018–2025 年 17 个顶级 AI 会议的 121,048 篇论文，构建了包含 3,950 个图组件、67,502 个节点、164,948 条谱系边和 80,000 个多面检索查询的基准。在 19 个代表性检索系统上的实验表明：经验谱系检索仍具挑战性，性能随谱系距离急剧下降；孤立检索命中常无法恢复紧密连接的实证比较邻域。
