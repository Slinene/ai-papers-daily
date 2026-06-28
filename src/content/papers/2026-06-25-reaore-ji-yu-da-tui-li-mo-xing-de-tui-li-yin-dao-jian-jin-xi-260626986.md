---
title: 'ReaORE: Reasoning-Guided Progressive Open Relation Extraction Empowered by
  Large Reasoning Models'
title_zh: ReaORE：基于大推理模型的推理引导渐进式开放关系抽取
authors:
- Xin Lin
- Liang Zhang
- Guoqi Ma
- Hongyao Tu
- Jinsong Su
affiliations:
- National Institute for Data Science in Health and Medicine, Xiamen University
- School of Informatics, Xiamen University
arxiv_id: '2606.26986'
url: https://arxiv.org/abs/2606.26986
pdf_url: https://arxiv.org/pdf/2606.26986
published: '2026-06-25'
collected: '2026-06-28'
category: Reasoning
direction: LLM推理 · 开放关系抽取
tags:
- Open Relation Extraction
- Large Reasoning Models
- Progressive Reasoning
- Coarse-to-Fine
- Comparative Reasoning
one_liner: 提出由粗到细的渐进式推理框架，利用大推理模型先过滤再比较预测，提升开放关系抽取对易混淆关系的区分度。
practical_value: '- 在需要区分大量易混淆标签的场景（如电商商品属性关系抽取、用户评论情感细粒度分类），可借鉴“粗筛—精排”的渐进式推理策略：先用大模型生成候选标签集合，再通过细粒度比较推理精确判别。

  - 关系过滤阶段结合多角度推理（如语义、角色、上下文）和 embedding 相似度过滤，可迁移至搜索查询意图识别：先生成多个候选意图，再用相似度排除无关项，提高召回和准确率的平衡。

  - 细粒度比较推理的设计思想可用于优化推荐系统中的个性化解释生成：让模型比较多个候选理由后再输出最贴切的解释，减少模棱两可的输出。

  - 框架中利用大模型的强推理能力进行关系理解和假设，可启发在 Agent 系统中构建类似的“先思考、再检索、后判断”的流程，提高决策的可靠性。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：开放关系抽取（OpenRE）的核心挑战是对未知关系类型的泛化。现有方法要么采用聚类，无法生成关系标签且泛化差；要么用 LLM 直接生成，但缺乏足够判别力区分易混淆关系。
**方法**：提出 ReaORE 框架，通过“粗到精”的关系推理执行抽取。第一阶段**关系过滤**：利用大推理模型（LRM）从多个方面理解文本和关系实例，生成初始关系集；再通过基于 embedding 的相似度计算补充和过滤，确保目标关系被包含。第二阶段**关系预测**：从候选关系集中通过细粒度比较推理预测最终关系，显式对比候选关系以区分高度相似的关系。
**结果**：在两个广泛使用的 OpenRE 数据集上，ReaORE 超越了现有基线方法，尤其在易混淆关系上的区分能力显著提升。
