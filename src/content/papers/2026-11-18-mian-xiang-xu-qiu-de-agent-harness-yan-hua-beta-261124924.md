---
title: 'Agentic Harness Engineering Beta: Requirement-Centered Evolution of Agent
  Harnesses'
title_zh: 面向需求的 Agent Harness 演化：Beta
authors:
- Jiahang Lin
- Jiahao Chen
- Yiding Wang
- Shichun Liu
- Chengjun Pan
- Shihan Dou
- Honglin Guo
- Yuyang Hu
- Changhao Jiang
- Zhenhua Han
affiliations:
- Fudan University
- Peking University
- Renmin University of China
- Shanghai Qiji Zhifeng Co., Ltd.
arxiv_id: '2611.24924'
url: https://arxiv.org/abs/2611.24924
pdf_url: https://arxiv.org/pdf/2611.24924
published: '2026-11-18'
collected: '2026-11-19'
category: MultiAgent
direction: 需求驱动的 Agent Harness 演化
tags:
- Agent Harness
- Requirement-Centered Evolution
- Multi-Agent
- User Simulator
- Pass@1
one_liner: AHE-Beta 用需求中心循环（模拟用户提 issue + 团队修改 + 需求驱动选择）将 held-out pass@1 从 21.9%
  提到 33.3%。
practical_value: '- 在电商/搜索推荐 Agent 的 prompt、工具和中间件迭代中，引入模拟用户多轮交互并提交 issue 的需求驱动流程，而不是只看点击率/转化率等指标，可以暴露隐式需求（如
  query 歧义、约束变更、偏好漂移），避免只在离线 benchmark 上过拟合。

  - 采用“多角色团队修改 + 需求评审合并”代替单 Agent 打补丁：每次变更必须解决一个已验证需求才合入，能在 agentic 推荐链路（工具选择、检索策略、结果解释）上产生更通用的改进。

  - AHE-Beta 比 Base Harness 少用 40.8% token，说明需求驱动的选择能淘汰低效改动；在线上多模型 A/B 中可复用其“harness
  与模型解耦”的架构，使工具/prompt 优化在不同底层 LLM 上迁移。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

动机：现有 agent harness 进化只用单一进化 agent 按 benchmark 分数修改，忽略隐式需求和交互需求，容易产生窄补丁和 benchmark 特定局部最优。

方法关键点：AHE-Beta 提出需求中心循环，包含三步：1) 用户驱动评估：模拟用户多轮使用 harness 并将其需求以 issue 形式提出；2) 团队式修改：多角色团队把需求实现为可泛化改动，而非任务特定补丁；3) 需求驱动选择：仅当改动解决已验证需求并通过评审才合并。

关键结果：在 held-out 任务上，AHE-Beta 将 pass@1 从 21.9% 提升到 33.3%，同时 token 使用比 Base Harness 低 40.8%；超过 Claude Code、Meta-Harness 和 AHE。盲测人类 A/B 中，真实用户在 48 个有效对里 31 次偏好 AHE-Beta，五个维度评分均更高，且与模拟用户偏好方向一致。无需进一步演化，收益直接迁移到 GLM-5.3 和 DeepSeek-V4.1-Flash，pass@1 分别提升 15.8% 和 5.3%。
