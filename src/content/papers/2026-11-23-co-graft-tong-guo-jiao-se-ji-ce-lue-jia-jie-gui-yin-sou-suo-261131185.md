---
title: 'CO-GRAFT: Attributing Reinforcement Learning Gains in Search Agents via Role-Level
  Policy Grafting'
title_zh: CO-GRAFT：通过角色级策略嫁接归因搜索 Agent 的强化学习增益
authors:
- Ramraj Chandradevan
- Sayontan Ghosh
- Vinoth Selvendran
arxiv_id: '2611.31185'
url: https://arxiv.org/abs/2611.31185
pdf_url: https://arxiv.org/pdf/2611.31185
published: '2026-11-23'
collected: '2026-11-24'
category: Eval
direction: 搜索 Agent RL 增益角色级归因
tags:
- Search Agent
- RL Attribution
- Shapley Value
- Policy Grafting
- Möbius Interaction
one_liner: 将 RL 搜索 Agent 的精度增益按推理/决策/查询/答案四角色做 Shapley 分解，发现查询改进占比不超过15%，增益主要在推理或答案抽取
practical_value: '- 将搜索/推荐 Agent 链路按功能角色（推理、决策、query 生成、答案抽取）拆解，用 grafted rollout
  对比 RL 前后策略，可低成本定位端到端指标提升的真正来源，避免只看总体 EM 或转化率。

  - 采用 Shapley + Möbius 交互项做增量归因：Shapley 看单个角色的公平贡献，Möbius 区分独立提升与联合耦合；电商场景可拆分 query
  改写、召回触发、重排、文案生成等角色的贡献。

  - 固定搜索预算替换诊断值得复用：若固定搜索/召回深度能匹配 RL 策略，说明学习的是任务级预算而非自适应停止，可直接固化规则，降低线上复杂度；控制实验分离格式合规与内容提升，避免被奖励格式干扰。

  - 预训练 answer validity 与 search retention 是增益分配的关键变量：初始化已能输出格式良好答案时，RL 增益会向格式/答案抽取倾斜；若模型放弃搜索，增益可能停滞，因此要监控搜索调用频率和有效答案率。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
RL 后训练可将搜索 Agent 的 Exact Match（EM）最高提升 32 个点，但端到端精度提升无法说明是查询生成、推理、搜索/回答决策还是最终答案抽取哪一个功能改善。现有的行为观察、单角色消融和离线干预都不能在闭环检索下隔离各角色的因果贡献，因此需要一种无奖励、不改权重的归因方法。

## 方法关键点
- 将搜索 Agent 轨迹切成四个互斥角色：R（中间推理）、D（搜索/回答决策）、Q（搜索 query 生成）、A（最终答案抽取），检索返回的信息块不属于任何角色。
- Grafted rollout：让 RL 训练后的策略 π+ 与 pre-RL 初始化 π− 在同一条轨迹中按角色分配生成 tokens；枚举所有 16 种角色分配，不动权重、不重训。
- 用 Shapley 值把总 RL 增益按效率公理分解到四个角色；用 Möbius interaction 项分离单角色独立增益、成对及高阶耦合。
- 控制实验：严格 EM vs 宽松匹配、固定搜索深度替代 D、冻结检索结果替换 Q，分别区分格式合规、搜索预算和检索质量的影响。

## 关键实验
在 Qwen2.5-3B/7B、Llama-3.2-1B/3B 的 base/instruct 初始化，GRPO/PPO 优化器，NQ 与 HotpotQA 上评估 1000 题。核心结果：Q 角色贡献在所有设置下均不超过 15%；较大模型或指令调优后，A 份额上升而 R 份额下降；小基座模型表现出强 R×D 正耦合。例如 Qwen2.5-3B base NQ 增益 29.4 点，R/D/Q/A 份额为 70/7/6/17%；Llama-3.2-3B base NQ 增益 31.6，份额为 33/18/15/34%；Qwen2.5-3B instruct NQ 增益 19.5，份额为 36/21/4/39%。控制实验显示，固定搜索深度能匹配完整 RL 策略，冻结检索结果使 Q 归因下降 60–100%，但让 RL 策略控制 R 仍带来 11–22 点增益。

## 最值得记住的一句话
RL 对搜索 Agent 的增益很少来自查询生成本身，而是来自推理质量与答案抽取/格式合规；预训练答案有效性和搜索保留决定增益分布，因此优化目标应优先放在推理和答案环节，而非查询词。
