---
title: 'Hybrid Product Search Without the Copy: Lexical, Semantic and Filtered Retrieval
  Served Directly from a Data Lake'
title_zh: 混合商品搜索无拷贝：从数据湖直接服务词法、语义与过滤检索
authors:
- Raghvendra Yadav
- Xiang Fu
- Chinmay Soman
affiliations:
- StarTree Inc., Mountain View, CA, USA
arxiv_id: '2611.11031'
url: https://arxiv.org/abs/2611.11031
pdf_url: https://arxiv.org/pdf/2611.11031
published: '2026-11-08'
collected: '2026-11-10'
category: RecSys
direction: 湖仓原生混合检索 · BM25+向量+RRF
tags:
- Hybrid Search
- BM25
- Vector Search
- Data Lakehouse
- Apache Iceberg
- RRF
one_liner: 用 Apache Pinot 对 Iceberg 湖仓表原地构建 BM25 与 HNSW 索引，SQL 内融合 RRF，无需复制目录，质量匹配精确检索且延迟毫秒级。
practical_value: '- 对现有 Lakehouse 上的商品目录，不必同步到 Elasticsearch/向量库；用支持外部表的 OLAP 引擎（如
  Pinot）按 Parquet 文件作为 segment 建 Lucene/HNSW 索引，避免复制行数据，只存索引，降低存储和同步成本。业务上可考虑将检索层直接坐在
  Iceberg 表上。

  - BM25 多文件分布时全局 IDF 很重要：per-file IDF 导致 nDCG 下降 .040；实现两阶段统计协议或按 snapshot 物化全局词典统计，避免相关性依赖于文件切分方式。

  - 过滤/排序布局：按常用过滤列（brand/category/seller）对 Iceberg 表做排序或聚类，选择性查询可只搜索少数文件，冷启动 p50 237ms，暖后
  7.5ms，吞吐提升 25 倍；注意处理过滤列全 NULL 文件，用 null count 跳过。

  - 在 SQL 里用窗口函数和 RRF 融合 BM25/向量结果，避免专用融合引擎；Pinot 的多阶段引擎中 SQL RRF 比客户端融合多约 25ms，但可接受，便于统一分析/聚合。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
电商目录越来越多存放在 lakehouse 表（Iceberg metadata + Parquet）里，但搜索仍然把这份目录复制到词法引擎和向量数据库，各自维护 ingestion pipeline、schema 和新鲜度窗口。复制带来存储、同步和运维成本，还受最慢 pipeline 拖累。

## 方法关键点
- 扩展 Apache Pinot，把 Iceberg snapshot 中每个 Parquet 文件映射为一个 segment，源文件即 forward index；服务端加载时构建 Lucene 文本索引和 HNSW 向量索引，只存索引不复制行。
- 解决多文件 BM25 分数不可比问题：增加 `TEXT_SCORE_STATS` 两阶段协议，按 snapshot 汇总全局 document frequency、average length，避免 per-file IDF 使 nDCG 从 .271 跌到 .271（实际 per-segment 是 .271，全局是 .312）。
- 混合检索在 SQL 内完成：BM25 和 ANN 分别取 top-k，结构化过滤 pushdown，再用 `ROW_NUMBER()` 窗口函数实现 reciprocal rank fusion (RRF)，无需自定义算子。
- 新鲜度：新文件只建自己的索引，不 force-merge；每 segment 独立 HNSW graph；Kafka 实时表可与湖外部表共享同一逻辑表，保持 kappa 风格。

## 关键实验
- Amazon ESCI-US 基准：1,215,854 商品、22,458 测试查询。混合检索 nDCG@10 = .361，与精确 BM25+精确向量融合一致；BM25 .312 与 Elasticsearch/OpenSearch 相同；HNSW .348 接近精确 .350。
- 277M 商品（0.8TB，2052 文件按 brand 排序）单节点 16 vCPU：brand 范围过滤下向量 p50 7.5ms、QPS 1103；BM25 p50 6.5ms、QPS 635；客户端 RRF 混合 8.9ms、375 QPS。
- 注册后 149s 可查询；新提交 10,000 商品可搜索 3.8s；索引额外存储 4.06GB（源表 4.38GB），成本为复制栈的 0.91–0.98。

## 最值得记住的一句话
搜索应用不需要复制目录：按过滤列排序/聚类湖表，在湖文件上原地构建索引，即可用毫秒级延迟服务选择性查询，质量与新鲜度不输给复制型引擎。
