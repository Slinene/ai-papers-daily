---
title: 'Scaling Graph Neural Networks for Friend Recommendation: Multi-Hash User Embeddings
  and Temporal Neighbor Sampling'
title_zh: 大规模好友推荐图神经网络：多哈希用户嵌入与时序邻居采样
authors:
- Maksim Utushkin
- Andrei Ovsiannikov
- Alexander D'yakonov
affiliations:
- AI VK
arxiv_id: '2608.27413'
url: https://arxiv.org/abs/2608.27413
pdf_url: https://arxiv.org/pdf/2608.27413
published: '2026-08-27'
collected: '2026-08-28'
category: RecSys
direction: 大规模图神经网络 · 多哈希嵌入与时间邻居采样
tags:
- GNN
- friend recommendation
- multi-hash embeddings
- temporal neighbor sampling
- industrial recommender
- scalability
one_liner: 用多哈希嵌入压缩98% ID表、以timestamp-sorted CSR+二分搜索加速时序邻居采样，线上好友添加提升16%
practical_value: '- 高基数 ID 特征可优先尝试 multi-hash：用 k=3 个独立哈希映射到共享表 B=2^21、d=256，拼接后线性投影，ID
  表从 203GB 降到 2GB，且离线 ROC-AUC 略高于 full table（0.6278 vs 0.6246），存在隐式正则化收益。电商/广告中的用户
  ID、店铺 ID、类目交叉等高基数特征可复用此套路。

  - 时序图训练务必做时间邻居采样，否则未来边泄漏导致明显掉点（本文 ROC-AUC 降 0.037）。工程上用 timestamp-sorted CSR + lower_bound
  二分搜索定位有效前缀再采样，将每 batch 采样时间从 1473ms 降到 595ms，接近非时序成本。对用户行为序列、社交/互动图等动态图尤其有用。

  - 大规模图训练采用 CPU 采样与 GPU 训练解耦的 producer-consumer 流水线，CSR 索引用 32-bit 存邻居 ID 和时间戳、64-bit
  存 offset，可把 225GB 图压缩到单机 8×A100 可承载；资源受限团队可直接借鉴该存储与调度方案。

  - GNN 在线推理成本高，可改为周期性离线刷新用户嵌入，服务时作为特征供下游 GBDT ranker 读取；同时用 query/candidate 双头区分同一用户作为请求方与候选方的不同角色，该技巧对双塔召回/排序也有迁移价值。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

好友推荐本质是图结构任务，排序信号主要来自多跳社交上下文，但在 194M 节点 / 28B 边的生产图上部署 message-passing GNN 面临三个硬约束：全量可训练 ID 表 >200GB 不可行；用户画像内容弱，但图结构信号强；动态图训练若直接聚合未来边会泄漏标签，而 naive 时序采样对 hub 用户要扫描完整邻接表（O(deg)）。文章围绕两个关键设计展开。

方法要点：
- 节点输入 = 表格特征（性别/年龄/度，投影后求和）+ 多哈希 ID 嵌入。多哈希：k=3 个独立哈希将用户 ID 映射到共享表 B=2^21、d=256，拼接后线性投影，ID 表从约 203GB 降到 2GB。
- 编码器为 2 层 GATv2，最后通过 query/candidate 双头投影，区分“请求方”与“候选方”角色。
- 时间邻居采样：邻接表按 timestamp 升序存储为 CSR，用 lower_bound 二分搜索定位有效前缀，再从前缀均匀采样 K 个邻居，复杂度从 O(deg+K) 降到 O(log deg+K)；同一切断时间传播到所有 hop。
- 训练系统解耦 CPU 采样与 GPU 训练，单机 8×A100 承载 225GB CSR 图；推理采用周期性离线刷新用户嵌入，避免在线图计算延迟。

关键结果：离线 per-user ROC-AUC 从 WalkGNN 的 0.5572 提升到 0.6278。多哈希与 full table 对比：0.6278 vs 0.6246，存储降到 <1%；非时序模型 0.5907，naive 时序采样每 batch 1473ms，二分搜索 595ms。线上 A/B：好友添加 +16%，唯一添加者 +11.5%，内容 feed 时长 +0.28%。最值得记住：多哈希 ID 压缩 98% 内存且质量不降，timestamp-sorted CSR + 二分搜索几乎以非时序成本实现时间正确性。
