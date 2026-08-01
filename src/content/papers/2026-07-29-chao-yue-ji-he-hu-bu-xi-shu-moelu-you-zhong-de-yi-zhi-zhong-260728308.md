---
title: 'Beyond Geometric Complementarity: Coherent Overlap in Sparse Mixture-of-Experts
  Routing'
title_zh: 超越几何互补：稀疏MoE路由中的一致重叠
authors:
- Huiyuan Tian
- Bonan Xu
- Shijian Li
affiliations:
- College of Computer Science and Technology, Zhejiang University
- Department of Aeronautical and Aviation Engineering, The Hong Kong Polytechnic University
arxiv_id: '2607.28308'
url: https://arxiv.org/abs/2607.28308
pdf_url: https://arxiv.org/pdf/2607.28308
published: '2026-07-29'
collected: '2026-08-01'
category: Training
direction: 稀疏MoE路由中的一致重叠与功能冗余分析
tags:
- Mixture-of-Experts
- Sparse Routing
- Expert Subspace
- Geometric Complementarity
- Functional Redundancy
one_liner: 发现MoE路由中专家子空间大量重叠，但多专家计算仍具功能增益，称“一致重叠”。
practical_value: '- 在推荐系统多专家路由模型中，不应仅凭专家表示空间的几何相似性进行剪枝或合并；需通过冻结路由或受控训练实验评估功能冗余，避免删除有用专家。

  - 路由上下文交互项为负，设计路由策略时可考虑该效应，适当保留多专家以弥补前缀信息带来的选择偏好缩小。

  - 进行专家负载均衡或容量分配时，可引入Expert Subspace Separation Index (ESSI) 等指标量化子空间分离度，结合下游任务表现综合决策。

  - 对Agent多智体系统中的路由，可从共享邻域选择相关专家，不必强制专家分化至互不相交，仍可获得多专家协同增益。'
score: 7
source: huggingface-daily
depth: abstract
---

## 动机
稀疏MoE语言模型为何从多专家路由获益？传统直觉假设共同选中的专家应贡献互补的表示方向（几何互补），但现有证据混淆了路由一致性、候选质量与上下文交互，难以判断功能冗余。

## 方法
提出Expert Subspace Separation Index (ESSI) 度量专家子空间重叠程度；设计前缀控制的2×2因子实验，分离候选质量与交互效应；通过冻结路由干预和受控Top-k训练，检验多专家计算的功能价值。在OLMoE、Mixtral、DeepSeek等六个MoE架构上进行系统对比。

## 关键结果
1. 六个架构中专家子空间存在大量重叠（ESSI值低），但实际路由对token表示的拟合能力显著优于随机匹配的替代路由。
2. 在39个因子单元中，每一单元内被选中专家对残差的解释始终强于最强未选专家，然而实际前缀一致地缩小了这一优势：所有交互项为负，且95%置信区间全部位于零以下。
3. 几何优势的缩小并不导致功能冗余：冻结路由实验中，添加后续专家在24/39例中显著提升下一token预测（剩余15例结论不明确）；受控训练实验在所有种子下Top-2均优于Top-1。

结论：路由在共享的几何邻域中选择token相关专家，形成“一致重叠”：有益的多专家计算不依赖于不相交的线性子空间覆盖，单纯几何相似性不足以作为专家冗余或剪枝依据。
