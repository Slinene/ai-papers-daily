---
title: 'From Atomic Evidence to Logical Composition: Structured Compositional Reasoning
  over Compound Answer Options'
title_zh: 从原子证据到逻辑组合：复合答案选项的结构化组合推理
authors:
- Obed Junias
- Maria Leonor Pacheco
affiliations:
- University of Colorado Boulder
arxiv_id: '2608.12836'
url: https://arxiv.org/abs/2608.12836
pdf_url: https://arxiv.org/pdf/2608.12836
published: '2026-08-12'
collected: '2026-08-15'
category: Reasoning
direction: LLM 结构化组合逻辑推理
tags:
- LLM
- Logical Reasoning
- Compositional Reasoning
- Integer Linear Programming
- MCQ
- Calibration
one_liner: 将复合选项分解为原子判断并用整数规划组合，大幅提升 LLM 在 AND/OR/NEITHER-NOR 逻辑题上的表现
practical_value: '- 在电商搜索/推荐中，用户 query 常隐含 AND/OR/NOT 组合（如“红色且不是羽绒服”），可直接借鉴本框架：先对每个原子条件独立打分，再用约束求解器组合，避免让
  LLM 直接处理复合条件。

  - 对 Agent 决策中的规则匹配（如同时满足多个商品属性、排除某些类目），可将复合条件拆成原子判断，分别用对比假设校准每个原子，然后用整数规划做最终决策，提升逻辑一致性。

  - 对于多条件排序/召回场景，可以在召回后增加一层逻辑组合重排：用 LLM 对单个条件打分，再用 ILP 约束组合，替代直接让模型输出复合判断，减少 NEITHER/NOR
  类负向组合的错误。

  - 该工作证明了“分解-校准-组合”的范式在逻辑推理上的有效性，可用于构建电商问答中复合查询的理解模块，尤其是需要处理排他性条件时。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：LLM 在需要组合原子判断的 MCQ 选项上表现不佳，且错误模式与逻辑运算符高度相关：AND 尚可，OR 变弱，NEITHER/NOR 崩溃。这种与运算符相关的失败表明问题出自逻辑可能性的表征与组合方式，而不是知识缺失。

**方法关键点**：
- 将每个复合选项分解为多个原子答案，对每个原子分别评分，模型从未看到复合选项本身。
- 对每个原子采用对比假设打分：分别评估其为真和为假的证据，再校准为概率。
- 用一个 operator-constrained integer linear program（ILP）根据逻辑运算符约束组合各原子的校准分数，得到整个选项的最终判断。

**关键结果**：
- 在 human-validated LOGICAL-COMMONSENSEQA split 上，Macro-F1 从 48.3 提升到 77.0。
- 在自建 LOGICAL-SATA 阅读理解 benchmark 上，Macro-F1 从 47.0 提升到 75.6。
- 最大的增益出现在 NEITHER/NOR 类选项上，证实了分解-组合策略对负向逻辑的修复作用。
