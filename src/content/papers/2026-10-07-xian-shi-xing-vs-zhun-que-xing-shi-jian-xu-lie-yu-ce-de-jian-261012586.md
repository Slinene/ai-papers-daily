---
title: 'Realism VS Accuracy: Event Sequence Forecasting from a Generative Modeling
  Perspective'
title_zh: 现实性 vs 准确性：事件序列预测的生成建模视角
authors:
- Dmitry Osin
- Egor Surkov
- Petr Mokrov
- Igor Udovichenko
- Ivan Karpukhin
- Evgeny Burnaev
- Egor Shvetsov
- Alexander Korotin
affiliations:
- Applied AI Institute
- ITMO University
- Vega Institute Foundation
- SB AI Lab
- AXXX
arxiv_id: '2610.12586'
url: https://arxiv.org/abs/2610.12586
pdf_url: https://arxiv.org/pdf/2610.12586
published: '2026-10-07'
collected: '2026-10-24'
category: Other
direction: 事件序列条件生成建模与评估基准
tags:
- Event Sequence Forecasting
- Generative Modeling
- Diffusion Models
- Wasserstein Barycenter
- Benchmark
- Accuracy-Realism Trade-off
one_liner: 提出事件序列预测基准与Wasserstein BaryBooster算法，揭示准确性与分布真实性权衡，并将扩散模型样本聚合为SOTA预测器
practical_value: '- 评估生成式推荐/用户行为序列模型时，除 hit rate 等 accuracy 指标外，引入分布真实性指标（如 Wasserstein
  距离、MMD）检测模式坍塌，避免生成结果集中在少数高频事件。

  - Wasserstein BaryBooster 的思路可迁移到生成式推荐：用扩散模型生成多个候选 item 或序列，再通过最优传输聚合（如 Wasserstein
  barycenter）得到确定性排序或预测，将生成多样性转化为点预测精度。

  - 事件序列同时包含数值特征（如交易金额）和类别特征（如商品类目），该基准的异构建模方式可参考用于电商交易序列、用户行为序列的长期预测。

  - 准确性-真实性权衡的发现提醒：追求 likelihood 或逐点预测可能牺牲生成质量，应根据业务目标（如推荐多样性 vs 点击率）选择模型或设计混合策略。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：事件序列预测（如信用卡交易、临床记录、游戏行为）面临异构特征（数值+类别）和多步长预测挑战，传统 temporal point processes (TPP) 难以原生处理这些特征。

**方法**：将事件序列预测形式化为条件生成建模问题，构建了一个综合基准，包含两类评估指标——预测准确性和分布真实性（distributional realism），并纳入统计基线、邻域适应模型及真实数据集。提出 Wasserstein BaryBooster 算法：以 realism-strong 的扩散模型为基础，通过最优传输重心聚合其样本，得到确定性但高精度的预测器。

**结果**：实验显示没有任何方法能同时在准确性和真实性上领先，揭示了二者间的根本权衡。Wasserstein BaryBooster 成功将扩散模型的分布真实性转化为预测准确性，取得 state-of-the-art 表现。代码已开源。
