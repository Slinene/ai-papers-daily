---
title: 'MOON: Multi-Objective OrthoNormalized Updates for Multitask Learning'
title_zh: MOON：多目标正交归一化更新用于多任务学习
authors:
- Shiji Zhou
- Kunlin Lyu
- Lei Zhang
- Ruodong Wang
- Yifan Sun
affiliations:
- Institute of Artificial Intelligence, Beihang University
- Beijing Advanced Innovation Center for Future Blockchain and Privacy Computing,
  Beihang University
- Beijing Academy of Artificial Intelligence (BAAI)
- Center for Applied Statistics, School of Statistics, Renmin University of China
arxiv_id: '2608.11749'
url: https://arxiv.org/abs/2608.11749
pdf_url: https://arxiv.org/pdf/2608.11749
published: '2026-08-12'
collected: '2026-08-13'
category: Training
direction: 多任务学习优化 · 矩阵几何梯度操纵
tags:
- Multitask Learning
- Multi-Objective Optimization
- Gradient Manipulation
- Matrix Geometry
- Orthonormal Updates
one_liner: 在矩阵几何下做多目标梯度操纵，用谱-核范数几何与正交归一更新提升多任务优化效率
practical_value: '- 多任务推荐/广告模型里任务冲突常见，现有梯度操纵方法（MGDA、PCGrad、FAMO）都把参数展平成向量，在欧氏空间操作，忽略了
  Transformer 权重矩阵的几何结构。改用矩阵几何下的谱-核范数梯度方向和正交归一更新，可直接替换现有 MTL 优化器，特别适合含 Embedding 矩阵、Attention
  权重矩阵的模型。

  - 工程实现上：对每个任务梯度矩阵做 SVD 或谱范数归一化，再合并成正交归一方向，计算开销可控；可先对共享底层参数应用，避免全模型展开。

  - 若业务中使用多目标融合（如 CTR、CVR、GMV、时长），可尝试在共享底层或 MoE 专家层用该更新规则，替代简单梯度加权，可能改善任务间冲突和收敛速度。

  - 注意论文主要验证在通用多任务学习基准，直接迁移到大规模推荐系统需先做离线小规模对比实验，确认收益与额外计算成本。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

动机：多任务学习中不同任务梯度冲突，主流多目标优化（MOO）方法通过梯度操纵缓解冲突，但大多先把模型参数展平成向量，在欧氏几何下操作，忽略了 Transformer 等架构中权重矩阵的结构。欧氏空间中的梯度操纵方向未必是矩阵几何下的最速下降方向，可能限制优化效率。

方法关键点：借鉴矩阵值参数最速下降理论，提出在谱-核范数几何下进行梯度操纵，并对操纵后的梯度做正交归一化，得到 MOON 更新。该方法保留矩阵结构，按矩阵几何选择下降方向，用于多任务参数更新。

关键结果：对光滑非凸多目标，确定性设置下平均 Pareto 平稳性度量的收敛速率为 O(T^{-1/2})，随机梯度下为 O(T^{-1/4})。在多个多任务基准上，MOON 相较于基线持续提升优化效率和最终多任务表现。
