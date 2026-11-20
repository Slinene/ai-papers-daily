---
title: 'AutoRAGBench: A Benchmark for LLM Agents Automating RAG System Development'
title_zh: AutoRAGBench：面向 LLM Agent 自动化 RAG 系统开发的基准
authors:
- Hang Zhang
- Yuzhi Pan
- Ziyao Zhong
- Chaokun Wang
- Shuo Cao
- Zeyu Huang
- Yue Xue
- Fang Niu
- Bofan Xie
- Guanchen Ge
affiliations:
- Tsinghua University, Beijing, China
- Sina Weibo Corp, Beijing, China
arxiv_id: '2611.25582'
url: https://arxiv.org/abs/2611.25582
pdf_url: https://arxiv.org/pdf/2611.25582
published: '2026-11-19'
collected: '2026-11-20'
category: Agent
direction: LLM Agent 自动化构建与优化 RAG 系统
tags:
- LLM Agent
- RAG
- Benchmark
- AutoML
- Code Generation
- Iterative Optimization
one_liner: 首个在开放代码空间评测 LLM Agent 从零构建并迭代优化 RAG 系统的基准，GPT-6.1 Sol 均分 56.1 超过 Human-SOTA
  的 44.4
practical_value: '- 评估 Agent 从零构建 RAG 系统而非固定 pipeline，可借鉴为内部自动化检索策略搜索：让 LLM Agent
  自行实现 chunking、embedding、rerank 等模块，仅提供小规模验证集与反馈循环，替代大量人工消融实验。

  - 给 Agent 明确资源预算（6 小时 / 单卡 GPU）和开放代码空间的评测方式，可复用到 agentic AutoML 或实验平台：把时间、算力作为约束，让
  Agent 自己分析数据、写代码、读指标、迭代，比固定超参搜索更灵活。

  - 结果说明通用 LLM Agent 在 RAG 系统自动开发上已具竞争力；但在业务中建议作为初始方案生成器或优化器，结合领域先验与人工 review，避免全自动上线黑盒系统。

  - 从 human-designed 系统出发，Agent 平均提升 16.6 分，说明可把现有线上检索/生成链路作为起点，让 Agent 在受限搜索空间内迭代优化，保留核心机制，降低风险并提取增量收益。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：RAG 系统效果依赖大量任务特定工程选择（语料处理、检索策略、生成配置），不同任务/领域的最优设计差异大，人工迭代成本高。随着 LLM Agent 能力增强，需要系统性回答：Agent 能否自主从零构建 RAG 系统，并通过实验反馈有效迭代。

**方法关键点**：AutoRAGBench 包含 9 个 RAG 开发任务，在开放代码空间中评测 Agent；Agent 无 starter code、无预设策略，仅在单张 H800 GPU、6 小时预算内分析任务数据、实现 RAG pipeline、根据指标反馈迭代。评测覆盖 9 种 Agent 配置，既看最终系统得分，也分析开发轨迹；还额外评测从 Human-SOTA 系统起点继续优化的能力。

**关键结果**：GPT-6.1 Sol + Codex CLI 配置平均得分最高，为 56.1；Human-SOTA 组合基线平均 44.4。在 7 个任务上，从 human-designed 系统出发，GPT-6.1 Sol + Codex CLI 平均再提升 16.6 分，同时保留原有方法核心机制。结果表明 LLM Agent 已能自动化构建有效 RAG 系统，并可作为已有系统的迭代优化器。
