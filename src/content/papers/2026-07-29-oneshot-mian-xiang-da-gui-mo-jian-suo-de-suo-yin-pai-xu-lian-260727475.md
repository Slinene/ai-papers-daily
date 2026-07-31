---
title: 'OneShot: Index-in-Ranking with Neural Scoring for Large-Scale Retrieval'
title_zh: OneShot：面向大规模检索的索引排序联合学习与神经评分扩展
authors:
- Ziwei Li
- Shuyao Li
- Xufeng Cai
- Xue Zou
- Yiming Ma
- Huiting Lu
- Wujie Yan
- Zhichen Zhao
- Yang Lu
- Zhe Wang
affiliations:
- Meta Platforms, Inc.
arxiv_id: '2607.27475'
url: https://arxiv.org/abs/2607.27475
pdf_url: https://arxiv.org/pdf/2607.27475
published: '2026-07-29'
collected: '2026-07-31'
category: RecSys
direction: 检索阶段索引-排序联合学习
tags:
- In-model indexing
- Neural scoring
- Hierarchical index
- Index balancing
- Large-scale retrieval
- End-to-end training
one_liner: 首个端到端可训练的检索索引框架，将索引学习与排序目标对齐，并通过神经评分突破点积瓶颈，已在 Instagram 全量部署。
practical_value: '- **端到端联合训练索引与排序**：可将聚类中心作为可训练参数，与推荐损失（如 SSM）直接联合优化，通过直通估计器（STE）解决离散分配的梯度问题，消除先训练再聚类的错位。

  - **在检索阶段引入非线性交互**：使用小型 DNN 替代点积计算用户-物品分数，并通过 segment-wise 多路矩阵乘法控制计算复杂度，可在召回粗排或向量检索中提升表达能力。

  - **全局索引平衡策略**：利用随机组合优化导出的代理损失，通过维护全局硬分配统计量并用软分配回传梯度，能有效防止索引坍塌、保持聚类均匀，适用于大规模物料库的检索效率保障。

  - **Engagement ID 优于离线 Semantic ID**：实验表明，端到端学出的 EID 在召回和聚类平衡性上远超传统语义 ID；若无法完全替换，可先冻结码本、仅学习物品到
  ID 的分配（Hybrid 方式），也能恢复大部分收益。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业检索系统存在索引与排序目标的结构性错位：排序优化用户行为对齐，索引则基于嵌入空间近邻聚类（如 k-means），二者割裂导致交互建模只能局限于点积，限制了检索表达的提升。已有在模型内建索引的方法（如 Streaming VQ）要么非端到端，要么无法扩展交互复杂度。

### 方法
**1. 端到端分层 in-model 索引**
- 在 item tower 上附加多层级 one-hot 编码层，码本训练与排序损失联合优化，前向使用硬分配，反向通过 STE 以软分配传递梯度。
- 每层码本输出作为簇心向量，各层分数按残差提升方式累加，构成 boosting 架构。

**2. 神经评分交互扩展**
- 将用户-物品打分函数从点积升级为可训练神经网络（NNd, NNl），实现深层次交叉；同时引入 segment-wise 多路矩阵乘法降低 O(B²) 交互的计算开销。
- dense embedding 与 code embedding 解耦，前者保留细粒度评分，后者专注粗排与索引。

**3. 全局索引平衡正则**
- 从 KL 散度出发，将聚类均衡需求建模为全局均匀分布约束，利用随机组合优化理论推导出可直接加入训练的代理损失 L_bal：维护硬分配的 running mean，用当前 batch 软分配与其对数内积计算梯度，避免崩溃。

**4. 在线服务**
- 索引阶段对每层码本使用 beam search 选取 Top 路径，密集打分阶段对所有路径对应物品进行神经评分，显著压缩排序量。

### 关键结果
- **离线**：1% 排序量下，单层 OneShot（16384 码）比 k-means ANN 召回相对提升 20%；双层 (2048,1024) 在同等召回下排序量减少 90%（效率 10×）。增大交互网络宽度 m 和深度 K 可进一步提高召回。平衡方法对比中，OneShot 的 KL 方案召回 0.4679，聚类比最均匀。
- **在线**：在 Instagram 全量推送后，用户会话 +0.035%，观看时长 +0.136%，检索源贡献率 +61.6%。
- **生成式 ID**：OneShot 学出的 Engagement ID 召回达 0.4308，远超离线语义 ID（0.1354），且 Hybrid 方案（冻结码本仅学分配）即可恢复绝大部分性能。
