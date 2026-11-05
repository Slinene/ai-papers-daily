---
title: Koopman Generative Operators for Efficient Probabilistic Time-Series Forecasting
title_zh: Koopman 生成算子实现高效概率时间序列预测
authors:
- Raz Marshanski
- Liran Nochumsohn
- Mayank Jauhari
- Boris N. Oreshkin
- Omri Azencot
affiliations:
- Ben-Gurion University of the Negev
- Amazon Science
arxiv_id: '2611.04760'
url: https://arxiv.org/abs/2611.04760
pdf_url: https://arxiv.org/pdf/2611.04760
published: '2026-11-03'
collected: '2026-11-05'
category: Other
direction: 概率时序预测 · Koopman 算子
tags:
- Koopman operator
- probabilistic forecasting
- flow matching
- time series
- efficient inference
- uncertainty estimation
one_liner: 用 Koopman 算子把概率时序预测变成隐空间单步生成，精度领先且推理快 25 倍以上
practical_value: '- 将扩散/流匹配的迭代采样替换为矩阵指数闭式单步生成，可直接用于电商销量、流量、广告消耗等实时概率预测，显著降低在线推理延迟与
  GPU 成本。

  - KoPE 对时序补丁做 Koopman 潜在外推，思路可迁移到用户行为序列、商品生命周期曲线的结构化表示，提升长周期趋势建模的稳定性。

  - AUG 按变量和预测步长自适应调制方差，适合多商品、多地域需求预测中差异化置信区间，避免手工调方差或统一校准。

  - 整体架构强调推理效率与不确定性质量并重，适合作为 Agent 决策中的轻量 world model / reward 预测器，提供快速轨迹采样。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**  
概率时序预测需要同时具备结构化动态建模、表达能力强的预测分布和高效推理。现有潜变量模型结构约束强但生成机制受限，扩散或流匹配方法虽然灵活，却依赖迭代采样、推理昂贵。实际应用如能源、金融、医疗场景对不确定性和时效性要求都很高。

**方法关键点**  
KGO 由三个模块组成：  
- Koopman Patch Embedding (KoPE)：在隐空间用 Koopman 算子对时序补丁做时间一致的外推，捕捉结构化动态。  
- Koopman Flow Matching (KoFM)：在 Koopman 隐空间通过矩阵指数闭式解实现单步生成，避免迭代采样。  
- Adaptive Uncertainty Gate (AUG)：按变量和预测步长自适应学习 aleatoric uncertainty 分解，自动调整预测方差。

**关键结果**  
在 ProbTS 17 个基准上，CRPS 13/17 最优，NMAE 16/17 最优；相比迭代生成模型，推理时间至少减少 25 倍。
