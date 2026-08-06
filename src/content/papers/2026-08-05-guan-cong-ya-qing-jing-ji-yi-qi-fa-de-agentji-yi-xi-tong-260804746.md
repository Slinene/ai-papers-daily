---
title: 'Caching for the Future: Scrub Jay Episodic Memory Principles for Agent Memory
  Systems'
title_zh: 灌丛鸦情景记忆启发的Agent记忆系统
authors:
- Kartikey Singh Bhandari
- Aarya Wadhwani
- Dhruv Kumar
- Pratik Narang
affiliations:
- Birla Institute of Technology and Science, Pilani
arxiv_id: '2608.04746'
url: https://arxiv.org/abs/2608.04746
pdf_url: https://arxiv.org/pdf/2608.04746
published: '2026-08-05'
collected: '2026-08-06'
category: Agent
direction: Agent记忆系统 · 时间衰减
tags:
- Agent Memory
- Episodic Memory
- Temporal Decay
- What-Where-When
- LLM Agents
- ScrubJay-MEM
one_liner: 将灌丛鸦的What-Where-When记忆与类型条件时间衰减引入LLM Agent记忆，有效处理过期事实
practical_value: '- 对话式推荐或搜索Agent中，用户偏好与促销事实时效性不同，可借鉴类型条件衰减系数，为每条记忆（如短期价格 vs 长期偏好）自动分配不同半衰期，避免过期信息污染上下文。

  - 记忆存储采用WWW元组及可腐性π_i和效用期限τ_i，检索时结合查询自适应打分，可对已有向量知识库做动态时效加权，提升检索精准度。

  - 更新机制仅需O(1)次LLM调用，工程上轻量，适合电商高并发场景下记忆增量修正。

  - 引入的Temporal Generalization Test（TGT）和Generalization Gap指标可用于评估自家记忆系统对时间泛化的能力，辅助上线前量化时效性风险。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：当前LLM Agent记忆系统将所有记忆等同视之，不区分内容类型，导致过期事实污染检索上下文，影响长时Agent性能。

**方法**：受灌丛鸦情景记忆的What-Where-When（WWW）启发，提出ScrubJay-MEM。每条记忆编码为WWW元组，并自动分类得到可腐性系数π_i与效用期限τ_i；检索时用查询自适应打分融合类型条件时间衰减；更新时回溯修正，每次仅需O(1)次LLM调用。

**结果**：在Temporal Generalization Test上，ScrubJay-MEM是唯一获得显著正GenGap（+0.108）的检索系统；在MemoryAgentBench EventQA-64k上，F1相比Mem0提升+2.66，相比Qwen3-Embedding-4B提升+3.09。消融去除衰减后GenGap下降5.7倍，验证类型条件衰减的必要性。增益在更强骨干下收窄，且在事实固化任务上反转，表明贡献集中在易腐事实的时间推理。
