---
title: 'Same Graph Cross-Task Transfer in GNNs: Protocols and Predictors'
title_zh: 图上同图跨任务迁移的协议与预测方法
authors:
- Neelam Akula
- Surbhi Kumar
- Murat Kantarcioglu
- Baris Coskunuzer
affiliations:
- University of Texas at Dallas
- Virginia Polytechnic Institute and State University
arxiv_id: '2607.28525'
url: https://arxiv.org/abs/2607.28525
pdf_url: https://arxiv.org/pdf/2607.28525
published: '2026-07-30'
collected: '2026-08-02'
category: Other
direction: 同图跨任务迁移的评估协议与预测因子
tags:
- GNN
- transfer learning
- node classification
- link prediction
- homophily
- cross-task
one_liner: 提出无泄漏评估协议并揭示节点分类与链路预测跨任务迁移的方向性和可预测性
practical_value: '- **泄漏防护协议可迁移至多任务图学习评估**：在电商推荐中，用户-商品交互图常同时需要节点分类（如用户属性）和链路预测（如购买行为），可采用固定节点/边划分、消息传递图排除评估边、固定负样本的策略，避免数据泄漏导致的错误乐观估计。

  - **根据同质性选择迁移方向**：实验表明 NC→LP 在 homophilic 图上稳定正向，而 LP→NC 仅在结构易学且节点分类任务不饱和时才有效。在构建多任务模型时，可先计算图的同质性指数，指导是采用共享编码器还是分离任务分支。

  - **LP 作为结构预训练**：在用户-商品图中，若节点属性稀疏或不可靠，可先用链路预测任务预训练 GNN，再微调到节点分类（如用户流失预测），但需监控目标任务的饱和程度，防止负迁移。

  - **CoTask Score (CTS) 作为联合目标**：当需要单一编码器同时服务 NC 和 LP 时，CTS 能综合衡量两者效用，帮助选择最佳模型架构和训练机制，避免多任务折衷中的性能退化。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：真实图常同时支撑节点分类（NC）和链路预测（LP），但现有跨任务迁移评估因数据划分泄漏、负采样不一致而不可靠。
**方法**：形式化同图 NC–LP 迁移，提出泄漏防护协议：固定节点/边划分，共享消息传递图排除评估边，LP 使用固定负样本。在 GCN、GraphSAGE、GPS 上系统实验，发现迁移方向性强：NC→LP 在 homophilic 图上一致正向；LP→NC 脆弱，仅在 LP 容易而 NC 未饱和时（结构主导区间）成为可靠的结构预训练。引入 **CoTask Score (CTS)**，为共享编码器联合 NC+LP 性能提供单值度量。
**关键结果**：NC→LP 在 Citeseer、Cora 等 homophilic 图上平均提升 5-10%；LP→NC 在 naive 表示重用下可能造成精度下降，但在特定条件下（LP easy, NC unsaturated）能提供稳定的增益，且数据集统计量（同质性）可强力预测迁移方向与幅度。
