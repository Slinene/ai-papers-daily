---
title: 'Better Decomposition, Free Aggregation: A Synthesizer-Folding Framework for
  Multilingual Multi-Hop Question Answering'
title_zh: 面向多语言多跳问答的延迟翻译与合成器折叠框架
authors:
- Yilin Wang
- Yuchun Fan
- Weidong Bao
- Zili Wei
- Shi Feng
- Tong Xiao
- Zhengtao Yu
- Jingbo Zhu
affiliations:
- School of Computer Science and Engineering, Northeastern University, Shenyang, China
- Yunnan Key Laboratory of Artificial Intelligence, Kunming University of Science
  and Technology, Kunming, China
arxiv_id: '2608.13160'
url: https://arxiv.org/abs/2608.13160
pdf_url: https://arxiv.org/pdf/2608.13160
published: '2026-08-13'
collected: '2026-08-16'
category: RAG
direction: 多语言RAG · 问题分解与延迟翻译
tags:
- Multilingual RAG
- Multi-hop QA
- Question Decomposition
- Deferred Translation
- Graph Alignment
- LLM
one_liner: Syfer 通过延迟翻译和子问题图质量检查，在保持精度同时降低多语言 RAG 成本
practical_value: '- 跨语言电商搜索/问答中，不必默认把 query 翻译成英文再召回；可先按原语言分解并做质量检查，通过则直接在目标语言检索与作答，失败才启用英文翻译路径，节省翻译成本和保留本地化语义。

  - 复杂购物意图可拆成带约束的子问题图，在 Agent 执行前增加一道 decomposition-quality check，避免冗余子任务引入的错误累积。

  - 多跳检索问答采用顺序 retrieve-then-answer，让子问题共享上下文，比先生成全部子问题再聚合结果更能抑制误差放大；这一点可迁移到多 Agent
  协作的任务规划。

  - 双语子问题图对齐只在翻译 fallback 时启用，作为低成本的跨语言一致性保障，适合需要兼顾效果与推理预算的生产环境。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：多语言 RAG 处理复杂多跳问题时，现有方案要么统一翻译检索文档，丢失目标语言特有信息、引入翻译噪声并抬高成本；要么分解子问题后贪心推理和最终聚合，冗余子问题会逐步放大错误。

方法关键点：Syfer 采用延迟翻译而非默认翻译。先用格式约束的分解器在原语言生成子问题图，并做分解质量检查；检查通过就在目标语言按 retrieve-then-answer 顺序回答子问题，不触发翻译；检查失败才激活英文翻译路径，并通过双语子问题图对齐保持原语言与英文子问题的一致性。

关键结果：多语言实验显示 Syfer 达到竞争性准确率，同时在性能和计算成本之间取得更优平衡。
