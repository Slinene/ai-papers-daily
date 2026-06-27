---
title: Hierarchical Partial-Order Models for Ranking
title_zh: 层次偏序模型用于排名聚合
authors:
- Dongqing Li
- Geoff K. Nicholls
- Jeong Eun Lee
- Chuxuan
- Jiang
affiliations:
- University of Oxford
- University of Auckland
arxiv_id: '2606.25062'
url: https://arxiv.org/abs/2606.25062
pdf_url: https://arxiv.org/pdf/2606.25062
published: '2026-06-23'
collected: '2026-06-27'
category: RecSys
direction: 偏序排名聚合 · 层次聚类
tags:
- partial orders
- rank aggregation
- hierarchical model
- Bayesian inference
- MCMC
- clustering
one_liner: 将偏序排名模型扩展到层次结构，建模分组偏好并保持不可比性，优于现有方法。
practical_value: '- 在推荐系统中，用户行为（点击、购买）常表现为偏序关系而非全序，使用偏序建模可更准确地捕捉偏好不确定性，避免强制排序带来的噪声。

  - 层次结构允许跨用户群组共享信息，可应用于冷启动用户或稀疏评分场景，通过纳入群体先验提升预测精度。

  - 无监督聚类扩展 HCPO 能自动发现用户群体结构，可直接用于用户分群或兴趣聚类，替代传统 k-means 等硬聚类方法。

  - MCMC 推断输出后验分布，可提供不确定性量化，有助于推荐可解释性及风险控制，例如在广告投放中评估偏好排序的置信度。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：传统排名聚合模型假设用户偏好为全序，但真实场景中存在大量不可比性。现有偏序模型未考虑分组数据，而实际业务中用户常呈现群体性偏好。为此需要一种既能保留偏序结构，又能跨组共享信息的层次化模型。

**方法**：提出 **层次偏序模型（HPO）**，通过在用户组间建立潜在偏序的层次结构，实现信息共享。该框架将 Plackett-Luce 等经典模型纳入为特例；进一步开发 **层次聚类偏序模型（HCPO）**，在组标签未知时同时进行聚类与偏好推断。推断采用 **贝叶斯 MCMC** 方法，得到完整的后验分布。

**结果**：在合成数据、声学偏好配对数据集及 **LLM agent 轨迹** 上评估，HPO 和 HCPO 在留出样本的预测对数似然和聚类结构恢复等指标上显著超过基线，同时生成的偏序图提供了可解释的群体偏好结构。
