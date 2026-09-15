---
title: 'RESKILL: Explicit Failure Attribution and Structured Repair for Interactive
  Language Agents'
title_zh: RESKILL：交互式语言 Agent 的显式失败归因与结构化修复
authors:
- Mengyi Deng
- Xin Li
- Duyi Pan
- Zilin Wang
- Zhiwei Li
- Zhijiang Guo
- Wei Wang
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- The Hong Kong University of Science and Technology
arxiv_id: '2609.15684'
url: https://arxiv.org/abs/2609.15684
pdf_url: https://arxiv.org/pdf/2609.15684
published: '2026-09-14'
collected: '2026-09-15'
category: Agent
direction: Agent 技能失败归因与结构化修复
tags:
- Language Agents
- Skill Repair
- Failure Attribution
- Retest-Conditioned Update
- Self-Refinement
one_liner: 提出 RESKILL，通过显式失败归因、覆盖度归因选择局部技能补丁及重测条件更新，显著提升交互式语言 Agent 的修复效果
practical_value: '- 在电商推荐/广告策略 Agent 中，用「覆盖度归因」替代全量重写：失败后仅对覆盖失败解释的局部技能或提示词打补丁，避免影响无关行为，降低回归风险。

  - 显式维护修复状态（repair state）：记录失败假设、候选补丁、重测结果，使迭代修复可追溯；可将此数据结构纳入线上推荐 Agent 的调优流程，便于人工审核与回滚。

  - 将「重测失败」也作为后续修复的输入：不丢弃不成功的 retest，而是用它更新活跃失败解释，让模型在下一轮聚焦未解决问题；适用于多轮策略搜索、query 改写、工具调用等需要反复试错的场景。

  - 把 LLM 生成的修复因子结构化（如 JSON 字段：failure_hypothesis, patch, coverage），由程序控制选择与更新，而不是依赖一次性的自然语言
  reflection；工程实现上可复制此模式，提升修复的稳定性和可复用性。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：语言 agent 依赖可复用技能，但失败后的修复常采用不透明的一次性 reflection——直接生成技能补丁，没有显式维护失败解释与候选修复之间的关联，也未利用重测结果指导后续编辑，导致修复不持续、易引入副作用。

**方法关键点**：RESKILL 维护跨轮次的显式修复状态。给定失败 rollout，将失败假设与候选技能补丁链接；通过 coverage-based attribution 选择局部补丁，即比较候选补丁对活跃失败解释的覆盖程度，优先修复最相关技能；在环境中重测编辑后的技能集，并将重测结果（尤其失败）纳入后续修复轮次。LLM 负责生成结构化修复因子，修复程序记录这些因子并主导选择与更新，形成“归因—补丁—重测—再归因”的闭环。

**关键结果**：在 ALFWorld 和 TextCraft 两个环境、三种模型规模、固定修复预算下，RESKILL 在所有 6 个 benchmark-model 设置中均取得最高最终成功率，平均比 direct repair 高 3.7 个百分点，比 hypothesis-conditioned repair 高 3.3 个百分点。结果表明，显式归因本身不够，持久的改进源于归因、修复选择与重测条件更新的整合。
