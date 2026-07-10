---
title: 'EdgeRefine: Privacy-Utility Balance for Graphs via Jaccard Sampling under
  Edge Differential Privacy'
title_zh: EdgeRefine：Jaccard 采样边差分隐私的图效用平衡方法
authors:
- Wenxiu Ding
- Muzhi Liu
- Zheng Yan
- Mingjun Wang
- Yifan Zhao
- Qiao Liu
affiliations:
- State Key Laboratory of Integrated Services Networks, School of Cyber Engineering,
  Xidian University
- School of Cyber Engineering, Xidian University
arxiv_id: '2607.08659'
url: https://arxiv.org/abs/2607.08659
pdf_url: https://arxiv.org/pdf/2607.08659
published: '2026-07-09'
collected: '2026-07-10'
category: Other
direction: 图隐私保护 · 边缘差分隐私
tags:
- Edge Differential Privacy
- Graph Neural Networks
- Jaccard Similarity
- Privacy-Utility Trade-off
- Adaptive Sampling
one_liner: 通过 Jaccard 相似度估计边概率并自适应采样，在边差分隐私下显著提升 GNN 准确率。
practical_value: '- 用户-物品交互图添加边差分隐私时，不再均匀加噪，可先用 Jaccard 相似度评估边重要性（共现性），按隐私预算划分排名，优先保留强关联边、剔除弱关联边，再补充少量假边，大幅减少噪声注入。

  - 两阶段采样控制图稀疏性：用 ε 确定真/假边比例，用采样率 k 控制总边数，这一策略可直接应用于隐私保护下的 GNN 推荐模型训练，在保证 ε-差分隐私的同时维持图质量。

  - 可嵌入联邦图学习：各客户端本地应用 EdgeRefine 生成隐私保护子图后上传，降低通信噪声并提升聚合模型精度。

  - Jaccard 相似度计算复杂度低，适合大规模工业图加速，可借助 MinHash 等近似算法实现高效部署。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：GNN 处理社交、电商等图数据时，边结构可能泄露用户交互隐私。边缘差分隐私（edge-DP）通过向邻接矩阵注入噪声提供保护，但隐私越强噪声越大，图效用严重退化。现有方法常均匀加噪，未区分边的重要性，导致高噪声下准确率崩溃。

**方法**：提出 EdgeRefine，一种本地差分隐私框架。先用 Jaccard 相似度估计每条边存在的概率，并据此排序；利用隐私预算 ε 计算真边与假边的保留比例，按概率排名分别进行无放回采样，优先抽取高概率真边、低概率假边；再通过额外采样率 k 控制最终总边数，维持图稀疏性。整个过程仅依赖单跳邻居信息，符合本地隐私设定。

**关键结果**：
- 节点分类：ε=2.5 时，ACM 上 GAT 准确率提升 17.8%，Cora 上 GCN 提升 19.7%，均大幅优于 SOTA 隐私基线；
- 图分类：相比无噪声基线，平均精度下降仅约 5%；
- 抗攻击：图重构攻击下的相对绝对误差始终 >1（Cora 平均 1.962，AMAP 1.472），有效抵抗隐私泄露。
