---
title: 'CanniUplift: A Holistic Framework for Mitigating Seller and Incentive Cannibalization
  in E-commerce Uplift Modeling'
title_zh: CanniUplift：缓解电商激励分配中商家与激励双重蚕食效应的 uplift 框架
authors:
- Zuwang He
- Shihao Shu
- Yuli Qu
- Hanyu Gao
- Ziliang Zhang
- Diwei Chen
- Xiangda Yan
- Buyu Gao
- Tanchao Zhu
- Yumeng Li
affiliations:
- Taobao & Tmall Group of Alibaba
arxiv_id: '2607.05242'
url: https://arxiv.org/abs/2607.05242
pdf_url: https://arxiv.org/pdf/2607.05242
published: '2026-07-06'
collected: '2026-07-07'
category: RecSys
direction: Uplift 建模 · 多源蚕食缓解
tags:
- uplift modeling
- cannibalization
- e-commerce
- personalized incentive
- SUTVA
- counterfactual
one_liner: 通过平台全局对齐和兑换分解去噪，解决电商 uplift 建模中的跨店替代与激励混合噪声问题
practical_value: '- **平台级全局对齐 (PGA) 可直用于多卖家营销场景**：在卖家级 uplift 模型上增加一个聚合平台 GMV 的约束头，训练时要求所有候选卖家的预测之和逼近用户真实平台总
  GMV，隐式捕捉跨店替代效应，缓解仅优化单店带来的“零和”增量。实现简单，可在现有 local uplift 模型上扩展。

  - **兑换分解去噪 (RDD) 显著净化 uplift 信号**：将处理方的结局拆分为“兑换路径”和“未兑换路径”，通过兑换概率加权融合，避免未兑换的有机转化被误归因为激励增量。该思路可用于含有兑换/核销环节的优惠券、满减活动，即使无兑换标签，也可通过类似分解减少伪增量。

  - **Treat-Attention 增强个性化激励表示**：用候选激励（店铺+券）作为 query 对用户行为序列做交叉注意力，生成候选级交互向量，更精细捕捉用户对不同激励的异质性响应。可迁移到广告、推荐场景的候选感知特征交互。

  - **Tweedie 损失适用于零膨胀长尾 GMV 预测**：直接建模 GMV 的复合分布（点质量+连续正值），相比 MSE 更稳定，适合电商 GMV、转化金额等变量的
  uplift 预估。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统 uplift 模型依赖 SUTVA 假设，即一个用户的处理不影响其他用户结局。在电商多卖家场景下，该假设常被违反：**卖家级蚕食**表现为给某店发券，用户从另一高价店转到低价店，平台总 GMV 反而下降；**激励级蚕食**指用户持有更高值券，即便领测试券也不核销，但仍被误归因为增量。现有局部卖家 uplift 模型会高估约 35% 的平台增量，近 25% 的领券后转化无实际核销，造成严重噪声。亟需一个能同时缓解两类蚕食的框架。

### 方法关键点
- **平台全局对齐 (PGA)**：在 EUEN 等 local uplift 结构上增加一个平台头，强制所有候选卖家预测的 GMV 之和逼近用户真实平台总 GMV。通过累加一致性损失，促使模型隐式学习跨店替代关系，抑制伪增量。
- **兑换分解去噪 (RDD)**：利用兑换标签，将处理方 GMV 拆分为“兑换路径”和“未兑换路径”两个增量，并由 Redem 头预测的兑换概率加权融合。这遵循 Entire-Space 多任务设计，避免未兑换的转化被错误归因。
- **Treat-Attention 交互编码**：将候选激励（店铺+券属性）作为 Query 对用户行为序列做交叉注意力，生成候选级表示，精细刻画用户对特定激励的敏感度。
- **Tweedie 损失**：针对 GMV 的零膨胀和长尾特性，使用 Tweedie 损失统一捕捉，提升训练稳定性和尾部建模效果。

### 关键结果
- **工业数据集**：PGA+RDD 将 seller AUUC 从 EUEN 的 0.744 提至 0.769，user AUUC 从 0.794 提至 0.849，QINI 也一致提升。
- **合成数据集**：仅 PGA 即可在受控 seller 蚕食下提升 seller AUUC（1.1596 vs 1.0940）和 user AUUC。
- **在线 A/B 测试**：相对生产基线，平台增量 GMV 提高 4.08%，营销成本降低 2.45%，ROI 提升 6.69%。
- **分析验证**：预测的蚕食率与用户近期浏览同品类高价商品数、同品类店铺数呈单调正相关；RDD 使无核销段的 uplift 高估降低约 7%。

> 最值得记住：**在卖家级 uplift 上叠加一个求和对齐的平台头，再配合兑换路径分解，能以极简方式缓解多源蚕食，让模型学会“不抢自己平台的生意”。**
