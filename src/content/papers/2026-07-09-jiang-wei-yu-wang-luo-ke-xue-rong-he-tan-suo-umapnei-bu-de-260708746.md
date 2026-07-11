---
title: 'Dimensionality Reduction Meets Network Science: Sensemaking on UMAP''s kNN
  Graph'
title_zh: 降维与网络科学融合：探索UMAP内部kNN图的分析潜力
authors:
- Duen Horng Chau
- Donghao Ren
- Fred Hohman
- Dominik Moritz
affiliations:
- Apple
arxiv_id: '2607.08746'
url: https://arxiv.org/abs/2607.08746
pdf_url: https://arxiv.org/pdf/2607.08746
published: '2026-07-09'
collected: '2026-07-11'
category: Other
direction: 降维图分析 · 内部图结构利用
tags:
- UMAP
- kNN graph
- PageRank
- k-core decomposition
- clustering coefficient
- sensemaking
one_liner: 用PageRank、k-core、聚类系数等图算法挖掘UMAP的kNN图，发现被2D投影掩盖的数据结构
practical_value: '- **典型样本发现**：在电商商品表征的kNN图上运行PageRank，可自动挑出“最标准”的商品图片用于训练或人工审核，也能发现边缘奇怪的异常商品（如错标、假货）。相比k-medoids，完全复用UMAP构建好的图，零额外计算。

  - **密集子类挖掘**：k-core分解用于商品嵌入图，能剥离长尾噪声，找出核心密集区域；在时尚数据集上成功拆出“包包”下的腰包、邮差包等微类，可迁移到商家类目自动细化或搜索词的分簇打标。

  - **高相似度商品去重**：聚类系数揭示某个商品近邻的连接紧密程度，直接定位高度同质化的商品群，用于同款检测、反低质铺货。

  - **嵌入质量诊断**：在迭代生成式推荐的语义ID或item嵌入时，不应只看2D散点图；应回溯UMAP的kNN图结构指标（k-core、聚类系数），评估原始空间是否已有塌缩或空洞，前置发现问题。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：通常UMAP只使用降维后的2D投影进行可视化分析，但其内部构建的kNN图保留了原始高维空间的流形结构，未被利用。2D投影会引入扭曲，导致类簇形状、相对距离失真。本工作挖掘该kNN图的潜力，用标准图算法提升数据理解。

方法：在UMAP的加权有向kNN图上，应用三种图分析：(1) PageRank——识别最具代表性的点（高得分）和异常点（低得分）；(2) k-core分解——揭示数据核心与外围结构，过滤出致密子集；(3) 局部聚类系数——探测高度相似点的紧密邻域。在MNIST和Fashion MNIST上，将这些分析结果与专门设计的k-medoids、HDBSCAN等方法进行定量和定性对比。

结果：PageRank找出的典型样本质地干净，比k-medoids更稳定且能同时给出异常样本；k-core分解从2D散点混杂区域中分离出语义连贯的子类（如从“包”中分离出腰包、邮差包）；聚类系数准确定位极度相似的局部簇。三种方法计算成本极低，可与专门方法互补，为数据探索提供新的解读视角。
