---
title: HNSW with Accuracy Guarantees Using Graph Spanners -- A Technical Report
title_zh: 基于图Spanner的HNSW精度保证框架
authors:
- Minghao Li
- Raghav Mittal
- Sanjivni Rana
- Suraj Shetiya
- Gautam Das
- Nick Koudas
affiliations:
- University of Toronto
- The University of Texas at Arlington
- IIT Bombay
arxiv_id: '2607.02338'
url: https://arxiv.org/abs/2607.02338
pdf_url: https://arxiv.org/pdf/2607.02338
published: '2026-07-02'
collected: '2026-07-04'
category: Other
direction: 近似最近邻检索 · 精度保证
tags:
- HNSW
- Graph Spanner
- Approximate Nearest Neighbors
- Certify-Rectify
- Vector Search
- Filtered Search
one_liner: 通过Certify-then-Rectify框架，动态认证HNSW搜索并利用spanner理论提供最坏情况正确性保证
practical_value: '- 可在线部署轻量级认证器评估HNSW召回质量，避免因贪婪搜索遗漏关键近邻，适合高召回率场景（如广告匹配）。

  - 利用极值理论估计spanner拉伸因子提供距离上界，无需重建索引即可动态平衡效率与准确性。

  - 过滤搜索扩展可直接应用于带属性约束的商品向量检索（如分类、价格筛选），提升复杂查询的可靠性。

  - 分层纠正策略允许在绝大多数查询中保持HNSW速度，仅在必要时触发精确搜索，适合大规模在线服务。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：HNSW是业界标准的向量索引，但其贪婪图遍历缺乏正确性保证，可能导致丢失真正最近邻，影响关键应用（如电商搜索、推荐）的召回质量。

**方法**：提出“Certify-then-Rectify”框架。先使用分布无关的统计认证器（基于邻居对的距离分布）快速评估HNSW返回结果的质量；若认证失败，则触发严谨的精确修复算法。精确修复将HNSW图重新解释为几何spanner，并利用极值理论随机估计最大经验拉伸因子，从而用数学上界限定真实k近邻可能存在的距离范围，随后执行范围搜索实现100%召回。该方法还扩展至过滤搜索场景。

**结果**：在多个基准数据集上，框架在平均情况下保持了HNSW的对数复杂度查询速度，同时保证了最坏情况下的精确召回，优于其他可用的准确率保证方案。
