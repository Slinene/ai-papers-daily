---
title: 'FactorJEPA: Factorizing Monolithic Futures into Layout-Agent-Interaction Channels
  for Crowded and Chaotic Global South Urban Worlds'
title_zh: FactorJEPA：将单一未来分解为布局-实体-交互通道，用于拥挤南半球城市场景预测
authors:
- Kapil Wanaskar
- Gaytri Jena
- Aman Chadha
- Vinija Jain
- Vasu Sharma
- Amitava Das
affiliations:
- San Jose State University
- UC Berkeley
- Apple
- Meta
- PocketFM
- BITS Pilani Goa
arxiv_id: '2608.01049'
url: https://arxiv.org/abs/2608.01049
pdf_url: https://arxiv.org/pdf/2608.01049
published: '2026-08-01'
collected: '2026-08-08'
category: Other
direction: 世界模型 · 多模态动态预测
tags:
- World Model
- JEPA
- Multi-Agent
- DENSEWORLD
- Factorized Prediction
- Global South
one_liner: 将世界模型预测分解为布局、实体、交互三个因子，在拥挤南半球城市场景中显著提升预测精度与鲁棒性
practical_value: '- 世界模型与电商/推荐业务距离较远，直接迁移价值有限

  - 将复杂动态系统显式分解为场景布局、实体状态、交互关系的思路，可启发推荐系统中对用户状态、物品属性、交互关系的分离建模

  - 使用 visibility gate 处理部分可观测（如用户行为缺失、冷启动）的设计，在序列推荐或 Agent 交互建模中有参考意义

  - 提供大规模多样性数据集构建方法（覆盖22城市、多天气、混杂交通），对需要构建多域推荐数据集的团队有一定借鉴'
score: 6
source: huggingface-daily
depth: abstract
---

**动机：** 现有世界模型（如 JEPA）主要在结构化、低密度交通场景下评估，难以应对南半球城市普遍存在的拥挤、混乱、边界模糊、高度代理异质性和严重遮挡等挑战。为此，作者构建了 DENSEWORLD-115k，一个覆盖22个城市、1000小时多视角视频的大规模数据集，并揭示现有方法在保留密集交互动态上的不足。

**方法：** 提出 FactorJEPA，将未来表示从单一潜变量分解为布局（场景结构）、实体（每个代理状态）和交互（代理间关系）三个因子。引入可见性门控（visibility gate）独立预测每个实体的可见性，并通过分离的子空间编码不同因子，阻止跨因子的预测捷径。该设计使模型在高度混乱场景下仍能保持对被遮挡或弱势代理的感知。

**关键结果：** FactorJEPA 在 Future-frame L1、Causal L1、Mask-ratio slope 三项指标上均显著优于基线；同时揭示了运动信息与潜表示质量之间的可重现权衡（Motion cosine）。方法排名在 2B 和 1B V-JEPA 2.1 骨干网上高度一致（ρ = 0.895–0.978）。数据集与模型均开源。
