---
title: 'GRASP: Generating, Revising, and Assessing for Strategic Planning with Agentic
  AI'
title_zh: GRASP：面向战略规划的生成、修订与评估智能体框架
authors:
- Arunabh Srivastava
- Mohammad A.
- Khojastepour
- Srimat Chakradhar
- Sennur Ulukus
affiliations:
- University of Maryland, College Park
- NEC Laboratories America, Inc.
arxiv_id: '2609.30147'
url: https://arxiv.org/abs/2609.30147
pdf_url: https://arxiv.org/pdf/2609.30147
published: '2026-09-24'
collected: '2026-09-25'
category: Agent
direction: LLM Agent 多阶段战略规划优化
tags:
- Agentic Planning
- LLM Agents
- Strategy-aware
- Multi-stage
- Context Isolation
one_liner: 通过生成宏观指南、隔离探索局部策略、独立评估轨迹，提升LLM在复杂规划任务上的可靠性
practical_value: '- 在电商/搜索推荐 Agent 工作流中，把“全局策略生成”“局部候选探索”“结果评估”拆成独立上下文模块，避免把所有约束塞进同一个
  prompt，减少长指令下的约束冲突和注意力衰减。

  - 借鉴 GenPlan 将业务规则、推荐 policy、多目标约束预编译为宏指南，后续生成或改写 query/文案/推荐策略时只引用指南，不重复展开全部细节，可提升长链路规划的稳定性。

  - RevPlan 的隔离探索思路可用于多策略 A/B 生成：在单独上下文中为不同用户分群或场景生成候选推荐策略，互不干扰，再通过 VerPlan 式多准则判别器（转化、多样性、GMV）过滤排序。

  - 若你的团队在做多任务 Agent（如同时优化点击率、转化率、停留时长），可参考 GRASP 的上下文隔离与正则化机制，缓解多任务性能坍塌，尤其适合生成式推荐或自动营销文案生成的复杂规划场景。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLM 在任务复杂度上升时可靠性下降，出现“指令诅咒”，长程规划中的约束冲突与注意力疲劳导致幻觉和执行失败。直接让 LLM 处理分层长指令效果差，需要新的规划架构。

**方法关键点**：GRASP 将规划管道解耦为三个上下文隔离模块。GenPlan 预编译全局宏指南，为后续规划提供策略约束；RevPlan 在隔离上下文窗口内探索局部替代策略，避免不同层级信息互相干扰；VerPlan 使用多准则判别器独立评估每个生成轨迹，选出最优可执行方案。

**关键结果**：在 Natural Plan Calendar Scheduling、ZebraLogic、SciBench Math 上均达到 SOTA，分别相对直接 LLM 规划器提升约 12.4%、30.8%；在多任务扩展场景下，GRASP 完全消除了基线模型的多任务退化惩罚；在交错双任务环境中实现最高 16.7% 的绝对准确率提升；通过上下文隔离和严格宏正则化，比 GPT-5-mini 高出 14.5%。
