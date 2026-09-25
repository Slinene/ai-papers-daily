---
title: Self-Play Pretraining with Zero Data
title_zh: 零数据自博弈预训练
authors:
- Aditya Cowsik
- Kfir Dolev
- Michael Y. Li
- G. Bruno De Luca
- Nourya Cohen
- Noah D. Goodman
- Yoav Levine
affiliations:
- Independent Researcher
- Tel Aviv University
- Stanford University
- LAPTh, USMB
arxiv_id: '2609.30063'
url: https://arxiv.org/abs/2609.30063
pdf_url: https://arxiv.org/pdf/2609.30063
published: '2026-09-24'
collected: '2026-09-25'
category: Training
direction: 自博弈合成数据预训练
tags:
- Self-Play
- Synthetic Data
- Pretraining
- Turing Machine
- Reinforcement Learning
- Curriculum Learning
one_liner: 自博弈零数据预训练用生成器-学习器对训，以图灵机程序生成数据，零样本损失随算力可预测缩放
practical_value: '- 自博弈课程生成器-学习器架构可迁移到搜索/推荐中的难例挖掘：让 query 或候选生成器专门产出当前排序/召回模型易错的边界样本，替代固定人工负样本或模板，训练目标随模型能力动态调整。

  - 双模型分离（生成器 RL + 学习器 CE）比单一模型自生成训练更稳定，适合生成式推荐中的 Semantic ID 或 query 改写：生成器负责探索新
  token 组合，学习器只做密度估计。

  - “用算力换人类知识”的思路对数据稀缺场景有参考价值：如果领域内可定义可执行的结构化生成器（如商品标题语法、用户行为序列模拟器），可先小规模验证合成数据的零样本收益是否随算力可预测。

  - 注意通用图灵机搜索空间过大，直接工业落地成本高；业务上需把程序空间约束为领域特定 DSL 或模板，否则大量算力浪费在无效结构上。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：现有语言模型预训练依赖大规模人工筛选与设计的数据，数据多样性受人类知识限制；目标转向让模型自己生成对自身提升最有用的数据，理论上以算力为边界而非人类知识。

方法关键点：从随机初始化同时训练两个模型——generator 生成程序，由通用图灵机解释执行后产生字节序列；learner 自回归预测这些字节序列，用标准交叉熵训练。generator 通过强化学习优化，生成处于 learner 当前能力前沿的序列，形成自适应课程。通用图灵机把搜索空间定义为所有可计算数据生成过程，不做领域假设；self-play 在这个空间中搜索对 learner 有用的训练数据。评估采用零样本自然数据，生成器和学习者都不接触自然数据。

关键结果：在多个自然数据集上，零样本 loss 随 self-play compute 可预测地缩放；模型表现出 in-context learning 能力，并在训练过程中发现了可识别的数学序列。
