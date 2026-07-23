---
title: 'CIR at iKAT SCAI 2026: Exploring Clarification Need Prediction in Agentic
  Conversational Search'
title_zh: CIR 在 iKAT SCAI 2026：探索代理式对话搜索中的澄清需求预测
authors:
- Nolwenn Bernard
- Jüri Keller
- Philipp Schaer
affiliations:
- TH Köln
arxiv_id: '2607.19801'
url: https://arxiv.org/abs/2607.19801
pdf_url: https://arxiv.org/pdf/2607.19801
published: '2026-07-22'
collected: '2026-07-23'
category: Agent
direction: 代理式对话搜索 · 澄清需求预测
tags:
- Agentic Search
- Clarification Need
- Conversational AI
- Query Rewriting
- Mixed Initiative
one_liner: 构建代理式对话搜索系统，比较两种澄清需求预测模型在混合主动搜索中的效果
practical_value: '- 代理式架构将检索、重排序、生成等组件工具化，由编排代理统一调度，这种设计可直接复用到对话推荐系统，实现多轮交互中的灵活工具组合与状态管理。

  - 澄清需求预测模型可作为对话推荐的关键触发器：在商品属性模糊或用户意图不确定时，主动生成确认性问题（如“您更看重价格还是品牌？”），提升推荐精度与用户体验，尤其适用于高客单价决策场景。

  - 采用轻量级 BERT 变体做二分类判断“是否需要澄清”，工程上易于集成进现有搜索/推荐 pipeline，延迟低，可作为强化学习智能体的 reward 信号或规则的前置条件。

  - 混合主动（mixed-initiative）模式让系统在必要时介入提问，而非完全被动响应，平衡了自动化与人工干预，可降低推荐冷启动和长尾 query 的失败率。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：对话搜索中，用户查询往往简短模糊，系统若无法有效澄清意图，会传递错误信号至下游检索与生成，导致答案偏离真实需求。iKAT 任务要求在个性化知识库约束下主动判断何时提出澄清问题，以提升对话质量。

**方法关键点**：
- 设计代理式架构，将查询改写、检索、重排序、答案生成、澄清需求预测与问题生成均封装为工具，由一个 LLM 编排代理（orchestrator）根据对话状态决定调用顺序与参数。
- 聚焦澄清需求预测组件，实验两种神经分类模型：MuSIc 和基于 BERT 的 Zef-CNP，输入为对话上下文与用户 PTKB 表征，输出二分类标签（需要/不需要澄清）。
- 在 iKAT SCAI 2026 交互式评估框架下，使用模拟用户自动评测系统性能。

**关键结果**：两种澄清预测模型性能差异微弱，整体效果受限于训练数据与任务先验的不足，表明澄清触发机制仍是对话搜索中的难点，未来需更细粒度的上下文建模或与检索模块联合优化。
