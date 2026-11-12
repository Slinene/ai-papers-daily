---
title: 'INTENT: Out-of-Sample, Out-of-Time, and Cold-Start Evaluation on User Event
  Sequences'
title_zh: INTENT：用户事件序列的分布外、跨时间与冷启动评估
authors:
- Mattias Kvist
- Erik Lidman Hillbom
- Edoardo de Cal
- Davis Siemens
- Adam Fredriksson
- Rickard Brüel-Gabrielsson
affiliations:
- KTH AI Society
- Unbox AI
- MIT
arxiv_id: '2611.13069'
url: https://arxiv.org/abs/2611.13069
pdf_url: https://arxiv.org/pdf/2611.13069
published: '2026-11-09'
collected: '2026-11-12'
category: Eval
direction: 序列推荐评估 · 时间泛化与冷启动
tags:
- evaluation benchmark
- user event sequences
- out-of-time
- cold-start
- next-action prediction
- sequence recommendation
one_liner: 提出 INTENT 基准，按用户、时段、物品是否在训练中划分七个评估单元，揭示序列模型在不同单元的表现差异
practical_value: '- 离线评估序列模型时，不要只用 last-item holdout，应显式划分用户/时段/物品的新旧组合，否则会高估模型在未来真实场景的泛化能力。

  - 业务中物品冷启动很常见，可参考 INTENT 的 cell 划分，单独报告新物品（cold-start）指标，避免复杂模型在新物品上得零分被平均指标掩盖。

  - 把“重复用户最后物品”作为无参数 baseline 加入评估：如果复杂模型在新物品上打不过这个简单规则，说明特征或训练目标需要重新设计。

  - 工业界序列数据集必须保留真实事件时间戳，否则无法构建有效的 temporal split；INTENT 对 59 个数据集家族的审计显示缺少时间戳是最常见缺陷。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：银行等机构在用户事件序列上训练基础模型，部署时需预测未来，常遇到训练中未见过的用户、时段和物品，但公开基准很少测试模型未见过的时段，推荐研究也多用 last-item holdout，无法反映真实分布外与冷启动性能。

**方法**：提出 INTENT 基准，按用户、时段、目标物品是否出现在训练中划分七个评估单元。审计 59 个公共数据集家族，仅保留 5 个含日历时间戳的数据集，每个按固定规则切分 cutoff，确保评估可重复。

**关键结果**：参考结果中，transformer 在 cutoff 后已见物品上领先，但在新物品上得分为零；嵌入物品元数据的变体主要在 MicroLens 上带来提升；重复用户最后物品的无参数 baseline 在五个数据集中的四个新物品单元上领先，且表明三个数据集上 cutoff 后得分下降主要由用户行为变化而非模型退化造成。
