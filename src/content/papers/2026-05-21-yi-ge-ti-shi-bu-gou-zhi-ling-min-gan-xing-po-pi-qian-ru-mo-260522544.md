---
title: 'One prompt is not enough: Instruction Sensitivity Undermines Embedding Model
  Evaluation'
title_zh: 一个提示不够：指令敏感性破坏嵌入模型评估
authors:
- Yevhen Kostiuk
- Kenneth Enevoldsen
affiliations:
- Aarhus University
arxiv_id: '2605.22544'
url: https://arxiv.org/abs/2605.22544
pdf_url: https://arxiv.org/pdf/2605.22544
published: '2026-05-21'
collected: '2026-05-25'
category: Eval
direction: 嵌入模型评估的指令敏感性
tags:
- instruction embedding
- prompt sensitivity
- evaluation
- benchmark robustness
- model ranking
one_liner: 指令嵌入模型性能对提示措辞高度敏感，单点评估掩盖真实分布，排行榜排名不稳健。
practical_value: '- 在电商搜索、推荐系统中使用指令嵌入模型时，**不能仅依赖官方给出的单个默认提示**，应针对同一任务编写多个语义等价的指令变体，测试性能分布，避免因提示波动导致线上效果恶化。

  - **构建内部基准测试时，加入提示稳健性指标**：除了报告平均得分，还应报告标准差或绘制箱线图，识别易受提示影响的模型，选择更稳定的模型上线。

  - **在 A/B 测试或模型选型阶段，刻意用不同的指令措辞评估多个候选模型**，防止选出一个只在特定提示下表现好但泛化差的模型。

  - **工程上，可预先存储多组任务指令**，在推理时随机选择或按历史效果加权，降低单点提示带来的方差，提升系统鲁棒性。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：当前指令微调的嵌入模型（如 e5、Qwen 系列）在评估时只使用每个任务的一条默认提示，忽略了指令措辞对模型性能的敏感性。这导致报告的分数可能偏离真实分布，影响模型比较和选型。

**方法**：作者在 6 个主流指令嵌入模型、11 个数据集上，为每项任务设计了 15 个语义等价但措辞不同的指令（共 990 组实验），量化了模型在不同提示下的性能波动，并检验排行榜排名的稳健性。

**关键结果**：(1) 单点评估常常高估或低估实际性能——默认提示可能系统性“膨胀”或“缩水”得分；(2) 通过刻意选择有利提示，任何一个参与测试的模型都可以被推到榜单第一，排行榜排名极度不稳；(3) 强调评估应纳入多提示均值和敏感度指标，而非仅报告单点估计。
