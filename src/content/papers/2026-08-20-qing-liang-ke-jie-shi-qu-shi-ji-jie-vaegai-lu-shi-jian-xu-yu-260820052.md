---
title: 'DecoVAE: a Lightweight Interpretable Trend-Seasonal VAE Framework for Efficient
  Probabilistic Time Series Forecasting'
title_zh: 轻量可解释趋势季节VAE概率时间序列预测框架
authors:
- Alexander Marusov
- Dmitry Anikin
- Alexey Zaytsev
affiliations:
- Applied AI Institute
arxiv_id: '2608.20052'
url: https://arxiv.org/abs/2608.20052
pdf_url: https://arxiv.org/pdf/2608.20052
published: '2026-08-20'
collected: '2026-08-22'
category: Other
direction: 概率时间序列预测 · 趋势季节分解VAE
tags:
- Probabilistic Forecasting
- Time Series
- VAE
- Trend-Seasonal Decomposition
- Lightweight
- Interpretable
one_liner: 显式分解趋势与季节，用差分正则与频域复VAE实现轻量高精度概率预测
practical_value: '- 电商中销量、流量等时间序列预测可借鉴趋势/季节显式分解：趋势流用差分正则化平滑latent，季节流用频域复高斯VAE捕捉周期，比统一建模更准确，尤其适合大促、季节性商品。

  - 轻量化设计对线上推理友好：模型权重减少93%、推理加速74%，适合需要实时更新预测的推荐/广告系统，降低计算成本。

  - 可复用的正则化技巧：对latent trajectory施加HP滤波式差分惩罚，可迁移到任何需要平滑趋势的预测任务（如CTR趋势、GMV预测）作为辅助损失。

  - 频率域建模周期性的方法可借鉴到推荐中的周期性特征（如用户周行为、节假日效应），用复VAE学习振幅和相位，增强对周期波动的泛化。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：概率时间序列预测需要准确建模趋势和季节，但现有方法常忽略成分差异、缺乏可解释性或计算开销大。

方法：DecoVAE显式分解时间序列为趋势和季节两路。趋势流在latent轨迹上施加差分正则化（类比Hodrick-Prescott滤波器）强制结构平滑；季节流采用频域复高斯VAE，原生捕捉周期模式的振幅和相位。两路组合实现轻量可解释的VAE框架。

结果：在7个真实基准上评测，DecoVAE显著优于强基线：短期预测CRPS降低最高14.96%、NMAE降低23.30%；长期预测CRPS降低最高52.68%、NMAE降低26.51%。同时模型权重减少最高93%，推理速度提升最高74%。
