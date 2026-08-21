---
title: 'Manifold Drift in Flow Preference Optimization: A Root Cause of Reward Hacking'
title_zh: 流匹配偏好优化中的流形漂移：奖励黑客的一个根因
authors:
- Yansen Han
- Shengyi Liao
- Yuanxing Zhang
- Pengfei Wan
- Tao Lin
affiliations:
- Westlake University
- Zhejiang University
- Kling Team, Kuaishou Technology
arxiv_id: '2608.20011'
url: https://arxiv.org/abs/2608.20011
pdf_url: https://arxiv.org/pdf/2608.20011
published: '2026-08-20'
collected: '2026-08-21'
category: Training
direction: 流匹配偏好优化 · 奖励黑客
tags:
- Flow Matching
- Preference Optimization
- Reward Hacking
- Manifold Drift
- ThermoDPO
- Text-to-Image
one_liner: 提出 ThermoDPO 及加权变体，用偏好样本锚定缓解流匹配偏好优化中的流形漂移与奖励黑客
practical_value: '- 在生成式推荐、广告文案/商品图生成中若用 DPO/RLHF 做偏好对齐，需监控生成结果是否偏离原始数据流形（例如用重建误差或密度估计），否则
  reward 提升但真实质量和多样性可能下降，即 reward hacking。

  - ThermoDPO 的“偏好样本锚定 + 温度控制”思路可迁移：增加 winner-side anchor 项，等价于在 rejection sampling
  fine-tuning 与 DPO 之间插值，能控制偏离程度；温度低时信号减弱，可改用加权变体强化高分样本梯度。

  - 如果业务中有 flow matching 生成（商品图、创意素材），偏好更新会通过法向位移把终端样本推出预训练支持集，建议加入流形距离正则或重建代理项，保持生成内容的自然度和可编辑性。'
score: 7
source: arxiv-cs.CV
depth: abstract
---

## 动机
Flow matching 扩展偏好优化时，reward-driven update 会修改运输轨迹，但缺乏对预训练数据流形的约束，使终端样本偏离预训练支持集，造成奖励提升但质量下降的 reward hacking。论文将这一失效模式形式化为 manifold drift。

## 方法关键点
理论上证明：最优 flow matching 恢复终端数据分布；而偏好更新只要其诱导的终端位移存在非零法向分量，就会离开预训练流形。为此提出 ThermoDPO：一个温度控制目标，将成对偏好优化锚定在 preferred samples 上。不同温度下，该目标连接 rejection sampling fine-tuning 与 FlowDPO，并控制基于逐点重建的流形距离代理。进一步引入 ThermoDPO-weighted 变体，通过加权缓解低温度下信号衰减。

## 关键结果
在 toy benchmark 上，ThermoDPO-weighted 的 StrictScore 达 0.899，对比 FlowDPO 0.629、FlowDPO+RFT 0.857。在 SD3.5-M 的 CFG=4.5 设置下，OCR 指标提升 47.5%，四项指标均值提升 16.0%。
