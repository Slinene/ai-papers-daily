---
title: 'Plover: Steering GUI Agents through Plan-Centric Interaction'
title_zh: Plover：以计划为中心的人机协同 GUI Agent 系统
authors:
- Madhumitha Venkatesan
- Shicheng Wen
- Jiajing Guo
- Jorge Piazentin Ono
- Liu Ren
- Dongyu Liu
affiliations:
- University of California, Davis
- Bosch Research North America
arxiv_id: '2607.15193'
url: https://arxiv.org/abs/2607.15193
pdf_url: https://arxiv.org/pdf/2607.15193
published: '2026-07-16'
collected: '2026-07-19'
category: Agent
direction: GUI Agent 的可监督规划与交互修正
tags:
- GUI Agents
- Plan-Centric Interaction
- Human-in-the-Loop
- Replanning
- Mixed-Initiative
- Interactive Task Automation
one_liner: 通过将任务计划外化为可编辑的交互工件，让用户能局部修正 Agent 行为而保持进度
practical_value: '- **在业务 Agent 中暴露执行计划**：对搜索推荐系统的多步调用（如意图解析→召回→排序→文案生成），可将内部步骤结构化为可读的计划树，让产品或运营人员实时查看、暂停或修改中间决策。

  - **支持局部编辑与进度保持**：当 Agent 某一步出错（如误判意图），允许直接编辑该步参数或替换子任务，而不丢弃已完成的有效步骤，避免全盘重试带来的延迟和算力浪费。

  - **结合自然语言与界面截图交互**：对于电商后台配置、广告创编等 GUI 密集型任务，可以借鉴自然语言指导与截图标注干预，让领域专家无需懂代码即可修正 Agent
  行为。

  - **借助失败案例分析改进 Agent 设计**：通过显式记录计划执行轨迹，分析哪些步骤易出错，定向优化提示或模型，或积累常见修正模式用于主动提示用户或自动修复。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：现实 GUI 自动化中，动态布局、意外弹窗等常使视觉-based Agent 行为偏离用户意图，而其规划与调整过程不透明，用户无法有效监督或修正。

**方法关键点**：提出 Plover，一个 planner-executor 架构：
- 任务规划被外化为持久化、可检查、可编辑的 artifacts，用户可随时介入；
- 支持局部修正：通过编辑计划节点、自然语言指导、截图标注等方式，仅调整出错部分，保留已完成进度；
- 通过形成性研究（6 名参与者）来优化交互设计，确保可用性。

**关键结果**：
- 在基准测试的失败案例修复中，发现许多 GUI Agent 的失败是结构上可修复的，当计划可见且介入局部化时；
- 显式重规划让自动化更透明、可控、可适应。
