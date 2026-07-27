---
title: 'Bringing GRACE to Recommendation: Fine-Tuning for Sustainable and Accurate
  Personalization'
title_zh: GRACE：通过可微绿色损失与梯度投影的可持续推荐微调框架
authors:
- Yibowen Zhao
- Yinan Zhang
- Ning Liu
- Lizhen Cui
- Chunyan Miao
affiliations:
- 山东大学
- 南洋理工大学
- 阿里巴巴-南洋理工大学全球电子可持续实验室 (ANGEL)
arxiv_id: '2607.22341'
url: https://arxiv.org/abs/2607.22341
pdf_url: https://arxiv.org/pdf/2607.22341
published: '2026-07-24'
collected: '2026-07-27'
category: RecSys
direction: 可持续推荐 · 微调优化
tags:
- Green Recommendation
- Fine-Tuning
- Differentiable Ranking
- Gradient Projection
- Multi-Objective Optimization
one_liner: 提出 GRACE，用 Gumbel-softmax 可微排序近似与梯度投影在预训练模型上微调，不增推理开销地提升推荐可持续性
practical_value: '- **可微列表级目标**：通过 Gumbel-softmax 构建软排列矩阵，直接优化 top-K 离散指标（如健康分、碳足迹），可迁移至电商中对商品质量分、品牌分、GMV
  等不可微指标的端到端优化，避免 pairwise 负采样不稳定问题。

  - **梯度投影缓解多目标冲突**：将辅助目标（绿色）梯度投影到主目标（CTR / 偏好）梯度的正交方向，再加回更新，可应用于搜索推荐中的任何辅助目标（多样性、新颖性、冷启动曝光等），在不显著损害主指标的前提下注入约束。

  - **无需重训与推理零开销**：仅在预训练模型上微调，不改推理管线，不增加额外排序步骤。适合线上已有大模型快速迭代，例如在 CTR 模型上注入业务绿色标签、内容质量标签等。

  - **外部离散标签的直接优化方案**：当存在商品级别的离散标注（如认证等级、营养等级）时，无需将其转化为 pairwise 偏好，直接用可微分数近似，梯度更稳定且可控。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：推荐系统可用于引导用户选择更健康、更环保的食品，但现有“绿色推荐”方法需从头训练（高成本）或推理时重排（增加延迟）。此外，可持续性标签多为不可微的离散值，难以直接梯度优化；且追求绿色可能损害个性化准确度，形成冲突。

**方法**：GRACE 是一个在预训练推荐模型上进行微调的框架，核心包括：
1. **可微绿色损失**：利用 Gumbel-softmax 扰动构建软排列矩阵，得到每个排名位置的可微命中/绿色分数，直接最大化 top-*N* 列表的可持续性分数，同时用可微 NDCG 保持准确性。
2. **梯度投影**：分别计算推荐梯度 *g*_rec 和绿色梯度 *g*_green，将 *g*_green 投影到 *g*_rec 的正交方向，再与 *g*_rec 合成最终更新方向，避免绿色目标干扰偏好学习。另引入投影比例 *α* 控制绿色信号强弱。
3. **无推理改动**：微调只调整模型参数，不改变推理流程，没有额外的排序开销。

**实验**：在 GreenRec 和 RecipeEmission 两个食品推荐数据集上，基于 SASRec、FDSA、FEARec、GRAPE 四个预训练模型，与 FHFRS、CFARS 等重排基线对比。SASRec 上 GRACE 将 Hit@15 提升 18.38%，EIS 降低 5.79%，NIS 提高 25.45%；FDSA 上 CO2 降低 13.83% 且精度持平。消融证实可微损失和梯度投影是关键。
