---
title: Towards Explaining Query Expansion Performance in Information Retrieval
title_zh: 解释信息检索中查询扩展性能的框架
authors:
- Sourav Saha
- Aditya Dutta
- Soumajit Pramanik
- Mandar Mitra
affiliations:
- Indian Statistical Institute
- IIT Bombay
- IIT Bhilai
arxiv_id: '2610.09724'
url: https://arxiv.org/abs/2610.09724
pdf_url: https://arxiv.org/pdf/2610.09724
published: '2026-10-07'
collected: '2026-10-09'
category: QueryRec
direction: QueryRec · 查询扩展可解释性
tags:
- Query Expansion
- Explainable IR
- Ideal Query
- Separability
- BM25
- Post-hoc Analysis
one_liner: 提出理想扩展查询与可分性两个视角，系统解释查询扩展性能差异，验证相似度与检索效果正相关
practical_value: '- 可用理想查询作为离线评估扩展质量的参考：若有小规模标注（如电商搜索点击/相关标注），可构造近似理想查询，度量 LLM 生成的扩展词/改写
  Query 与理想查询的余弦相似度，作为自动评估指标，避免昂贵的在线实验。

  - 使用 separability（Cohen''s d）快速评估扩展 Query 质量：在标注子集上计算相关商品与不相关商品得分的分离度，与线上效果相关性高，可用于
  A/B 测试前的快速筛选或模型迭代中的监控指标。

  - 诊断 LLM 生成查询扩展失败：当 LLM 生成的扩展词效果不好时，检查其是否缺少关键 term 或权重不当；可尝试用 DFO/LS 方法从标注数据中学习理想权重，反过来指导生成或后处理，例如对
  LLM 生成的扩展词重新加权。

  - 注意负权重处理：LS 理想查询含负权重，但 BM25 优化（如 Lucene）不支持负权重，实际系统中需截断或用支持负权重的检索器。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
查询扩展（QE）是解决词汇不匹配问题的核心手段，在现代检索系统（包括基于 LLM 的方法）中依然广泛应用。但不同 QE 方法在单个查询上表现差异极大，平均效果相近的方法可能在个别查询上表现迥异，缺乏对差异来源的系统性解释。本文面向 IR 研究者和开发者，提供 post-hoc 可解释框架。

**方法关键点**
- 提出理想扩展查询（IEQ）概念：给定信息需求，能使 BM25 达到近乎完美 AP 的查询向量。用完整相关性判断通过两种方式近似构造：
  - DFO：以 Rocchio 向量为起点，迭代调整项权重直接最大化 AP，AP≥0.9 时停止。
  - Least-Squares（LS）：以最小二乘目标使相关文档得分高，求解得到稠密查询向量（含负权重），正则参数 λ 取 0.1 或 1。
- 度量扩展查询与 IEQ 的余弦相似度，计算其与 AP 的相关性（RQ1）。
- 提出 separability 度量：计算相关与非相关文档 BM25 分数的 Cohen's d，量化分离程度，并分析其与 AP 的相关性（RQ2）。
- 通过旋转 IEQ 生成合成扩展查询，考察不同轨迹上的关系；并定义 Restricted AP（仅在已标注文档集上计算）以支持含负权重的高效评估。

**关键实验与结果**
- 在 TREC Robust、DL19-20 Passage、DL19-20 Document、DL21-22 Passage 四个集合上，用 RM3、KL、Bo1、CEQE、HyDE 等 5 种方法生成 90 个扩展查询变体。
- LS 理想查询 MAP 极高：Robust 上 0.951，DL19-20 Passage 上 0.967；DFO 在 DL21-22 Passage 上更优，说明理想查询不唯一。
- 合成查询中，相似度与 AP 的 Pearson 相关为 0.678~0.883；真实扩展查询中为 0.411~0.677，中等相关。
- separability 与 AP 的相关性更强：Pearson 0.650~0.785，其中 Robust 上最高 0.785。
- 分析发现真实扩展查询与 IEQ 的角距离范围窄（约 80°~84°），且不同轨迹导致聚合后相关性下降。

**最值得记住的一句话**
扩展查询与理想查询的相似度和相关/非相关文档得分分离度是两个互补、可解释的 QE 性能诊断指标，其中 separability 与检索效果相关性更强，适合低成本的离线评估。
