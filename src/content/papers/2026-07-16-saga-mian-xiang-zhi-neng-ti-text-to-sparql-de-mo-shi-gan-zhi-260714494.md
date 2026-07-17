---
title: 'SAGA: Schema-Aware Grounding for Agentic Text-to-SPARQL Generation'
title_zh: SAGA：面向智能体 Text-to-SPARQL 的模式感知接地框架
authors:
- Yiming Zhang
- Koji Tsuda
affiliations:
- The University of Tokyo
- National Institute for Materials Science
- RIKEN Center for Advanced Intelligence Project
arxiv_id: '2607.14494'
url: https://arxiv.org/abs/2607.14494
pdf_url: https://arxiv.org/pdf/2607.14494
published: '2026-07-16'
collected: '2026-07-17'
category: Agent
direction: Agent 交互式 SPARQL 生成 · 模式感知接地
tags:
- Text-to-SPARQL
- KBQA
- Agent
- Schema-Aware
- Grounding
- LLM
one_liner: 提出 SAGA 训练无关框架，通过模式约束接地解决智能体 SPARQL 生成中的类型盲问题，显著提升 KBQA 性能并消除空查询。
practical_value: '- 在电商搜推场景中，若利用 LLM Agent 与商品知识图谱交互生成推荐理由或查询，可引入类型约束（如商品类别、属性域/范围）过滤不可能的属性，避免返回空结果。

  - 借鉴 SAGA 的双向类型状态（bidirectional type state）机制，在 agent 每一步推理后即时更新实体与属性的类型兼容性，缩小后续接地搜索空间。

  - 以紧凑的模式注释格式（schema-annotated format）向 LLM 展示剩余合法属性，减少 token 开销并提升生成准确率。

  - 对图谱中缺失的模式信息，可结合历史轨迹局部证据和经验统计宽容处理，适应真实业务图谱的不完整性。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有 LLM 智能体在交互式 KBQA 中通过交替推理、查询与 SPARQL 生成来解析复杂问题，但接地（grounding）时主要依赖词汇相似与实例观察，忽略实体类型、属性域/范围等 schema 约束，常产生语义不兼容的三元组，导致空查询结果。这种 **类型盲接地** 膨胀搜索空间且影响可执行性。

**方法**：SAGA 是一个无需训练的框架，核心是将属性探索转化为模式约束的接地操作：① 维护 **双向类型状态**（bidirectional type state），跟踪当前实体、属性及目标答案的类型约束；② **构建时过滤**，基于类型兼容性提前剔除已知不相容的属性候选；③ 将剩余图模式以 **紧凑模式注释** 格式呈现给 LLM，降低 token 成本并突出合法路径；④ 对缺失 schema 信息采用 **宽松处理**，融合经验统计与局部执行轨迹证据。

**结果**：在 Wikidata 与 Freebase 的 9 个基准上，SAGA 取得全部 **最高 F1** 与 **8 项精确匹配第一**，并在所有 Wikidata 设定中将空查询结果比例降至零，证实了类型感知接地对 agentic text-to-SPARQL 的有效性。
