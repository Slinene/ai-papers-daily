---
title: 'ALRA: Adaptive Local Relational Alignment for Logit-Based Pre-training Distillation
  of Autoregressive Language Models'
title_zh: 自适应局部关系对齐：自回归语言模型预训练蒸馏的 logit 方法
authors:
- Quang Hoang Trung
- Quang Huu Hieu
- Nguyen Van Hoang Phuc
- Vo Nguyen Le Duy
affiliations:
- VJ Technologies
- AJ Technologies
- Vietnam National University
- University of Information Technology
arxiv_id: '2609.03355'
url: https://arxiv.org/abs/2609.03355
pdf_url: https://arxiv.org/pdf/2609.03355
published: '2026-09-03'
collected: '2026-09-06'
category: Training
direction: 知识蒸馏训练优化
tags:
- knowledge distillation
- autoregressive LM
- pre-training
- adaptive token selection
- pairwise relational alignment
one_liner: ALRA 结合学生提议与教师锚点，自适应局部对齐改进 logit 蒸馏，提升预训练学生模型零样本性能
practical_value: '- 在生成式推荐（如 Semantic ID、商品标题生成）的蒸馏中，可借鉴 ALRA 的候选 token 选择策略：让学生提出高概率
  token，同时将教师的 top1 token 作为锚点加入，避免只用教师或学生导致候选集偏差，尤其适合训练早期学生排序不准确的场景。

  - Adaptive Local Divergence 用单位系数替代教师质量系数，防止低概率但语义重要的 token 区域被忽略；这可以迁移到电商长尾商品或
  query 的蒸馏，保护稀有但相关的 token 信号不被全局分布淹没。

  - Student-Weighted Pairwise Relational Alignment 强调学生概率差小但教师偏好的 token 对，可用于校准推荐生成中
  top-k 的局部排序，提升生成结果的多样性与准确性。

  - 位置特定且 batch 自适应的 token 数量选择，减少了手工设定 top-k 的超参负担，适合在线学习或增量更新场景，能动态适应数据分布变化。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：自回归语言模型的 logit 蒸馏通常对齐全词表的下一 token 分布，忽略了可能 token 之间的相对偏好。现有局部方法要么只用教师候选（易漏掉学生认为可能的 token），要么只用学生候选（训练早期排序不可靠）。

**方法关键点**：提出 ALRA，在每个有效预测位置结合学生提议与教师指导。学生提出可能 token，教师最可能 token 作为锚点；根据教师在该候选集内的概率分布相对于当前 batch 的广度，自适应调整选择数量。Adaptive Local Divergence 保留质量匹配项，分别匹配选定区域与剩余区域的相对 token 分布，用单位系数替换教师质量系数，避免低概率区域被过度降权。Student-Weighted Pairwise Relational Alignment 强调学生概率差小的高概率 token 对，降低不可能或明显分离 token 对的权重。

**关键结果**：在 The Pile 上预训练，随机初始化 200M 和 500M 参数学生，九个 zero-shot benchmark 平均准确率分别为 36.62% 和 37.40%。比最强竞争蒸馏基线高 0.94 和 0.83 个百分点，比无蒸馏预训练高 2.31 和 2.91 个百分点。
