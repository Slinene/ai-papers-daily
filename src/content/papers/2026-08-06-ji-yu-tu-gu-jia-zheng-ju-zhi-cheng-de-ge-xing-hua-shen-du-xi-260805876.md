---
title: Personalized Deep Research Query Refinement with Graph-Scaffolded Evidence
  Grounding
title_zh: 基于图骨架证据支撑的个性化深度研究查询细化
authors:
- Soojin Yoon
- Dongha Lee
affiliations:
- Yonsei University
arxiv_id: '2608.05876'
url: https://arxiv.org/abs/2608.05876
pdf_url: https://arxiv.org/pdf/2608.05876
published: '2026-08-06'
collected: '2026-08-07'
category: QueryRec
direction: 个性化查询细化 · 意图引出图 · 澄清策略
tags:
- Deep Research Agent
- Personalized Query Refinement
- Intent Elicitation Graph
- Clarification Policy
- Evidence Grounding
one_liner: 利用意图引出图学习澄清策略，在平衡目标覆盖与证据成本下生成个性化查询，用户提问减少三分之二
practical_value: '- 在对话式推荐/搜索中，可借鉴意图引出图建模用户意图间的依赖关系，自动决定何时澄清、调用用户画像或记忆，避免低效反问。

  - 澄清策略训练可基于图结构轨迹，模拟不同依赖与证据条件，学习最优的问询次数与顺序，平衡个性化增益与交互成本。

  - 对于黑盒生成式 Agent（如商品文案、搜索 query 改写），可通过优化输入 query 实现个性化，无需侵入内部 pipeline，降低工程耦合。

  - 证据条件判断（已有上下文是否足够）可直接用于多轮对话中判断是否需要召回外部知识或用户历史，减少无效检索。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：深度研究代理报告需反映用户具体目标、约束与偏好，但现有方法要么侵入代理内部，要么缺乏对用户个人化因素的系统澄清。

**方法**：提出 G-STEER，将用户请求细化为个性化研究规范。构建意图引出图（Intent Elicitation Graph），将框架因素（目标、偏好等）组织为有依赖关系的引出目标。从多样化的图骨架轨迹中，使用强化学习训练一个澄清策略，动态决定：哪些因素相关、现有用户上下文是否足够、是否需检索用户记忆或直接询问用户，最终生成精炼的查询。策略在目标覆盖率和证据获取成本之间取得平衡。

**结果**：在两个深度研究代理上，G-STEER 实现了最高的加权目标覆盖率（+6~8%）和最高的下游报告个性化评分，同时用户提问次数仅约强力澄清基线的 1/3，大幅降低交互负担。
