---
title: Intent-Driven Situation Tracking for User-Centric Multi-Turn Agents
title_zh: 用户中心多轮智能体的意图驱动情境追踪
authors:
- Meiling Tao
- Yiling Tao
- Peng Wang
affiliations:
- University of Electronic Science and Technology of China
- Shenzhen International Graduate School, Tsinghua University
arxiv_id: '2608.15755'
url: https://arxiv.org/abs/2608.15755
pdf_url: https://arxiv.org/pdf/2608.15755
published: '2026-08-16'
collected: '2026-08-18'
category: Agent
direction: Agent 情境状态追踪
tags:
- Intent Tracking
- Situation State
- Multi-turn Agents
- Tool Use
- Constraint Propagation
- Context Management
one_liner: 提出训练无关的IDSS框架，显式分离工具事实与任务状态，通过约束传播提升多轮Agent完成率与效率
practical_value: '- 在电商多轮导购/客服 Agent 中，可把工具返回（商品、订单、库存、履约）解析为带 provenance 的结构化事实层，与“用户目标/缺失变量/约束”状态分离；这能显著降低长对话中的事实遗漏和错误执行。

  - 借鉴跨层约束传播：把预算、配送时效、库存/券可用性、退换政策等建模为可被新事实更新的约束；一旦违反就 block 不可行意图并自动激活替代路径，减少无效工具调用和违规下单。

  - 用 <state> 块让 LLM 自更新任务状态并回注下一轮 prompt，不增加额外 LLM 调用；同时把历史中的原始工具返回替换为事实层引用，可低成本控制
  prompt 长度，适合线上低延迟场景。

  - 变量打标 askable / retrievable / derivable 可指导 agent 何时问用户、调工具或推导，尤其适合需要偏好澄清的电商导购与推荐式对话。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

动机：用户中心多轮 Agent 需要同时处理多意图、逐步释放的偏好、工具事实与执行约束，但大多数上下文管理方法只压缩/检索历史，Agent 仍需从混合痕迹中隐式重建当前情境，容易产生事实遗漏、意图漂移和约束违反。

方法关键点：
- IDSS 训练无关，维护显式情境状态 Dt=(Ft,St)，把工具事实与任务判断分离。
- 事实层用确定性解析将工具返回转成带 provenance 的实体/属性，支持 ADD/UPDATE/DELETE/MERGE，冲突按来源可信度处理；历史中的工具返回被替换为事实引用，压缩提示。
- 状态层跟踪意图 active/pending/completed/blocked、变量 askable/retrievable/derivable 及约束 satisfied/unsatisfied/violated；Agent 每轮输出 <state> 块，解析后回注，零额外 LLM 调用。
- 跨层约束传播在新事实更新时重估约束，违反则 block 关联意图并激活可行替代路径。

关键结果：在 τ-bench、VitaBench、UserBench 三个交互基准上，8 个 LLM 中 IDSS 整体领先 ReAct、StateAct、ReSum、IterResearch、U-Fold。τ-bench Airline 比最强基线 U-Fold 高 1.5 Avg@4 和 2.0 pass4；VitaBench OTA/Cross-domain 分别高 1.7/2.1 分；UserBench Score 相对 U-Fold 提升约 4.6%，CER 提升约 4.0%。消融显示事实层对 τ-bench 影响最大（Avg@4 -2.2），状态层对 UserBench 影响最大（Score -8.4%）。错误分析中事实遗漏从 14% 降到 8%，缺失信息错误从 8% 降到 5%。效率上以最少平均 7.8 轮达到最高平均 50.5% 任务完成。

最值得记住：可靠的用户中心 Agent 需要显式、面向决策的情境状态，而不是只靠历史访问。
