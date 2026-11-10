---
title: 'TS-GEAR: Taobao Shangou GEnerative Ad Retrieval'
title_zh: 淘宝闪购生成式广告检索 TS-GEAR
authors:
- Guofeng Tong
- Xu Zhang
- Guangliang Yu
- Haiqiang Wang
- Guannan Cong
- Xing Guo
- Yang Zhou
- Jingjing Duan
- Shuang Li
- Feng Shi
affiliations:
- Alibaba Group
arxiv_id: '2611.12180'
url: https://arxiv.org/abs/2611.12180
pdf_url: https://arxiv.org/pdf/2611.12180
published: '2026-11-09'
collected: '2026-11-10'
category: GenRec
direction: 生成式检索 · Geo-Semantic ID
tags:
- generative retrieval
- geo-semantic ID
- GRPO
- on-demand delivery
- search advertising
- set-level RL
one_liner: 用 Geo-Semantic ID 将地理可达性编码为前缀约束，结合 Query-Geo Target Attention 和集合级 GMPO
  对齐，广告收入提升 4.2%
practical_value: '- 硬约束编码为 Semantic ID 前缀：把不可导的地理/配送范围过滤变成受限前缀解码，减少 beam 浪费并让模型在约束内学习排序，可迁移到
  LBS、同城电商、本地生活等场景。

  - Query-Geo Target Attention 可复用：用当前 query 和实时位置（或场景）作为双 target 聚合历史行为，并在 key 中融合行为发生时的上下文，能缓解高频但不相关行为主导表示，适合跨区域/跨场景用户兴趣建模。

  - GMPO 的 marginal advantage 思路：在 GRPO/DPO 对齐检索模型时，按去重后集合的边际贡献计算 advantage，能抑制 beam
  search 下重复候选导致的策略坍缩，适合召回/广告候选集联合优化，无需额外多样性损失。

  - 工程部署：地理前缀预计算 + 9-cell 可达前缀强迫 prefill 并复用 KV cache，把生成 token 从 6 降到 4，配合 TensorRT/混合精度，0.1B
  模型即可在 70ms 内服务 150M 日请求，轻量模型 + 结构化约束比盲目放大模型更划算。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
淘宝闪购（Taobao Shangou）是即时配送平台，配送范围是硬约束：不在配送范围内的商家是无效候选，而非低排名。现有生成式检索的 Semantic ID 只编码内容/协同信号，地理只能做不可导的后置过滤，浪费 beam 且无法端到端优化；用户兴趣随实时位置和 query 变化，历史行为聚合存在偏差；AR 训练 token-level 而检索目标是集合级覆盖，beam 易被近似重复商家填满。

**方法关键点**
- **Geo-Semantic ID**：商家 ID 拆为 geohash 地理前缀（3 token，层级约 1250/39/1.2 km）和 RQ-KMeans 语义后缀（3 token），通过九宫格可达前缀受限解码，将可达性变成生成目标而非后过滤。
- **Query-Geo Target Attention**：encoder 中以实时 query+location 为双 target，行为 key 融合其发生时的位置和语义，降低无关历史的影响；User-Geo Gate 在 decoder 生成地理 token 时注入用户位置嵌入，调节邻近 cell 探索。
- **GMPO**：用去重后组奖励的边际贡献（MA）融合 GRPO 单样本 advantage，直接优化候选集覆盖，抑制 beam collapse，无需辅助多样性损失。

**关键结果**
TS-Delivery 工业数据（0.1B 用户/4.8M 商家/0.5B 交互）上，δ=20km 生产半径下相对最强 baseline OneLoc，HR@50 提升 36.3%（0.5929→0.8080），ValidRate@50 达 95.8% vs 35.4%；公开 Foursquare NYC/TKY 全部最优；7 天在线 A/B：广告曝光 +3.8%、广告收入 +4.2%，0.1B 模型日服务 150M 请求。

**最值得记住的一句话**
把硬约束编码为 ID 前缀并结构性满足，优于后过滤；RL 对齐要面向集合覆盖而非单样本奖励。
