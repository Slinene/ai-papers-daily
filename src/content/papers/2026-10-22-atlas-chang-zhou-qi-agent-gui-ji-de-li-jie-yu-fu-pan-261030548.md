---
title: 'Atlas: Making Sense of Long Horizon Agent Trajectories'
title_zh: Atlas：长周期 Agent 轨迹的理解与复盘
authors:
- Sangho Suh
- Joseph Chee Chang
- Pao Siangliulue
- Amy X. Zhang
- Matt Latzke
- Jonathan Bragg
- Doug Downey
- Daniel S. Weld
affiliations:
- Allen Institute for AI
- University of Washington
arxiv_id: '2610.30548'
url: https://arxiv.org/abs/2610.30548
pdf_url: https://arxiv.org/pdf/2610.30548
published: '2026-10-22'
collected: '2026-10-24'
category: Agent
direction: 长程 Agent 轨迹可视化与复盘
tags:
- Agent
- Trajectory Visualization
- Sensemaking
- Decision Transparency
- Human-AI Interaction
one_liner: 用轨迹树和产物投影，把长程 Agent 运行表示为目标-决策-产物三层，提升决策透明和复盘效率
practical_value: '- 在电商/广告 Agent 流水线（选品、投放策略、搜索 query 生成/改写）中，不仅记录最终产出，也记录 trajectory
  tree 的决策节点：采取的、搁置的、排除的方向和理由，便于事后审核与调优。

  - 借鉴 artifact projection：对同一批中间产物（商品候选集、query 候选、广告文案）提供表格/时间线/图等多视图切换，并支持从产物反查产生它的决策节点，降低复盘成本。

  - 把“决策透明度、artifact 可理解度、与业务目标的关联”作为 Agent 产品验收指标；Atlas 的 goal/decision/artifact
  框架可迁移为“业务目标-策略决策-候选产物”。

  - 交互上，用可展开的 branching tree 做运行回放，比线性日志更能暴露 Agent 在长程任务中的错误分叉或过早排除选项。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

动机：AI Agent 已能执行长周期科研任务（检索文献、生成假设、分析数据、跑实验），但研究者事后难以理解 Agent 做了什么、关键决策如何形成、是否服务原始目标。
方法关键点：将事后复盘建模为三层表示问题——goal（目标）、decision（决策）、artifact（产物）。开发 Atlas：轨迹树展示分支结构，包括被选择、搁置、排除的方向及理由；artifact projection 对同一组产物提供 6 种表示（表格、时间线、图等），并支持 artifact 与决策节点双向跳转。
结果：N=14 的 within-subjects 研究显示，相比 baseline，Atlas 在决策透明度、产物理解和目标关联上评分更高，主观 workload 明显更低。
