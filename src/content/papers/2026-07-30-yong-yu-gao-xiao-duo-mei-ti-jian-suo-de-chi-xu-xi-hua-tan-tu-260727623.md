---
title: An Exploration Graph with Continuous Refinement for Efficient Multimedia Retrieval
title_zh: 用于高效多媒体检索的持续细化探索图
authors:
- Nico Hezel
- Kai Uwe Barthel
- Konstantin Schall
- Klaus Jung
affiliations:
- HTW Berlin
arxiv_id: '2607.27623'
url: https://arxiv.org/abs/2607.27623
pdf_url: https://arxiv.org/pdf/2607.27623
published: '2026-07-30'
collected: '2026-08-02'
category: RecSys
direction: 图索引构建与探索式搜索优化
tags:
- ANNS
- proximity graph
- exploratory search
- graph refinement
- dynamic index
- recommendation
one_liner: 提出 crEG，快速构建紧凑且连通性保证的图索引，专为探索搜索优化，推荐场景价值突出
practical_value: '- **实时增量索引**：crEG 构建速度极快，内存占用低，适合电商高频更新的物品库，可直接用于 embedding 索引的在线增量更新。

  - **item-to-item 探索推荐**：图连通性始终保证，天然适合“以物品搜物品”的场景（如详情页相似推荐），避免死胡同，提升可探索性。

  - **动态边优化**：可选的边优化算法能在不重建全图的情况下持续提升精度，适合需要渐进式索引质量提升的线上服务。

  - **评估校准**：实验表明标准 ANN 指标（recall@k）高不代表探索搜索表现好，推荐系统评估需加入探索场景（query 来自库内点）的专用指标，避免离线评测与线上效果脱节。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有多媒体检索的图索引（如 HNSW）在近似最近邻搜索（ANNS）中性能优异，但构建速度慢、内存高，且大多忽略“探索搜索”场景（query 本身是数据库内元素），而该场景对推荐、探索系统至关重要。

**方法**：提出**持续细化探索图（crEG）**，通过两阶段构建：1）快速生成度数为偶数的连通无向图，保证从任意节点可达全图；2）可选边优化，迭代替换非最优邻接边以提升搜索精度。图始终保持连通、度数均匀，天然适配探索搜索的起点优势。

**关键结果**：在多个大规模数据集上，crEG 构建速度比主流图索引快 1-2 个数量级，内存减少 30-50%，在标准 ANNS 任务中精度接近 HNSW。但在探索搜索（库内点查询）中，crEG 显著优于 HNSW，证明现有 ANNS 的高效率不等同于探索搜索下的高效，强调为推荐系统单独设计索引的重要性。
