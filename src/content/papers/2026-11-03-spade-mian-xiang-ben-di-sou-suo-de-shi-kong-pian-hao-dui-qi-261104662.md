---
title: 'SPADE: Spatiotemporal Preference Alignment and Diversity Enhancement for Local
  Search'
title_zh: SPADE：面向本地搜索的时空偏好对齐与多样性增强框架
authors:
- Chenxu Wang
- Wenxuan Yang
- Yueqi Mou
- Shuxian Bi
- Biao Tang
- Peng Yan
affiliations:
- Meituan
- Independent
arxiv_id: '2611.04662'
url: https://arxiv.org/abs/2611.04662
pdf_url: https://arxiv.org/pdf/2611.04662
published: '2026-11-03'
collected: '2026-11-04'
category: QueryRec
direction: 生成式 Query 推荐 · 本地搜索时空建模
tags:
- Query Recommendation
- Local Search
- Generative Recommendation
- DPO
- Spatiotemporal Encoding
- Diversity Decoding
one_liner: 联合优化词表、时空编码、DPO 对齐与解码多样性，显著提升本地生活 query 推荐
practical_value: '- **OA-BPE 可直接迁移到生成式 item/Semantic ID/query 模型**：用 CTR、CVR、曝光归一化作为
  BPE merge 权重，替代纯频次统计，给高价值长尾实体更短 token 化，训练前就注入业务先验，几乎无额外成本。

  - **STAR 的连续多尺度正弦编码 + 零初始化软门控注入**，适合需要 GPS/时段信号的 LLM 推荐或 Agent 工具调用；比离散 city/geohash
  token 更细粒度，且不破坏预训练表示。

  - **MARS-DPO 是低成本生产对齐方案**：直接复用线上 impression-click 列表构造偏好对，复合 reward 融合 rank/LLM
  可执行性/距离，自适应选 hard negative，再加 SFT anchor 和分反馈权重，能避免 DPO 概率坍塌。

  - **SDBS 做 top-K 多样性比 Diverse Beam Search 更稳**：只给低 rank beam 加 sigmoid bonus，top
  beam 不动，复杂度 O(B)，几乎不掉 HR；适合短候选 slate 需要去重又保召回的场景。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：本地生活 App 首页主动 query 推荐是开集生成问题，输出空间为百万级自由文本，而非固定 item 排序。生成结果必须同时满足长尾意图覆盖、细粒度时空落点、用户偏好对齐、top-K 多样且可执行。现有方法通常孤立处理这些维度：标准 BPE 压制长尾 query，粗粒度位置 token 无法区分商圈，通用偏好优化不匹配生产曝光点击分布，标准 beam search 输出近重复候选。

**方法关键点**：
- **OA-BPE**：用业务价值加权 BPE merge 得分，给高价值长尾 query 更短 token 化，不增加训练成本；
- **STAR**：多尺度六边形正弦空间编码 + 小时周期编码，MLP 融合后经零初始化软门控加性注入 encoder 占位符，逐步引入细粒度时空信号；
- **MARS-DPO**：先跨域 Next Search Query 预训练，再用线上 impression-click 列表构造偏好对；复合 reward 融合 rank、LLM 可执行性、地理距离，自适应 hard negative + SFT anchor + impression/click/conversion 分层权重；
- **SDBS**：对较低 rank beam 加位置相关 sigmoid bonus，top beam 不变，凹且有界，复杂度 O(B)。

**关键结果**：在 100K 用户、1.48M queries 生产数据上，对比 AIGQ、OneSug、Local-SUG 等 baseline，SPADE 的 HR@5 为 13.2 vs 12.5（+5.6%），GeoC@5 为 1.66 vs 2.78（-40.3%），Exec@5 提升 1.9%。长尾意图 HR@5 提升 13.5%，geo-sparse 区域 GeoC@5 降低 48.3%。线上 A/B 测试 Module CTR +1.88%，Search Volume +0.177%，Search DAU +0.105%，P95 延迟 65.4ms。

**一句话**：生成式 query 推荐的核心瓶颈不在模型规模，而在词表、时空编码、偏好对齐和解码四个环节是否联合设计。
