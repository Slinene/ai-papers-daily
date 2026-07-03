---
title: 'Adoption and Impact of Command-Line AI Coding Agents: A Study of Microsoft''s
  Early 2026 Rollout of Claude Code and GitHub Copilot CLI'
title_zh: 微软 2026 年 CLI AI 编码代理大规模推广的采纳与影响研究
authors:
- Emerson Murphy-Hill
- Jenna Butler
- Alexandra Savelieva
affiliations:
- Microsoft
arxiv_id: '2607.01418'
url: https://arxiv.org/abs/2607.01418
pdf_url: https://arxiv.org/pdf/2607.01418
published: '2026-07-01'
collected: '2026-07-03'
category: Other
direction: AI 编码工具组织采纳分析
tags:
- AI coding agents
- adoption
- productivity
- organizational rollout
- CLI tools
- Pull Request
one_liner: CLI 编码代理的采纳通过社交网络蔓延，活跃工程师更易保留，采纳后 PR 合并量提升 24%
practical_value: '- 推广内部 Agent 工具（如搜索/推荐系统的交互式开发助手）时，设计可见的“社交线索”（如团队使用看板、成功案例分享）可触发从众采纳，因为首用主要通过社交网络传播。

  - 识别可能长期使用 Agent 的用户时，更应关注其已有工作活跃度（如代码提交频率、任务执行量）而非岗位或资历，这与“保留率与编码活动而非人口统计相关”一致。

  - 衡量 Agent 对算法工程师产出的影响，可用类似“合并 PR”的操作指标（如成功上线的实验次数、发布模型版本数）作为简易代理，前提是明确该指标的局限性。

  - 大规模采购前，可在团队内小范围试点并追踪 token 消耗与产出增量，若 4 个月内提升效果不衰退则更值得全量推广。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

**动机**：企业大规模部署 CLI AI 编码代理（如 Claude Code、Copilot CLI）时，必须预判谁会试用、谁会留存，以及工具带来的产出能否覆盖数百万美元的 token 开销。本文通过在微软 2026 年初数万名工程师的早期推广中分析真实数据，旨在回答这三个核心决策问题。

**方法**：作者利用遥测数据追踪工程师对两个 CLI AI 编码代理的首次使用、持续使用行为，并以合并拉取请求数（merged PRs）作为产出代理。分析维度包括：首用的传播渠道（社交网络 vs. 单向通知）、留存与工程师特征（人口统计 vs. 编码活跃度）的关联，以及采纳后产出的因果效应（通过准实验对比采纳者与未采纳者的 PR 合并趋势）。

**关键结果**：首次使用主要通过同事间的社交影响传播，而非自上而下的邮件或文档；工程师的留存概率与其日常编码活动（如提交频率）强相关，与职级、工龄等人口统计属性弱相关；采纳者合并的 PR 数量平均提升了约 24%，且这一提升在四个月的观察期内持续存在，未出现衰退迹象。这些发现表明 CLI AI 编码代理的采纳并非均匀或短暂的尝鲜效应，组织应将“可见的同辈使用”作为推广策略的核心。
