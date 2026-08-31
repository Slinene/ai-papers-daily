---
title: 'Timing-Aware Repurchase Prediction for Web-Scale E-Commerce: Survival Models
  for Multi-Surface Grocery Recommendation'
title_zh: 时间感知复购预测：面向多渠道电商的生存模型
authors:
- Akshay Kekuda
- Shreeranjani Srirangamsridharan
- Ishan Bhatt
- Yanan Cao
- Sinduja Subramaniam
- Evren Korpeoglu
- Kaushiki Nag
- Kannan Achan
affiliations:
- Walmart Global Tech
arxiv_id: '2608.28393'
url: https://arxiv.org/abs/2608.28393
pdf_url: https://arxiv.org/pdf/2608.28393
published: '2026-08-28'
collected: '2026-08-31'
category: RecSys
direction: 生存分析复购预测 · 多时间面排序
tags:
- survival analysis
- repurchase prediction
- AFT
- grocery recommendation
- calibration
- multi-horizon
one_liner: 用单个加速失效时间模型替代多时间窗口复购预测的多个二分类器，在提升排序的同时降低约3倍算力
practical_value: '- 多 horizon 的复购/重购买 surface，可以直接把每个 horizon 的二分类器换成一个 XGBoost `survival:aft`，排序用
  `-exp(leaf value)` 或预测的 time-to-repurchase，保持原特征与推理管线不变；训练/服务成本约降 3×，离线各 horizon
  不降。

  - 经验 hazard 显示 shape k≈0.9（略递减），不要默认“越 overdue 越可能买”；排序面用 Log-Normal，概率消费面用 Exponential/Weibull
  k=1，再用 4 参数共享斜率+分段截距校准，保证跨 horizon 单调性零违例，ECE 可低至 1e-4 量级。

  - 右删失样本（未复购）必须保留，尤其长周期用户；删除大 lapsed 的 censored 样本会导致长周期买家排序崩坏，正则化也救不回。

  - 生存目标会重塑特征重要性：渠道节奏、最近性、缺货/部分履约信号上升，总频次类特征下跌；可据此做特征裁剪，或构造 IPI-lapse residual、interval-relative
  features 这类 timing gap 特征。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：电商复购推荐常被建模为“W 天内是否复购”的二分类问题，但首页 7 天购物清单、App 14 天补货、邮件 30 天备货等不同 surface 实际问的是“什么时候买”。为每个 horizon 训练独立模型浪费算力且丢失时间结构；生存分析直接预测 time-to-repurchase。

**方法关键点**：
- 用 XGBoost `survival:aft` 预测标量 `λ=exp(f(x))`，一个模型服务多个 horizon；比较 Weibull/Log-Normal/Logistic。
- 对千万级样本做经验 hazard 分析：Weibull shape k̂=0.911，hazard 略递减，并非“越 overdue 越可能买”。
- Log-Normal 边际拟合 R²=0.998、排序最好；Weibull 条件残差拟合最好，体现 loss 的 inductive bias 与拟合目标不完全一致。
- 离散时间 hazard 模型：person-period 扩张成 3 个 interval + interval-relative features；单模型可输出分 horizon CDF。
- 4 参数校准：共享斜率 a + 每 horizon 截距 b_t，把 survival CDF 映射为概率，保证跨 horizon 单调性零违例。

**关键实验**：数据集为大型杂货电商千万级 (customer,item) pairs，30 天右删失；对比生产上 3 个 XGBoost 二分类器，每个 800 棵树。单个 Log-Normal AFT P@14d=0.3788，较最强单 horizon baseline 0.3757 提升 +0.82%；各 horizon 均匹配或超越；总树数从 2400 降到约 700，约 3× 节省。Exponential AFT 校准 ECE≈1.3e-4，比 Log-Normal 低约 6 倍，排序差距 <0.3%。特征重要性重塑：渠道节奏/最近性上升，3 个月订单总数从 rank12 跌到 54。

**最值得记住**：把“会不会买”改成“什么时候买”，只换 objective 不换特征和树模型，就能用更少模型覆盖多 surface，并免费获得更好排序。
