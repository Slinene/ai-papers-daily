---
title: The Value of Memory in Language Agents
title_zh: 语言智能体记忆的价值
authors:
- Zehao Lin
- Erenkai Zhu
- Helan Hu
- Xixuan Hao
- Chunyu Li
- Kai Chen
affiliations:
- MemTensor
- Shanghai Jiaotong University
- The Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2610.31303'
url: https://arxiv.org/abs/2610.31303
pdf_url: https://arxiv.org/pdf/2610.31303
published: '2026-10-22'
collected: '2026-10-24'
category: Agent
direction: Agent 记忆价值决策论
tags:
- Agent Memory
- Decision Theory
- Risk-Cost
- Retrieval
- Evaluation
- Lifecycle
one_liner: 提出决策论框架，量化记忆在保留、使用、恢复与修订中的价值，并用反例和诊断揭示信息时序、检索接口、读策略与需求不确定性的作用
practical_value: '- **把存储内容和 reader 使用分开评估**：线上 Agent 记忆系统故障时，不要只看检索命中。可以固定 reader，对比不同持久化状态（例如完整日志
  vs 摘要 vs 索引）的 realized value；再用固定证据、换 reader 评估使用缺陷。这能避免把“没存”和“没用”混为一谈。

  - **存 locator 而非完整内容**：论文的 pointer 例子显示，一个与答案互信息为 0 的地址指针，能把付费恢复成本从期望 2.5 次读取降到
  1 次。在电商/推荐 Agent 中，记忆可以存用户会话的检索键、商品 ID 索引或版本号，而不是完整上下文；需要时通过 BM25 或 database read
  获取，兼顾容量与延迟。

  - **写记忆时考虑未来 query 是否已知**：query-agnostic 写入需要更多容量保留区分度。构建用户级 memory 或 session 摘要时，如果未来任务是开放式的，不要过早做不可逆压缩；保留可恢复路径（比如原始日志指针），按需求概率和恢复成本做分配。

  - **把测量过程 J 和系统 Σ 分离**：论文中同一输出在 strict operation rule 下 17/28 接受，consequence-based
  check 下 22/28 接受，差异 17.9 个百分点。做线上 A/B 或 offline eval 时，应固定评分规则、损失定义和 label 标准，否则会把
  scorer 变化误判为记忆系统改进。

  - **修订时记录依赖关系，按依赖闭包更新**：不要按项目/文档边界更新记忆。记录 source、object、version、reason，商品属性或用户偏好变化时，只更新受影响的结论、计划和缓存，减少误改和遗漏。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
语言 Agent 长期运行中，记忆从历史到持久状态、读取、恢复、修订，价值取决于哪些信息被保留、有界 Agent 是否能用、以及未来需求变化时能否低成本恢复或修订。现有工作常把信息量、使用效果和评估规则混在一起，导致无法定位记忆系统失败原因。

**方法关键点**
- 用统一的任务损失单位定义 potential value、retained value 和 realized value，区分最优风险 R*(M) 与固定 reader 的实际风险 R(π,M)，并定义实现遗憾 Gπ(M)。
- 提出成本感知仿真条件（Proposition 1）：如果新表示在预算 b+δ 下能仿真旧策略的交互轨迹，则最优风险不劣于旧表示。
- 给出五个最小反例：① 查询时序影响所需容量，写前知道 query 时 n 位历史只需 1 bit；② 零互信息的 pointer 可大幅降低付费检索成本；③ 记忆与 reader 增益互补，分开归因需要固定另一侧；④ 交互反馈下两个策略的排序可能与 forced replay 完全相反；⑤ 未来需求不确定时不同记忆各有优劣，必须保留风险剖面。
- 将测量过程 J 与系统 Σ 分离，要求比较契约明确信息时序、接口、策略、需求、损失、资源和测量规则。
- 提出三个可测试设计假设：后果感知分配、保留未来恢复选项、依赖导向修订。

**关键实验**
- LoCoMo 12 问题诊断：saved ledger 单独 F1 仅 0.016，加 BM25 bounded recovery 后提升到 0.329；complete history 只有 0.123，而换用 short-answer 指令后达到 0.512，说明分数主要由 reader 接口和任务损失决定，而非仅信息量。
- Pointer 构造：N=4 时 I(M;Y)=0，但期望读取次数从 search 的 2.5 降至 pointer 的 1；一次读取预算下风险从 3/8 降至 0。
- 两项目更新：28 次 reader 评测中，strict operation rule 接受 17 个完整 artifact，consequence-based check 接受 22 个，差异 5/28（17.9 个百分点），仅由测量规则变化导致，未改变任何 Agent 输出。

**最值得记住的一句话**
记忆的价值取决于它支撑的未来决策，而不仅是存储的信息量；固定 reader 和测量规则会系统性改变观测到的记忆价值。
