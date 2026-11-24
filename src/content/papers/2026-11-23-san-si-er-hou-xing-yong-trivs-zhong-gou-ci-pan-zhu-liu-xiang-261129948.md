---
title: 'Look Before You Leap: Re-Architecting Disk-Resident Vector Search with TriVS'
title_zh: 三思而后行：用 TriVS 重构磁盘驻留向量搜索
authors:
- Yizou Chen
- Baotong Lu
- Peiqi Yin
- Zhisheng Hu
- Qi Chen
- Ming-Chang Yang
affiliations:
- The Chinese University of Hong Kong
- Microsoft Research
arxiv_id: '2611.29948'
url: https://arxiv.org/abs/2611.29948
pdf_url: https://arxiv.org/pdf/2611.29948
published: '2026-11-23'
collected: '2026-11-24'
category: Other
direction: 磁盘向量检索 · I/O 优化
tags:
- ANNS
- Disk-resident
- Vector Search
- I-O Optimization
- SSD
- TriVS
one_liner: 提出 TriVS 三阶段范式，通过粗聚类路由、内存蒸馏和向量级收敛，大幅降低磁盘 I/O 并提升吞吐
practical_value: '- 在电商/推荐的大规模向量召回场景，当索引超内存时，可借鉴 TriVS 的“粗聚类路由（避免随机 I/O）+ 内存量化蒸馏（渐进缩小候选）+
  向量级磁盘精排（精确收敛）”架构，设计分层检索链路，减少 SSD 访问。

  - 利用紧凑量化向量（如 PQ）在内存中构建短列表，代替直接读取完整簇，能显著降低磁盘 I/O 并保持召回，适合做超大 item embedding 的召回缓存。

  - 粗粒度聚类可大幅减少 centroid 路由索引占用的内存，把省下的内存用于短列表缓存或量化向量，整体内存预算不变，适合内存受限的在线服务。

  - 若自建向量库或选型，可参考 TriVS 在 Recall@10=0.9 时相对 PipeANN 降低 63.7% 磁盘 I/O 的结论，评估磁盘向量搜索方案对延迟和吞吐的改善潜力。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：磁盘驻留近似最近邻搜索（ANNS）即使采用高速 SSD 和复杂 I/O 调度，仍受限于 I/O 瓶颈。现有系统或采用聚类搜索，通过内存路由避免接近阶段的 I/O，但收敛阶段读取粗粒度完整簇；或采用图搜索，全程向量级 I/O，收敛高效但接近阶段不可避免产生 I/O。

**方法**：TriVS 将搜索重构为三阶段：粗粒度接近（approach coarsely）、渐进蒸馏（distill progressively）、精确收敛（converge exactly）。创新点：1）解耦接近与收敛阶段，用聚类搜索避免接近阶段 I/O，用向量级 I/O 保证收敛效率；2）在两者之间新增内存蒸馏阶段，使用紧凑量化向量将路由到的簇渐进缩减为向量级短列表后再访问磁盘；3）采用更粗的聚类，缩小 centroid 路由索引，释放内存用于蒸馏，不增加内存预算。

**结果**：在五个数据集 Recall@10=0.9 条件下，TriVS 平均达到 PipeANN 的 3.42 倍吞吐，降低 51.2% 延迟和 63.7% 磁盘 I/O，且内存和存储开销更低。
