---
title: 'SAHC-NS: Structure-Aware and Hardness-Calibrated Negative Sampling for Implicit
  Collaborative Filtering'
title_zh: SAHC-NS：面向隐式协同过滤的结构感知与硬度校准负采样
authors:
- Jiayi Wu
- Zhengyu Wu
- Xunkai Li
- Hongchao Qin
- Rong-Hua Li
- Guoren Wang
affiliations:
- Beijing Institute of Technology
arxiv_id: '2608.16587'
url: https://arxiv.org/abs/2608.16587
pdf_url: https://arxiv.org/pdf/2608.16587
published: '2026-08-17'
collected: '2026-08-18'
category: RecSys
direction: 负采样 · 结构感知与硬度校准
tags:
- Negative Sampling
- Collaborative Filtering
- Implicit Feedback
- Graph Neural Networks
- Hardness Calibration
- Structure-Aware
one_liner: 用逐层匹配分数的均值与标准差捕获跨层结构差异，并基于候选池硬度动态校准负样本难度
practical_value: '- 在电商双塔召回或 GNN 推荐模型中，可以保留各层传播的 user/item 表示，计算逐层匹配分数的均值与标准差，筛选出“跨层结构不一致”的负样本（如外观相似但交互结构不同的商品），而不仅看最终分数，提升
  hard negative 质量。

  - 可借鉴候选池感知的硬度校准：统计每个用户负样本池的匹配分数分布（均值/方差），对候选池整体偏容易的用户加大负样本增强强度，对偏难的用户降低强度，避免固定负采样策略导致的训练不稳定。

  - 适用于点击、加购、转化等隐式反馈场景，可在现有 GNN 召回/排序模型中增加逐层分数统计与校准模块，工程实现成本可控。

  - 如果业务中存在大量未观测样本或易混淆广告，可参考其结构感知评估方式，增强模型对相似商品/广告的判别边界。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

## 动机
隐式反馈协同过滤中负采样直接影响模型学习用户偏好的效果。现有方法多采用两阶段范式：先为每个用户构造候选负样本池，再按固定规则采样，忽略了不同用户候选池的难度差异，无法自适应调整负样本的难度与信息量。此外，多数采样器只用最终聚合的 user/item embedding 计算匹配分数，忽略多层邻居聚合捕获的结构差异，导致负样本训练价值刻画不足。

## 方法关键点
该方法使用逐层匹配分数的均值和标准差，分别刻画候选负样本的整体匹配强度与跨层结构差异，从而选择具有结构不一致性的高信息量负样本，而非只依赖最终匹配分数。同时引入候选池感知的硬度校准模块，根据候选池的硬度分布动态调整负样本增强强度，生成硬度可控的负样本，缓解不同用户候选池难度变化带来的偏差。

## 关键结果
在多个基准数据集上的实验显示，相比现有负采样方法取得更优推荐精度，验证了结构感知评估与候选池硬度校准的有效性（具体数值见原论文）。
