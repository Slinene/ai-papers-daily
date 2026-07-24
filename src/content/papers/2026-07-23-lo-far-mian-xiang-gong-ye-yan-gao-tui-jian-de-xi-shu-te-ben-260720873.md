---
title: 'LO-FAR: A Cost-Aware Local Filter for Sparse Feature Ranking in Industrial
  Ad Recommendation'
title_zh: LO-FAR：面向工业广告推荐的稀疏特征成本感知局部过滤
authors:
- Egemen Erbayat
- Luis Duque
- Sohini Roychowdhury
- Mohammad Amin
- Srihari Reddy
affiliations:
- Meta Platforms, Inc.
arxiv_id: '2607.20873'
url: https://arxiv.org/abs/2607.20873
pdf_url: https://arxiv.org/pdf/2607.20873
published: '2026-07-23'
collected: '2026-07-24'
category: RecSys
direction: 稀疏特征选择 · 工业广告推荐
tags:
- Sparse Feature Ranking
- Feature Selection
- CTR Prediction
- Industrial Recommendation
- Embedding Tables
- Cost-Aware
one_liner: 仅用CPU的局部过滤方法独立评估稀疏特征预测信号，实现低成本快速排序并保持下游CTR/CVR竞争力
practical_value: '- **低成本快速特征筛选流水线**：仅用 CPU 即可在 2 小时内完成数百个稀疏特征的排序，适合嵌入到日常迭代中，避免与训练抢
  GPU 资源。

  - **独立并行化设计**：每个特征独立打分、易于并行，适合拥有大量稀疏特征池的电商/广告团队快速收敛候选特征集。

  - **两阶段筛选策略**：可先用 LO-FAR 快速剔除大量低信号特征，再对保留的特征用更昂贵的交互感知方法（如 BSN）做精细选择，兼顾成本与效果。

  - **直接控制存储与参数规模**：通过特征预算直接决定嵌入表数量，实现 40%~75% 的稀疏存储压缩，降低训练和推理的内存压力。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
工业广告推荐模型中，稀疏 ID 列表特征（如用户历史、页面元素）占模型参数量的 97% 以上，是存储、训练和推理成本的主要来源。特征选择需要反复进行，但传统方法（置换重要性、随机门控）依赖 GPU 重训练，成本高、周期长，无法满足高频迭代需求。需要一种低成本、可快速重跑的特征排序方法。

## 方法关键点
- **流程**：采样 → 训练/测试切分 → 特征展开（将每个 ID 拆成单独一行） → 局部估计器（ID 级） → 聚合回样本级 → 按 log loss 排序。
- **局部估计器**：对高频 ID 直接计算经验正率；对低频 ID 使用 K 近邻回退，基于频率加权 token 距离。
- **设计亮点**：完全解耦下游模型，特征独立评估，CPU 并行，总复杂度 O(p·n·ℓ·log(nℓ))，支持大规模特征池。
- **明确范围**：定位为第一阶段过滤，不能替代交互感知方法；适用于短 ID 列表特征。

## 关键实验
- **数据集**：100 万+ 日志交互，475 个短稀疏 ID 列表特征，CTR 与 CVR 任务。
- **对比基线**：覆盖率启发式、置换重要性、BSN。
- **结果**：在 100~400 特征预算下，LO-FAR 的 Normalized Entropy 增益与 BSN、置换重要性相当，但排序仅需约 2 CPU 小时，后两者需多 GPU 天；实现 40%~75% 的稀疏存储压缩。
- **核心发现**：在工业场景中，低成本局部过滤可以在不牺牲下游质量的前提下，大幅降低特征管理成本。
