---
title: 'DeclineCraft: A RAG Abstention Benchmark for Jointly Measuring Combined Retrieval
  and Parametric Knowledge'
title_zh: DeclineCraft：联合衡量检索与参数知识的 RAG 弃答基准
authors:
- Atharva Thakur
- Abulhair Saparov
- Bruno Ribeiro
affiliations:
- Purdue University
arxiv_id: '2610.28340'
url: https://arxiv.org/abs/2610.28340
pdf_url: https://arxiv.org/pdf/2610.28340
published: '2026-10-20'
collected: '2026-10-21'
category: Eval
direction: RAG 弃答能力基准与行为分析
tags:
- RAG
- Abstention
- Benchmark
- LLM
- Iterative RAG
- Knowledge cutoff
one_liner: 提出 DeclineCraft 基准，度量模型在检索与参数知识均不足时正确弃答的能力，揭示迭代 RAG 等增强策略反而降低弃答率。
practical_value: '- 在电商客服/商品咨询等 RAG 场景中，不要盲目堆叠迭代检索、query rewriting、reranking 等“增强”组件：它们可能让模型对无法回答的问题过度自信，降低正确弃答率。对高频未知问题（如新商品属性、未收录政策），应显式加入弃答判定或置信度阈值。

  - 单轮检索已能提升正确弃答率（38/40 配置），说明即使检索不到确切答案，提供相关但不完整的上下文也能帮助模型识别知识缺口，而非直接依赖参数记忆编造。在知识截止后新商品/新政策问答中，可先检索同类商品/旧政策作为参照。

  - 思考模式（thinking）会显著降低弃答率，但常从“承认不确定”转为“否定前提”，这对安全敏感场景是隐患。实际部署时不宜只用 CoT 自我评估，应设置独立的
  abstention 分类器或规则。

  - 模型规模与弃答率无显著关联，只与作答准确率正相关。因此不能指望换更大模型解决拒答问题，需针对弃答行为做专门训练或 prompt 设计。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：可靠 RAG 不仅要回答可答问题，还要在检索文档与参数知识均不支撑时正确弃答。现有基准对此评测不足，尤其缺乏动态、可审计参数暴露的不可回答问题集。

**方法**：构建 DeclineCraft，用 Minecraft 知识截止后的新增特性生成不可回答问题，审计模型可能的参数暴露，支持未来截止日期扩展。对 27 个 LLM 评测三个指标：Correct Abstention Rate（CAR，不可答问题上的正确弃答率）、Answerable Attempt Rate、Answer Accuracy。对比无检索、单轮检索、迭代 RAG（模型自评估上下文可再请求两轮检索）、以及加入 query rewriting 与 reranking 的 hybrid dense & sparse 检索。

**关键结果**：
- 单轮检索在 40 个配置中 38 个显著提高 CAR，优于无检索。
- 迭代 RAG 在 40 个配置中 30 个显著降低 CAR（均值 46.4%），但 Answer Accuracy 仅从 68.5% 微升至 69.3%，说明模型更敢答却不更准。
- 在 hybrid 检索上叠加 query rewriting 和 reranking，对全部 12 个模型都降低了 CAR。
- 模型规模与 Answer Accuracy 正相关（Spearman ρ=+0.60），但与 CAR 无显著关联；发布时间也与 CAR 无关。
- 无检索时启用 thinking，在 13 个模型中的 8 个显著降低 CAR（平均降 14 个百分点），响应从承认不确定转为否定问题前提。
