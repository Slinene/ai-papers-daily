---
title: 'Object-Oriented Harness: Evolving Agent Harnesses through Object-Oriented
  Design'
title_zh: 面向对象 Harness：用继承与路由进化 Agent 执行框架
authors:
- Gaotang Li
- Bhavana Dalvi Mishra
- Yifei Ming
- Yanfei Chen
- Zhongying CuiZhu
- Lesly Miculicich
- Long T. Le
- Rui Meng
- Chun-Liang Li
- Hanghang Tong
affiliations:
- University of Illinois Urbana-Champaign
- Google Cloud AI Research
arxiv_id: '2610.28380'
url: https://arxiv.org/abs/2610.28380
pdf_url: https://arxiv.org/pdf/2610.28380
published: '2026-10-20'
collected: '2026-10-21'
category: Agent
direction: Agent harness 分层进化与路由
tags:
- Agent Harness
- Object-Oriented Design
- Harness Evolution
- Routing
- AutomationBench
- Tool Use
one_liner: 用继承构建可复用 harness 类并基于执行轨迹路由，三基准最高提升15.79个百分点
practical_value: '- 面向 Agent 工作流：不要用单一 global harness/prompt 硬扛所有场景。把 harness 代码按业务任务聚类做子类继承，公共能力留在父类，差异用
  override/add method，回归风险更小、维护更清晰。

  - 路由时同时输入 task metadata 和观测到的 base 执行轨迹（工具调用、错误模式、输出格式），并沉淀 routing lessons；在 AutomationBench
  这类跨域执行中，轨迹信息可带来 12.64 点提升，比仅看任务描述更可靠。

  - 保留 base harness 作为兜底，路由不确定或 OOD 任务直接复用 base 结果，避免强制用不合适的 specialist；论文中 OOD 场景下
  Base 复用保持 59.18 PASS，而 global harness 降到 44.90。

  - 训练/搜索效率：只在该任务簇上评估候选 harness，不必 rerun 整个发现集；可作为 LLM agent 自动化调参的工程优化，显著降低 API 成本（论文中搜索时长
  29h vs 109h）。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：Agent harness 是围绕 LLM 的可执行代码，决定 prompt、工具和控制流。单一 global harness 难以同时适配异构任务；全局优化中好的改动可能损害其他任务，甚至 easy 任务退化。对象继承天然适合表达共享与专用行为，因此提出 OO-Harness，用面向对象设计进化一套可继承的 harness 类族。

**方法关键点**：
- 用继承表示 harness：每个 specialized harness 是 base 或已有 specialized harness 的子类，可 override 或 add method，通过 super() 复用父类能力；执行时整个类在一个实例内运行。
- 训练阶段先跑 base harness 获取执行记录，按共享执行需求聚类任务；进化 agent 迭代选择 cluster + parent，生成子类并只在目标 cluster 上评估，避免重跑全量发现集。
- 每次 proposal 的成功/失败会更新 design lessons 和 routing lessons；被拒绝多次的 cluster 降低搜索优先级。
- 测试阶段由 harness router 根据 task、observable base trajectory 和 frozen routing lessons 选择 base 或某个 specialized harness；不确定时复用 base 结果，不碰 grader。

**关键实验结果**：
- 在 AutomationBench、Workspace-Bench、Toolathlon-GYM 三个长程基准上，OO-Harness 均取得最高 primary score。AutomationBench Mean 77.41 vs base 61.62，绝对提升 15.79 个百分点；Toolathlon-GYM PASS 37.45 vs base 31.15。
- 相比 Meta-Harness 全局优化，搜索时长从 109.1h 降到 29.0h，且 held-out 得分更高。
- 路由消融：轨迹信息在 AutomationBench Mean 上带来 +12.64，Toolathlon PASS +4.37；Workspace-Bench 上只 +0.53，说明任务类型明显的场景轨迹增益较小。
- 继承消融：OO 40.56 > Flat 35.60 > Base-reset 29.39，证明继承比拷贝代码或每次从 base 重写更有效。
- OOD 设置中保留 Base 选项可避免泛化损失：OO-Harness 复用 Base 保持 59.18 PASS，而 Meta-Harness 只有 44.90。

**最值得记住的一句话**：把 harness 当代码类来继承与路由，比训练一个全局 harness 更稳、更省、更可泛化。
