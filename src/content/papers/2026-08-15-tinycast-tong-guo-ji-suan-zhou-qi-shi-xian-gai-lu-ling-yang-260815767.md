---
title: 'TinyCast: Probabilistic Zero-Shot Forecasting with Computed Periodicity'
title_zh: TinyCast：通过计算周期实现概率零样本预测
authors:
- Armin Steinhauser
affiliations:
- RA WS Labs
arxiv_id: '2608.15767'
url: https://arxiv.org/abs/2608.15767
pdf_url: https://arxiv.org/pdf/2608.15767
published: '2026-08-15'
collected: '2026-08-22'
category: Other
direction: 零样本时序预测 · 轻量概率模型
tags:
- zero-shot forecasting
- probabilistic forecasting
- spectral periodicity
- dilated convolution
- quantile decoder
- tiny model
one_liner: 146K参数零样本概率预测器，用频谱计算周期并做相位折叠，定义尺寸-精度前沿
practical_value: '- 电商/供应链的时序预测（销量、流量、广告消耗）可借鉴“先算周期再折叠相位”：用频谱检测主周期，将序列按周期相位折叠，能大幅降低模型要学习的周期性，适合轻量模型。

  - 要在端侧或广告平台 RTB 场景部署预测器，可参考其只含卷积+矩阵乘法的设计：能导出 static INT8 并端到端运行，无需逐信号拟合。

  - 分位数解码器输出预测分布而非点估计，适合库存安全水位、预算控制、告警阈值等需要 uncertainty 的业务决策；比仅有点预测的小模型更可控。

  - “block-autoregressive”生成未来一段再自回归，可迁移到多步需求预测/预算分配，减少长程误差累积，同时保持小参数。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：时序基础模型越做越大，但边缘部署需要小模型；同时概率预测对控制、告警等业务重要。此前小于 1.4M 参数、无 test leakage 的零样本模型通常只输出点预测。TinyCast 想在极小参数量下保留概率输出。

**方法关键点**：
- 零参数频谱检测器计算支配性周期，不做学习；
- 将上下文按周期相位折叠，显式暴露周期性结构；
- 用 dilated convolutional encoder + block-autoregressive quantile decoder，无 attention，只含卷积与矩阵乘法；
- 通过分位数输出预测分布。

**关键结果**：
- 参数量仅 146,505，比 GIFT-Eval 榜上所有可查参数的零样本模型都小；
- 在概率精度上定义 size-accuracy frontier；在宣称无 test leakage 的零样本模型中，是唯一低于 1.4M 参数且能输出预测分布的，比它更好的模型至少需要 1.4M 参数预算；
- 在 Chronos-ZS 和 fev-bench 上，比它强的神经模型参数量至少大 28 倍；
- 可导出 static INT8，在嵌入式设备端到端预测，无需逐信号拟合。
