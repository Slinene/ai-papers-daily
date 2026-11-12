---
title: 'WMIP: A Working-Memory-Inspired Programmable Probe of Cumulative State Tracking
  in Large Language Models'
title_zh: WMIP：受工作记忆启发的 LLM 累积状态跟踪可编程探针
authors:
- Dengzhe Hou
- Lingyu Jiang
- Deng Li
- Zirui Li
- Fangzhou Lin
- Kazunori D Yamada
affiliations:
- Tohoku University
- Lappeenranta-Lahti University of Technology LUT
- Texas A&M University
- Worcester Polytechnic Institute
arxiv_id: '2603.27343'
url: https://arxiv.org/abs/2603.27343
pdf_url: https://arxiv.org/pdf/2603.27343
published: '2026-10-29'
collected: '2026-11-12'
category: Eval
direction: LLM 工作记忆与状态跟踪评测
tags:
- state tracking
- working memory
- LLM evaluation
- protocol sensitivity
- cumulative updates
- tool use
one_liner: 提出可编程评测探针 WMIP，量化 LLM 在单 prompt 内隐式累积状态跟踪能力及协议敏感性
practical_value: '- 在电商 Agent 或对话推荐中，若需要模型在单 prompt 内隐式更新购物车、用户偏好或筛选条件，不要依赖模型隐式记忆：核心条目
  3–7 次更新后准确率仅 31.7%，50 次更新后归零，应显式维护状态或要求模型写出中间步骤。

  - 可将 WMIP 的协议约束迁移到 prompt 工程：要求模型把最终答案放在最后一行、明确写步骤，可显著提升累积跟踪准确率（31.7% → 88.0%），且提升主要来自指令变化而非
  token 预算。

  - 在选型用于多轮工具调用或状态跟踪的 LLM 时，可参考其 Berkeley Function Calling Leaderboard 分数，该分数与 WMIP
  核心准确率正相关。

  - WMIP 的生成器可脚本化产生 3–100 次更新的回归测试集，适合在业务侧构建针对状态跟踪能力的自动化评测与模型上线门槛。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：LLM 在单 prompt 内维护并更新累积状态（类似人类工作记忆）是理解叙述、跟踪指令、多轮工具调用等场景的基础能力；但现有测试对是否允许写出中间步骤约束不一，导致难以测量真实的隐式状态跟踪能力。

**方法关键点**：提出 WMIP，一个受工作记忆启发的可编程探针。用程序计算答案，覆盖 3–100 次更新，支持 final-state、intermediate-state、multi-target 三类查询；在相同条目上比较不同输出协议，包括是否写步骤、答案位置、token 预算等。

**关键结果**：在 18 个 LLM 上，单步算术准确率达 84.9%，但要求 3–7 次更新后给出一个数字的核心条目准确率仅 31.7%；从 50 次更新起，所有模型准确率不超过 10%。在更大预算并指令要求写步骤、将答案放最后一行时，核心准确率升至 88.0%，分析表明提升主要来自指令变化而非预算。核心准确率与 Berkeley Function Calling Leaderboard 分数正相关。结论：强单步算术不保证可靠累积跟踪，输出协议显著改变测量准确率；项目开源生成器、条目、评分代码与模型响应。
