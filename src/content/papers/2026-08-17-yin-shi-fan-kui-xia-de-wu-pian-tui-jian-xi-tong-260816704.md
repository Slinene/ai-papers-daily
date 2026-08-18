---
title: Unbiased Recommender Systems with Implicit Feedback
title_zh: 隐式反馈下的无偏推荐系统
authors:
- Md Aminul Islam
affiliations:
- University of Illinois Chicago
arxiv_id: '2608.16704'
url: https://arxiv.org/abs/2608.16704
pdf_url: https://arxiv.org/pdf/2608.16704
published: '2026-08-17'
collected: '2026-08-18'
category: RecSys
direction: 无偏推荐 · 位置/流行度偏差
tags:
- position bias
- popularity bias
- unbiased learning
- collaborative filtering
- graph neural networks
- learning to rank
one_liner: 系统研究推荐中位置偏差与流行度偏差的缓解方法，覆盖LTR、CF和GNN社交推荐
practical_value: '- **位置偏差处理**：在电商搜索/推荐排序中，可直接借鉴无偏LTR的思路，如使用逆倾向加权（IPW）或引入位置作为特征，在训练时对点击/成交等隐式反馈进行去偏，减少高排名项的虚假优势。

  - **流行度偏差缓解**：面对冷启动或长尾商品，可参考CF和GNN上的去偏方法，例如对热门物品进行负采样抑制、在损失函数中加入流行度正则项，或使用图结构上的邻居重加权，提升长尾物品曝光公平性。

  - **社交推荐扩展**：若业务中有社交关系或用户-用户图，可将该研究中的GNN去偏思路迁移至社交电商场景，例如在聚合邻居时考虑交互偏差，避免高流行度节点主导表示。

  - **工程实现建议**：部署时需监控线上指标与离线指标的一致性，位置偏差可能导致离线AUC虚高，建议在评估阶段也采用无偏指标或对曝光概率进行校正。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：推荐系统依赖点击等隐式反馈推断偏好，但这类数据天然存在位置偏差（排名靠前的物品获得更多交互）和流行度偏差（热门物品被过度曝光，冷门物品被低估）。直接基于有偏数据训练会误导模型，导致推荐偏离真实用户偏好。

**方法关键点**：
- 针对学习排序（LTR）系统，研究如何消除位置偏差，使模型关注物品真实相关性而非展示位置；
- 针对协同过滤（CF）模型，研究流行度偏差的校正方法，避免热门物品挤压长尾物品；
- 针对基于图神经网络（GNN）的社交推荐系统，研究如何在聚合社交信息时同时缓解位置与流行度偏差。

论文提出一系列方法，克服现有去偏技术的局限，提升推荐的个性化和相关性。

**关键结果**：在多个隐式反馈数据集上验证，所提方法在缓解位置偏差和流行度偏差后，推荐准确性与用户偏好对齐程度显著提升，尤其在长尾物品推荐和公平性指标上表现更优。
