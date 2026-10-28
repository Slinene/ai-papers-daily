---
title: The Trinity:Capability-Driven Recursive Self-Improvement for Multimodal Agents
title_zh: 三位一体：能力驱动的多模态智能体递归自改进
authors:
- Weidong Tang
- Ruiheng Wang
- Jingxuan Zhang
- Hexin Wang
- Haoyuan Chen
- Zhengfeiyang Zhang
- Yixing Ma
- Zichen Jiang
- Ziyu Guo
- Haodong Li
affiliations:
- The Trinity Research Team
arxiv_id: '2610.36077'
url: https://arxiv.org/abs/2610.36077
pdf_url: https://arxiv.org/pdf/2610.36077
published: '2026-10-25'
collected: '2026-10-28'
category: Agent
direction: 多模态 Agent 递归自改进
tags:
- Multimodal Agents
- Self-Improvement
- Capability Tree
- Harness Evolution
- Real2Sim2Real
- Agent Router
one_liner: 提出 Trinity 框架，通过 Creator/Explorer/Evolver 将任务重组为能力树，递归进化 Harness 并路由选择
practical_value: '- 在电商/搜索/推荐的 Agent 工作流里，可以按底层能力需求而非业务场景（搜索、推荐、广告）来组织任务与模块：定期用已验证执行轨迹重新聚类任务，把“表面
  query 分类”换成“能力树”，减少场景间重复建设。

  - 借鉴 Capability-Driven Real2Sim2Real：用历史日志或仿真沙箱构造简化的可验证环境，让 Agent 先做离线能力学习，再在原任务上评估迁移；适合在推荐文案生成、Query
  改写等高频能力上做低成本迭代。

  - 参考 Harness 树 + Capability-Aware Router 的做法：维护一组可复用的 Harness/模块配置，不改动整体拓扑，只在固定拓扑内累积验证更新；再根据公开任务元信息（如
  query 类型、商品类目）路由到不同模块组合，类似多任务 MoE 的轻量路由。

  - 对具身或多模态业务场景，优先抽取共享能力做仿真训练，而不是为每个异构场景单独建环境；实测在 unseen benchmark 上仍有 26 分提升，说明能力抽象具备迁移性。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：多模态智能体缩放面临两个瓶颈——异构可验证环境构建成本高，人工 Harness 迭代跟不上任务多样性与复杂度。关键洞察是不同模态和表面形式的任务可以共享底层能力需求。

方法：Trinity 框架引入 Creator、Explorer、Evolver 三个角色。Evolver 基于验证执行轨迹，把原始任务树重组为层次化能力树；Creator 通过 Capability-Driven Real2Sim2Real，将同节点异构任务的共性需求抽象成简化、可验证的仿真世界，用于能力学习，再在原任务上评估迁移；Explorer 沿能力树通过选择性继承逐步进化可复用能力模块，形成 Harness 树，并在固定拓扑内累积验证更新；Capability-Aware Harness Router 根据公开任务信息从树中选择兼容的模块配置。

结果：进化后的 Harness 在 28 个训练 benchmark 上平均性能提升 34 分，在 18 个未见 benchmark 上平均提升 26 分，其中包括两个真实具身任务。
