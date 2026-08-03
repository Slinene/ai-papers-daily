---
title: 'Beyond Retrieval: Analytic Memory for Multimodal Agents'
title_zh: 超越检索：多模态智能体的分析记忆框架
authors:
- Zhoujin Tian
- Yao Tian
- Hao Zhang
- Cheng Chen
- Yakun Li
- Lei Zhang
- Xiaofang Zhou
affiliations:
- HKUST
- ByteDance
arxiv_id: '2607.29440'
url: https://arxiv.org/abs/2607.29440
pdf_url: https://arxiv.org/pdf/2607.29440
published: '2026-07-31'
collected: '2026-08-03'
category: Agent
direction: 多模态Agent记忆 · 结构化分析访问
tags:
- multimodal memory
- analytic memory
- agent systems
- attribute-value extraction
- query decomposition
one_liner: 提出分析记忆，将多模态交互历史结构化为可查询表以支持过滤、聚合等分析运算
practical_value: '- 对话式推荐/电商助手中，用户长期交互（对话、图片、购买记录）可自动提取为结构化属性对（偏好、行为），构建动态分析视图，答导购询问（如“上个月买的最贵的商品”）

  - 记忆感知规划器的“分解-路由”模式可直接用于推荐Agent：将复杂用户查询拆解为检索部分（召回相关物品/历史）与分析部分（聚合、排名、时间对比），再交给对应工具，提升多步推理准确性

  - 物化分析表的设计思想可落地为实时特征工程：从流式多模态日志中自动发现重复字段并固化，为推荐模型提供交互聚合特征

  - 工程上，可借鉴属性值提取的出处链接机制，让分析结果可解释、可溯源，增强用户信任与调试效率'
score: 7
source: arxiv-cs.AI
depth: abstract
---

动机：智能体长期交互积累海量多模态历史（对话、图像、文档），传统记忆只做线性摘要与检索，无法回答“过去一周平均每天买了几杯咖啡”这类需要聚合计算的问题。

方法关键点：
1. 将“分析记忆”形式化为支持过滤、聚合、排名、时间比较的查询结构，与检索记忆互补。
2. AdaMM自动从多模态交互中提取属性-值对，关联原始出处，发现重复出现的字段结构，并将其物化为结构化表。
3. 推理时，记忆感知规划器接收用户查询，分解为检索操作与分析操作，并路由到相应工具执行。

关键结果：在MemEye和MemGallery两个长期多模态记忆基准上，AdaMM将问答性能分别提升最高11.3%和7.3%，证明分析记忆能显著增强智能体对历史信息的计算能力。
