---
title: Sheaf-Inspired Structured Scoring Extensions of LightGCN for Collaborative
  Filtering
title_zh: 受层启发结构化评分扩展的 LightGCN 协同过滤
authors:
- Ksenia Belkovskaya
- Timur Lidzhiev
- Maria Stebliy
- Alexander Tarakanov
arxiv_id: '2611.17226'
url: https://arxiv.org/abs/2611.17226
pdf_url: https://arxiv.org/pdf/2611.17226
published: '2026-11-12'
collected: '2026-11-15'
category: RecSys
direction: 图协同过滤 · 评分函数结构化扩展
tags:
- LightGCN
- collaborative filtering
- sheaf-inspired
- scoring
- coverage
- recommendation
one_liner: 在 LightGCN 之上比较对角、秩一、全矩阵残差等结构化评分器，发现排名质量变化温和但覆盖率变化显著
practical_value: '- 如果现有图召回/排序模型采用内积打分，可以低成本插入可学习的结构化 scorer（diagonal / 秩一 / 全矩阵残差）作为即插即用模块；rank-one
  适合轻量线上场景，参数量小且不改变图传播。

  - 评估时除了 Recall/NDCG，建议加入 item catalog coverage@K；论文发现结构化 scorer 对覆盖率的改变有时远大于排名质量，这在电商/广告中对应长尾库存曝光和广告多样性。

  - 几何 inspired 的结构并不自动带来收益：业务上引入新评分结构前，应先用参数匹配的 MLP 基线做对比，并做严格 ablation，避免把性能变化归因于未实现的
  sheaf 机制。

  - 可考虑将结构化 scorer 与重排/多目标结合，例如对用户-物品 pair 学习不同的线性变换矩阵，用于 CTR 与 eCPM 等异构目标打分。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：LightGCN 使用用户和物品 embedding 的内积作为兼容性分数，隐式假设共享嵌入坐标系，难以显式建模用户与物品表示之间的异构变换。借鉴 cellular sheaf 中局部向量空间与线性 restriction map 的思想，在不动图传播结构的前提下，对评分函数做结构化改造。

**方法**：在 3 层 LightGCN backbone 上叠加模块化结构化评分扩展。比较 identity 内积 scorer、diagonal、rank-one 低秩、full matrix 残差 scorer，以及参数匹配的 residual MLP 基线 mlp_full。实验覆盖 Amazon-Book、Gowalla、MovieLens-1M、Yelp2018，评估 cutoff 10/20 下的排名质量与 catalog coverage。

**结果**：结构化变体在排名质量上仅有 modest、依赖数据集的改变；覆盖率有时出现较大变化。作者明确指出该方法没有构造 cellular sheaf 或实现 sheaf-Laplacian diffusion，因此无法建立 sheaf geometry 本身的因果收益。整体贡献是系统比较了 LightGCN 上层结构化评分扩展的模块化设计与效果。
