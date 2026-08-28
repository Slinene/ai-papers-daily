---
title: 'Beyond a Single Story: Meta-Reviewing Sparse and Incomplete User-generated
  Contents for Recommendation'
title_zh: 超越单一评论：稀疏不完整UGC的元评论推荐
authors:
- Hongren Wang
- Tianjun Wei
- Yingpeng Du
- Jie Zhang
- Yin-Leng Theng
affiliations:
- Nanyang Technological University, Singapore
arxiv_id: '2608.26728'
url: https://arxiv.org/abs/2608.26728
pdf_url: https://arxiv.org/pdf/2608.26728
published: '2026-08-27'
collected: '2026-08-28'
category: RecSys
direction: 评论增强推荐与属性级可解释性
tags:
- meta-review
- MMoE
- UGC sparsity
- explainable recommendation
- rating prediction
one_liner: 聚合邻居评论构建元评论，通过 MMoE 与个性化注意力缓解 UGC 稀疏性，提升评分预测与解释质量
practical_value: '- 借鉴 meta-review 聚合：电商中 UGC 评论稀疏的场景（用户少写评价、长尾商品评论少），可聚合相似用户/商品的评论文本，抽取属性-情感向量（如“物流快”“性价比高”）作为用户或商品表征补充，缓解冷启动与数据稀疏。

  - MMoE 多任务结构：联合优化主任务（点击/转化/评分预测）和属性情感预测，通过多专家网络与门控减少任务冲突，比简单共享底层更稳定；可迁移到推荐系统多目标学习（CTR
  + 解释生成 + 属性偏好）。

  - 个性化注意力聚合：不用全局平均的元评论，而用注意力按目标用户兴趣加权邻居评论，类似 user-based CF 但更细粒度，可在召回或排序前融合作为用户侧特征，增强个性化。

  - 属性级可解释性：输出面向属性的情感解释（如“房间干净、位置便利”），可用于电商推荐卡片、推荐理由展示或对话式推荐 Agent 的响应依据，提升用户信任和转化。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：UGC 评论包含细粒度偏好，但用户往往不写评论或只覆盖部分属性，造成缺失与不完整，使基于评论的推荐性能下降。

方法关键点：受学术同行评议中 meta-review 启发，为每个目标用户聚合邻居用户评论中的属性-情感证据，构建 meta-review；采用多门控专家混合（MMoE）联合优化评分预测与属性-情感预测，并用注意力模块依据目标用户偏好个性化加权聚合信号，最终输出更准确的评分和属性级解释。

关键结果数字：在四个真实数据集上，MOSAIC 在推荐准确率和解释质量上均优于先进基线，并在交互历史有限的用户上提供一致增益，缓解 UGC 稀疏和不完整。
