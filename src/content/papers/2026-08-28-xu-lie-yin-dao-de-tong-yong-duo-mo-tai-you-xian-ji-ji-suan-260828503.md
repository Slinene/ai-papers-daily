---
title: 'SG-UMP: Sequence-Guided Universal Multimodal Prioritization Calculation Framework'
title_zh: 序列引导的通用多模态优先级计算框架 SG-UMP
authors:
- Xinyi Zhang
- Yutong Li
- Peijie Sun
affiliations:
- Imperial College London
- University College London
- Nanjing University of Posts and Telecommunications
arxiv_id: '2608.28503'
url: https://arxiv.org/abs/2608.28503
pdf_url: https://arxiv.org/pdf/2608.28503
published: '2026-08-28'
collected: '2026-08-31'
category: RecSys
direction: 多模态序列推荐 · 动态模块路由
tags:
- Multimodal Sequential Recommendation
- Module Routing
- User Modeling
- Dataset-aware
- Plug-and-play
one_liner: 即插即用插件 SG-UMP，用模块组合器与模块路由器动态调整多模态处理顺序，适配用户偏好与数据集偏差
practical_value: '- 多模态融合从静态拼接/固定权重升级为用户级+数据集级动态路由：在电商推荐中，不同类目对模态敏感度差异大（美妆看图片、家电看参数文本），可借鉴
  Module Router 根据用户最近行为序列自动调整图像/文本/属性特征的组合顺序与权重，替代全局统一方案。

  - 插件式设计不改动主模型 backbone：SG-UMP 作为 drop-in 插件，能低成本接入已有精排/召回模型，在结构基本不变的情况下提升多模态信息利用效率，适合快速实验与
  A/B 测试。

  - 把“哪个模态先处理”建模为可学习路由问题：相比注意力加权，模块顺序路由更显式控制信息流，在搜索推荐系统里可用于决定商品标题、主图、用户评论等在特征编码中的处理次序，提升可解释性。

  - 关注数据集级模态偏差：电商不同场景（首页猜你喜欢 vs 搜索）模态贡献差异大，学习 dataset-aware 路由策略可以避免一套权重打天下，方便跨场景迁移。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：多模态序列推荐（MSR）整合文本、图片和行为，但现有方法常忽略用户级偏好异质性和数据集级模态偏差，导致同一套多模态处理方式难以适配不同用户和不同数据分布。

**方法关键点**：SG-UMP 是一个即插即用插件，包含两类核心组件：Module Combiner 提供灵活的多模态模块组合能力；Module Router 基于用户行为序列动态计算各模块的优先级并决定执行顺序。序列引导的路由既能捕捉用户对模态的偏好，也能感知数据集特征，从而调整多模态信息编码路径。该框架不改变原有推荐模型 backbone，可插入不同序列推荐模型中使用。

**关键结果**：在四个真实世界数据集上，SG-UMP 在不同 backbone 和多模态设置下均带来一致的推荐性能提升。
