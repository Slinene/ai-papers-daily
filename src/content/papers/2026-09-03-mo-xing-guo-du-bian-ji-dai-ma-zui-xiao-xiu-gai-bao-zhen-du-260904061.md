---
title: 'When Models Edit Too Much: On the Fidelity of Minimal Code Edits'
title_zh: 模型过度编辑：代码最小修改保真度研究
authors:
- Tongyao Zhu
- Wei Hern Lim
- Min-Yen Kan
affiliations:
- National University of Singapore
arxiv_id: '2609.04061'
url: https://arxiv.org/abs/2609.04061
pdf_url: https://arxiv.org/pdf/2609.04061
published: '2026-09-03'
collected: '2026-09-06'
category: Other
direction: LLM 代码修复 · 编辑保真度
tags:
- LLM
- code repair
- edit fidelity
- minimal edits
- reinforcement learning
- evaluation
one_liner: 提出可度量的编辑保真度指标，发现LLM普遍过度编辑，保留指令与RL训练能有效减少不必要修改
practical_value: '- 在推荐/广告系统中用 LLM 自动修改策略配置、特征代码、SQL 或推荐逻辑时，要求模型只做必要修改、保持原有结构，可显著降低
  review 成本和意外行为风险。

  - 设计自动修复/优化 Agent 时，把 ''编辑距离'' 或 ''diff 大小'' 作为质量指标，而不只看正确性（如单测通过/线上效果），防止 Agent
  大面积重写导致难以审查和回滚。

  - 后训练选择：如果业务要求对未见过的新错误/新场景保持最小改动和性能，RL 比 SFT 更稳健；SFT 容易过拟合训练中见过的损坏模式，域外泛化差。

  - 评估框架可迁移：构造带已知最小补丁的合成损坏任务，用于系统性地度量 Agent 的编辑保真度，并纳入离线回归测试。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 越来越多用于自动修复代码，但实际开发中仅有正确性不够，补丁还应该最小、易于审查、忠实于原始实现。现有工作主要关注 Pass@1，忽略了过度编辑问题。作者提出“编辑保真度”（edit fidelity）作为独立质量维度。

**方法关键点**：从 400 个 BigCodeBench 题目构造评估框架，向参考解法注入受控的 AST 级损坏，使每个修复任务都有已知的最小补丁。对比前沿 LLM 的过度编辑行为，并分析保留指令（preservation instruction）、推理预算、模型规模对编辑保真度的影响。进一步探索后训练方式：比较 SFT 与 RL 学习最小编辑的效果。

**关键结果数字**：前沿模型普遍过度编辑，即使 GPT-5.5 也同时存在高 Pass@1 和过大补丁、增加认知复杂度。加入保留指令后，平均 excess Levenshtein distance 从 0.195 降到 0.131，added cognitive complexity 降低 26.6%，Pass@1 提高 2.3 个点。但增益并不随推理预算或模型大小单调提升。后训练中 SFT 对见过的损坏模式过拟合，RL 则给出最佳的域外编辑保真度和性能保留权衡。
