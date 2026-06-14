---
title: 'Dense Supervision, Sparse Updates: On the Sparsity and Geometry of On-Policy
  Distillation'
title_zh: 密集监督，稀疏更新：策略蒸馏的稀疏性与几何性质
authors:
- Guo Yu
- Wenlin Liu
- Yulan Hu
- Hao-Xuan Ma
- Jun-Peng Jiang
- Han-Jia Ye
affiliations:
- School of Artificial Intelligence, Nanjing University
- National Key Laboratory for Novel Software Technology, Nanjing University
- Amap, Alibaba Group
arxiv_id: '2606.13657'
url: https://arxiv.org/abs/2606.13657
pdf_url: https://arxiv.org/pdf/2606.13657
published: '2026-06-11'
collected: '2026-06-14'
category: Training
direction: 后训练on-policy蒸馏的参数分析
tags:
- knowledge distillation
- on-policy
- sparsity
- parameter analysis
- post-training
one_liner: 发现on-policy蒸馏的更新是坐标稀疏且FFN为主的，训练子网络可恢复性能，并揭示了更新的几何特性。
practical_value: '- OPD更新具有坐标稀疏性，可固定大部分参数仅更新重要子网络，显著降低微调计算开销，适合大规模推荐模型的高效部署与迭代。

  - 发现AdamW优于SGD，因自适应学习率能处理密集监督带来的异构梯度尺度，推荐在蒸馏或微调任务中优先选用AdamW。

  - 几何分析表明更新远离主奇异子空间且集中于小权重坐标，提示可基于权重大小设计结构化稀疏微调策略，减少对主特征方向的干扰。

  - 在学生生成轨迹上使用密集监督但生成稀疏更新，为推荐模型中online知识迁移提供了新范式：保持监督密度但约束参数变化量，有助于稳定多任务对齐。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：on-policy distillation (OPD) 已成为大模型后训练的主流方法，它结合了学生在线生成轨迹和教师密集监督，但其参数变化特性尚未明确。本文旨在系统分析OPD引起的权重更新在稀疏性和几何上的规律，以指导高效微调策略。

**方法**：在多种语言与视觉-语言模型对上，对比OPD、离策略蒸馏和监督微调的参数更新，统计更新的坐标稀疏度、层分布、FFN/Attention模块比例；通过奇异值分解分析更新的谱特性和与源权重的主子空间关系；并检验优化器（AdamW vs SGD）的影响。

**关键结果**：1) OPD更新量级小且具备高坐标稀疏度，更新主要分布在FFN模块，跨层分散；训练时仅保留发现的重要子网络（稀疏掩码），可恢复接近全量OPD的性能。2) 尽管更新稀疏，SGD性能显著低于AdamW，因密集监督保留了各坐标梯度的异质尺度，自适应学习率更有效。3) 几何上，更新矩阵数值全秩但谱能量集中，更新方向主要偏离源权重的左、右主奇异向量空间，且更新幅度与初始权重值呈负相关，即权重越小的坐标更新越多。这些发现说明OPD并非简单的密集参数重写，而是保留了on-policy训练的特定几何印记，为设计高效微调策略提供了依据。
