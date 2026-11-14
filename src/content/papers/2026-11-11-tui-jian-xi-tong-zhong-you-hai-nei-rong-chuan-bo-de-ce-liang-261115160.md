---
title: Measuring, Revealing and Mitigating Harmful Content Propagation in Recommender
  Systems
title_zh: 推荐系统中有害内容传播的测量、揭示与缓解
authors:
- Xiaokun Zhang
- Youlin Wu
- Junyu Lu
- Jiamin Chen
- Zhaochun Ren
- Hongfei Lin
- Fenglong Ma
- Xue Liu
- Chen Ma
affiliations:
- City University of Hong Kong
arxiv_id: '2611.15160'
url: https://arxiv.org/abs/2611.15160
pdf_url: https://arxiv.org/pdf/2611.15160
published: '2026-11-11'
collected: '2026-11-14'
category: RecSys
direction: 推荐系统有害内容治理与缓解
tags:
- Harmful Content
- Recommender Systems
- Responsible AI
- Mitigation
- Evaluation Metrics
one_liner: 构建有害内容推荐基准并提出 MitiHarm 框架，在保持用户满意度同时显著抑制有害内容传播
practical_value: '- 内容安全评估体系：在推荐系统离线评估中引入 harmful exposure rate、harmful recall 等指标，监控模型对违规内容（如低俗、虚假、违禁品）的推荐概率，而不只看
  CTR 或转化率。

  - 多任务融合 harmful 信号：借鉴 MitiHarm，在用户和物品 embedding 学习中增加辅助任务（如内容有害性分类），通过共享表示或对抗训练降低模型对有害内容的偏好，同时主任务损失保证推荐性能。

  - 用户表示去偏：经验发现用户会自然点击有害内容，不能单纯依赖用户行为数据；可在用户塔加入对有害内容点击的惩罚权重，或构建 counterfactual 样本进行
  debias。

  - 线上干预：将 harmful 得分作为 ranking 阶段的一个特征或过滤阈值，结合业务规则动态调整，平衡内容安全与用户体验。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：推荐系统根据用户历史行为过滤信息，决定用户看到什么，但现有方法只优化用户兴趣，忽视有害内容（暴力、仇恨言论、色情等）的传播，可能导致有害信息被放大。

**方法关键点**：
1. 构建带有伤害性标注的数据集，并提出新的评估指标量化推荐结果的伤害程度。
2. 通过实证分析揭示两个关键现象：用户倾向于与有害内容互动；主流推荐算法（如协同过滤、深度模型）会加剧有害内容的扩散。
3. 提出通用缓解框架 **MitiHarm**，将伤害性信号整合到物品和用户表示学习中（例如通过多任务学习或约束损失），在不牺牲推荐质量的前提下降低有害内容曝光。

**关键结果**：实验表明 MitiHarm 能显著降低推荐列表中的有害内容占比，同时保持用户满意度（如点击率等指标）基本不下降。资源已开源。
