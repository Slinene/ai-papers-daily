---
title: Efficient Swing Computation for Retrieval in Large-Scale Recommender Systems
title_zh: 大规模推荐系统中面向召回的 Swing 高效计算
authors:
- Runhao Jiang
- Renchi Yang
affiliations:
- Hong Kong Baptist University
arxiv_id: '2609.16850'
url: https://arxiv.org/abs/2609.16850
pdf_url: https://arxiv.org/pdf/2609.16850
published: '2026-09-15'
collected: '2026-09-16'
category: RecSys
direction: 图算法加速 · Swing 相似度
tags:
- Swing
- i2i retrieval
- approximate algorithms
- top-K retrieval
- Monte Carlo
- graph algorithms
one_liner: 提出 ASC 与 K-ASC，用概率误差界替代截断启发式，将 Swing 检索提速数个数量级
practical_value: '- 用 K-ASC 的过滤-精炼模式替代工业界截断（如只取 600 邻居）：先用少量采样生成 top-(K+κ) 候选和置信界，只对边界
  item 精炼，避免均匀分配采样预算，可显著加速 i2i 召回而不损失精度。

  - 对高热度物品采用采样估计（GNS），低热度物品用枚举（USS），在线系统可按物品度数动态切换算法，降低尾部延迟，适合实时召回/粗排场景。

  - QFilter++ 利用 SIMD + popcount 仅计算交集基数而不材料化交集，可复用于 itemCF、Swing 等任何基于用户共现的相似度计算，提升单机吞吐。

  - 在十亿边图上，K-ASC 可实现毫秒级 top-K Swing 检索，适合作为召回阶段的实时信号，避免大规模 MapReduce 离线任务，对电商/广告的
  item 相似度计算有直接工程价值。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
Swing 是工业界广泛使用的 item-to-item 相似度，被阿里、快手、Shopee 等用于冷启动、广告推荐、query 改写等场景。但精确计算 Swing 的复杂度为 O(d(v_q)^2 · avg_user_degree)，高热度 item 可能涉及百万级用户对，单次查询需数小时；工业界常用截断启发式（如只取 600 个邻居）但会损失召回质量。本文形式化 (ε,λ)-近似 Swing 查询与 top-K Swing 查询，旨在用概率误差保证替代硬截断。

## 方法关键点
- **GNS（Grouped Naïve Sampling）**：对 Naive Monte Carlo 的优化，将重复采样的用户对分组计数，集合交集只对 distinct 用户对计算一次，保持无偏估计，显著减少冗余交集运算。
- **USS（User Subset Sampling）**：从用户邻居中采样子集，只计算交集基数而不材料化大交集，避免高复杂度内存占用，适合低度物品的枚举场景。
- **ASC（Adaptive Swing Computation）**：基于解析成本模型，按查询 item 的度数在 GNS 和 USS 之间自适应选择，同时满足 (ε,λ) 近似保证。
- **K-ASC**：针对 top-K 查询的过滤-精炼框架。先用约 10% 采样预算粗估 Swing，生成 top-(K+κ) 候选集；利用经验 Bernstein 不等式构建置信界，识别边界候选；剩余预算仅精炼这些边界项。在十亿边图上保持高性能。
- **QFilter++**：对集合交集的底层优化，使用 SIMD 指令和 popcount 快速计算交集基数，避免显式物化交集。

## 关键实验
在 8 个真实数据集（MovieLens、Gowalla、AmazonBook、SteamGame、MIND、Twitch、Yambda、MAG）上对比 Exact、Truncated、Naive-MC、GNS、USS、All-Pairs、WHIMP。ASC 和 K-ASC 在相同精度下比基线快数个数量级。在最大图 MAG 上，K-ASC 实现 top-100 查询平均精度 >99.9%，仅需 1.5ms，而精确方法需 8.5s；在 Twitch 上，Exact 对热门 item 平均超过 3.8s，K-ASC 降至毫秒级。

## 最值得记住的一句话
概率误差控制 + 过滤-精炼 + 自适应选择，能把 Swing 检索从小时级压缩到毫秒级，同时保持 top-K 精度 99.9%。
