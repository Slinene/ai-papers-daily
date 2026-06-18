---
title: 'RankGraph-2: Lifecycle Co-Design for Billion-Node Graph Learning in Recommendation'
title_zh: RankGraph-2：十亿节点图学习生命周期协同设计
authors:
- Renzhi Wu
- Zikun Cui
- Junjie Yang
- Tai Guo
- Hong Li
- Xian Chen
- Li Yu
- Ke Pan
- Sri Reddy
- Mahesh Srinivasan
affiliations:
- Meta Platforms
arxiv_id: '2606.18379'
url: https://arxiv.org/abs/2606.18379
pdf_url: https://arxiv.org/pdf/2606.18379
published: '2026-06-16'
collected: '2026-06-18'
category: RecSys
direction: 图学习全生命周期协同优化
tags:
- graph learning
- co-design
- billion-node
- popularity bias correction
- cluster index
- U2U2I retrieval
one_liner: 通过图构建-训练-服务三阶段协同设计，在十亿规模图上实现高召回、低延迟检索，服务成本降低83%
practical_value: '- **用预计算PPR邻居替代在线图采样**：即便面向高阶相似性检索（U2U2I/U2I2I），离线PPR产生的邻居质量不低于在线随机游走，且省去图存储与分布式采样引擎。可直接在标准ML训练框架上训练GNN。

  - **联合训练残差量化索引替代在线KNN**：将向量检索转化为聚类查表（U2Cluster2I），服务成本降低83%。关键在于引入码本使用频率正则化与偏置码选择，避免连续训练下码本坍缩，这一技巧可直接移植到其他需要联合训练索引的场景。

  - **热度偏差校正与边子采样策略**：对I-I边按邻居流行度降权（α=0.3），再结合top-K边截断，可将百亿规模图压缩三个数量级同时保留长尾结构信号，对电商场景中的热门商品霸榜问题有直接借鉴。

  - **异构共现边统一构建**：仅从交互日志同时生成U-I、U-U、I-I三类边，无需引入社交或知识图谱，且U-U和I-I边的权重用共同重合边的对数归一化，可简单有效捕捉协同信号。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
在实际的十亿节点推荐系统中，图检索面临三个紧密耦合的问题：图构建、表示学习与实时服务。现有方案各自孤立优化，忽视了三者之间的级联需求：服务需低成本的聚类索引，训练需无在线图依赖的数据，构建需满足小时级刷新与高质量邻居。RankGraph-2 通过全生命周期协同设计，打破这一割裂，显著提升召回并降低服务成本。

### 方法关键点
- **图构建**：从交互日志生成U-I、U-U、I-I三类边；通过热度偏差校正（I-I边权重乘上邻居的归一化逆频率）和top-K边截断，将数百兆边压缩至数百亿；使用个性化PageRank（PPR）并行预计算每个节点的K个重要邻居，封装为自包含的边中心训练数据，无需在线图基础设施。
- **模型训练**：采用异构聚合器融合用户特征、用户邻居、物品邻居，无在线采样；负样本由批内、批间以及多头多视图增强组成；损失函数结合margin ranking loss与InfoNCE，并通过不确定性加权自动调整各边类型损失权重。
- **索引联合训练**：在训练中协同学习两层残差量化码本（5000×50簇），通过重构损失和对比损失联合优化；为防止码本坍缩，引入基于历史分布的码频率正则化项和偏置码选择，使冷门码有更多被选中的机会。
- **服务**：U2I2I通过离线预计算I2I KNN解决；U2U2I则利用学到的用户簇索引，实时维护各簇最近活跃用户的物品队列，检索时直接读取簇队列，彻底消除在线KNN。

### 关键实验结果
- 在Meta双平台10万用户评估中，召回@5是GAT+Deep Graph Infomax的3.8倍，是万亿参数序列模型HSTU的11倍；物品嵌入召回@100是PyTorch-BigGraph的2.1倍。
- 14天A/B测试，U2I2I检索带来最高+0.96% CTR和+2.75% CVR；U2U2I也有正向提升。
- 联合训练索引使服务计算成本降低83%，且点击率、转化率与在线KNN持平。
- 消融实验证实异构边、PPR邻居、热度校正各自显著贡献。
