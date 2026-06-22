---
title: 'AURA: Adaptive Uncertainty-aware Refinement for LLM-as-a-Judge Auditing'
title_zh: 自适应不确定性感知的LLM裁判审计精炼框架
authors:
- Zilong Zhang
- Yi-Ting Hung
- Weiyi He
- Junxi Zhang
- Lei Ding
- Chi-Kuang Yeh
affiliations:
- Georgia State University
- Michigan State University
- Concordia University
- University of Manitoba
arxiv_id: '2606.19714'
url: https://arxiv.org/abs/2606.19714
pdf_url: https://arxiv.org/pdf/2606.19714
published: '2026-06-18'
collected: '2026-06-22'
category: Eval
direction: LLM-as-a-Judge 审计与人类一致性校准
tags:
- LLM-as-a-Judge
- Uncertainty Estimation
- Human-in-the-Loop
- Evaluation
- Auditing
- Pairwise Comparison
one_liner: 在有限人工验证下，迭代学习人类一致性信号并优先审查不确定比较，提升LLM评判可靠性
practical_value: '- 当用LLM评判器离线评估搜索推荐系统的生成式内容（如推荐理由、对话推荐）时，可借鉴AURA的不确定性感知主动学习机制：优先将LLM低置信度的成对比较送人工审核，少量标注即可显著校准评判器偏见，降低大规模人工评估成本。

  - 将“信任度”显式建模为隐变量并迭代更新的思路可以迁移到业务中：例如在推荐系统的A/B实验解读中，LLM对实验报告的分析结论可能因数据分布偏移而不稳定，通过收集少量人工验证反馈迭代修正信任权重。

  - 提出的可靠证据传播策略可启发在多轮对话评估或序列推荐评估中，如何利用已确认的高质量判断来推断相邻未标注样本，从而提高评估效率。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**：LLM作为评判器广泛用于开放式生成评估，但其偏好与人类判断存在偏差，且传统审计方法依赖事先可靠样本或大量人工标注，实际中难以满足。

**方法**：提出AURA框架，将评判器的信任度视为隐变量，通过迭代精炼逐渐逼近人类一致性。核心机制包括：(1)基于当前信任估计主动选择不确定性最高的成对比较进行人工审核；(2)利用已确认的可靠证据传播信任；(3)以紧凑的概率公式更新隐变量，实现稳定精炼。

**结果**：在合成和真实配对LLM答案数据上，AURA在少量人类干预下有效纠偏，显著提升与人类判断的一致性，且精炼过程稳定。
