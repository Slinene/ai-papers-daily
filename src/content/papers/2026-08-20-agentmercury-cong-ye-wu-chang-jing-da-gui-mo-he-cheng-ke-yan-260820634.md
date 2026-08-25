---
title: 'AgentMercury: Your Agent Can Synthesize Verifiable Environments for Business
  Scenarios at scale'
title_zh: AgentMercury：从业务场景大规模合成可验证可执行环境
authors:
- Minbyul Jeong
- Chanwoong Yoon
affiliations:
- Meridian Intelligence Global Inc.
- University of Massachusetts Amherst
arxiv_id: '2608.20634'
url: https://arxiv.org/abs/2608.20634
pdf_url: https://arxiv.org/pdf/2608.20634
published: '2026-08-20'
collected: '2026-08-25'
category: Agent
direction: 业务场景可执行环境合成 · 策略强化学习
tags:
- environment synthesis
- reinforcement learning
- agent training
- tool use
- business scenarios
- verifiable environments
one_liner: 提出从高层业务场景自动合成可执行世界，作为策略强化学习训练基底，并证明环境构建本身可学习
practical_value: '- **场景驱动仿真生成**：在电商/广告 Agent 业务中，不要围绕特定任务或评测集手工搭建环境，而是从业务流程（订单、库存、营销、客服、履约）生成多服务、有状态、带跨服务约束的可执行环境，让任务自然涌现。这样一套环境可支撑多个任务和多种策略训练，复用性远高于
  task-centric 仿真。

  - **将业务不变量与状态转移解耦**：把跨服务约束（如支付成功后必须生成发货单、推荐展示后必须同步库存）做成 episode 结束时的 SQL/确定性 verifier，而不是在模拟器中自动满足。训练
  agent 主动发现并满足这些约束，能提升策略在真实业务流程中的可靠性和一致性。

  - **用合成业务环境做 RL 预训练/继续训练**：AgentMercury 的实验显示，在多样化的业务工具环境上做 GRPO/SAO 训练，即使不针对下游评测集，也能提升
  tool-use、推理、代码等能力，并显著降低工具调用轨迹的方差。电商 Agent 团队可以批量生成带真实工具调用、状态追踪、多步交互的环境，作为通用能力底座。

  - **把环境构建本身做成可学习任务**：收集从业务 brief 到可执行世界的构建 trace（中间 schema、服务图、validator 修复），对模型做
  SFT，让模型从需求描述直接生成可执行仿真。这能大幅加速新业务场景的环境覆盖，并让非技术业务方参与环境定义。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
现有 Agent 训练环境多为 task-centric：围绕特定任务手工或合成，难以扩展出反映真实持续工作流的可执行世界。真实业务中任务不是孤立目标，而是从用户意图、持久状态、多服务交互中涌现。本文主张从高层业务场景出发生成 persistent world，让多样任务和轨迹自然产生，而非为每个任务单独造环境。

## 方法关键点
- 引入 PLANET 角色：输入业务场景 σ，输出完整可执行世界 w = ⟨S,A,Ω,T,O,s0,R⟩，其中 R 是世界级不变量，关联可执行的 SQL 验证条件，与状态转移 T 解耦。
- 结构化世界合成：按 p(C|σ)p(G|C)p(Σ|G,C)p(s0|Σ)p(R|G,Σ,s0) 分解，先确定公司身份、服务图、状态 schema，再生成种子状态和跨服务不变量。
- 任务从世界实例化：对同一世界可生成多个任务，任务 rubric 与世界不变量分离，避免任务目标与规则混淆。
- 确定性 grading：轨迹结束后用 rubric 和隐藏不变量通过数据库状态检查打分，保证可复现。
- 构建 4,783 个可执行环境，覆盖 14 行业、50 国家，每个环境含持久状态、多服务、工具、跨服务约束；训练策略直接在这些环境中用 GRPO/SAO 做 RL。

## 关键结果
- 在 EnterpriseOps-GYM 上，Qwen3.5-4B 平均分从 12.3 提升到 15.7（+27.6%）；Qwen3.5-35B-A3B 从 24.8 提升到 28.1（GRPO）或 28.3（SAO）。
- Out-of-domain 基准：Qwen3.5-4B + GRPO 在 AIME26 从 45.9 到 56.0，HMMT 从 28.5 到 35.4，LiveCodeBench 从 36.6 到 44.0，SciCode 从 22.6 到 25.7；工具调用基准方差显著降低。
- 环境构建可学习：用 29,823 条构建 trace 微调 Qwen3.5-35B-A3B，在 30 个 held-out 业务 brief 上可执行世界构建成功率从 3.3% 提升到 83.3%，追平最强 API 模型。

> 最值得记住的一句话：环境的有效学习信号不取决于对目标 benchmark 的匹配，而来自多样化可执行世界提供的可复用交互、状态追踪与约束满足模式。
