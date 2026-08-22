---
title: 'SWE-bench Science: Can Coding Agents Resolve Engineering Tasks in Science?'
title_zh: SWE-bench Science：编码智能体能解决科学工程任务吗？
authors:
- Zhipeng Xu
- Jiahao Lu
- Yining Zheng
- Yuxin Wang
- Xipeng Qiu
affiliations:
- Shanghai Innovation Institute
- Fudan University
arxiv_id: '2608.19799'
url: https://arxiv.org/abs/2608.19799
pdf_url: https://arxiv.org/pdf/2608.19799
published: '2026-08-19'
collected: '2026-08-22'
category: Eval
direction: Coding Agent 评估 · 科学软件工程基准
tags:
- Coding Agents
- Benchmark
- Scientific Software
- Failure Analysis
- LLM
- SWE-bench
one_liner: 提出含119个任务、覆盖20个科学领域的仓库级科学软件工程基准，最佳编码智能体pass@1不足50%，并归纳四类失败机制
practical_value: '- 在推荐/搜索 Agent 中引入领域知识（类似 RAG 或 tool/context）时，要区分「高质量 grounding」与「弱对齐指导」：前者可提升平均性能并降低
  token 成本，后者会诱导 anchoring，反而不提升精确修复。落地时建议做 A/B 或消融评估，不要默认注入更多领域知识一定更好。

  - 论文把失败归为四类：知识/抽象不足、探索误导、修复覆盖/系统集成缺失、跨案例泛化不足。这可以迁移为 Agent 故障诊断框架，在电商场景下为推荐解释、代码生成、自动调参等
  Agent 建立错误分类看板，针对四类分别改进 memory、search/tool 使用、集成测试与 few-shot 策略。

  - 基准的三类任务范式 Issue-driven / Expert-exploratory / Engineering-integration 可用于设计 Agent
  评估集：不只基于用户 issue 做修复，还要加入专家探索性任务和跨系统集成任务，能暴露真实业务 Agent 的鲁棒性问题。

  - 成本敏感场景可同时监控「精确成功」和「token 效率」，高质量知识上下文即使不提升 exact match，也可能通过减少 token 消耗提升业务收益。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**
科学软件已成为科研仪器的一部分，代码缺陷不仅影响程序行为，还可能动摇科学结论。但现有 coding agent 评估只关注聚合成功率，缺少对失败原因的结构化分析。

**方法**
发布 SWE-bench Science，一个仓库级科学软件工程基准，包含 119 个任务、来自 98 个 GitHub 仓库、覆盖 20 个科学领域；任务分为三类：Issue-driven、Expert-exploratory、Engineering-integration。在多种 coding agent 上进行评测，并对失败样本做归类，同时用配对消融检验科学指导的作用。

**结果**
最佳智能体 Claude Code + Opus-5 (max) 的 pass@1 仍低于 50%。失败机制集中在四类：科学知识/抽象不足、探索误导或表面修复、修复覆盖/系统集成不全、无法将科学知识泛化到新案例。消融显示，科学知识并非总有益：高质量、对齐好的信息能约束修复、改善平均性能和 token 效率；而弱对齐指导会造成 anchoring，并未提升精确修复成功率。
