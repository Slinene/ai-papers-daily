---
title: Top-K Is Not a Budget for Hybrid Retrieval
title_zh: Top-K 不是混合检索的预算
authors:
- Chunran Zhang
affiliations:
- Southwest Jiaotong University
arxiv_id: '2609.15143'
url: https://arxiv.org/abs/2609.15143
pdf_url: https://arxiv.org/pdf/2609.15143
published: '2026-09-14'
collected: '2026-09-16'
category: RAG
direction: RAG 混合检索预算优化
tags:
- Hybrid Retrieval
- RRF
- Budgeted Retrieval
- RAG
- Efficient Retrieval
one_liner: DiBud 以访问预算为输入，增量认证 RRF 排名精确前缀，用更少访问量保留混合检索质量
practical_value: '- 将访问预算作为第一输入替代固定 Top-K 截断：在电商搜索/推荐混合召回中，向量与倒排融合常固定取前 L 条，但长尾查询成本波动大。可借鉴
  DiBud，对每次请求设定硬访问预算（如最多读取多少候选），通过选择性访问动态决定每个通道的读取深度，保持延迟稳定。

  - 增量认证与预算停止：DiBud 不会一次性计算完整融合，而是逐步输出已确定顺序的 RRF 前缀，预算耗尽即停止。推荐系统可据此实现流式/增量融合，优先保证已认证
  top 项的正确性，并设置强制停止点，降低线上最坏延迟。

  - 质量保留校准：用 held-out 查询校准预算参数，在满足 95% nDCG 保留的前提下大幅减少访问。可以按不同流量桶/查询类型离线校准预算，线上按查询特征动态选择预算，替代全局统一
  Top-K，实现成本与质量的最优折中。

  - 长尾成本意识：论文显示完成精确 Top-20 的访问分布长尾，少量高成本查询拖累系统。应监控访问成本分布，对异常高成本查询设置兜底预算。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：混合检索融合 dense/sparse top-L 结果，固定截断深度不能随查询与语料变化而迁移；精确融合虽摆脱固定深度，但完成指定 Top-K 仍产生可变访问成本。

**方法关键点**：DiBud 直接以访问预算为输入，增量地认证并返回完整列表上 RRF 排名的精确前缀；选择性访问（selective access）在预算内提升认证输出，预算停止（budgeted stopping）绑定每次请求的访问次数上限。

**关键结果**：5 个查询集上，完成精确 Top-20 的访问成本呈现长尾分布；在 2048 访问预算下，DiBud 在前 100 位置内平均认证输出比 balanced access 增加 7.86%；按 95% 质量保留校准预算后，held-out 查询保留 95.05%–97.68% 的 mean nDCG@20，访问量比完成精确 Top-20 减少 65.92%–99.53%。
