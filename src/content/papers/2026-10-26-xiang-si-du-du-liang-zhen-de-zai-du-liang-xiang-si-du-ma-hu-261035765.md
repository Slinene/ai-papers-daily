---
title: Do Similarity Measures Measure Similarity? How User Activity Creates Phantom
  Correlation in Recommender Systems
title_zh: 相似度度量真的在度量相似度吗？用户活跃度如何在推荐系统中制造幻影相关
authors:
- Marco Favier
- Noah Daniëls
- Jens Leysen
- Sander Marinus
- Bart Goethals
affiliations:
- University of Antwerp
arxiv_id: '2610.35765'
url: https://arxiv.org/abs/2610.35765
pdf_url: https://arxiv.org/pdf/2610.35765
published: '2026-10-26'
collected: '2026-10-27'
category: RecSys
direction: 推荐系统 · 物品相似度 · 活跃度偏差
tags:
- Item-item similarity
- Phantom correlation
- User activity
- Rasch model
- Popularity bias
- Implicit feedback
one_liner: 证明 item-item 相似度中存在由用户活跃度差异而非共同偏好导致的幻影相关，并用 Rasch 模型量化其占比
practical_value: '- 在电商/广告的 item-item 相似度或召回中，先拟合单维活跃度 Rasch 模型作为 baseline，把 raw lift/cosine/Pearson
  与 activity baseline 做残差或标准化，避免把高频用户带来的共现误判为偏好。

  - 理解相似度度量的 popularity baseline 形状：lift/PMI 在稀有 item 上天然偏高，cosine 在热门 item 上天然偏高。排序聚合相似度时，热门
  item 会获得与偏好无关的 head start，需要显式去偏或改用残差相似度。

  - 工程上可用历史长度方差快速判断幻影相关风险：若 Var(history length) 远大于 Σ p_i(1-p_i)，活跃度异质性会贡献大量 item
  协方差；在 top-N 截断或固定长度数据上该现象会减弱，评估离线数据时注意数据生成机制。

  - 对 EASE/SLIM 等学习到的相似度矩阵同样适用；真实偏好主要存在于偏离 activity baseline 的 pair 排序中，而不是绝对相似度值。构建生成式推荐或
  Semantic ID 时也应先去除活跃度混杂。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
item-item 相似度是推荐系统最基础的信号之一：两个物品被相同用户消费常被解读为共同偏好。但用户活跃度分布高度异质，活跃用户更可能消费所有物品。论文证明即使没有任何偏好结构，仅凭用户活跃度差异，标准相似度度量也会产生显著正相关，称为 phantom correlation。这直接影响对协同过滤信号的解释和后续排序。

**方法关键点**
- 用三个条件刻画纯活跃度模型：给定活跃度 trait θ 用户独立消费；θ 对所有物品消费概率非递减；消费总数 S 是 θ 的充分统计量。三者等价于 Rasch 模型：logit P(X_i=1|θ)=h_i+θ。
- 由此推导幻影相关性质：任意物品对协方差非负；总协方差由历史长度方差决定，Var(S)-Σp_i(1-p_i)。lift 在稀有物品上 baseline 偏高、随流行度下降；cosine 在热门物品上偏高；Pearson 介于两者之间。
- 用 EM 拟合非参数θ分布和 item 参数，仅使用 item 流行度与用户历史长度分布，不用 pair co-occurrence，得到 activity model 的共现和相似度。
- 比较 observed vs activity model vs independence，用 Poisson deviance / standardized error 量化 activity 解释比例，并用 popularity surface 拟合度量的流行度形状。

**关键实验**
在 MovieLens-1M、MovieLens-20M、Last.fm、Amazon Books 上评估。MovieLens 数据中 activity model 移除大部分 independence 系统性偏差：deviance share 0.81/0.73，lift/cosine/Pearson 在 block 上达 0.98/0.99；Amazon Books 移除约一半，因用户还存在 mainstreaminess 第二维度；Last.fm 因 top 50 截断导致历史长度方差不足，activity 无法解释。EASE 权重结果类似但略低。observed 与 activity model 的 lift Spearman 相关仅 0.31，说明偏好信息主要存在于偏离 baseline 的 pair 排序中。

**最值得记住的一句话**
每次把 item-item 相似度解读为共同偏好前，先问其中多少只是用户活跃度。
