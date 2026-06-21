---
title: A Solver-Free Training Method for Predict-then-Optimize
title_zh: 无求解器训练的预测后优化方法
authors:
- Beichen Wan
- Mo Liu
affiliations:
- Department of Statistics and Operations Research, University of North Carolina at
  Chapel Hill
arxiv_id: '2606.19587'
url: https://arxiv.org/abs/2606.19587
pdf_url: https://arxiv.org/pdf/2606.19587
published: '2026-06-17'
collected: '2026-06-21'
category: Other
direction: 预测后优化 · 决策导向学习
tags:
- Decision-focused learning
- Predict-then-Optimize
- Linear Programming
- Surrogate Loss
- Solver-Free
one_liner: 提出无需求解器的代理损失训练预测模型，用于线性优化决策，在保持决策质量的同时大幅减少训练时间。
practical_value: '- 若推荐/广告系统中存在预测模块驱动下游优化（如动态定价、预算分配、库存分配），可借鉴该无求解器训练方式，避免每个梯度步调用优化求解器，实现高效迭代。

  - 代理损失基于测度变换构建，具有Fisher一致性理论保证，可提供可靠的训练信号，不必担心近似引入偏差。

  - 方法适用于线性目标优化，且允许决策区域为一般紧集（包括离散组合），可尝试迁移至广告组合优化、多目标物料分配等场景。

  - 实验显示训练时间可减少两个数量级以上，对于需要频繁训练预测模型的生产系统有显著工程价值。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**：在预测后优化（predict-then-optimize）范式中，预测模型输出作为线性规划的目标系数，但直接最小化决策悔恨时，由于决策映射分段常数导致梯度几乎处处为零，难以训练。现有方法通过平滑求解器输出获取梯度，但每个梯度计算都需调用一次优化求解器，计算开销巨大，无法扩展。

**方法**：提出一种基于测度变换（measure transformation）的决策导向学习管线。核心思想是将原始悔恨最小化问题转化为一个完全不需要求解器的新代理损失。该代理损失在训练过程中完全避免优化求解器的调用，且具有理论保证：Fisher 一致性和超额风险界。

**结果**：在多个预测后优化任务（包括线性规划、组合优化）上，新方法的最终决策质量与现有基于求解器平滑的 SOTA 方法相当，但训练时间减少了两个数量级以上，实现了显著的可扩展性提升。
