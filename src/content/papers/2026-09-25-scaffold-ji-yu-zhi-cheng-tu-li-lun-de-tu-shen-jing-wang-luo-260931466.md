---
title: 'Scaffold: Support Graph Theory Based Sparsification for Graph Neural Networks'
title_zh: Scaffold：基于支撑图理论的图神经网络稀疏化框架
authors:
- Siddhartha Shankar Das
- Sai Karthik Navuluru
- S M Ferdous
- Ryan A. Rossi
- Baris Coskunuzer
- Lakshman Tamil
- Edoardo Serra
- Alex Pothen
- Robert Rallo
- Mahantesh M Halappanavar
affiliations:
- Pacific Northwest National Laboratory
- University of Texas at Dallas
- University of North Carolina at Charlotte
- Adobe
- Boise State University
arxiv_id: '2609.31466'
url: https://arxiv.org/abs/2609.31466
pdf_url: https://arxiv.org/pdf/2609.31466
published: '2026-09-25'
collected: '2026-09-28'
category: Other
direction: 图神经网络稀疏化 · 支撑图理论
tags:
- GNN
- Graph Sparsification
- Support Graph Theory
- Dilation-Congestion
- Training Efficiency
- Open Source
one_liner: 用支撑图理论联合控制 dilation 与 congestion 的拓扑稀疏化方法，在 GNN 上大幅降存提速且保持性能
practical_value: '- 在大规模 user-item 二部图或商品知识图谱上训练 GNN 时，可将 Scaffold 作为预处理边稀疏化步骤，替代随机采样或度中心性采样，在
  10%-50% 边保留率下接近全图性能，显存占用减半以上，适合电商推荐中的大规模图训练。

  - dilation-congestion 联合约束可以直接借鉴到构建轻量图子图或缓存图结构：删边时评估替代路径长度（dilation）和路径集中度（congestion），避免切断关键通信路径，对实时推荐或增量更新子图有工程价值。

  - 方法在异配图（heterophilic）上同样有效，可用于处理社交关系、用户共现等噪声连接较多的场景，提升 GNN 抗噪能力。

  - 已开源实现，作为独立预处理模块可快速接入 PyG/DGL 训练流程，端到端训练时间（含稀疏化开销）仍低于全图训练，适合线上迭代。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：GNN 的消息传递计算和内存成本与图边数强相关，随机删边会破坏重要通信结构、降低预测性能。需要一种拓扑感知的稀疏化方法，在降本的同时保持 GNN 表达能力。

**方法关键点**：基于支撑图理论 preconditioners，提出 Scaffold 框架。核心是联合控制两个互补结构量：dilation（被删边产生的绕行路径长度）和 congestion（绕行路径在保留支撑边上的集中程度）。通过同时约束二者，保留短通信路径、避免结构瓶颈，从而在不监督的情况下生成高质量稀疏支撑图。

**关键结果**：在 19 个同配与异配基准（从小图到大图）上，Scaffold 取得最佳聚合排名；仅使用原始边的 10%-50% 即可恢复或接近全图 GNN 性能，训练内存不到全图的一半，且端到端训练时间（含稀疏化开销）显著降低。开源代码已发布。
