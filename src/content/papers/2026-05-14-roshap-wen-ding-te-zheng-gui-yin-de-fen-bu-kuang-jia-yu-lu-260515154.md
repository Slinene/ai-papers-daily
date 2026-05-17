---
title: 'RoSHAP: A Distributional Framework and Robust Metric for Stable Feature Attribution'
title_zh: 'RoSHAP: 稳定特征归因的分布框架与鲁棒度量'
authors:
- Lanxin Xiang
- Liang Shi
- Youhui Ye
- Boyu Jiang
- Dawei Zhou
- Feng Guo
arxiv_id: '2605.15154'
url: https://arxiv.org/abs/2605.15154
pdf_url: https://arxiv.org/pdf/2605.15154
published: '2026-05-14'
collected: '2026-05-17'
category: Eval
direction: 稳定特征归因与特征选择
tags:
- SHAP
- feature attribution
- stability
- bootstrap
- distribution estimation
- feature selection
one_liner: 通过bootstrap估计SHAP分布并证明渐近正态性，提出同时奖励活跃、高影响且稳定特征的鲁棒排序度量RoSHAP
practical_value: '- 推荐系统特征工程中，用RoSHAP替代单次SHAP排序，通过bootstrap多次计算均值与标准差，筛选出稳定且强效的特征，减少随机种子/数据划分带来的特征排名波动，提升特征选择的鲁棒性。

  - 在模型迭代或AB测试场景下，定期计算特征的RoSHAP分布，监控特征重要性是否发生漂移，及时发现数据分布变化或特征失效问题。

  - 对Agent决策解释，借鉴分布框架思想，对多轮推理或不同环境下的归因结果进行聚合，避免单次解释的随机性误导，增强解释可靠性。

  - 工程实现上，可将bootstrap SHAP计算与训练pipeline解耦，仅需少量额外计算即可获得特征稳定性指标，用于自动化特征筛选与模型压缩。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：特征归因分析常因训练过程的随机性（数据划分、随机种子等）导致归因分数和排序高度可变，单次计算不可靠。

**方法**：提出分布框架，通过bootstrap重采样和核密度估计获得SHAP值的分布。证明在温和正则条件下，聚合归因分数渐近服从高斯分布，极大降低分布估计的计算成本。在此基础上定义RoSHAP度量，综合特征的**活跃性**（非零归因的频率）、**强度**（归因值的大小）和**稳定性**（方差的倒数），给出稳定的特征排序。

**结果**：仿真和真实数据实验表明，RoSHAP在识别信号特征上优于单次归因方法；用RoSHAP选出的少量特征构建的模型，预测性能与全特征模型相当，同时大幅减少预测变量。该方法提高了模型的可解释性和稳健性。
