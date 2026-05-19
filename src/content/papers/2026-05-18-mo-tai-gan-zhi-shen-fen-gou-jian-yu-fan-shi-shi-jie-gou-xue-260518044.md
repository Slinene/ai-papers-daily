---
title: Modality-Aware Identity Construction and Counterfactual Structure Learning
  for ID-Free Multimodal Recommendation
title_zh: 模态感知身份构建与反事实结构学习实现无ID多模态推荐
authors:
- Hongjian Ma
- Wenxin Huang
- Yan Zhang
- Zhifei Li
- Zheng Wang
affiliations:
- Hubei University
- Wuhan University
arxiv_id: '2605.18044'
url: https://arxiv.org/abs/2605.18044
pdf_url: https://arxiv.org/pdf/2605.18044
published: '2026-05-18'
collected: '2026-05-19'
category: RecSys
direction: 生成式推荐 · ID-Free 多模态 · 反事实学习
tags:
- ID-Free
- Multimodal
- Counterfactual
- Graph Learning
- Popularity Bias
- Modality-Aware PE
one_liner: 通过动态模态感知位置编码和反事实图结构学习，大幅提升无ID多模态推荐的语义表达和长尾覆盖
practical_value: '- **模态感知位置编码（MAIC）**：用文本和视觉语义生成门控，动态调制位置编码，使ID-free表征具备内容感知性。可直接用于生成式推荐的身份构建，用商品图文特征调整区分信号，增强冷启动物品泛化。

  - **反事实图增强（CSL）**：通过流行度惩罚选取低曝光但语义相似的邻居，构建反事实图，缓解流行偏差。适合电商长尾商品发现，可嵌入现有GNN推荐管线，改善推荐多样性和公平性。

  - **自监督结构对比**：跨层对齐和去耦判别损失稳定低曝光语义结构在多层传播中的保留。该trick可迁移到任何图学习推荐模型，增强结构鲁棒性。

  - **多模态融合权重调优**：不同品类（如服装vs宠物）文本/视觉门控融合比例需单独优化，提示工程落地时宜按业务场景自适应调整多模态贡献。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
现有无ID多模态推荐用静态位置编码重构身份，导致表征与多模态语义对齐弱，且图学习受流行度偏差主导，长尾语义邻居挖掘不足，限制了推荐质量和公平性。

**方法关键点**
- **模态感知身份构建（MAIC）**：从文本和视觉特征生成门控，动态调制位置编码，得到内容感知的节点初始表征。
- **反事实邻居增强（CNA）**：在物品语义相似度中引入流行度惩罚，选取低曝光高语义相似邻居，融合到基础KNN图，缓解流行邻居主导的传播偏置。
- **结构对比增强（SCE）**：跨层对齐损失（身份表征与传播后表征对齐）和去耦判别损失（拉近初始表征与原始多模态，推远融合后公共结构表征），强化反事实结构稳定性。
- **推荐损失**：采用Softmax ranking loss，并保留跨模态InfoNCE对齐。

**关键结果**
在Amazon Baby、Sports、Clothing、Pet、Beauty五个数据集上，对比16个基线，MAIL的Recall@10平均提升7.81%，NDCG@10提升12.81%；较最强ID-free基线IDFREE，Recall@10分别提升13.78%、4.52%、5.03%、7.16%、8.56%。可视化表明身份表征与语义锚更强对齐，反事实图让长尾邻居比例从38.1%升至71.7%，平均邻居流行度从2.25降至1.69。各模块消融均带来显著增益，MAIC可即插即用提升其他模型。

**最值得记住**：动态模态感知位置编码与反事实流行度惩罚的组合，让ID-free推荐摆脱静态身份信号束缚，同时有效对抗流行偏差，是提升长尾覆盖和语义表达的实用方案。
