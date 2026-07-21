---
title: 'Evidence-in-the-Loop: Trace-Driven Optimization for Customer-Service LLM Agents'
title_zh: 证据在环：面向客服LLM智能体的追踪驱动优化
authors:
- Chunming Wu
- Dafei Qiu
- Congde Yuan
- Charles Quan
- Jun Wu
- Suipeng Li
- Mo Wu
- Gavin Xie
- Hope Chen
- Max Yao
affiliations:
- Flsdex
arxiv_id: '2607.18039'
url: https://arxiv.org/abs/2607.18039
pdf_url: https://arxiv.org/pdf/2607.18039
published: '2026-07-20'
collected: '2026-07-21'
category: Agent
direction: 客服Agent · 混合RAG与追踪驱动迭代
tags:
- LLM agents
- hybrid RAG
- trace-driven
- reranking
- policy-guided
- customer service
one_liner: 提出基于多路召回、交叉编码重排和跟踪分析的生产级客服Agent，重排序瓶颈大于LLM扩展
practical_value: '- **混合RAG证据构建**：多通道FAQ召回（BM25 + 标题向量 + 描述向量）经RRF加权融合和cross-encoder重排，可提升电商客服或商品搜索的覆盖率和边界可控性，重排器可微调以适配域内需求。

  - **证据驱动决策模块**：Agent最终行动严格基于召回证据和场景规则，避免LLM幻觉；可借鉴到推荐系统，将LLM的输出限制在可检索证据集内，增强可解释性与安全性。

  - **追踪驱动的迭代优化**：通过trace分析准确定位失败点（召回/排序/规则/澄清），形成诊断→优化→验证闭环；在推荐场景中可构建类似的bad case追踪流水线，指导检索或重排器微调，并监控遗忘风险。

  - **策略引导的编排范式**：使用固定LangGraph DAG融合RAG证据、对话记忆和澄清状态，保证多轮交互的可控性；在电商多轮对话或搜索Agent中可直接复用此类编排模式。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：生产环境客服机器人需持续提升回答质量，但LLM必须遵循证据边界、政策规则和人工兜底，不能随意生成。

**方法**：设计一个证据驱动的客服Agent工作流。在RAG层，采用**混合召回与重排**：BM25召回、问题标题向量召回、问题描述向量召回通过加权RRF融合，再用cross-encoder重排，产出可审计的FAQ证据。上层通过策略引导编排，将RAG证据、场景特定规则证据、对话记忆、澄清状态组合进固定LangGraph DAG。论文提炼出三个可复用模式：1）混合RAG证据构建；2）证据驱动的Issue/Action决策模块；3）**追踪驱动的RAG与重排器改进**——通过对线上trace的诊断，区分失败源自召回、排序、候选选择、澄清、规则证据或行动策略，进而针对性优化。

**结果**：在309条诊断查询子集上，混合召回top-50覆盖率达96.76%，但基础BGE重排器Hit@1仅56.31%；将LLM从Qwen3.5-27B换成GPT-4o时，最终问题选举准确率变化不到1pp，表明**重排序而非LLM骨干是目前主要瓶颈**。整体采用诊断→优化→验证的叙事结构，而非单一排行榜分数。
