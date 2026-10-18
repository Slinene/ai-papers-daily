---
title: 'Bridging the Topological Divide: Dual-Branch Graph Distillation with Semantic
  Priors for Robust Cold-Start Recommendation'
title_zh: 桥接拓扑鸿沟：语义先验驱动的双分支图蒸馏用于鲁棒冷启动推荐
authors:
- Yuanfeng Qiu
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2610.19578'
url: https://arxiv.org/abs/2610.19578
pdf_url: https://arxiv.org/pdf/2610.19578
published: '2026-10-14'
collected: '2026-10-18'
category: RecSys
direction: 冷启动推荐 · 图知识蒸馏
tags:
- Cold-start Recommendation
- Graph Collaborative Filtering
- Knowledge Distillation
- Semantic Features
- Dual-Branch
one_liner: 双分支图知识蒸馏：教师端语义先验重塑流形，学生端余弦蒸馏跨模态对齐，冷启动显著提升
practical_value: '- 冷启动 item 的多模态语义特征不要直接拼进协同图或共享空间，建议解耦两阶段训练：先训练协同教师并用语义 prior 做平滑/初始化，再蒸馏到语义学生，避免破坏已有
  ID 协同信号。

  - 蒸馏损失用余弦相似度替代 MSE/点积，保持方向对齐、不强制匹配模长，更适合跨模态 embedding 迁移，且可减少对热物品向量尺度的扰动。

  - 线上全局检索时，对冷启动物品向量做 dynamic norm reconstruction，按冷/暖物品分桶校准模长，避免语义分支模长不一致导致内积排序偏差；可直接复用到新品召回。

  - 电商新品/广告冷启动可把“新品语义描述或图像”作为学生分支，老品协同教师蒸馏，发布即获得可检索表示；需评估两阶段训练的离线成本与更新频率。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：Graph Collaborative Filtering 在严格冷启动下，未交互 item 因拓扑隔离出现表示塌缩；直接注入多模态语义特征又容易引起表示退化和与协同信号的优化冲突。

**方法关键点**：DualGCN 采用解耦两阶段训练。第一阶段构建协同教师网络，item 表示由拓扑平滑的语义 prior 锚定，重塑潜在流形；第二阶段语义学生分支通过残差映射机制和幅值不敏感的 cosine 蒸馏目标，实现高保真跨模态对齐，避免扰动既有协同表示。同时引入 dynamic norm reconstruction 机制，校准 novel 与 warm item 的物理尺度，支撑全局检索。

**结果**：在三个真实世界基准数据集上，DualGCN 在严格冷启动场景显著超越 SOTA，同时保持高活跃物品的推荐精度。
