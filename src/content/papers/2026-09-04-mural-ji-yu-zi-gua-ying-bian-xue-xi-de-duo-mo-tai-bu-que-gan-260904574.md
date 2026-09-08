---
title: 'MURAL: Multimodal Uncertainty-aware Recommendation via Adaptive edge Learning'
title_zh: MURAL：基于自适应边学习的多模态不确定性感知推荐
authors:
- Ahmad Mousavi
- Majid Alikhani
- Yeon-Chang Lee
- Roberto Corizzo
- Yeganeh Abdollahinejad
affiliations:
- American University
- Ulsan National Institute of Science and Technology
- Michigan State University
arxiv_id: '2609.04574'
url: https://arxiv.org/abs/2609.04574
pdf_url: https://arxiv.org/pdf/2609.04574
published: '2026-09-04'
collected: '2026-09-08'
category: RecSys
direction: 多模态推荐 · 动态图与不确定性融合
tags:
- Multimodal
- GNN
- Uncertainty
- Adaptive Edge
- Recommendation
one_liner: 用动态自适应边学习和不确定性感知融合，解决多模态推荐静态图与噪声融合瓶颈
practical_value: '- 动态边学习替代静态 item-item 相似图：推荐系统里用可微检索 + ANN 实时构建 item 图，能跟随用户行为变化，O(N
  log N) 复杂度适合大规模商品库。

  - 不确定性感知多模态融合：对商品标题、图片、视频等模态建模 aleatoric uncertainty，动态降低噪声模态权重，在 UGC 素材质量参差时提升稳定性。

  - Teacher-student 对齐到行为信号：将多模态表征蒸馏到协同过滤表征，用点击/购买等行为 anchor 做对比学习，避免模态噪声破坏协同信号。

  - 鲁棒性与可解释性：在数据缺失/损坏场景下有效；通过模态权重可解释垂直域依赖，如时尚重图、电子重文本，便于业务沉淀特征优先级。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：多模态图神经网络推荐通常依赖静态预计算相似图，结构僵化，不能随偏好演变；同时多模态信号不加区分融合，噪声会污染协同信号。

方法关键点：
- 提出 MURAL，将多模态推荐从固定结构增强转向动态拓扑发现。
- Adaptive Edge Learner：可微检索增强策略 + 近似最近邻搜索，动态挖掘语义自适应的 item-item 关联，复杂度 O(N log N)。
- Uncertainty-Aware Fusion：对异构模态的 aleatoric uncertainty 建模，动态降低不可靠特征权重，优先高置信信号，防御跨模态噪声。
- 对比 teacher-student 对齐：把模态特定表征锚定到稳定行为信号，保证优化稳定、防梯度泄漏。

关键结果：在 TikTok、Amazon 大规模基准上，显著超过结构类和生成式 SOTA；在准确率、极端数据损坏鲁棒性、模态主导可解释性方面均占优。
