---
title: Federated Imputation under Heterogeneous Feature Spaces
title_zh: 异构特征空间下的联邦缺失值填补
authors:
- Imane Hocine
- Chaimaa Medjadji
- Sylvain Kubler
- Gregoire Danoy
- Yves Le Traon
affiliations:
- University of Luxembourg
arxiv_id: '2605.16099'
url: https://arxiv.org/abs/2605.16099
pdf_url: https://arxiv.org/pdf/2605.16099
published: '2026-05-15'
collected: '2026-05-18'
category: Training
direction: 联邦缺失值填补 · 特征图消息传递
tags:
- Federated Learning
- Heterogeneous Features
- Data Imputation
- Graph Neural Networks
- Message Passing
- Privacy-Preserving
one_liner: 利用全局特征图的消息传递，在联邦学习中实现异构特征空间的间接跨客户端知识迁移与缺失值填补
practical_value: '- **电商多源数据填补**：当不同业务线（如搜索、推荐、广告）或不同客户端（如不同地区的用户画像）特征空间不重叠时，可借鉴该方法的特征关联图建模，通过消息传递间接填补缺失特征，提升用户/商品特征完整性。

  - **联邦推荐特征对齐**：在跨部门联合建模场景下，无需共享原始数据，利用全局特征图即可发现特征间的统计关系，指导本地模型的填补与更新，解决特征异构问题。

  - **特征图构建启发**：采用互信息或相关性构建全局特征图，作为联邦通信中的共享知识，可迁移到其他需要特征补全的分布式任务（如 Agent 环境感知或冷启动特征推断）。

  - **工程实现参考**：联邦架构仅交换特征图结构和少量消息，通信开销低，适合生产环境中隐私受限的多方数据协作。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：联邦学习通常假设客户端特征空间一致，但现实表格数据中不同客户端常仅有部分重叠特征，这种结构性特征不可用导致传统参数平均（如 FedAvg）无法有效传递跨客户端信息，联邦缺失值填补效果差。

**方法**：提出 FedHF-Impute，将结构性特征缺失与常规缺失值区分开，构建一个共享的全局特征图（基于特征间互信息或相关性），通过图神经网络的消息传递机制在特征维度上传播信息。本地客户端利用该图对本地观测到的特征进行编码，并通过消息传递间接恢复未观测特征的信息，实现跨客户端知识迁移，即使两个特征从未被同一客户端联合观测到。联邦通信仅需同步特征图与少量图网络参数，保留了标准 FL 通信范式。

**结果**：在 SECOM 和 AirQuality 数据集上模拟部分特征重叠，填补 RMSE 较 FL 基线分别降低 26.9% 和 8.4%；在 PhysioNET 上与最佳基线仅差 0.3%，性能相当。
