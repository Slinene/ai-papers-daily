---
title: 'EntityBench: Towards Entity-Consistent Long-Range Multi-Shot Video Generation'
title_zh: EntityBench：面向实体一致性的长距离多镜头视频生成基准
authors:
- Ruozhen He
- Meng Wei
- Ziyan Yang
- Vicente Ordonez
affiliations:
- ByteDance
- Rice University
arxiv_id: '2605.15199'
url: https://arxiv.org/abs/2605.15199
pdf_url: https://arxiv.org/pdf/2605.15199
published: '2026-05-14'
collected: '2026-05-18'
category: Multimodal
direction: 多镜头视频生成 · 实体一致性评估
tags:
- Multi-Shot Video Generation
- Entity Consistency
- Benchmark
- Memory Augmentation
- Evaluation
- Visual Narrative
one_liner: 提出多镜头视频实体一致性基准 EntityBench 及记忆增强方法 EntityMem，显著提升跨镜头实体保真度
practical_value: '- 实体级一致性评估框架可迁移至商品图像/视频生成：拆解为属性、类别、外观等细粒度维度，配合 fidelity gate 过滤不合格生成再评分，避免低质量样本干扰评估。

  - 显式实体记忆库（pre-computed visual references）类似用户长期偏好向量存储，在生成式推荐中可维护商品或用户画像记忆，用于跨会话一致性生成（如个性化商品描述图的连贯性）。

  - 按实体间隔距离划分难度等级的思路适用于推荐系统长期行为一致性测试，例如构建用户跨 session 行为与兴趣保持的评测集。

  - 三支柱评估（片内质量、指令对齐、跨片一致性）可用于拆解推荐多阶段输出质量，分别优化即时点击、上下文连贯、跨 session 兴趣稳定。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：多镜头视频生成需要跨镜头保持人物、物体、地点等实体的一致性，但现有基准实体覆盖有限、评估简单，无法标准化对比。

**方法**：从真实叙事媒体构建 EntityBench 数据集（140 集，2491 镜头），按实体跨镜头重复间隔分为简单/中等/困难三级，最多追踪 13 个角色、8 个地点、22 个物体，间隔最长 48 镜头。配套三支柱评估：片内视觉质量、提示遵循对齐、跨镜头一致性，核心支柱通过嵌入相似度和 LLM 逐维度评判，且设有 fidelity gate 只对准确出现的实体评分。基线方法 EntityMem 在生成前规划并存储经验证的实体视觉参考到持久记忆库，生成时检索以保持一致性。

**结果**：现有方法跨镜头实体一致性随间隔距离急剧衰减；EntityMem 的角色保真度提升显著（Cohen's d = +2.33），实体存在率最高。
