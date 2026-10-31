---
title: Your Benchmark Is an Empirical Measure Over Difficulty
title_zh: 你的基准本质上是难度的经验测度
authors:
- Yifan Sun
- Naicheng Yu
- Jiawen Gong
- Jingyan Shen
- Huan Zhang
affiliations:
- University of Illinois Urbana-Champaign
- University of California San Diego
- New York University
arxiv_id: '2610.29927'
url: https://arxiv.org/abs/2610.29927
pdf_url: https://arxiv.org/pdf/2610.29927
published: '2026-10-20'
collected: '2026-10-31'
category: Eval
direction: 基准评估 · 难度分布诊断
tags:
- Benchmark Evaluation
- Difficulty Measure
- Coverage Gap
- Measure Mismatch
- Item Rewriting
one_liner: 从测度视角揭示基准评估两大失败模式：难度分布错配与覆盖空洞，并提出诊断指标及 BenchFill 重写算法
practical_value: '- 评估集构建前先做难度分布审计：用 IRT 或模型正确率估计每个样本难度，检查是否过度集中在简单/中等区域，避免排行榜结论被难度分布带偏。

  - 针对电商 query 推荐、搜索改写、商品文案生成等任务的评测集，可按目标难度分层采样或主动补齐高难度样本，否则模型在困难 query 上的提升无法被评测捕捉。

  - 训练过程中用难度分桶监控不同区间的指标变化，而不是只看整体均值，便于定位模型是全局提升还是只在易样本上过拟合。

  - BenchFill 的难度定向重写思路可直接迁移：给定一批种子样本，用 LLM 按目标难度生成同语义变体，低成本扩充评测集覆盖缺口，适合快速构建分层测试集。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：基准评估常被当作对固定题目的平均打分，但结论不仅取决于模型能力，还取决于题目难度分布。如果基准的难度分布与应用场景不一致，或某些难度区间缺少题目，排行榜和训练监控都可能产生误导。

**方法关键点**：将基准视为在难度轴上的经验测度，形式化两个失败模式：measure mismatch（基准难度分布偏离目标分布）和 coverage gaps（难度轴上未被覆盖的区域导致局部训练进展不可见）。提出两个对应诊断指标，并给出理论保证。进一步提出 BenchFill，一种难度定向的题目重写算法，通过改写已有题目填充低覆盖难度区间。

**关键结果**：分析 25 个流行基准、覆盖 7 个领域，发现许多基准隐含地过度加权某些难度区域，排行榜结论需谨慎解读；另一些基准在难度轴上留下大面积空白，难以监控模型改进过程。BenchFill 能有效减少局部覆盖空洞。
