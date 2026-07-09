---
title: 'Progressive Disclosure for LLM-Maintained Wiki Knowledge Bases: a Preregistered
  Ablation'
title_zh: 渐进式披露在 LLM 维护 Wiki 知识库中的预注册消融研究
authors:
- Theodore O. Cochran
affiliations:
- AI for Altruism (A4A)
arxiv_id: '2607.04576'
url: https://arxiv.org/abs/2607.04576
pdf_url: https://arxiv.org/pdf/2607.04576
published: '2026-07-06'
collected: '2026-07-09'
category: Agent
direction: Agent 自主路由优化知识检索
tags:
- Progressive Disclosure
- Agent Routing
- Knowledge Base
- Retrieval Efficiency
- Evaluation Validity
one_liner: 工具型 Agent 直接推断页面路径，避免索引加载，成本节约来自更精准的访问而非预期节省
practical_value: '- 在 Agent 设计中不必预装大型索引，让模型自路由推断所需页面路径，结合轻量目录可大幅减少工具调用和 token 消耗

  - 电商商品知识库可借鉴“目录+摘要”结构，推荐引擎先查目录再按需取详情，减少无关上下文

  - 自路由 Agent 在无需严格协议时效率更优，RAG 或 Agent 工作流可给模型适当自由度

  - 预注册消融与工具性效度威胁分析可用于构建严谨的对比评估，尤其多臂实验的变量控制'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：LLM 代理维护并查询知识库时，渐进式披露（目录 + 单行摘要）被认为能避免加载大型索引以降低成本。然而，在真实 709 页 wiki 上的预注册消融发现，能力强的工具型代理从不加载索引，而是根据问题直接推断页面路径并读取，因此预期的节省并未实现。

**方法关键点**：设计 4 个知识库版本，页面内容完全相同（通过 git 标签冻结），仅访问结构不同：索引 vs 渐进式披露的检索臂。代理在三种条件下工作：协议受限代理、自由自路由代理、目录预加载。使用跨模型族盲审回答质量（主要指标）和成本（次要指标）。

**关键结果**：质量非劣（检索臂在预注册边界内匹配索引基线）。所有条件下成本均显著下降：自路由代理节省约 1/3，目录预加载节省超过一半，置信区间均排除零。节约并非来自跳过大索引，而是检索臂引用更少页面、使用更少工具轮次。研究还系统性考察了工具性效度威胁。
