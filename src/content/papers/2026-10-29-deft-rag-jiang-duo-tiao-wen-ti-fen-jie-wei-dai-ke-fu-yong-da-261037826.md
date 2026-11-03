---
title: 'DeFT-RAG: Decomposing Multi-Hop Questions into Self-Contained Sub-Questions
  with Reusable Answers'
title_zh: DeFT-RAG：将多跳问题分解为带可复用答案的自包含子问题
authors:
- Dingyi Kang
- Bingzhe Li
affiliations:
- University of Texas at Dallas
arxiv_id: '2610.37826'
url: https://arxiv.org/abs/2610.37826
pdf_url: https://arxiv.org/pdf/2610.37826
published: '2026-10-29'
collected: '2026-11-03'
category: RAG
direction: 多跳 RAG 子问题分解与缓存复用
tags:
- RAG
- multi-hop QA
- question decomposition
- QA caching
- self-contained sub-questions
- LLM
one_liner: DeFT-RAG 用自包含子问题分解、规则化状态跟踪和 QA 缓存复用，提升多跳 RAG 准确率并降低 LLM 调用成本
practical_value: '- 在电商客服或商品知识问答中，把多跳问题拆成“自包含”子问题，每个子问题显式带出所有实体，避免让 LLM 自己规划依赖图；可显著减少状态跟踪和错误传播。

  - 将“哪些已答、下一步该问什么”等状态更新从 LLM 中剥离，用规则表维护 QA 状态，再用轻量决策模型做 yes/no 判断，能大幅降低 LLM token
  消耗和推理延迟。

  - 缓存跨请求的 QA 对，遇到语义相同的子问题直接复用答案，适合推荐系统中用户高频重复的子查询（如商品属性、活动规则），可在不牺牲准确率的前提下减少 12%+
  的 LLM 调用。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：RAG 在多跳问题上表现差：图方法一次性检索只覆盖问题中出现的实体，难以恢复完整证据链；迭代方法逐步找回证据，但要求 LLM 同时完成子问题规划、依赖判断、重写和状态跟踪，准确率受限。

**方法关键点**：
- **自包含子问题生成**：每次基于原始问题和已回答的 QA 对生成一个子问题，子问题显式命名所有涉及实体，无需规划依赖、重写或跟踪全局状态。
- **状态跟踪外置**：用规则更新 QA 表跟踪已知信息，用微调的轻量决策模型做 yes/no 判断，仅保留生成子问题这一项核心 LLM 任务。
- **QA 缓存复用**：缓存 QA 对，后续子问题语义相同时直接复用答案，减少 LLM 调用。

**关键结果**：在 MuSiQue、2WikiMultiHopQA、HotpotQA 三个基准上，以 gpt-4o-mini 和 Qwen3.6 为骨干，DeFT-RAG 在 13 个 baseline 中准确率最高，同时输入 token 少于所有其他迭代方法；跨 1000 个 MuSiQue 问题的 QA cache 使 23.1% 的子问题从缓存回答，LLM 调用减少 12.9%，准确率不降。
