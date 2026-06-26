---
title: Forecasting Future Behavior as a Learning Task
title_zh: 将未来行为预测作为学习任务
authors:
- Mosh Levy
- Yoav Goldberg
- Asa Cooper Stickland
affiliations:
- Bar-Ilan University
- Constellation
- Allen Institute for AI
- UK AI Security Institute
arxiv_id: '2606.11445'
url: https://arxiv.org/abs/2606.11445
pdf_url: https://arxiv.org/pdf/2606.11445
published: '2026-06-08'
collected: '2026-06-26'
category: Other
direction: 行为预测 · 推理模型可解释性
tags:
- behavior forecasting
- large reasoning models
- explainability
- fine-tuning
- reasoning trajectory
one_liner: 训练Behavior Forecaster从推理轨迹直接预测大推理模型的行为，比强LLM更准且成本更低。
practical_value: '- 若使用大推理模型（如DeepSeek-R1）做搜索排序、Agent决策，可通过训练小模型预测其输出一致性，低成本做线上预检。

  - 自动构建训练数据的方法：多次查询LRM获取轨迹与行为标签，无需人工标注，适合构建自定义监控模型。

  - 预测LRM对输入扰动的敏感性，可用于评估输入中哪些特征对推荐结果影响大，辅助特征工程。

  - 推理轨迹包含比纯文本阅读更丰富的信息，建议在LLM诊断时利用轨迹特征训练下游预测模型，而非依赖提示工程。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：大推理模型（LRM）的决策过程难以解释，传统的基于解释预测行为的方法在长推理轨迹上泛化性差，且轨迹本身常不忠实。为可靠地预测LRM的未来行为（如一致性、敏感性），需要更直接的途径。

**方法**：提出将行为预测作为学习任务，训练Behavior Forecaster。该模型输入LRM的单条推理轨迹（不含最终答案），预测该LRM的行为，如：重复运行给出相同答案的概率、移除部分输入后答案是否改变。训练数据全自动获得：对每个问题多次查询LRM得到答案分布，或对扰动输入查询得到答案变化情况。Forecaster使用目标LRM的backbone初始化并端到端微调。

**关键结果**：在GSM8K、MATH等三个推理数据集上，训练得到的Behavior Forecaster在两项预测任务上均显著优于GPT-5.4和Claude Opus-4.6直接阅读轨迹的baseline，且推理成本仅为后者的很小一部分。消融实验表明，必须使用目标LRM的权重初始化并端到端微调才能获得强性能，冻结特征或随机初始化效果大幅下降。这表明推理轨迹中隐含着LRM未来行为的丰富信息，但需要适配的模型才能提取。
