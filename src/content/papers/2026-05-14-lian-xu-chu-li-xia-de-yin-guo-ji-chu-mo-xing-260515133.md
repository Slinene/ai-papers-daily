---
title: Causal Foundation Models with Continuous Treatments
title_zh: 连续处理下的因果基础模型
authors:
- Christopher Stith
- Medha Barath
- Vahid Balazadeh
- Jesse C. Cresswell
- Rahul G. Krishnan
arxiv_id: '2605.15133'
url: https://arxiv.org/abs/2605.15133
pdf_url: https://arxiv.org/pdf/2605.15133
published: '2026-05-14'
collected: '2026-05-17'
category: Other
direction: 因果基础模型 · 连续处理
tags:
- Causal Inference
- Foundation Model
- Meta-Learning
- In-Context Learning
- Continuous Treatment
- Individual Treatment Effect
one_liner: 首个面向连续处理的因果基础模型，通过元学习和上下文学习实现个体处理效应曲线的零样本预测
practical_value: ' - 电商中价格、折扣、广告预算等连续干预的因果效应估计，可借鉴该模型的元学习思路，预训练一个能快速适应新场景的基础模型，避免每次活动都从零建模。

  - 利用合成数据生成丰富的因果训练集（类似论文的 prior over DGPs），可大幅降低真实业务标注成本，尤其适合干预变量连续且实验成本高的场景。

  - Transformer 作为结构，以上下文学习方式直接输出个体处理效应曲线，相比传统的反事实预估模型，能更细粒度地刻画异质性，为个性化定价或补贴决策提供依据。

  - 该模型展示的“摊销贝叶斯后验”思想，可启发我们在推荐系统中用统一的神经网络替代反复的 MCMC 推断，提升在线实验效率。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：因果推断中连续处理（如剂量、价格）的效应估计比二元处理更具挑战，需建模整个干预连续体上的反应曲线。现有方法多为特定任务从头训练，缺乏跨任务泛化能力。

**方法**：提出首个面向连续处理的因果基础模型。首先设计了一种新颖的关于数据生成过程的先验，用于合成大量多样的连续处理因果数据作为训练语料。然后训练一个 Transformer，仅给定观测数据，便可通过上下文学习直接重建个体处理-反应曲线（即条件平均处理效应函数），该过程相当于摊销了昂贵的贝叶斯后验推断，无需对新任务进行微调。

**结果**：在个体处理反应曲线重建基准上，模型表现超过专门针对各任务训练的因果模型，首次在连续处理设定下验证了基础模型范式的有效性。
