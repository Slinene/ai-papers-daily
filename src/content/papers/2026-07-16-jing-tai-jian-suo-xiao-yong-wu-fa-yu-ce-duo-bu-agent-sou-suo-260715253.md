---
title: 'Bridge Evidence: Static Retrieval Utility Does Not Predict Causal Utility
  in Multi-Step Agentic Search'
title_zh: 静态检索效用无法预测多步 Agent 搜索中的因果效用
authors:
- Debayan Mukhopadhyay
- Utshab Kumar Ghosh
- Shubham Chatterjee
affiliations:
- University of Calcutta
- Missouri University of Science and Technology
arxiv_id: '2607.15253'
url: https://arxiv.org/abs/2607.15253
pdf_url: https://arxiv.org/pdf/2607.15253
published: '2026-07-16'
collected: '2026-07-17'
category: Agent
direction: 多步 Agent 搜索中的检索效用评估
tags:
- Agentic Search
- Counterfactual Utility
- Bridge Evidence
- Retrieval Evaluation
- Multi-step Reasoning
- Entity Discrimination
one_liner: 在多步 Agent 搜索中，静态低相关文档可能通过提供区分性实体成为关键的“桥梁证据”，静态效用与因果效用近乎独立。
practical_value: '- 构建 Agent 检索模块时，不能用传统静态指标（如 NDCG）评估文档价值，应引入反事实评估（移除文档观察最终答案变化）来识别“桥梁文档”。

  - 在电商对话助手等多步 Agent 场景，重视文档的“行动效用”：设计机制让 Agent 从文档中提取区分性实体（如属性、品牌），用于重定向后续搜索。

  - 借鉴 CTU 指标（综合最终答案质量、下一步检索质量、步数变化）来全面衡量文档对 Agent 轨迹贡献，而不只看单步问答匹配。

  - 训练检索模型时，可利用 Agent 交互数据生成反事实效用标签，直接学习检索对最终任务有用的文档，而非仅优化静态相关性。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：传统检索系统评估基于静态有用性（文档是否直接提升当前答案质量），但在多步 Agent 搜索中，文档的价值可能体现在引导下一步行动，而非直接回答当前问题。

**方法**：使用 ReAct 风格 Agent 在 HotpotQA 上重放 1000 个开发问题，对 Agent 读过的每个文档执行反事实删除并重跑后续轨迹。通过比较原始与反事实轨迹，定义 Counterfactual Trajectory Utility (CTU)，综合最终答案质量、下一步查询检索质量和步数变化三个增量。将 CTU 与 Static RAG Utility (SRU) 交叉分析，发现两者近乎统计独立（Spearman ρ = -0.026）。约 1/3 的文档是“桥梁文档”：静态无用但对 Agent 有因果负载。进一步，用 Observable Entity Relevance (OER) 度量发现，区分性实体在 Agent 下一步查询中出现的概率 4.02 倍高于非相关文档中的实体（6.1% vs 1.5%）。

**关键结果**：静态效用与因果效用独立；27.2% 的文档在 BM25 和交叉编码器代用轴上同样成为桥梁；桥梁文档通过提供区分性实体重定向搜索。
