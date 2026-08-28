---
title: 'Stageboost: Recommending Signals Based on Counterfactual Estimation'
title_zh: Stageboost：基于反事实估计的商品详情页信号推荐模型
authors:
- Darpan Singhal
- Matan Mandelbrod
- Tal Franji
- Manasa Kolla
- Vipul Gaba
- Yuri Brovman
affiliations:
- eBay India
- eBay Israel
- eBay USA
arxiv_id: '2608.27366'
url: https://arxiv.org/abs/2608.27366
pdf_url: https://arxiv.org/pdf/2608.27366
published: '2026-08-27'
collected: '2026-08-28'
category: RecSys
direction: 电商信号推荐 · 反事实估计
tags:
- Signals
- Counterfactual
- XGBoost
- Conversion
- Recommendation
- eBay
one_liner: eBay利用两阶段XGBoost反事实估计在商品详情页优化信号展示，GMB提升0.08%
practical_value: '- 借鉴反事实估计校正信号展示偏差：记录信号曝光与转化数据，用IPW/DR等方法估计每个信号对转化的因果增益，而非简单看CTR，避免位置偏差误导。

  - 两阶段解耦价值评估与组合优化：先独立预测信号收益，再在placement容量约束（如Urgency最多1个，Conversational最多2个）下求最优组合，提升可解释性和工程可控性。

  - 对高客单价商品强化信号推荐：实验表明高平均价格商品转化提升显著，可针对此类商品增强信任/紧迫感类信号（如库存、退货政策）的投放。

  - 工程上采用XGBoost，训练快、可解释，适合电商大规模候选信号的线上快速迭代。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：eBay商品详情页(VI)每天数亿访问，页面上的短文本/视觉信号（如“仅剩1件”“免费退货”）能显著影响购买决策。但现有信号展示方式缺乏全局优化，转化提升有限。

**方法关键点**：提出Stageboost，采用两阶段XGBoost模型。第一阶段利用反事实估计，从历史数据中学习不同信号在特定placement上对转化的因果增益，校正展示偏差；第二阶段在placement容量约束（Urgency最多1个，Conversational最多2个，共3个信号）下，求解最优信号组合。

**关键结果**：线上A/B实验显示，整体GMB提升0.08%，Parts and Accessories品类GMB提升0.58%，主要归因于高平均价格商品的转化率提升。
