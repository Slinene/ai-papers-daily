---
title: 'Balancing Trial and Reorder: A Hybrid Sequential Transformer-GBDT Ranker for
  On-Demand Delivery'
title_zh: 平衡试新与复购：按需配送场景的混合序列Transformer-GBDT排序器
authors:
- Marcel Kurovski
- Attila Nagy
- Steffen Klempau
- Aleksandr Fedintsev
affiliations:
- Wolt (DoorDash, Inc.)
arxiv_id: '2609.16407'
url: https://arxiv.org/abs/2609.16407
pdf_url: https://arxiv.org/pdf/2609.16407
published: '2026-09-14'
collected: '2026-09-16'
category: RecSys
direction: 排序模型 · 序列推荐 · 混合架构
tags:
- Sequential Recommendation
- Learning to Rank
- GBDT
- Transformer
- Trial vs Reorder
- Production System
one_liner: 生产级统一排序器UVR结合双向Transformer序列编码与GBDT，通过标签平滑和试新偏置采样提升商家试新率
practical_value: '- 混合架构值得借鉴：用双向 Transformer encoder 学习用户序列并输出 embedding，作为特征输入 GBDT
  ranker，兼顾序列建模能力与 GBDT 对表格特征、业务规则（局部配送约束）的处理便利性，适合需要快速迭代和可解释性的工业排序场景。

  - 试新/复购权衡的调参 trick：通过 trial-biased sample weighting（提高试新样本权重）和 label smoothing 引导模型推荐新商家，同时离线监控
  reorder MRR 的退化，在线用融合指标 Global CVR 兜底，可在电商新品冷启动或类目探索中复用。

  - 跨域统一排序模型：将餐厅和零售四个独立模型合并为一个 UVR，共享用户序列表示，不仅提升试新率还简化 serving stack，减少多模型维护成本，适合多业务线推荐系统整合。

  - 离线/在线指标拆分：离线分别评估 trial MRR 和 reorder MRR，发现试新提升伴随复购下降，但在线核心指标稳定；建议业务中定义融合指标并分层监控，避免单一离线指标误导。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：按需配送平台的店铺排序受本地可用性、实时配送约束，核心张力在于提升新店铺试新率与保持复购会话排序质量。Wolt 原有四个独立排序模型（三个餐厅、一个零售），难以统一优化。

**方法关键点**：提出 Universal Venue Ranker (UVR)，采用双向 Transformer 编码器建模用户历史序列，输出序列表示作为特征，与上下文、用户、店铺特征一起输入 GBDT ranker；跨国家、跨领域联合训练，推理时强制局部配送约束。为引导模型推荐新店铺，引入 label smoothing 和 trial-biased sample weighting，提高试新样本在 loss 中的权重。

**关键结果**：离线 trial MRR 相对生产提升 +12% 至 +30%，但 reorder MRR 在六个国家中有五个出现下降；在线核心指标 Global CVR（融合试新与复购）保持统计不显著变化。三次线上 A/B 验证：V1 带来 +5.5% Merchant Trial Rate 和 +0.16% Global CVR；V2 额外 +0.45% Merchant Trial Rate；V3 跨域统一餐厅与零售模型，额外 +1.31% Retail Merchant Trial Rate，同时带来显著 gross order value 增量并大幅简化服务栈。
