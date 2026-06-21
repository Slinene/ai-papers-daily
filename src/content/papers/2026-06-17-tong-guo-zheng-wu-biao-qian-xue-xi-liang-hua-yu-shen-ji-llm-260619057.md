---
title: Quantifying and Auditing LLM Evaluation via Positive--Unlabeled Learning
title_zh: 通过正无标签学习量化与审计 LLM 评估
authors:
- Zilong Zhang
- Yi-Ting Hung
- Lei Ding
- Chi-Kuang Yeh
affiliations:
- Georgia State University
- University of Manitoba
arxiv_id: '2606.19057'
url: https://arxiv.org/abs/2606.19057
pdf_url: https://arxiv.org/pdf/2606.19057
published: '2026-06-17'
collected: '2026-06-21'
category: Eval
direction: LLM评估校准与偏置校正
tags:
- Positive-Unlabeled Learning
- Optimal Transport
- LLM-as-a-Judge
- Bias Mitigation
- Human Alignment
one_liner: 将选择性人工监督下的 LLM 评估建模为正无标签学习，通过部分最优传输几何对齐纠正裁判偏差
practical_value: '- 当用 LLM 做推荐理由/对话质量等主观评估时，可利用少量人工“好”样本（正例）通过部分最优传输自动找出嵌入空间中与人类偏好一致的未标注样本，无需大规模重标。

  - 该方法不重新训练 LLM 裁判，仅通过几何对齐修正评分，适合线上部署时快速校准频繁出现的冗长偏差等系统性偏置。

  - 输出的可解释置信度估计可直接用于过滤低质量评估结果，减少误判对线上推荐系统的影响。

  - 可直接套用现有嵌入模型（如sentence embedding），只需构建正样本集合，即可运行审计流程，成本低、工程改造成本小。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**：LLM-as-a-Judge 虽可扩展，但存在与语义质量无关的系统偏差（如冗长偏差），且人工标注成本高、覆盖面小，通常仅能确认少量正面样本，大量输出无标签且质量混杂。

**方法**：将选择性人工监督下的 LLM 评估形式化为正无标签（PU）学习问题，提出基于部分最优传输（Partial Optimal Transport）的几何审计框架。在固定嵌入空间中，对齐少量人类验证的正例与可靠的无标签子集，以此发现与人类一致的偏好顺序，无需重新训练即可校正有偏的 LLM 裁判。

**关键结果**：实验表明该方法能提升与人类偏好的对齐度，增强对呈现偏差的鲁棒性，并提供可解释的置信度估计，为现有 LLM 评估流水线提供了统计上更可靠的替代方案。
