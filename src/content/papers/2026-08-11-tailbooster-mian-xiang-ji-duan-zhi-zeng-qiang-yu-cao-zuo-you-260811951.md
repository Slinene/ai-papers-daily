---
title: 'TailBooster: A Dual-Layer Generative Framework for Extreme Value Augmentation
  with Operational Validity Enforcement'
title_zh: TailBooster：面向极端值增强与操作有效性约束的双层生成框架
authors:
- Karim Aly
- Alexei Sharpanskykh
- Jacco Hoekstra
affiliations:
- Delft University of Technology
arxiv_id: '2608.11951'
url: https://arxiv.org/abs/2608.11951
pdf_url: https://arxiv.org/pdf/2608.11951
published: '2026-08-11'
collected: '2026-08-15'
category: Training
direction: 生成式数据增强 · 极端事件预测
tags:
- Generative Data Augmentation
- Tail Augmentation
- Tabular VAE
- Anomaly Detection
- Operational Validity
- Imbalanced Regression
one_liner: 提出 TailBooster 双层框架，用 IQR 提取尾部训练生成模型，再用自编码器清洗，保证合成样本操作可行，极端预测 MAE 降低 47-57%
practical_value: '- 对长尾/极端样本单独建模：可用 IQR 或业务阈值从历史中切出极端样本（大促流量峰值、黑产攻击、异常转化、长尾物品冷启动），仅用这些样本训练专用生成模型（如
  Tabular VAE），比全量数据训练 GAN/VAE 更能生成高质量尾部样本。

  - 生成后加可行性过滤层：在生成器后接一个自编码器，用重建误差作为操作包络，自动剔除不符合历史数据约束的合成样本；无需手工规则即可过滤不合逻辑组合（如超低价格与高成本、短浏览时长与高转化）。

  - 评估增强效果直接看下游 MAE：不只评估分布相似性，而是把合成样本加入训练集，观察对极端值预测 MAE 的改善；在推荐/广告系统中可对极端延迟、极端转化等目标做类似回归评估。

  - 方法模型无关、数据驱动：不依赖特定生成模型或下游模型，可嵌入现有 pipeline；在缺乏明确业务规则的场景下尤其适用。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：航空运输中的极端事件（严重到达延误、异常飞行时间）在历史记录中稀少，常规生成模型会低估分布尾部，且可能生成操作上不可行的样本（如短飞行时间配长距离）。现有方法无法同时解决混合类型表格数据的尾部低估与操作可行性问题。

**方法关键点**：提出 TailBooster，一个双层生成框架。统计层使用 IQR 提取极端样本，作为尾部集中的训练信号，训练专用生成模型（论文中为 Tabular VAE）。深度学习层应用自编码器进行清洗，基于历史数据学习操作包络，丢弃违反该包络的合成记录。评估覆盖五个维度：多样性、统计相似性、保真度、操作有效性、实用性，后两者是主要改进目标。

**关键结果**：在 US 航班记录上，数据驱动清洗显著提升操作有效性，定向增强提升极端事件预测实用性。与常规合成数据相比，六个回归算法训练后 MAE 降低 47-49%（极端飞行时间）和 29-57%（极端到达延误）；真实记录加入合成极端样本也有类似收益。框架完全数据驱动、模型无关，可推广到无领域规则的极端事件预测场景。
