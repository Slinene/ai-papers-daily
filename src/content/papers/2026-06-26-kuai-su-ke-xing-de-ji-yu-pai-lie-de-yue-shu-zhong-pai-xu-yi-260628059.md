---
title: 'Fast and Feasible: Permutation-based Constrained Reranking for Revenue Maximization'
title_zh: 快速可行的基于排列的约束重排序以实现收益最大化
authors:
- Svetlana Shirokovskikh
- Anastasiia Soboleva
- Ekaterina Solodneva
- Aleksandr Katrutsa
- Roman Loginov
- Egor Samosvat
affiliations:
- Avito
- MSU, AI Center
arxiv_id: '2606.28059'
url: https://arxiv.org/abs/2606.28059
pdf_url: https://arxiv.org/pdf/2606.28059
published: '2026-06-26'
collected: '2026-06-29'
category: RecSys
direction: 约束优化重排序 · 排列近似算法
tags:
- Reranking
- Constrained Optimization
- Revenue Maximization
- E-commerce
- Permutation Algorithm
- ILP
one_liner: 提出 PermR 排列邻域搜索算法，在 0.05 秒内近似求解收益最大化 ILP，线上收入提升 2%
practical_value: '- 重排序建模为 ILP：以当前生产排序的指标值作为约束下界，保证可行且不显著损害用户体验，可直接借鉴到电商搜索重排场景。

  - 排列邻域搜索算法 PermR：通过交换相邻商品提升目标或修复约束，复杂度极低（≤0.05s），适合线上实时部署；采样概率由商品得分差驱动，清晰可复现。

  - 位置偏置使用指数衰减（γ_j = 0.97^j）计算曝光收益，可按平台实际曝光率拟合；多条约束可定义在不同截断前缀（如 top-5 相关度），适应分屏业务需求。

  - 离线/在线验证流程：先离线评估 ILP 最优上限、确定 PermR 迭代次数（如 750），再上线 A/B（14 天，56M 查询），最终收益 +2%，适合作为搜索/推荐重排模块的落地范本。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商搜索/推荐结果已能提供高相关性的排序，但平台希望在不显著降低用户体验的前提下最大化收益（如付费推广产品收入）。传统直接最大化收益会损害相关性、欺诈风险等指标，而精确求解约束整数线性规划（ILP）对于线上实时响应太慢。需要一种轻量、可部署的重排序近似算法，既能提升收益又能满足多项指标约束。

### 方法关键点
- **问题建模**：将重排序定义为最大化总收益（F0），同时约束其他指标（Fm）不低于当前生产排序的对应值（含 top-K 约束），并引入位置偏置 γ_j（0.97^j）衡量曝光价值，形成 ILP。
- **PermR 算法**：基于排列的迭代搜索。每一步检查是否有约束被违反：若全满足，按相邻商品收益差采样一次交换提升目标；若存在违反，随机选一个违反约束，按该约束得分差采样邻对交换；当无法通过邻对交换修复前缀约束时，直接将该约束最高分商品插入到相应位置。算法返回历史最优排列，迭代次数 I 控制延迟。
- **低延迟设计**：邻域仅限于相邻交换，复杂度 O(I·N)，生产环境中 I=750 时平均耗时仅 0.038 秒，远低于 ILP 求解器的 0.6 秒以上。

### 关键结果
- **离线评估**（27,000 个查询，商品数 N=50）：ILP 最优解（MOSEK 12 线程）收益提升 +4.1%，但耗时超标；PermR（I=750）达到 +2.6%（约为 ILP 的 63%），耗时 0.038 秒满足线上要求；遗传算法仅 +0.4% 且不稳定。
- **在线 A/B 测试**：14 天，覆盖 5600 万搜索查询，35% 流量，PermR 提升整体收入 **+2.0%**。主要子类别如 Fashion +4.2%，Home & Garden +6.0%，所有约束均未违反。
- **核心结论**：以当前生产排序为锚点的约束设置和轻量排列搜索，能在极为有限的延迟内实现可观的收益提升，适合大规模实时投放。
