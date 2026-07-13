---
title: 'ProjAgent: Procedural Similarity Retrieval for Repository-Level Code Generation'
title_zh: ProjAgent：基于过程相似检索的仓库级代码生成
authors:
- QiHong Chen
- Aaron Imani
- Iftekhar Ahmed
affiliations:
- University of California, Irvine
arxiv_id: '2607.08691'
url: https://arxiv.org/abs/2607.08691
pdf_url: https://arxiv.org/pdf/2607.08691
published: '2026-07-09'
collected: '2026-07-13'
category: Agent
direction: Agent 工作流与检索增强代码生成
tags:
- Procedural Similarity
- Repository-Level Code Generation
- Agentic Workflow
- Static Analysis Feedback
- RAG
one_liner: 提出程序化相似性作为显式检索信号，结合 Agent 工作流与静态分析反馈，提升仓库级代码生成效果
practical_value: '- 过程相似检索思路可迁移：将任务分解为子步骤，为每个子步骤检索历史上相似的“过程序列”（如策略、操作链），而不仅依赖语义或字面匹配，适合推荐解释生成、多步推荐策略选择等场景。

  - Agent 工作流与校验反馈循环：使用静态分析反馈迭代修复代码，类似推荐系统中利用规则或业务逻辑对推荐结果进行事后校验与修正，可设计保守的反馈回路提升生成质量。

  - 混合相似度检索策略：将程序化相似度与传统语义相似度融合，构建更丰富的上下文，可借鉴用于推荐系统的多路召回或特征融合，例如同时考虑行为序列相似和内容语义相似。

  - 上下文动态构建：Agent 在每步按需检索相关代码片段，可类比为推荐 Agent 在不同决策阶段动态检索不同知识库，提升生成结果与项目级约束的一致性。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：仓库级代码生成由于跨文件依赖和项目规范难以靠传统检索解决，现有方法多基于词汇、结构或语义相似度，易忽略实现相似过程逻辑但标识符异或领域不同的函数。

**方法**：提出 ProjAgent，将目标函数拆解为中间推理步骤，利用 Agent 工作流为每一步检索具有相似程序行为的仓库函数，并将获得的程序化上下文与常规语义检索结果融合，构建更丰富的仓库上下文。此外，引入保守的静态分析反馈循环，通过编译器和静态分析反馈迭代修复生成的代码。

**结果**：在 REPOCOD 基准上，Pass@1 达到 41.14%，显著优于现有基于检索的基线方法，验证了程序相似性作为检索维度的有效性。
