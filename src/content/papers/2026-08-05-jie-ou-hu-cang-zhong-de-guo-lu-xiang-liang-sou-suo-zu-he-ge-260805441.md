---
title: 'Filtered Vector Search in a Disaggregated Lakehouse: Composing Table-Format
  Pruning with Per-File ANN'
title_zh: 解耦湖仓中的过滤向量搜索：组合表格式剪枝与逐文件ANN
authors:
- Rakesh Jain
- Thomas Griffin
- Syed Zawad
affiliations:
- IBM Research
arxiv_id: '2608.05441'
url: https://arxiv.org/abs/2608.05441
pdf_url: https://arxiv.org/pdf/2608.05441
published: '2026-08-05'
collected: '2026-08-07'
category: Other
direction: 湖仓原生过滤向量搜索 · 文件剪枝
tags:
- filtered vector search
- lakehouse
- Apache Iceberg
- IVF
- file pruning
- distributed index build
one_liner: 将IVF索引嵌入Parquet文件尾部，复用Iceberg表已有的文件剪枝能力，先按过滤条件剪枝文件再执行向量搜索，避免独立的过滤步骤
practical_value: '- **过滤与向量搜索一体化**：在电商/推荐系统中，大量查询带有结构化过滤（类目、品牌、价格），可借鉴将过滤条件融入文件剪枝（分区/zone-map），先大幅削减数据文件再执行本地向量索引，避免跨系统的过滤后搜素开销。

  - **利用湖仓元数据构建索引**：索引构建通过Iceberg `replace` 等元数据操作，不重写数据文件，对已有数据管道无侵入，适合在现有数据湖上增量构建向量索引。

  - **分布式索引与缓存**：逐文件独立构建IVF集群、部署rendezvous-hash缓存层，可缓解对象存储高延迟；在电商海量商品库中，可按属性分区构建局部IVF索引，结合本地缓存加速重复查询。

  - **安全继承**：向量搜索直接作用于湖仓表，继承目录的访问控制，避免将向量外拷到单独向量数据库带来的权限同步问题。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：过滤向量搜索通常需要将相似度与结构化过滤分开处理，维护两套系统。本文探索在开放湖仓表（Apache Iceberg on Parquet）中直接支持高效过滤向量搜索的可能性。

**方法**：在每个Parquet文件尾部嵌入一个IVF索引（聚类中心等），索引构建通过Iceberg元数据替换操作完成，不改变数据文件本身，其他引擎仍可正常读取。搜索时，查询规划器先利用表已有的文件剪枝能力（分区剪枝、zone-maps、bitmap索引）根据过滤谓词剪枝文件，然后仅对幸存文件执行IVF ANN；向量从未离开表，访问控制由湖仓目录统一管理。引入rendezvous-hash逐文件缓存层来降低对象存储延迟。

**结果**：在1150万×768维数据上，选择性过滤（444个文件中仅剩89个）后，温缓存IVF搜索比暴力搜索快约32×，recall@10≥0.90；在500万真实IBM Granite嵌入上，跨连接过滤剪枝5个分区中的4个，推理速度快近两个数量级（14.7s→157ms）。分析表明该方法收益取决于过滤列的文件级局部性，且残余谓词仅对严格分区列安全下推。
