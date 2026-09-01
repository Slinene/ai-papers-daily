---
title: 'ICEGR: An Intent-Coherent End-to-End Generative Retrieval Framework for E-commerce
  Search'
title_zh: ICEGR：面向电商搜索的意图一致端到端生成式检索框架
authors:
- Jiayi Tuo
- Hehan Li
- Dongjun Fu
- Xin Lu
- Ling Zhuang
- Fuwei Zhang
- Meifang Li
- Peizhi Xu
- Hanmeng Liu
- Shuanglong Li
affiliations:
- University of Science and Technology of China
- Baidu
- Beihang University
- Renmin University of China
arxiv_id: '2608.29652'
url: https://arxiv.org/abs/2608.29652
pdf_url: https://arxiv.org/pdf/2608.29652
published: '2026-08-30'
collected: '2026-09-01'
category: GenRec
direction: 生成式检索 · Query-intent 一致
tags:
- Generative Retrieval
- Semantic ID
- E-commerce Search
- Query Intent
- Preference Optimization
- Synthetic Query
one_liner: 提出 ICEGR，通过意图感知 Semantic ID、合成查询增强 SFT 与相关性校准偏好优化，提升电商生成式检索的查询意图一致性
practical_value: '可迁移点：

  - Semantic ID 构建：不要只用标题/描述等静态文本。用 query-product 点击 logs 对齐 embedding（InfoNCE），构建
  shared-query co-click 图做语义锚定图传播，再融合产品历史 query 的加权意图向量，并用 confidence gate 控制强度；最后
  RQ-KMeans 量化。利于 SID 空间编码搜索意图，可直接用于生成式检索/推荐中的 item ID 学习。

  - SFT 数据补足：对全目录商品用结构化字段（SPU/品牌/类目/系列/属性）自动生成多粒度合成 query（实体指定 + 属性约束），采用 two-stage：先
  synthetic query-to-SID 训练，再真实日志微调。对长尾低曝光商品尤其有效（Low 组 Recall@20 +36.2%），可显著缓解 query-to-item
  监督稀疏问题。

  - 业务偏好优化：做 DPO/RL 时先限制候选需通过语义相关性 scorer（SRS），只在相关子集内比较业务价值（SBP）；用 pairwise composite-score
  margin 动态缩放 DPO 系数，避免过度优化强偏好对，保留 query 意图。辅助 SFT 项防退化。线上可直接作为端到端生成路径插入 MCA：beam
  search 生成 top-k 直接进最终列表，其余候选走原排序。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

动机
生成式检索（GR）在电商搜索中虽有统一多级召回架构的潜力，但 SID 构建、监督微调和偏好优化三个阶段各自缺乏 query-intent 一致性：静态商品信息构建的 SID 难以编码产品与查询意图的关联；仅有在线日志的 query-to-SID 监督导致长尾低曝光产品监督稀疏；面向业务价值的偏好优化会偏向热门或高价值但偏离 query 的产品，削弱相关性。

方法关键点
- Intent-Aware SID (IA-SID)：先用历史点击对做 query-product embedding 对齐（InfoNCE）；再基于 shared-query co-click 构建加权产品图，做语义锚定的图传播；将产品历史 query 的加权 embedding 作为 query-intent profile，用 confidence gate 做残差融合，最后 RQ-KMeans 量化为层次 SID。
- Synthetic Query-Enhanced Unified SFT (SQE-SFT)：对全目录产品，从 SPU、品牌、类目、系列、属性等结构化信息自动生成实体指定与属性约束两类多粒度 synthetic queries；先训练 synthetic query-to-SID，再在真实日志 query-to-SID 上微调，统一指令格式。
- Relevance-Calibrated Preference Optimization (RCPO)：用 beam search 生成候选，先以语义相关性 scorer（SRS）过滤 off-intent；结合 smoothed business preference（点击/支付/GMV 加权）构造偏好对，按 pairwise composite-score margin 动态调节 DPO 系数，辅助 SFT 项保留相关性。

实验结果
离线在百度电商搜索日志近三个月数据（12.8M query、14.6M 商品）上，与生产生成式检索 baseline ProdGR 对比：Recall@20 +21.7%，NDCG@20 +26.6%。消融显示 SQE-SFT 占 Recall@20 累计增益的 76.7%，RCPO 17.7%，IA-SID 5.6%；SQE-SFT 对 Low/Tail 商品提升 36.2%/21.2%。线上 A/B 测试 CTR +3.52%，订单量 +15.96%，GMV +7.53%；0.5B 模型以 beam 50 达到 2200 QPS、平均 156ms。

最值得记住的一句话：生成式检索不是把 SID、SFT、偏好优化拼起来，而是要把 query-product relevance 作为统一约束贯穿全链路，才能把离线召回提升转成线上 CTR、订单和 GMV。
