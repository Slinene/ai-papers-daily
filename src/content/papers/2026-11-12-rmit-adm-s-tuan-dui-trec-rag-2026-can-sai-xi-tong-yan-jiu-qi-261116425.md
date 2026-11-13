---
title: 'RMIT-ADM+S at TREC RAG 2026: Research Agents, Retriever Ablations, and Open-Weight
  Replication'
title_zh: RMIT-ADM+S 团队 TREC RAG 2026 参赛系统：研究型 Agent、检索器消融与开放权重复现
authors:
- Oleg Zendel
- Kun Ran
- Chenglong Ma
- Nguyen Khoi Vo
- Shuai Wang
affiliations:
- RMIT University
- The University of Queensland
arxiv_id: '2611.16425'
url: https://arxiv.org/abs/2611.16425
pdf_url: https://arxiv.org/pdf/2611.16425
published: '2026-11-12'
collected: '2026-11-13'
category: RAG
direction: RAG 研究型 Agent 与检索消融
tags:
- RAG
- research agent
- open-weight models
- Reciprocal Rank Fusion
- retrieval ablation
- TREC RAG
one_liner: 在 TREC RAG 2026 用研究型 Agent 对比检索策略与模型，发现 writer 选择与相邻 chunk 扩展影响最大，开放权重模型可低成本复现
practical_value: '- 在构建 RAG/Agent 系统时，先做消融定位关键变量：该工作发现 writer 模型选择与相邻 chunk 扩展对答案质量影响最大，避免盲目堆叠复杂
  Agent 工作流或检索模块，优先投入这两个方向

  - 开放权重模型在人工偏好上可超过闭源模型，但自动化覆盖率指标不一定同步；评估生成式 RAG 系统时需结合业务指标与人工评测，不能只看 n-gram 覆盖率

  - 相邻 chunk 扩展是低成本高效的检索增强 trick，可迁移到电商商品描述、评论、知识库等长文本检索场景，提升上下文完整性

  - 混合检索 + RRF 融合在 ClimbMix 上表现稳定，可借鉴到多路召回融合（如商品语义召回与关键词召回）的排序阶段'
score: 7
source: arxiv-cs.IR
depth: abstract
---

## 动机
参赛 TREC RAG 2026，任务是在 ClimbMix-400B-shuffle 语料上为 119 个测试叙述生成最多 1024 字的带引用报告。核心问题是：复杂 Agent 工作流和闭源模型是否值得额外成本，开放权重模型能否以更低成本复现接近质量。

## 方法关键点
提交 7 个研究型 Agent run，覆盖不同检索策略、writer 模型和 Agent 工作流。预提交消融显示 writer 选择与相邻 chunk 扩展是影响答案质量的主要因素。系统采用混合检索与 Reciprocal Rank Fusion 等融合策略，对比 OpenAI 闭源模型与开放权重模型。

## 结果
官方 NIST 评估中，7 个 run 有 6 个在三个 rubric/nugget 集合上超过 track 中位数。最佳 run `brief-hybrid` 获得所有提交中最高的 all-item coverage，并在 Batch-1 vital coverage 上追平 track 最大值 0.892。人工 side-by-side 偏好呈现批次差异：开放权重 `owa-glm5` 在 Batch 1 领先，尽管自动化 coverage 较低；`sol-research-first` 在 Batch 2 领先。结论：自动化 coverage 指标与人工偏好存在差异，低成本开放权重模型在研究型 Agent 系统中具备实用潜力。
