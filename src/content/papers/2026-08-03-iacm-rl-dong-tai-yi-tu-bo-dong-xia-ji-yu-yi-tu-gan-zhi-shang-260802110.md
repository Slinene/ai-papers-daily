---
title: 'IACM-RL: Intent-Aware Context Management and Reinforcement Learning for Complex
  Tool Invocation under Dynamic Intent Fluctuations'
title_zh: IACM-RL：动态意图波动下基于意图感知上下文管理与强化学习的复杂工具调用
authors:
- Dingwei Zhu
- Jiahan Li
- Chengjun Pan
- Yunxian Yang
- Yunbin Zhao
- Yunke Zhang
- Zhonghang Lu
- Zhuohui Sheng
- Chenhao Huang
- Jiahang Lin
affiliations:
- 复旦大学
- 荣耀终端有限公司
- 北京大学
arxiv_id: '2608.02110'
url: https://arxiv.org/abs/2608.02110
pdf_url: https://arxiv.org/pdf/2608.02110
published: '2026-08-03'
collected: '2026-08-04'
category: Agent
direction: Agent 上下文管理与强化学习优化
tags:
- tool invocation
- context management
- reinforcement learning
- belief state
- intent fluctuation
- agent
one_liner: 提出自生成上下文管理器与分层意图奖励，解决动态意图噪声下工具调用中的状态漂移和无限循环问题
practical_value: '- **状态管理与动作生成解耦**：在电商 Agent（如售后、导购）多轮对话中，可将用户需求（商品参数、配送偏好）抽离为显式信念状态块，标记过时字段，避免模型重复使用已修改信息，可直接借鉴
  CM 的九块结构设计领域专用状态模板。

  - **分层奖励设计**：推荐系统 Agent 的 RL 训练可使用类似分层奖励——参数级（如属性正确）、行为级（避免重复推荐）、结果级（推荐链完成度），提供密集、可诊断的信用分配，替换稀疏奖励。

  - **辅助损失内部化状态能力**：通过 CM 提取损失 L_ext 直接优化状态块生成质量，再用蒸馏损失 L_dist 将状态跟踪蒸馏进模型权重，实现无额外推理开销的隐式状态管理，适合对延迟敏感的线上系统。

  - **对抗训练构建干扰数据**：用类似 DynamicIntent 的数据增强方法，模拟用户中途插入闲聊、假任务等噪声，训练鲁棒的多轮推荐策略，可提升真实场景下的任务完成率。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：真实多轮工具调用中，用户意图频繁波动（中途改任务、插话、歧义指令），传统方法假设静态指令，导致过时信息稀释模型注意力，引发意图偏离与无限 API 循环。现有压缩或记忆方案在长周期并行工具场景中崩溃，缺乏显式、可学习的意图状态管理。

**方法关键点**：
- **DynamicIntent 数据管线**：通过工具抽象、依赖图构建与 5 类 13 种精细意图波动注入（修改、中断、澄清、累积、链式），合成大量多轮轨迹，覆盖 ID/OOD 工具集。
- **自生成上下文管理器（CM）**：基于信念状态（BeliefState）的九块结构，主动追踪当前目标、搁置参数、待澄清信息等，并用结构性“陈旧标记”隔离被覆盖参数，强制解耦状态跟踪与动作生成。
- **分层意图驱动奖励**：认知层奖励参数准确性与陈旧处罚，行为层奖励循环抑制与澄清主动性，结果层奖励链完成与意图切换成功，实现场级别信用分配。
- **PPO 优化 + 三项辅助损失**：动作校准损失 Lcal 关联响应似然与工具正确性；CM 提取损失 Lext 用优势信号直接优化 CM 块质量；状态蒸馏损失 Ldist 将 CM 条件蒸馏回无 CM 策略，使模型内化状态跟踪能力。

**关键实验**：在 DynamicIntent Benchmark（ID/OOD）、BFCL-V3 和 τ2-Bench 上评估。IACM-RL 平均分 64.0 最高；ID 认知得分 36.5，OOD 认知 36.3，展现强泛化；BFCL 63.3；τ2-Bench 航空域 38.0。消融表明三项损失独立增益，Lext 移除时 OOD 认知下降至 32.7，长对话中 CM 增益显著（16K+ 从 0 提升至 34.8）。对抗干扰测试中，插 3 假任务 + 5 闲聊后准确率仍高 11.2 个百分点。

**核心句**：显式解耦状态跟踪并内化于策略参数，是应对动态意图噪声下长效工具调用的关键。
