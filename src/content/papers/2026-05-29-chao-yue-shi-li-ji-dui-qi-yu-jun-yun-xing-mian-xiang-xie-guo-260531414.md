---
title: 'Beyond Instance-Level Alignment and Uniformity: Semantic Factor Learning for
  Collaborative Filtering'
title_zh: 超越实例级对齐与均匀性：面向协同过滤的语义因子学习
authors:
- Yajie Yu
- Chenzhong Bin
- Zhoubo Xu
- Zhixin Zeng
- Tongxin Xu
- Cihan Xia
- Jiafeng Wu
affiliations:
- Guilin University of Electronic Technology
- Johns Hopkins University
arxiv_id: '2605.31414'
url: https://arxiv.org/abs/2605.31414
pdf_url: https://arxiv.org/pdf/2605.31414
published: '2026-05-29'
collected: '2026-06-01'
category: RecSys
direction: 协同过滤 · 语义增强正例扩充
tags:
- collaborative filtering
- semantic factor learning
- alignment and uniformity
- false negative mitigation
- recommendation
one_liner: 通过语义因子匹配发现假负例并构造潜在正例对，在未扩展图结构的MF框架下捕获高阶协同信号，显著提升稀疏数据下的推荐精度与效率。
practical_value: '- 提出 **Semantic Factor Routing (SFR)** 模块，用迭代软路由从 item 嵌入中解耦出全局语义因子，可作为即插即用组件放入现有
  MF/GCN 推荐模型中，提升对稀疏行为的建模能力。

  - **Semantic Factor Matching (SFM)** 通过匹配共享语义因子的未交互 item 来扩充正例信号，缓解隐式反馈中假负例问题；该思想可直接迁移到电商推荐中处理冷启动物品或长尾用户。

  - 整体框架 **SaFeAU** 完全基于矩阵分解，无需图卷积即可达到甚至超越 GCN 方法的效果，训练复杂度低，易于在百万级交互的电商场景中部署。

  - 对均匀性（Uniformity）损失的权重调优发现：数据越稀疏，均匀性正则化越重要；这一结论可用于指导损失函数中正例扩充项与均匀项的比例设置。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：协同过滤在隐式反馈下面临严重的假负例问题——大量未交互 item 可能是用户潜在感兴趣的，但被错误地当作负样本推开，损害模型泛化。同时，基于 GCN 的方法计算成本高，并易受过平滑影响，难以捕获精确的高阶偏好。为解决这两个痛点，本文提出从语义因子层面发现假负例并补充监督信号，让 MF 也能有效利用高阶协同关系。

**方法关键点**：
- **Semantic Factor Routing (SFR)**：受胶囊网络动态路由启发，在 batch 内通过多次迭代软路由将每个 item 的嵌入分配到 K 个全局语义因子，每个因子隐含品牌、材质等属性，实现 item 属性解耦。
- **Semantic Factor Matching (SFM)**：对每个交互 item，选取其 top-k 语义因子，将 batch 中共享至少 δ 个这些因子的未交互 item 视作潜在正例，扩充监督信号。
- **Semantic Pairs Alignment (SPA)**：在传统对齐+均匀性损失基础上，加入语义正例对齐项，拉近用户与潜在正例物品的表示，同时保持全局均匀性。
- **整体优化**：多任务联合优化，无需显式负采样，避免随机采样带来的性能波动。

**关键结果**：在 Gowalla、Toys-and-Games、Beauty、Yelp2018 四个稀疏数据集上，SaFeAU 在 Recall@K 和 NDCG@K 上全面超越 LightGCN、DirectAU、LightCCF 等最强基线，尤其在稀疏数据上提升显著（Gowalla 上 Recall@20 相对最佳基线提升 5.39%）。同时，SFM 产生的潜在正例质量远超随机选取，验证了语义匹配的有效性。时间复杂度分析表明，SaFeAU 与轻量级 MF 方法相当，远优于 GCN 方法。

**一句话结论**：用语义因子匹配发现假负例并构造潜在正例对齐，在保持高效训练的同时，赋予协同过滤模型处理稀疏信号的能力。
