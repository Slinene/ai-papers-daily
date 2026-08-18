---
title: Forecast Collapse in Time-Series Foundation Models
title_zh: 时间序列基础模型中的预测坍缩现象与校准-排序权衡
authors:
- Shu Wan
- Miles Ma
- Hank Zhu
- Guangqi Liu
- Stephen Wang
- Qingsong Wen
- Huan Liu
affiliations:
- Abel AI Lab
- Arizona State University
- University of Oxford
arxiv_id: '2608.14106'
url: https://arxiv.org/abs/2608.14106
pdf_url: https://arxiv.org/pdf/2608.14106
published: '2026-08-13'
collected: '2026-08-18'
category: Other
direction: 时序基础模型 · 校准-排序权衡
tags:
- Time-Series
- Foundation Models
- Calibration
- Ranking
- Financial Forecasting
- CalibRank
one_liner: 发现时序基础模型预测坍缩现象，提出 CalibRank 平衡校准与排序，横截面相关性近三倍提升。
practical_value: '- 排序目标与校准目标未必一致：若业务指标是物品排序质量（如信息流/广告 CTR 排序），只优化 pointwise MSE/Logloss
  可能导致预测趋于均值、区分度不足。可尝试在损失中加入 batch-level 排序项（如 pairwise/listwise loss 或相关性正则），类似 CalibRank。

  - 评估需补横截面/排序视角：逐样本 AUC/准确率可能掩盖排序结构失灵，增加 IC、Spearman 或 NDCG 等指标监控，尤其对于低信号目标（点击、转化）。

  - 低可预测性 + 校准约束会使预测振幅过小：若线上排序模型打分过于集中，可放松校准约束或对 logits 做温度缩放/振幅重标定，但需监控校准误差。

  - 多实体共享模型（用户/商品）时，逐实体损失不识别全局序；可尝试在训练中构造 batch 内样本对或跨实体排序损失。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：在对 1000 只美国股票小时收益预测中，发现时间序列基础模型（TSFM）的预测几乎平坦、横截面排序差，作者称之为预测坍缩；而交易量预测无此现象，引发系统研究。

方法关键点：跨越多个 TSFM、12 个深度学习模型、97 个公开基准配置，发现预测坍缩与目标可预测性高度相关。两个直接原因：低可预测性限制校准点预测的振幅；逐序列优化目标无法识别横截面结构。进一步揭示校准-排序权衡——优化平方误差导致预测平坦，直接优化横截面相关性虽提升排序但振幅会膨胀一个数量级以上。为此提出 CalibRank，一个简单目标函数，平衡校准与排序。

关键结果：在 Finance1K 数据集上，CalibRank 使横截面相关性近三倍提升，同时振幅接近真实目标，并在所有测试模型上改善相关性。该工作揭示传统逐序列评估的盲点：per-series 指标会掩盖下游决策所依赖的横截面结构失效。
