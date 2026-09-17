---
title: 'ProgramDistill: From Interactive Web Apps to Verifiable Reference-Guided SWE
  Tasks'
title_zh: ProgramDistill：从可交互 Web 应用构建参考引导的软件工程任务
authors:
- Jeonghye Kim
- Minseon Kim
- Young Jin Kim
- Matheus Pereira
- Marc-Alexandre Côté
- Alessandro Sordoni
- Xingdi Yuan
- Zhengyan Shi
affiliations:
- KAIST
- Microsoft Research Montréal
- Microsoft AI
arxiv_id: '2609.18805'
url: https://arxiv.org/abs/2609.18805
pdf_url: https://arxiv.org/pdf/2609.18805
published: '2026-09-15'
collected: '2026-09-17'
category: Eval
direction: 编码智能体评测基准
tags:
- benchmark
- coding agents
- reference-guided
- SWE
- interactive web apps
- replay verification
one_liner: 通过「挖掘-构建-补丁」流水线自动生成4,063个可回放验证的参考引导SWE任务，评测编码智能体
practical_value: '- 借鉴 mine-craft-patch 流水线：在电商前端/页面改版场景，可用可交互参考应用自动提取“特征-行为-金牌补丁”三元组，无需人工标注即可构建回归/代理评测集；回放验证机制能过滤不可验证行为。

  - 若团队用 LLM coding agent 做 A/B 实验落地或 UI 组件迁移，参考引导任务比 issue 描述更接近真实开发：agent 必须从运行中的参考版本推断隐式行为，适合评估“照原型实现”能力。

  - 可控制 restoration depth 的难度分级可直接复用为 curriculum：从补 1 个特征到补 8 个特征逐步增加上下文与依赖，用于训练或筛选
  agent，降低长任务失败率。

  - 关注 cumulative workflow 指标而不是单任务成功率：完整应用重构更贴近真实迭代，避免只优化孤立 patch。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：现有 coding agent 评测通常由 issue/指令明确指定行为，但真实 Web 开发中常需从可运行参考应用推断并补全不完整实现。方法：构建 ProgramDistill 基准，用 mine-craft-patch 流水线将 26 个应用分解为不同粒度特征，每个特征关联可回放行为与 gold patch，自动发现 1,975 个经回放验证的行为并生成 4,063 个任务。任务分 full-application reconstruction 与 partial-application reconstruction，通过隐藏参考源码、只允许交互来评估 agent 推断与实现能力。结果：在 9 个前沿编码 agent 中，GPT-6 Astra 与 Claude Opus 5 在 full-application 累积工作流上分别达到 49.2% 和 28.8%；partial 设置下随 restoration depth 从 1 增到 8，成功率分别由 100% 降到 64.0%、96% 降到 32%，显示任务难度可控且仍具挑战性。
