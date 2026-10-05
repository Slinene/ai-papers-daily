---
title: 'SOLO: Certified-Recall Metric Similarity Search with Scan-Only Sampled Inverted
  Lists'
title_zh: SOLO：基于扫描采样倒排列表的可认证召回相似性搜索
authors:
- Édgar Chávez
affiliations:
- CICESE
arxiv_id: '2610.02387'
url: https://arxiv.org/abs/2610.02387
pdf_url: https://arxiv.org/pdf/2610.02387
published: '2026-10-01'
collected: '2026-10-05'
category: RecSys
direction: 向量检索 · 可认证召回 ANN 索引
tags:
- ANN
- Vector Search
- Inverted Index
- Recall Certification
- Memory Efficiency
one_liner: SOLO 索引以无排序启发式的扫描倒排列表实现可证明召回，在 1GB 内存下 Deep-100M 召回 0.9977
practical_value: '- 大规模向量召回的内存优化：在商品 embedding 库亿级甚至十亿级时，SOLO 的扫描式倒排索引只需少量字节/对象（如
  10.7 字节）即可达到 0.9977 召回，远低于 HNSW/DiskANN 的内存下限；适合作为电商推荐召回的高性价比底座，尤其在内存受限的在线服务或边缘部署中。

  - 可认证召回特性：SOLO 召回等于覆盖概率，可通过一次查询样本的 ground-truth pass 离线算出所有操作点，无需在线反复 A/B；可将召回 SLA
  直接与索引参数绑定，降低质量风险。

  - 动态更新友好：插入等于一次搜索、删除精确，相比 HNSW 的复杂删除和图维护，更适合商品频繁上下架、embedding 定期更新的场景；可简化索引运维。

  - 结构可扩展：路由与扫描分离、叶节点扫描的设计便于与压缩/量化 embedding 结合，进一步节省内存；且路由器可递归索引，适合构建分层/多级召回。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：现有 ANN 索引（如 HNSW、DiskANN）在 10^8 规模下面临召回饱和、召回不可预测（需事后测量）、内存占用高、动态更新困难。

方法：SOLO 索引采用无排序启发式：查询先路由到数据库随机样本的 k_s 个最近点，再扫描被触及的倒排列表，对每个对象计算真实距离，不做任何近似排序；召回等于覆盖概率，可从索引直接计算，通过一次查询样本的 ground-truth pass 即可认证所有操作点；索引构建遵循单一递归规则：采样集合，每个对象 post 到其 b 个最近样本点，列表超限则分裂，叶节点总是扫描；召回近似为 f(b·k_s)，其水平是数据集的单标量特征；路由器自身也可用同一规则索引。

结果：Deep-100M 在 1GB 内存（10.7 字节/对象）下召回 0.9977，256MB 下 0.9964；Deep-1B 在 512MB 下召回 0.9925，depth3 96MB；插入成本等于一次搜索，删除精确；吞吐量在特定硬件上比 HNSW 高 1.8x，并覆盖 HNSW 饱和点右侧的操作点。
