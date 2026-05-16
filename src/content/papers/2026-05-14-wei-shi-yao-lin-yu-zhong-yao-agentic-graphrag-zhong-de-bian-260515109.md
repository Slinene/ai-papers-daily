---
title: 'Why Neighborhoods Matter: Traversal Context and Provenance in Agentic GraphRAG'
title_zh: 为什么邻域重要：Agentic GraphRAG 中的遍历上下文与溯源
authors:
- Riccardo Terrenzi
- Maximilian von Zastrow
- Serkan Ayvaz
affiliations:
- University of Southern Denmark
arxiv_id: '2605.15109'
url: https://arxiv.org/abs/2605.15109
pdf_url: https://arxiv.org/pdf/2605.15109
published: '2026-05-14'
collected: '2026-05-16'
category: RAG
tags:
- GraphRAG
- Citation Faithfulness
- Agentic RAG
- Provenance
- Knowledge Graphs
- Ablation Studies
one_liner: 发现 Agentic GraphRAG 中最终引用实体虽必要却不充分，答案还依赖未引用的遍历上下文与图结构
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：在 Agentic GraphRAG 中，代理在知识图谱上多步探索后才输出答案和少量引用，但评估引用忠实性时通常只看最终引用是否支持答案，忽略了遍历过程中访问过的未引用实体、邻域结构和路径信息，这些上下文可能同样影响答案生成，导致溯源不完整。

**方法关键点**：
- 从 2WikiMultiHopQA 构建包含 1815 实体、1692 关系、7 个社区的知识图谱，筛选 30 个多跳问题作为基准。
- 比较 6 种系统：纯 LLM、RAG、非代理 GraphRAG、Agentic GraphRAG 以及两个约束变体（visited‑only 和 evidence‑first）。
- 在图消融实验中，针对每个问题的代理运行轨迹，将实体分为未访问、访问且引用、访问但未引用三类，然后设计三种消融研究：① 隔离引用证据（全隔离/仅文本隔离），检验引用是否充分；② 移除引用实体 vs. 移除等量随机实体，检验引用是否必要；③ 移除访问但未引用实体或屏蔽其文本，衡量遍历上下文的影响。

**关键结果**：
- 基线准确率：Agentic GraphRAG 76%，而纯 LLM 仅 16.7%，说明外部图知识是关键。
- 移除引用实体后准确率骤降（Agentic GraphRAG 从 76% → 36%），而随机移除实体则未造成同等下降，甚至在某些设置下提升，表明引用实体是必要的，但移除后仍有超 30% 问题可正确回答，所以不充分。
- 全隔离实验中，仅保留引用实体时准确率仍下降至 68%，保留图结构但屏蔽非引用文本时可恢复至 72%，说明未引用实体及其邻域结构对答案有额外贡献。
- 移除访问但未引用实体也会降低准确率（下降至 68%），进一步证实遍历上下文的行为相关性。

**一句话**：引用评估在代理图检索中应从“最终输出级”进化为“轨迹级”，涵盖访问过的未引用实体、遍历路径和结构信号。
