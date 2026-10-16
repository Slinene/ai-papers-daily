---
title: Learning Self-Orchestration in Decentralized Agent Swarms
title_zh: 去中心化 Agent 群体中的自组织调度学习
authors:
- Guowei Xu
- Zhenting Qi
- Amani Kiruga
- Himabindu Lakkaraju
- Yilun Du
affiliations:
- Harvard University
arxiv_id: '2610.22322'
url: https://arxiv.org/abs/2610.22322
pdf_url: https://arxiv.org/pdf/2610.22322
published: '2026-10-14'
collected: '2026-10-16'
category: MultiAgent
direction: 去中心化多智能体自组织调度
tags:
- MultiAgent
- Self-Orchestration
- Market-Based Bidding
- Post-Training
- Decentralized Swarm
- Credit Assignment
one_liner: 提出市场机制后训练框架 MPT，让去中心化 Agent 联合学习行动策略与竞价式自组织调度，在多个多智能体任务上超越单一体模型
practical_value: '- 多 Agent 路由/编排可直接借鉴：在电商/广告多策略召回、多工具 LLM Agent、客服多专家协作中，给每个子系统或模型加一个可学习
  bidding head，代替固定路由或中心化调度；用梯度联合优化能力与参与概率，让编排自动适配流量分布变化。

  - 奖励信用分配更简单：使用全局结果作为训练信号，结合 bid 记录区分贡献，不必人工设计子任务奖励；适合广告出价、多商品推荐结果融合等端到端训练场景。

  - 推理时可扩展并容错：论文表明增大 Agent 池规模可提升性能且 agent dropout 损失更小；线上可将相似功能的多个模型/策略作为冗余候选池，用学到的
  bid 动态启用，兼顾性能和弹性降级。

  - 注意任务差异：论文验证于具身与深度研究任务，动作空间和交互协议与电商推荐有差距；迁移时需先抽象“行动”为可离散选择的策略或工具调用，并将环境状态编码为共享观测。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：现有多智能体系统通常固定编排结构，个体能力与集体协作行为分离训练，无法自适应决定谁参与、何时参与。核心假设是去中心化 Agent 群体可通过竞价机制自行组织调度。

方法关键点：市场机制后训练 MPT。每个 Agent 同时学习行动策略和竞价策略，输出 bid 表达参与意愿；根据 bid 决定哪些 Agent 行动，集体结果作为本地训练信用反向更新，无需中心协调者。行动与竞价联合优化，学习到的 bid 同时为行动训练提供有效信号。

关键结果：在 embodied crafting、robot navigation、deep research 等任务上对比 monolithic post-training 取得性能提升；学习到的自组织调度优于随机、固定或中心化协调策略；消融显示行动和竞价学习均必要，学习到的 bid 提供更有效的行动训练信号。迁移任务适应更快，推理时增大 Agent 规模性能提升，agent dropout 下性能损失更小。具体数值未披露，但趋势一致。
