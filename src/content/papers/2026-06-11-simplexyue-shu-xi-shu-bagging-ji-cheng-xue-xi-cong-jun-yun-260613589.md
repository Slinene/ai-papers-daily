---
title: 'Simplex-Constrained Sparse Bagging: Transitioning from Uniform Priors to Sparse
  Posteriors in Ensemble Learning'
title_zh: Simplex约束稀疏Bagging：集成学习从均匀先验到稀疏后验
authors:
- Meher Sai Preetam
- Meher Bhaskar
affiliations:
- Georgia Institute of Technology
arxiv_id: '2606.13589'
url: https://arxiv.org/abs/2606.13589
pdf_url: https://arxiv.org/pdf/2606.13589
published: '2026-06-11'
collected: '2026-06-14'
category: Other
direction: 集成学习压缩与概率校准
tags:
- ensemble pruning
- bagging
- probability calibration
- model compression
- simplex constraint
- concave regularization
one_liner: 提出Simplex约束稀疏Bagging，通过凹二次惩罚在单纯形上实现集成剪枝与校准，压缩率达96%
practical_value: '- 在推荐模型集成（如多模型融合）中，可直接使用SCSB对基模型权重进行稀疏化，仅保留最有价值的子集，显著降低线上推理延迟，特别适合实时推荐场景。

  - 面向CTR预估等需要概率输出的任务，利用OOB损失优化权重能提升概率校准，降低期望校准误差，避免过自信预测，改善模型可信度和拍卖阶竞价效率。

  - 方法模型无关，轻量级后处理，可快速集成到现有Bagging管道（如随机森林或Bagged NN）而不改动原始训练流程，方便在已有系统中试水。

  - 避开L1在单纯形上失效的坑，通过凹二次惩罚产生真正稀疏解，验证了稀疏正则项与约束空间关系的工程陷阱，对设计其他概率约束稀疏化方案有参考价值。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：标准Bagging（如随机森林、Bagged NN）给每个基学习器分配均匀投票权重，既忽视各模型在不同区域的局部能力差异，又导致集成输出过度自信、校准差，同时大集成计算成本高昂。需要一种后处理压缩方法，既稀疏化集成、加速推理，又能校准概率。

**方法**：将集成剪枝与概率校准建模为概率单纯形上的联合优化问题，通过最小化Out-Of-Bag（OOB）损失学习稀疏权重。解决经典L1惩罚在单纯形上恒为常数而失效的“L1-单纯形悖论”，引入凹二次惩罚项诱导稀疏结构。SCSB不依赖基模型内部细节，适用于任何Bagging集成。

**关键结果**：在多种数据集和基模型上实现最高96%的集成压缩，推理速度线性提升；与均匀加权和L1方法相比，期望校准误差（ECE）显著降低，同时分类准确率保持或略有提高。
