---
title: Multiagent Protocols with Aggregated Confidence Signals
title_zh: 多智能体协议中基于聚合置信度信号的可靠估计
authors:
- Ali Elahi
- Barbara Di Eugenio
affiliations:
- University of Illinois Chicago
arxiv_id: '2606.13591'
url: https://arxiv.org/abs/2606.13591
pdf_url: https://arxiv.org/pdf/2606.13591
published: '2026-06-11'
collected: '2026-06-13'
category: MultiAgent
direction: 多智能体系统置信度估计与聚合
tags:
- Multiagent Debate
- Confidence Aggregation
- Calibration
- Bayesian Fusion
- LLM Collaboration
one_liner: 首次为多智能体辩论系统设计聚合置信度，通过可比性转换与贝叶斯融合显著提升判别力
practical_value: '- 电商搜索/推荐中的多Agent协同（如Query理解、商品召回）可借鉴软投票或贝叶斯融合聚合各Agent置信度，用于触发人工审核或自动路由决策

  - 置信度转换（使输出概率跨模型可比）的思路可直接用于解决异构模型协作时的分数对齐问题

  - 参数与非参数校准实验显示校准主要提升决策正确率(F1)，若业务目标侧重可靠筛选(AUARC)则可放松校准需求，节约计算

  - 生成式推荐中使用多模型辩论生成商品描述或解释时，聚合置信度可作为生成内容的可靠性指标，辅助过滤低质量输出'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有NLP置信度估计仅用于单模型，多智能体系统（如辩论）缺乏整体置信度输出，限制了系统可靠性评估与下游决策（如人为干预触发、路由）。

**方法**：提出三种协议，通过两个阶段生成聚合置信度：
1. **可比性转换**：将各模型原始置信度（序列概率或自述分数）通过校准器（参数/非参数）映射到统一尺度，解决跨模型分数不可比问题。
2. **融合**：采用软投票或贝叶斯融合（条件概率推导）整合转换后的置信度，输出最终答案与单一置信度。

**结果**：在5个基准（涵盖推理、知识、对话等任务）上评估6对同构/异构辩论LLM（7B–30B），聚合置信度的AUARC（面积下置信度-正确性曲线）显著优于最佳单智能体与标准辩论基线；F1保持稳定，且能弥补多智能体辩论在模糊任务上的性能损失。两种置信度估计量（序列概率、自述）中，校准提升F1但对AUARC改善有限。
