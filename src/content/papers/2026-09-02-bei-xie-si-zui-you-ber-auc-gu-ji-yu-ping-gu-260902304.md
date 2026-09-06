---
title: 'Bayes-Optimal BER and AUC: Estimation and Evaluation of Estimators'
title_zh: 贝叶斯最优 BER/AUC 估计与评估
authors:
- Ryota Ushio
- Takashi Ishida
- Masashi Sugiyama
affiliations:
- The University of Tokyo
- RIKEN AIP
arxiv_id: '2609.02304'
url: https://arxiv.org/abs/2609.02304
pdf_url: https://arxiv.org/pdf/2609.02304
published: '2026-09-02'
collected: '2026-09-06'
category: Eval
direction: 最优性能估计与评估 · soft labels
tags:
- Bayes error
- BER
- AUC
- soft labels
- isotonic regression
- estimator evaluation
one_liner: 提出基于软标签的最优 BER 与 AUC 估计器，并扩展 FeeBee 框架评估任意估计器
practical_value: '- 在电商 CTR/CVR 预估、广告排序等高度类别不平衡场景，常用 AUC/BER 评估；可用该方法估计业务数据上的贝叶斯最优
  AUC/BER，量化“不可约误差”与模型可提升空间，辅助判断模型是否已接近天花板。

  - 若线上能采集到软标签（如用户停留时长、成交概率、点击概率），可尝试用 isotonic regression 校准并估计最优指标；该方法对标签噪声和保序变换鲁棒，适合真实日志中常见的标注偏差。

  - 评估最优指标估计器本身难，可借鉴 FeeBee 扩展流程，在无 ground truth 最优值的情况下比较不同估计器的表现，作为离线评估工具。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**：估计任务的最优可达到性能能区分不可约误差与模型缺陷，但现有工作聚焦 accuracy/Bayes error，在类别不平衡或噪声标注下，BER 和 AUC 更合适。

**方法关键点**：
- 基于软标签构造最优 BER 和 AUC 的估计器。
- 先处理已知真实软标签和类别先验的 clean setting；
- 再推广到更现实设置：类别先验未知，软标签受未知保序变换和加性噪声破坏。此时用 isotonic regression 结合辅助硬标签近似恢复干净软标签；用截断硬标签均值估计类别先验；并给出有限样本误差界。
- 评估方面，扩展 FeeBee 框架到最优 BER/AUC，无需知道真实最优即可评估任意估计器。

**关键结果**：合成和真实数据集实验验证了估计器和评估流程的有效性；推导的 plug-in 估计器具有有限样本误差界。
