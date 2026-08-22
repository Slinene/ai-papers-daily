---
title: 'DICS: Data-Informed Centroid Splitting for Decision Tree Classifiers'
title_zh: DICS：面向决策树分类器的数据驱动质心分裂方法
authors:
- MD Saifur Rahman Mazumder
- Feng Yu
affiliations:
- Department of Mathematical Sciences, University of Texas at El Paso
arxiv_id: '2608.20258'
url: https://arxiv.org/abs/2608.20258
pdf_url: https://arxiv.org/pdf/2608.20258
published: '2026-08-20'
collected: '2026-08-22'
category: Training
direction: 决策树分裂搜索加速 · 训练效率优化
tags:
- decision tree
- split search
- clustering
- training efficiency
- classification
- GBDT
one_liner: 用聚类构建类感知的紧凑候选分裂集，大幅缩小分裂搜索空间，加速决策树训练且精度不降
practical_value: '- 在电商/广告排序常用的 GBDT（LightGBM/XGBoost）训练中，可借鉴 DICS 思路：对高基数数值或类别特征先做聚类，用聚类质心作为候选分裂点，替代逐值扫描或直方图分桶的固定候选，有潜力进一步降低分裂增益计算量。

  - 类感知的质心分裂能保留判别信息，适合处理类别不平衡或特征与标签强相关的场景，例如 CTR 预估中的用户行为计数特征、商品价格等连续特征。

  - 该方法可作为特征预处理步骤集成到现有树模型训练框架中，对训练数据采样聚类得到候选分裂集，再交给树模型搜索，工程实现上只需增加一次聚类开销，换来后续所有节点分裂搜索空间减小。

  - 注意 DICS 的理论保证依赖假设，实际落地时需在小规模数据上验证精度损失；若精度敏感，可结合已有直方图方法做混合候选集。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：决策树及集成模型（RF、GBDT）训练的主要瓶颈在于每个节点对候选分裂点的穷举搜索，数据量大、特征维度高时计算成本显著。

**方法关键点**：提出 Data-Informed Centroid Splitting（DICS），利用聚类技术构建紧凑且信息量高的候选分裂集。具体引入数据驱动先验和类感知结构，将候选分裂点由全量取值缩减为聚类质心，从而大幅减少每个节点的分裂搜索空间。DICS 可无缝嵌入分类决策树、随机森林和梯度提升模型。理论分析表明，在给定假设下，DICS 相比穷举分裂搜索不会降低分类性能。

**关键结果**：在合成数据集和多个基准数据集上的实验显示，DICS 在保持与穷举搜索相当的分类准确率的同时，显著缩短了训练时间，验证了将数据驱动先验引入分裂选择对可扩展决策树学习的有效性。
