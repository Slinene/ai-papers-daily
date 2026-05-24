---
title: Forecasting Downstream Performance of LLMs With Proxy Metrics
title_zh: 基于代理指标的LLM下游性能预测
authors:
- Arkil Patel
- Siva Reddy
- Marius Mosbach
- Dzmitry Bahdanau
affiliations:
- Mila – Quebec AI Institute
- McGill University
- ServiceNow Research
arxiv_id: '2605.18607'
url: https://arxiv.org/abs/2605.18607
pdf_url: https://arxiv.org/pdf/2605.18607
published: '2026-05-17'
collected: '2026-05-24'
category: Eval
direction: 代理指标 · 专家轨迹 · 性能预测
tags:
- LLM
- evaluation
- proxy metrics
- entropy
- top-k accuracy
- expert token rank
one_liner: 聚合专家解答上的token级熵、top-k准确率、专家token排名作为代理指标，预测LLM下游性能，显著优于损失和计算基线
practical_value: '- 在模型选型或数据筛选阶段，用少量专家标注数据（如人工标注或用户行为序列）计算token级指标，代替昂贵的下游评估，节省千倍计算。

  - 训练早期监控代理指标趋势（如熵、top-k准确率），可提前预测最终下游表现，及时终止劣化实验，加速迭代。

  - 对多智体系统，可将高质量agent轨迹视为专家解答，聚合token级统计量评估agent决策质量，用于在线筛选prompt或模型。

  - 生成式推荐中，将用户交互序列作为专家轨迹，构造类似代理指标，可用于选型、数据筛选或训练过程中的表现预测。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：交叉熵损失与下游能力不对齐，直接评估成本高且在训练早期不敏感，导致模型开发中的比较决策（架构、数据、训练配方）缺乏可靠信号。

**方法**：从候选模型在专家解答上的下一个token分布中提取**熵、top-k准确率、专家token排名**等token级统计量，聚合为代理指标。无需完整下游评估，仅需少量专家标注数据。

**结果**：
- 跨家族模型选择：在一组异质推理模型上，代理指标排名Spearman ρ=0.81，远超交叉熵损失（ρ=0.36）。
- 预训练数据选择：用**约万分之一计算量**可靠排名25个候选语料库，超越现有方法。
- 训练中预测：跨18倍计算跨度外推下游准确率，误差约为现有方法的**一半**。

代理指标一致优于损失和计算基线，表明专家轨迹是评估模型能力的强信号，可用于模型开发全生命周期。
