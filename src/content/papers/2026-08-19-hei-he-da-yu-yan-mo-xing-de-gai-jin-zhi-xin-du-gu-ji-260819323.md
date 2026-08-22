---
title: Improved Confidence Estimates for Black-Box Large Language Models
title_zh: 黑盒大语言模型的改进置信度估计
authors:
- Sokhna Diarra Mbacke
- Mouloud Belbahri
- Gabriel Loaiza-Ganem
affiliations:
- Layer 6 AI
- TD Insurance
arxiv_id: '2608.19323'
url: https://arxiv.org/abs/2608.19323
pdf_url: https://arxiv.org/pdf/2608.19323
published: '2026-08-19'
collected: '2026-08-22'
category: LLM
direction: LLM 不确定性量化与部署安全
tags:
- uncertainty quantification
- confidence estimation
- black-box LLM
- abstention
- lightweight classifier
one_liner: 利用评估数据集训练简单分类器，以现有 UQ 分数和相似查询正确性为特征，提升黑盒 LLM 置信度估计。
practical_value: '- 在电商搜索/推荐的 LLM 应用（如 query 改写、商品卖点生成、客服自动回复）中，可在部署前利用积累的标注反馈数据（正确/错误）训练一个轻量置信度分类器，将现有
  UQ 分数（如 verbalized confidence、语义熵）作为输入特征，低成本实现自动审核与风险拦截。

  - 相似查询的正确性作为特征，可通过 kNN 在已有标注数据中快速检索得到，适合线上实时服务；不依赖模型内部 logits 或白盒访问，可直接用于 OpenAI、Claude
  等黑盒 API。

  - 结论：不要只依赖单一零样本 UQ 分数，利用少量标注数据做特征融合能稳定提升置信度区分能力，适合作为 Agent 系统中 LLM 输出的 guardrail。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

## 动机
LLM 幻觉使其在高风险场景部署受限，不确定性量化（UQ）是保障安全的关键。现有方法多为零样本启发式分数（如 verbalized confidence、多次生成一致性），无需标注数据，但实际部署前通常会有评估数据集可供使用。

## 方法关键点
- 不假设白盒访问，仅利用已有标注评估数据集。
- 构建简单分类器，预测 LLM 响应的正确性。
- 特征包含两部分：现有 UQ 分数（如置信度、熵等）以及相似查询的正确性（通过近邻检索获得）。
- 计算开销极小，可作为现有 UQ 方法的轻量增强。

## 关键结果
在多个基准数据集上一致优于现有零样本 UQ 分数；无需额外生成或模型改动，仅增加少量特征计算，适合真实应用中的快速部署。
