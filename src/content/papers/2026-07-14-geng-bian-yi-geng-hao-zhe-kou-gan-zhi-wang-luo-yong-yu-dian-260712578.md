---
title: 'Cheaper is Better: A Discount-Aware Network for Conversion Rate Prediction
  in E-commerce Recommendation System'
title_zh: 更便宜更好：折扣感知网络用于电商推荐CVR预测
authors:
- Ruocong Tang
- Yang Huang
- Xing Fang
- Chenyi Yan
- Chuike Sun
- Jing Wang
arxiv_id: '2607.12578'
url: https://arxiv.org/abs/2607.12578
pdf_url: https://arxiv.org/pdf/2607.12578
published: '2026-07-14'
collected: '2026-07-15'
category: RecSys
direction: 折扣感知CVR预测
tags:
- CVR Prediction
- Discount-Aware
- Fourier Transform
- Bias Correction
- Multi-task Learning
one_liner: DANet通过傅里叶频谱、分布去偏和回归辅助任务建模商品折扣率对转化率的影响，离线AUC提升1.61%。
practical_value: '- 将折扣率作为显式特征引入CVR模型，并使用时频变换捕获长周期折扣趋势，可借鉴到价格敏感品类的推荐排序中。

  - 分布去偏模块设计适用于电商大促、满减等场景，能缓解用户折扣偏好和周期性活动带来的偏差，可迁移至其他有偏差的用户行为建模（如优惠券使用）。

  - 引入折扣率回归辅助任务，联合主CVR任务训练，能提升模型对折扣幅度的准确表达，可推广到其他数值敏感特征（如价格、评分）的多任务学习。

  - 整体架构轻量，已线上部署，证明折扣感知信号在工业级推荐系统中切实有效，可作为转化率模型的通用增强模块。'
score: 10
source: arxiv-cs.IR
depth: abstract
---

现有CVR模型普遍忽略商品折扣率对用户购买决策的影响，而折扣是电商促销的核心信号。本文提出DANet，将折扣率建模显式引入CVR预测。模型包含三部分：1) 时频变换模块：对商品折扣序列做傅里叶变换得到频谱，捕获长期周期性折扣趋势，缓解行为稀疏时折扣信号不足的问题；2) 分布去偏模块：用户折扣分布受购买组合和促销阶段影响存在偏差，通过偏置校正网络消除用户侧和周期性偏差；3) 有监督回归辅助任务：利用商品折扣标签进行回归，与CVR主任务联合训练，强化模型对折扣幅度的准确表达。离线实验AUC提升1.61%，线上A/B测试pCVR提升3.63%、GMV提升2.23%，已部署在天猫APP。
