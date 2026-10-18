---
title: 'Task-State Governance: A Virtual Machine for Verifiable and Recoverable GUI
  Agent Execution'
title_zh: 任务状态治理：一种可验证、可恢复的 GUI 代理执行虚拟机
authors:
- Wenkui Yang
- Yiming Hao
- Kai Zhou
- Chengyu Pu
- Yuzhe Zhang
- Jie Cao
- Jin Huang
- Shuai Ma
- Feng Tian
affiliations:
- SAIS, University of Chinese Academy of Sciences
- Institute of Automation, Chinese Academy of Sciences
- Meituan
- Peking University
- Institute of Software, Chinese Academy of Sciences
arxiv_id: '2610.20100'
url: https://arxiv.org/abs/2610.20100
pdf_url: https://arxiv.org/pdf/2610.20100
published: '2026-10-14'
collected: '2026-10-18'
category: Agent
direction: GUI Agent 状态治理与恢复
tags:
- GUI Agent
- Task-State Governance
- Recoverable Execution
- Verification
- Human-in-the-loop
- Interaction Paradigm
one_liner: 提出 TaskVM，将 GUI 任务建模为可编辑契约，实现可验证与可恢复的代理执行
practical_value: '- 将任务建模成 Desired / Preserve / Observed 三栏契约：在电商运营、广告投放等 Agent 流程中，允许用户编辑期望结果与“必须保持不变”的字段，减少执行漂移带来的失控。

  - 对每个 Agent 动作预标记 reversible / compensatable / irreversible：尤其适用于改价、发券、调整预算等高风险操作，便于在执行前评估恢复成本，提供回滚或补偿机制。

  - 采用独立 verifier，只依赖 fresh visible observation 验证目标是否满足，不信任 Agent 自身回报；可迁移到生成式推荐/Agent
  pipeline 的结果验证，例如页面元素是否出现、按钮状态是否改变。

  - 将用户编辑写回真实 GUI 操作：在自研自动化平台中实现可编辑控件与真实界面动作绑定，让业务人员直接修改任务参数后自动执行，提升控制感和信任感。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

**动机**：GUI Agent 在真实应用中执行跨应用工作流时，若执行发生漂移，用户很难判断哪些状态被意外修改、哪些应保持、哪些可以恢复。现有 Plan-centric 接口让用户监督过程，但用户真正关心的是应用状态变化，而不是代理的内部计划。

**方法关键点**：提出 task-state governance 交互范式，将任务表示为可编辑契约，包含期望结果（desired）、必须保持的事实（preserve）和观测到的应用状态（observed）。TaskVM 实例化该范式：将实时状态投影为可编辑任务控件；用户编辑被转换为真实 GUI 动作执行；通过独立观察验证结果，只信任 fresh visible observation；每个动作被标记为 reversible、compensatable 或 irreversible。

**关键结果**：在自动化契约基准、受控用户研究和开放 live-model 探索中，任务契约显著提升了契约合规性、用户恢复控制感和信任度，同时执行结果保持稳定（摘要未给出具体数字）。
