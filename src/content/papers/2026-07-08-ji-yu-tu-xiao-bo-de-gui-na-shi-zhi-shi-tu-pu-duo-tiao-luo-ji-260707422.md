---
title: 'InductWave: Inductive Multi-Hop Logical Query Answering on Knowledge Graphs'
title_zh: 基于图小波的归纳式知识图谱多跳逻辑查询回答
authors:
- Mayank Kharbanda
- Michael Cochez
- Rajiv Ratn Shah
- Raghava Mutharaju
arxiv_id: '2607.07422'
url: https://arxiv.org/abs/2607.07422
pdf_url: https://arxiv.org/pdf/2607.07422
published: '2026-07-08'
collected: '2026-07-11'
category: Other
direction: 归纳式多跳逻辑查询 · 图小波嵌入
tags:
- Knowledge Graphs
- Logical Query Answering
- Inductive Reasoning
- Graph Wavelets
- Multi-Hop Query
- EFO Queries
one_liner: 用图小波变换的归纳式嵌入，以更少消息传递层数实现大规模知识图谱上的多跳逻辑查询回答性能超越现有方法
practical_value: '- 电商场景中的结构化条件查询（如“价格低于X、品牌Y、带属性Z”）可视为多跳逻辑查询，InductWave 提供的归纳式嵌入能直接支持不断涌现的新品实体，无需重新训练。

  - 小波变换代替多层消息传递，大幅降低计算开销，适合大规模商品知识图谱上的实时复杂查询，工程实现上可借鉴其轻量级图卷积设计。

  - 归纳推理能力使模型在训练图仅覆盖部分节点时仍能泛化到全图，这对增量更新的商品库和用户动态标签场景很有价值。

  - 文中不同训练/测试比例消融实验的设定，可直接迁移为推荐系统中冷启动实体比例下的评测方案。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有知识图谱多跳逻辑查询回答方法多为转导式推理，无法处理训练时未见过的实体，而现实大规模图谱资源有限，无法训练所有节点。因此需要一种归纳式方法，能在训练图节点少于测试图时依然有效回答包括合取、析取、取反的EFO逻辑查询。

**方法**：提出 InductWave，基于图小波变换的归纳式嵌入方法。用可学习的稀疏小波基替代传统图卷积层，将实体嵌入投影到小波域进行消息传递，使得在显著减少层数的同时保持感受野。训练时仅使用部分节点构成的子图，推理时可泛化到全图甚至全新实体。该方法参数效率高，轻量且可扩展。

**关键结果**：在 FB15k-237 数据集上，按不同训练/测试节点比例设置，InductWave 仅需基线模型一半的层数即可达到相当性能；当使用基线75%的层数时，在多数查询类型上超越所有对比方法。还成功扩展至百万级节点的 Wiki-KG 图。
