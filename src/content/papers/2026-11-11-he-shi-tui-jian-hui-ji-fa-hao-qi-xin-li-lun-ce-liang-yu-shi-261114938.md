---
title: When Does a Recommendation Spark Curiosity? Theory, Measurement, and Field
  Evidence
title_zh: 何时推荐会激发好奇心？理论、测量与实地证据
authors:
- Pan Li
- Alexander Tuzhilin
affiliations:
- Scheller College of Business, Georgia Tech
- Stern School of Business, New York University
arxiv_id: '2611.14938'
url: https://arxiv.org/abs/2611.14938
pdf_url: https://arxiv.org/pdf/2611.14938
published: '2026-11-11'
collected: '2026-11-13'
category: RecSys
direction: 推荐系统好奇心度量与效用融合
tags:
- curiosity
- information-gap theory
- recommendation
- utility function
- online experiment
- metric
one_liner: 提出可计算的好奇心度量并融入推荐目标，在离线与线上实验中显著提升用户参与。
practical_value: '- 好奇心分数可作为 relevance 之外的第二目标，通过线性标量化 V=(1-α)*relevance + α*w*C 接入现有排序/重排流程，无需重构模型；α
  作为平台策略参数可以调节探索强度。

  - 三组件（信息缺口 g、周围上下文 f、参考缺口 τ）的计算可以复用：item 用 AutoEncoder 得到 latent，用户状态用 GRU 序列编码，g
  用欧氏距离，f 用高斯核在历史物品上累加并饱和映射，τ 用指数衰减加权近期 gap；全部依赖行为数据，无显式反馈。

  - 好奇心峰值由 τ(1-f) 决定，对高上下文用户用小 gap 更有效，对近期接触大 gap 的用户用大 gap 更有效。这提示在电商/短视频中，对熟悉品类用户可推荐「细分差异」而非完全陌生内容，对近期跨品类用户可加大探索幅度，避免纯
  novelty 的无效推荐。

  - 在线实验显示提升随历史深度与近期活跃度增大，建议先向重度用户/近活跃用户灰度好奇心策略，可能获得更高边际收益。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
数字平台用户不仅被喜欢驱动，也被好奇心驱动；好奇心可以打破 filter bubble、延长参与。信息缺口理论指出好奇心来自个体感知的知识缺口，但缺少可计算的度量；现有 unexpectedness、variety-seeking、Wundt-curve 等 proxy 无法区分相同距离但不同知识背景的物品。

## 方法关键点
- 定义三元组 (g, f, τ)：g 信息缺口 = 用户状态与物品在共享隐空间中的距离；f 周围上下文 = 用户历史中靠近该物品的加权饱和和；τ 参考缺口 = 用户近期经历 gap 的指数衰减均值。
- 从信息缺口理论提出五条公理（Gap Relativity、Perceivability、Context-Dependent Optimum、Reference-Gap Tracking、Recency Adaptivity），推导出 canonical 形式 C = f * exp(-(g - τ(1-f))^2 / (2σ^2))，峰值随 f 减小、随 τ 增大。
- 工程实现：AutoEncoder 学 item embedding，GRU 学用户状态；欧氏距离算 g，高斯核 + 饱和映射算 f，指数衰减算 τ。
- 推荐融合：V = (1-α)*relevance + α*w*C，任何 relevance 模型均可作为第一项，w 为用户好奇心响应系数。

## 关键实验
- 调查验证：300 名参与者，283 有效，4,245 样本；C 与 self-reported curiosity 相关系数 r=0.598 (computed) / 0.636 (designed)，显著高于 unexpectedness 等 proxy；回归中加入 C 增量 R²=0.243。
- 离线三数据集 Yelp、MovieLens、Alibaba-Youku，以 DIN 和 MF 为基础，对比 unexpectedness、variety-seeking、PCC、MMR、DPP；好奇心方法在所有指标上显著最优，例如 Yelp DIN HR@10 从 0.409 到 0.512，MovieLens 从 0.422 到 0.495，阿里 Youku 从 0.113 到 0.216。
- 在线大型亚洲视频平台对照实验：显著提升 CTR、视频浏览量、时长；效果随历史深度和近期活跃度增加而放大，已部署生产。

## 最值得记住的一句话
好奇心不是 novelty/unexpectedness，需要部分知识才能感知缺口；峰值由 τ(1-f) 决定，随周围上下文增大而左移、随参考缺口增大而右移。
