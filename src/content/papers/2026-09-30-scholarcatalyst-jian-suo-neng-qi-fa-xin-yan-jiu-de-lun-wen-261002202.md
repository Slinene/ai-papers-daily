---
title: 'ScholarCatalyst: A Benchmark for Retrieving Papers That Inspire New Research'
title_zh: ScholarCatalyst：检索能启发新研究的论文的基准
authors:
- Sohyeon Kim
- Yoonho Lee
- Bo Liu
- Dayoon Ko
- Rulin Shao
- Seungone Kim
- Graham Neubig
- Pang Wei Koh
- Aakanksha Chowdhery
- Akari Asai
affiliations:
- Stanford University
- Seoul National University
- University of Washington
- Carnegie Mellon University
- Allen Institute for AI
arxiv_id: '2610.02202'
url: https://arxiv.org/abs/2610.02202
pdf_url: https://arxiv.org/pdf/2610.02202
published: '2026-09-30'
collected: '2026-10-03'
category: Eval
direction: 科学文献检索基准与Agent评测
tags:
- Benchmark
- Retrieval
- Agentic Search
- LLM
- Scientific Discovery
- RAG
one_liner: 构建207篇论文的作者标注检索基准，揭示Agentic搜索未超越嵌入检索（R@20 0.42 vs 0.48）
practical_value: '- 对搜索/推荐中的复杂长尾查询，不要盲目叠加 Agentic 循环：强嵌入检索 + 合理 rerank 可能已达上限；应优先优化底库
  embedding、索引和 query 理解。

  - 用“项目完成者回看哪些早期论文真推进了项目”的方式构建评估集，能捕捉比点击/相关性更接近“灵感价值”的主观相关性；电商推荐可借鉴让业务 owner 标注哪些商品/内容真正影响决策。

  - 时间切分很重要：论文基准只允许检索项目开始前的文献，对应推荐/搜索中训练与评测需严格按 timestamp 切分，避免未来信息泄漏。

  - 自动标注 pipeline 通过 author 标注+理由生成可规模化，可用于构建需要专家判断的检索/排序训练语料，帮助模型学习领域专家直觉。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：科学家能凭直觉从海量文献中找出能推进新研究的先前工作，但现有 AI 系统缺乏这种能力，且缺少衡量该技能的基准。论文通过让完成项目的作者回溯哪些早期论文实际/可能推进了项目，构建检索评测。

**方法关键点**：
- 自动标注 pipeline：184 位第一作者对 207 篇近期 CS 论文标注候选论文是否推进了项目，并给出详细理由。
- 任务定义：给定初始研究问题，从项目开始时已有的文献中检索这些论文，使用作者判断作为 ground truth。
- 对比了 embedding retrieval、agentic search（调用同一 retriever）和 Claude Fable 5.1 等系统。

**关键结果**：
- Agentic search 的 Recall@20 为 0.42，反而低于 embedding retrieval 的 0.48；即使 Claude Fable 5.1（可能见过补齐论文）也仅 0.51。
- 说明仅靠工具调用和推理无法弥补基础检索器的不足，需要新的训练方法让模型具备专家级文献搜索直觉。
