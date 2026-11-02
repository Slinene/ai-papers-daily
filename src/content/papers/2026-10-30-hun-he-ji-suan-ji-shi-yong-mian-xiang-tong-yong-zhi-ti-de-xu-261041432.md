---
title: 'Hybrid Computer Use: A Unified Programmatic, Semantic, and Visual Interface
  for General Agents'
title_zh: 混合计算机使用：面向通用智体的程序化、语义与视觉统一接口
authors:
- Haoqing Wang
- Xiaoyi Zhang
- Sicheng Fan
- Zhexin Zhang
- Xinjie Zhang
- Jiahao Li
- Bin Li
- Yan Lu
affiliations:
- Microsoft Research
- Fudan University
- Tsinghua University
arxiv_id: '2610.41432'
url: https://arxiv.org/abs/2610.41432
pdf_url: https://arxiv.org/pdf/2610.41432
published: '2026-10-30'
collected: '2026-11-02'
category: Agent
direction: 多通道接口的通用计算机使用 Agent
tags:
- Computer Use
- Agent Interface
- Accessibility
- GUI
- Programmatic
- OSWorld
one_liner: 统一代码/CLI、无障碍语义AX与GUI视觉三通道，让智体灵活选择组合，在OSWorld 2.0上取得最高分
practical_value: '- 电商/广告自动化 Agent 可直接借鉴多通道设计：对内部系统优先暴露 API/CLI 程序化通道，对前端页面提取 AX 语义树而非只给截图，减少
  LLM 对像素的推理负担。

  - 动作批量执行 + 紧凑 diff 观察：将多个可独立操作合并为 batch，返回状态变更前后的差异（AX diff），避免逐步骤截图和往返，显著降低长流程任务的成本与时延。

  - 通道切换时引入 stale-state 防护：在 Agent 执行跨系统任务时，维护各通道状态版本并在切换前校验刷新，防止过期状态导致错误操作，对广告投放、订单处理等高风险场景尤其重要。

  - 为 LLM 提供通道选择 skill：编写接口选择手册，让模型根据任务类型（数据查询走程序化、页面操作走 AX、复杂视觉走 GUI）路由到最有效通道，减少自由探索成本。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

**动机**：现有计算机使用 Agent 以截图和鼠标键盘为主，反复解析屏幕、忽略语义和程序化能力，效率低且交互成本高。

**方法**：提出 Hybrid Computer Use (HCU)，统一三通道——程序化（代码/CLI）、语义（无障碍 AX）、视觉（GUI）。核心设计包括：
- 高效 AX 交互：返回紧凑观察、批量执行动作、以 AX diff 报告效果，减少往返次数；
- 通道切换时的 stale-state 防护，避免状态过期导致错误动作；
- 附加 HCU skill 指导模型选择合适的通道组合。

**结果**：在 OSWorld 2.0 上，HCU 获得最高的 Partial 和 Binary 分数，例如 HCU(GPT-6 Astra) 达 72.37%，超过 CUA Driver(GPT-6 Astra) 的 68.82% 和 Claude Opus 5 的 68.31%。所有评估模型在 HCU 下均有提升，不同模型在通道分配上表现不同，但效率和任务成功率均优于基线。
