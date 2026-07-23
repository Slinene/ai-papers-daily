---
title: 'ANNLib: A Development Framework for Efficient Approximate Nearest Neighbor
  Search'
title_zh: ANNLib：解耦算法与数据结构的高性能 ANNS 开发框架
authors:
- Zheqi Shen
- Jingbo Su
- Zijin Wan
- Yan Gu
- Yihan Sun
affiliations:
- UC Riverside
- William & Mary
arxiv_id: '2607.17582'
url: https://arxiv.org/abs/2607.17582
pdf_url: https://arxiv.org/pdf/2607.17582
published: '2026-07-20'
collected: '2026-07-23'
category: Other
direction: 解耦算法与数据结构的可扩展 ANNS 框架
tags:
- ANNS
- graph-based
- modular design
- filtered search
- dynamic updates
- C++ library
one_liner: 通过解耦算法与数据结构，实现灵活组合的图基 ANNS 框架，性能与专用系统相当或更优
practical_value: '- 模块化设计允许独立替换图算法（Vamana、HNSW）与底层存储容器（CSR、功能树、Chrono Prefix Array），推荐系统可快速适配静态索引、实时更新或历史快照回溯等不同场景。

  - 内置 Stitched-vamana 与 Filtered-vamana 过滤搜索，通过定制邻居访问闭包 (f_nbhs) 即可在向量检索中无缝融合商品标签或属性约束，避免预过滤的性能损失。

  - 批量删除采用惰性标记 + 并行边修复 (consolidation) 策略，能在不重建索引的情况下维护图连通性，适合电商场景中频繁上下架商品的向量索引维护。

  - Chrono Prefix Array 通过共享前缀压缩历史边版本，将多版本快照内存占用降低达 70.4%，可用于 A/B 测试或离线分析时高效保存索引状态。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
近似最近邻搜索（ANNS）是现代推荐、搜索和深度学习系统的核心组件。现有系统往往在功能丰富度与极致性能之间难以两全：向量数据库（如 Milvus）注重易用性，但性能弱于高度优化的专用库（如 DiskANN/ParlayANN），而后者又因代码耦合严重难以扩展新的功能（过滤、动态更新、快照）。ANNLib 试图弥合这一鸿沟，提供一个同时实现高灵活性和高性能的图基 ANNS 开发框架。

### 方法关键点
- **解耦设计**：将 ANNS 拆分为算法（Algorithms）与图容器数据结构（Data Structures）两个独立维度，通过统一接口进行组合。
- **算法抽象**：抽象出图遍历、候选收集 (collect) 和邻居修剪 (prune) 等通用原语，通过可调用的邻居函数 (f_nbhs)、距离函数 (f_dist) 和修剪谓词 (pred) 参数化，使新功能（如过滤搜索、动态删除）只需定制这些闭包即可，无需重写核心搜索逻辑。
- **内置算法与模块**：预置 Vamana、HNSW、HCNNG 基础算法，并封装了并行批量插入、过滤搜索（Stitched-vamana / Filtered-vamana）、惰性删除修复、历史快照等算法模块。
- **可插拔图容器**：通过边代理 (edge agent) 接口抽象图存储，提供嵌套数组（静态场景）、功能树（CPAM，写时复制支持历史版本）和自研 Chrono Prefix Array（利用前缀共享压缩连续版本的边集合）等容器，用户可按需选择以平衡空间、时间与功能。
- **性能保护**：容器后端可独立优化，不影响算法逻辑；接口设计避免不必要的数据拷贝，并通过 ParlayLib 实现并行。

### 关键结果
实验在 1 亿点 BIGANN、Deep、Cohere、OpenAI 等数据集上对比 ParlayANN、Filtered-DiskANN、Milvus、Weaviate：
- 批量插入：Vamana 比 ParlayANN 平均快 1.58×（最高 8.11×），HNSW 速度相当。
- 常规查询：QPS–Recall 曲线与高度优化的 ParlayANN 可比，高召回下性能持平。
- 过滤搜索：在 MS MARCO、YFCC 等带标签数据集上，AllLib 的实现几乎在所有特异性设置下均快于 Filtered-DiskANN、Milvus 和 Weaviate。
- 删除修复：惰性删除 + 并行修复可在不重建索引的情况下恢复召回，修复成本随删除比例变化。
- 快照：Chrono Prefix Array 相比全拷贝可节省高达 70.4% 内存，构建时间仅增加 1.13×–3.32×。

> **一句话**：ANNLib 证明，通过严谨的算法–数据结构解耦和精巧的抽象，可以在极简接口下实现与专用高性能系统匹敌甚至更优的向量检索效果，并轻松扩展过滤、动态更新、历史快照等复杂功能。
