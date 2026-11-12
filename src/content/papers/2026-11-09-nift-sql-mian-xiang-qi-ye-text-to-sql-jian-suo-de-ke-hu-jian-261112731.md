---
title: 'NIFT-SQL: Customer-Supervised Table Scoring for Enterprise Text-to-SQL Retrieval'
title_zh: NIFT-SQL：面向企业 Text-to-SQL 检索的客户监督表评分
authors:
- Arjun Rao
- Nishant Gopinath
affiliations:
- SAP
arxiv_id: '2611.12731'
url: https://arxiv.org/abs/2611.12731
pdf_url: https://arxiv.org/pdf/2611.12731
published: '2026-11-09'
collected: '2026-11-12'
category: RecSys
direction: 企业 Text-to-SQL 表检索排序与融合
tags:
- text-to-SQL
- schema linking
- cross-encoder
- learning to rank
- customer fine-tuning
- hybrid search
one_liner: 用客户问题微调检索器与 560M 交叉编码器，通过逻辑回归融合，将企业 Text-to-SQL 表检索 top15 命中率最高提升至 89.5%。
practical_value: '- 按客户/行业微调检索器和交叉编码器，在大型稀疏 schema 或类目体系中可大幅提升 query 到实体（表/商品/话题）的召回
  top-N；小样本客户问题即可训练，适合 B2B 场景。

  - 双塔检索器 + 小交叉编码器精排 + 逻辑回归融合，结构简单且效果稳定；融合时优先使用分数特征而非 rank fusion，便于控制与扩展。

  - 无标注时，引入零样本 LLM reranker（如 8B）按业务线/数据库路由打分，将其分数作为融合特征，可获得高精度模式，避免冷启动。

  - 评估指标用“参考集合全部命中 top-15”而非单个命中，更接近真实任务完成；务必在新增数据/线上分布上做一次泛化验证。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

动机：企业 text-to-SQL 需要先从几百张晦涩表中找到问题所需表，schema linking 是瓶颈；通用检索方法在 BEAVER 等基准上命中率低。

方法：NIFT-SQL 用客户示例问题分别微调：双塔检索器做混合搜索召回；560M 交叉编码器对每个表打分（判断查询是否需要该表）；用留出问题拟合逻辑回归融合两路分数。可选加入零样本 8B reranker 分数作为额外融合特征，并按数据库路由。

结果：在 BEAVER、LiveSQLBench、LiveSQLBench-Large 上，NIFT-SQL 将每个参考表放入 top15 的命中率分别达 69.2%、89.5%、85.6%，远超 hybrid search（30.4/41.0/21.8）和微调检索器（61.1/81.7/70.4）。不做微调的交叉编码器低 21 个点；零样本 8B reranker 无需标签，路由后与微调方法无显著差异，加入其分数可进一步提升至 72.4/92.5/88.6。学到的融合与按数据库分组的 rank fusion 无显著差异。在新版 BEAVER 上，NIFT-SQL 在合成测试 top8 领先，但在真实问题上 top15 落后于标签匹配检索器。
