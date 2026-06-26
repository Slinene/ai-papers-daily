---
title: 'TRUST: Item-Calibrated Interval Evidence for Temporal Session-Based Recommendation'
title_zh: 面向时序会话推荐的物品校准间隔证据
authors:
- Linjiang Guo
- Nitin Bisht
- Shiqing Wu
- Yifan Yin
- Guandong Xu
arxiv_id: '2606.27214'
url: https://arxiv.org/abs/2606.27214
pdf_url: https://arxiv.org/pdf/2606.27214
published: '2026-06-25'
collected: '2026-06-26'
category: RecSys
direction: 时序会话推荐 · 物品校准时间感知
tags:
- Temporal Session-Based Recommendation
- Item Calibration
- Interval Scoring
- Graph Neural Networks
- Plug-and-Play
one_liner: 揭示相同时间间隔在不同物品上代表不同兴趣强度，提出物品校准的间隔评分函数，即插即用提升时序会话推荐
practical_value: '- 核心trick：不以全局分布看待时间间隔，而是按物品建立各自的间隔分布，用该分布校准当前间隔的“兴趣证据”强度，可迁移到电商用户实时行为序列建模。

  - 架构可插拔：提出的评分函数是模型无关的，可嵌入现有基于图或序列的会话推荐模型中，用于邻居采样权重、图传播或兴趣聚合，适合快速实验验证。

  - 工程实现：只需预计算每个物品的间隔分布（如均值/std或分位数），在线时计算当前间隔的相对位置，轻量级，适合低延迟推荐场景。

  - 业务洞察：电商中不同品类/商品的生命周期和消费节奏差异大，用统一时间衰减或窗口会损失信息，物品校准的思路可推广到其他时间敏感特征（如商品浏览时长、购买周期）。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：现有时序会话推荐模型通常使用绝对时间间隔值，并假设相同间隔在所有物品上表达相似的用户兴趣强度。但作者通过数据分析发现这一假设不成立——不同物品的交互时间节奏差异显著，同一绝对间隔对快消品可能表示高兴趣，对耐用品可能表示兴趣不足。因此需要根据物品自身的历史间隔分布来校准时间信号。

方法：论文提出 TRUST 框架，核心是一个物品校准的间隔评分函数。对于每个交互间隔，计算其在对应物品历史间隔分布中的相对位置（如百分位或标准化得分），得到“物品校准的间隔证据”。该评分被注入三个关键组件：全局邻居采样（根据时间证据强度调整采样权重）、会话图编码（在图传播中用评分调节边权重）、最终兴趣聚合（用评分加权聚合物品表征以生成推荐）。框架可以端到端训练，且评分函数可剥离作为插件。

结果：在多个公开数据集上，TRUST 在 Hit@K、MRR 等指标上一致超越多种时序和非时序基线。插件实验进一步显示，将该评分函数嵌入到现有模型（如 T-GCN、NARM）中能带来显著提升。消融实验证实，在各个组件中校准时间信号比直接移除该组件效果更好，验证了时间校准的效用。
