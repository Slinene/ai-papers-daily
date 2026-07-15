---
title: 'Beyond Semantic IDs: Encoding Business-Value Ranking into Document Identifiers
  for Generative Retrieval'
title_zh: 超越语义ID：将业务价值排序编码入文档标识的生成式检索
authors:
- Gui Ling
- Zhihong Chen
- Yu Li
- Tong Xiong
- Kunhai Lin
- Kaixuan Zhang
- Yuliang Yan
- Dan Ou
- Haihong Tang
- Bo Zheng
affiliations:
- Alibaba
arxiv_id: '2607.11392'
url: https://arxiv.org/abs/2607.11392
pdf_url: https://arxiv.org/pdf/2607.11392
published: '2026-07-13'
collected: '2026-07-15'
category: GenRec
direction: 生成式检索 · 业务价值排序
tags:
- Generative Retrieval
- Document Identifier
- Business-value Ranking
- Semantic Clustering
- Collision-free
- E-commerce Search
one_liner: 提出 CRID，将DocID解耦为语义聚类与业务价值序数排名，实现无冲突、可增量更新的生成式检索，线上GMV提升1.06%
practical_value: '- **DocID设计巧思**：将业务价值（转化率等）作为序数排名编码到最后一层codebook，简单替换即可获得比OPQ、Sinkhorn等复杂量化方法更大的Hitrate提升，天然无冲突且支持增量更新。

  - **增量更新策略**：新物品仅需分配到最近的语义簇，每日根据最新业务统计重排簇内排名，无需重训codebook，对线上时效性友好。

  - **分析框架复用**：通过prefix N-gram匹配度和业务排名分组，可把生成式检索的召回增益拆解为「个性化偏好泛化」与「统计先验泛化」两个维度，进而指导语义簇大小的选取，平衡top-K与deep-K表现。

  - **动态beam校准**：多级codebook解码时，不同解码阶段的概率分布差异大，可按累积概率截止点分别设定beam size，在保持Hitrate覆盖的同时节省推理开销。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**

生成式检索（GR）将搜索建模为自回归生成DocID，DocID的设计是核心瓶颈。主流方案（如RQ-KMeans）仅基于语义嵌入量化，存在两个问题：一、多物品可能分配同一标识产生冲突；二、编码目标（语义重建）与系统优化目标（业务转化）错配。在淘宝这类大规模电商搜索中，语义相似的物品转化率可能相差极大，但纯语义ID无法区分，导致信息效率低下。

**方法关键点**
- **CRID结构**：DocID解耦为「语义聚类前缀」+「业务价值排名」。前两层用RQ-KMeans进行语义聚类；最后一层用业务价值（如30天转化数）在簇内做序数排名，每个排名唯一对应一个物品，天然无冲突。
- **增量更新**：新物品按嵌入距离归入最近语义簇，每日根据最新业务统计重排簇内排名，无需重训codebook。
- **分析框架**：按「prefix N-gram匹配度」和「业务排名分组」将检索增益分解为个性化偏好泛化（利用用户行为序列）和统计先验泛化（利用全局转化率），并定量分析语义簇大小如何通过改变分组构成影响总Hitrate。

**关键实验**
- **数据集**：淘宝搜索300M商品池，100M query-item对训练。
- **Baseline**：RQ-KMeans、OPQ、Sinkhorn-Knopp平衡、Tiger、FORGE等DocID方案。
- **离线结果**：CRID相比最强baseline，在查中转化HR@20提升3.72pp，HR@1000提升9.10pp；相比最强个性化EBR，HR@20提升13.26%。
- **在线A/B**：全量30天，GMV +1.06%，IPV +0.18%，订单量 +0.54%。

**一句话结论**：在DocID中把业务价值编为序数排名，比复杂的离散量化更有效，且将检索收益清晰解释为个性化与先验两个可分解部分的贡献。
