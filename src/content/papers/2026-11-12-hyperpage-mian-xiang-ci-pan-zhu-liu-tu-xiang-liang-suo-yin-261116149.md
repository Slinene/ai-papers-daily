---
title: 'HyperPage: Learned Page Layouts for Disk-Resident Graph Vector Indexes'
title_zh: HyperPage：面向磁盘驻留图向量索引的学习页面布局
authors:
- Xinyu Zhang
- Jingze Li
- Baihua Zheng
- Weiwei Sun
affiliations:
- Fudan University
- Singapore Management University
arxiv_id: '2611.16149'
url: https://arxiv.org/abs/2611.16149
pdf_url: https://arxiv.org/pdf/2611.16149
published: '2026-11-12'
collected: '2026-11-14'
category: Other
direction: Agent 搜索向量索引页布局优化
tags:
- page layout
- disk-resident index
- vector search
- agent workload logs
- DiskANN
- physical design
one_liner: 利用搜索智能体的遍历日志学习磁盘向量索引页布局，减少后续运行页读取，比 MARGO 少读 5.2%-21.2% 页
practical_value: '- **用日志重放做布局/缓存仿真**：在电商搜索、推荐或 RAG 场景中，Agent 或在线服务反复查询向量库，可记录每次图遍历扩展的记录
  ID。基于 DiskANN 式路由不依赖同页其他记录的性质，日志重放可精确评估任意页布局的页读取次数，无需真实读取，便于离线优化布局和缓存策略。

  - **内存预算分割优化**：将有限内存预算在“热点记录缓存”和“页缓存”之间动态分割，通过验证集重放选择最优配置。在向量索引服务中，小内存预算下效果尤为明显，可有效降低
  IO 并提升延迟，适合边缘部署或缓存受限场景。

  - **利用历史日志持续优化物理设计**：无需重新构建索引，可在低峰期用已有查询日志重新学习页布局和缓存分配，对新查询负载保持低页读取。对于频繁更新的电商商品向量库或用户兴趣向量库，可以定期重跑布局优化，保持索引性能。

  - **可迁移到其他磁盘驻留索引结构**：该方法的核心是“日志驱动布局 + 重放定价”，不局限于特定索引，也可用于 HNSW 等图索引的磁盘持久化版本，或广告召回阶段的向量检索服务，降低存储读取开销。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：磁盘驻留图向量索引（如 DiskANN）将向量及其边存储为 SSD 页面上的记录，搜索时每扩展一个记录都需要读取其所在页，页读取次数严重依赖页布局。现有布局方法（Starling、MARGO）仅基于图和向量计算，未利用实际查询负载。搜索智能体（如 Search-R1）用强化学习反复查询同一索引，产生大量遍历日志，这些日志可用于优化后续运行的页布局，减少页读取。

**方法关键点**：
- 关键观察：DiskANN 式搜索路由只依赖内存中的码和所扩展的记录，从不依赖同页其他记录，因此日志重放可给任意布局精确计算页读取成本，且缓存记录不增加额外页读取。
- HyperPage 首先在未缓存记录的日志遍历上为给定内存预算构建候选布局，然后通过重放验证步骤选择一个布局，并同时确定热点记录缓存与页缓存之间的预算分割。
- 拉格朗日下界用于衡量布局离理论最优的距离。

**关键结果**：从一次 Search-R1 智能体运行中学习，在后续使用不同奖励的运行上测试，覆盖 1M 和 21M 段落语料。在七个缓存预算下，HyperPage 比 MARGO 少读 5.2% 到 21.2% 页面，且所有对比布局中无更低者；小缓存时优势最大，例如 1% 预算下 MARGO 需要近 3 倍预算才能达到相同页读取数。在 21M 索引上，搜索每步时间最多降低 10.4%。该方法对第二个智能体模型和第二个语料仍然有效。
