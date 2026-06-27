---
title: 'Scoring Is Not Enough: Addressing Gaps in Utility-fairness Trade-offs for
  Ranking'
title_zh: 仅靠打分不够：排名中效用-公平性权衡的缺失及其弥补
authors:
- Shubham Singh
- Ian A. Kash
- Mesrob I. Ohannessian
affiliations:
- University of Illinois Chicago
arxiv_id: '2606.26369'
url: https://arxiv.org/abs/2606.26369
pdf_url: https://arxiv.org/pdf/2606.26369
published: '2026-06-24'
collected: '2026-06-27'
category: RecSys
direction: 排序效用与公平性权衡 · 后处理优化
tags:
- ranking
- fairness
- utility-fairness trade-off
- scoring function
- post-processing
- semi-greedy
one_liner: 证明排序中仅靠打分函数无法实现最优效用-公平性权衡，半贪婪后处理可逼近理想前沿
practical_value: '- 推荐系统重排序引入公平性目标时，避免仅依赖单一预测分数排序，应使用显式列表级后处理（如半贪婪方法）来平衡公平与效用

  - 半贪婪后处理计算开销远低于穷举搜索，可在线部署，适合电商/广告大候选集的公平性干预

  - 跨请求的累积公平性约束（多查询公平）比单次推荐公平更能改善长期生态，可作为长期公平优化方向

  - 实验表明基于分数的随机排序（如概率排序）也无法充分实现公平-效用前沿，建议直接优化排序策略而非调整分数'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：现代推荐与检索系统普遍学习一个打分函数，再按分数排序以最大化效用（如点击率）。随着公平性需求增加，常见做法是学习一个兼顾公平的打分函数，但本文指出这种做法存在根本局限：在一般公平性定义下，无论打分函数是确定性还是随机化，无论公平度量在单次查询还是多次查询范围，都无法实现所有可能的效用-公平性最优权衡。

**方法关键点**：通过一系列反例，理论上证明了基于打分排序的 Pareto 前沿有不可企及的区域。作为补救，提出半贪婪后处理 (semi-greedy post-processing)，它不改变原始打分，而是以计算上可控的方式近似穷举搜索理想排序，从而逼近完整效用-公平性前沿。

**关键结果**：实证表明半贪婪后处理能取得显著优于打分排序的权衡，且结果常接近穷举后处理的上界，验证了其有效性与可行性。
