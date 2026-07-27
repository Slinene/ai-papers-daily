---
title: Local-Global Geometric Insights for Graph Neural Networks via Entropic Curvature
title_zh: 基于熵曲率的图神经网络局部-全局几何洞察
authors:
- Rachid Caich
- Yassine Abbahaddou
affiliations:
- Centre de recherches mathématiques (CRM), Université de Montréal
- LIX, École Polytechnique, IP Paris
arxiv_id: '2607.22381'
url: https://arxiv.org/abs/2607.22381
pdf_url: https://arxiv.org/pdf/2607.22381
published: '2026-07-24'
collected: '2026-07-27'
category: Other
direction: 几何深度学习 · 全局图曲率
tags:
- Graph Curvature
- Oversmoothing
- Oversquashing
- Entropic Curvature
- GNN Architecture
- Graph Rewiring
one_liner: 引入全局熵曲率统一图神经网络的过平滑与过挤压，并提出E-Gate聚合、ENT编码和MCR重连三种机制。
practical_value: '- **E-Gate 聚合器可替代 GNN 中的均值/注意力聚合**：通过熵曲率加权邻居信息，能自适应抑制噪声节点，在用户-商品交互图上可缓解深度模型中节点表征坍缩，提升长尾物品推荐。

  - **ENT 结构编码作为节点初始化特征**：该编码捕获全局几何信息，类似图位置编码，可拼接至用户/物品原始特征，增强冷启动节点表示，适合电商异构图场景。

  - **MCR 图重连策略用于缓解信息瓶颈**：在社交推荐或协同过滤图中，对关键位置添加“中点边”或补全三角形，能加速长程依赖传播，可作为一种数据增强手段优化图结构。

  - **过平滑与过挤压的统一分析视角**：通过曲率谱指导网络深度与宽度设计，建议在推荐图深 GNN 中动态监控局部曲率，以平衡信息混合与保持辨别力。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有图曲率（Ollivier-Ricci、Forman）仅关注局部边级比较，无法刻画长程信息传播，使得 GNN 的过平滑（节点特征趋同）和过挤压（远距离信息被瓶颈压缩）问题缺乏全局几何解释。

**方法**：将 Lott-Sturm-Villani 框架推广到图，定义基于 W1-Wasserstein 测地线上熵位移凸性的 **全局熵曲率**，提出可计算的弱熵曲率代理 \(\kappa_w\)。由此导出三项理论结果：①控制过平滑的 Poincaré 型不等式；②运输-熵泛化界；③**扩展悖论**（大图中稀疏性、强谱扩展与正熵曲率不可共存），将过平滑与过挤压统一为曲率谱的两端。基于理论落地三种机制：**E-Gate 聚合器**（用 \(\kappa_w\) 对邻居加权）、**ENT 结构编码**（基于全局几何的节点特征）、**MCR 重连**（在负曲率边中点补全三角形以缓解瓶颈）。

**结果**：在 6 个节点分类和图分类基准上，所提机制优于 SDRF、FoSR、BORF、LCP、Graph Ricci Flow 等重连/编码方法，同时有效缓解过平滑和过挤压，验证了全局曲率指导 GNN 设计的有效性。
