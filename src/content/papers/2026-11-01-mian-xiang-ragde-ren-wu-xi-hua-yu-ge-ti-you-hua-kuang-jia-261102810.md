---
title: 'TRIO: Task Refinement with Individual Optimization for Retrieval-Augmented
  Generation'
title_zh: 面向RAG的任务细化与个体优化框架TRIO
authors:
- Yingtao Ren
- Xiao Luo
- Yiwei Fu
- Jinzhao Zhou
- Yu-Cheng Chang
- Chin-Teng Lin
affiliations:
- University of Technology Sydney
- University of Wisconsin–Madison
- Peking University
arxiv_id: '2611.02810'
url: https://arxiv.org/abs/2611.02810
pdf_url: https://arxiv.org/pdf/2611.02810
published: '2026-11-01'
collected: '2026-11-10'
category: RAG
direction: 多Agent迭代优化RAG全流程
tags:
- RAG
- Agent
- Query Expansion
- Curriculum Learning
- Reward Optimization
- LLM
one_liner: 用三个分别优化的Agent迭代细化查询扩展、检索判断与答案生成，提升RAG效果
practical_value: '- 将RAG拆成 query expansion / retrieval judge / answer 三个Agent，各自定义清晰的优化目标，避免端到端耦合导致的可优化性差。业务中可以按环节分别迭代Agent，便于定位和修复问题。

  - 用“全票投票(unanimity voting)”对扩展查询是否足够进行自动标注，利用生成结果作为 ground truth 优化 judge agent。这个思路可用于电商搜索中生成
  query 改写 / 语义匹配质量的监督信号，降低人工标注成本。

  - Answer agent 使用动态匹配奖励 + 课程学习(curriculum learning)，从易到难优化证据利用和答案准确性。适合广告文案生成、商品描述生成等场景，先让模型在简单样本上稳定，再逐步增加难度，提升线上稳健性。

  - Query expansion agent 以答案质量提升作为 reward 来优化，形成“改写策略由最终效果反馈驱动”的闭环。可借鉴到搜索广告的关键词拓词、推荐系统的
  query 改写模块，用下游任务指标指导上游生成策略。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：RAG 面临检索质量不足和生成幻觉两大痛点，现有方案往往只优化单一环节，缺乏对 query、检索、答案生成的联合迭代优化。

**方法关键点**：
- 设计三个 agent：query expansion agent、judge agent、answer agent，纳入迭代 refinement 范式。
- Query expansion agent：扩展模糊 query，以答案质量提升作为 reward 进行优化，提高扩展效率。
- Judge agent：用全票投票(unanimity voting)判断扩展 query 是否足够，其生成结果作为 ground truth 优化判断器，提升检索触发准确性。
- Answer agent：基于动态匹配奖励和课程学习(curriculum learning)优化证据利用，降低幻觉，提升最终答案精度。

**关键结果**：在多个基准数据集上与 SOTA 方法对比，TRIO 验证了有效性，显著提升 RAG 性能。代码开源。
