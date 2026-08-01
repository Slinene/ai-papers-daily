---
title: (Towards) Scalable Reliable Automated Evaluation with Large Language Models
title_zh: 面向可扩展可靠的大语言模型自动化评估
authors:
- Bertil Braun
- Martin Forell
affiliations:
- KIT
arxiv_id: '2607.28282'
url: https://arxiv.org/abs/2607.28282
pdf_url: https://arxiv.org/pdf/2607.28282
published: '2026-07-30'
collected: '2026-08-01'
category: Eval
direction: LLM自动化评估框架
tags:
- Evaluation
- Pairwise Comparison
- Elo Rating
- LLM-as-Judge
- Automated Metrics
one_liner: 利用多LLM成对比较与Elo评级系统，实现可扩展且可靠的文本质量自动评估，减少人工干预。
practical_value: '- 在推荐系统评估生成式文本（如商品描述、推送文案）时，可运用多LLM成对比较取代单模型评分，降低单个LLM偏差，提高评估稳健性。

  - 采用Elo评级系统将两两对比转化为全局排名，适合持续迭代优化的场景，如A/B测试后的模型选优，能生成稳定且可解释的质量排序。

  - 可调一致性阈值（从全票一致到多数投票）为工程实践提供灵活性：初期用高阈值保障高置信度，规模扩展时放宽阈值以提高覆盖率，权衡成本与信度。

  - 该方法领域无关，可直接迁移至电商搜索、广告文案、对话Agent等多文本生成场景的离线和在线评估，大幅减少人工评审工作量。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM生成文本的质量评估困难，现有自动指标难以捕捉复杂性和可变性，且依赖参考标准，限制其在主观开放领域的应用。亟需一种可扩展、可靠且领域无关的自动化评估方法，以降低人工评估成本。

**方法关键点**：提出一种新颖评估框架，利用多个LLM对同一任务的多份输出进行成对比较，综合多模型判断以减少单一模型偏差；引入Elo评级系统，根据比较结果计算每个输出的稳定排名分数；通过设定不同的一致性阈值（如全票一致到多数投票），灵活控制评估的置信度和覆盖率，实现可扩展的可靠评估。

**结果**：在从科学摘要提取能力概况的任务上验证，自动生成的排名与专家人工判断高度相关，证明该方法能在保证评估质量的同时，显著降低对人类评估的依赖，为广泛的应用场景提供高效、一致的评估层。
