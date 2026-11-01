---
title: 'Gym-Anything for Robotics: Scaling physical simulations with digital agents'
title_zh: Gym-Anything for Robotics：用编码智能体规模化物理仿真
authors:
- Pranjal Aggarwal
- Sean Welleck
affiliations:
- Carnegie Mellon University
arxiv_id: '2610.40565'
url: https://arxiv.org/abs/2610.40565
pdf_url: https://arxiv.org/pdf/2610.40565
published: '2026-10-29'
collected: '2026-11-01'
category: Agent
direction: 编码智能体自动生成仿真与基准
tags:
- Agent
- Robotics Simulation
- RL Environments
- Code Generation
- Benchmark
- VLA
one_liner: 让编码智能体自动创建机器人仿真环境，构建 RoboWorld 基准并利用特权教师等方法提升前沿模型在 RL 任务上的表现
practical_value: '- 借鉴“creation-audit loop”自动生成与校验训练环境：在电商搜索推荐中，可用 LLM Agent 批量生成模拟用户行为序列、查询、商品集合，并用另一个
  Agent 对抗式审核其真实性与难度，替代手工构造离线评估集。

  - 利用 GDP/价值导向的任务选择思路：优先覆盖高频、高价值业务场景（如高转化 query、高 GMV 类目），让生成的环境更贴近线上收益目标。

  - 引入 privileged teacher 机制：训练推荐或对话 Agent 时，可让模型在训练阶段访问真实用户意图/隐反馈作为“特权教师”，在上下文中指导学生策略，提升对稀疏反馈的利用效率。

  - 用 code policies 生成跨场景演示数据：在生成式推荐或 Agent 决策中，编写代码策略自动产出不同场景下的示范轨迹，用于蒸馏 VLA 型模型，降低人工标注成本。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**
现有机器人仿真覆盖范围窄、依赖专家手工设计，难以规模化支撑具身智能训练。核心洞察是：仿真创建本质是编码任务，编码智能体的进步可直接转化为更丰富、更真实的仿真环境。

**方法关键点**
- 基于美国 GDP 数据选择仿真场景，覆盖经济价值高的物理工作（职业→任务→原子动作分组）。
- 明确“好仿真”和“好任务”的定义，并开发对抗式 creation-audit loop：生成智能体创建仿真，审计智能体按定义检查其质量和难度。
- 构建 RoboWorld：25 个仿真、25 个测试环境、175 个训练 RL 环境，难度分层。
- 提出多种提升前沿模型表现的方法：跨尝试的 in-context learning；特权教师读取模拟器底层状态并教导学生；从模型自身特权经验中自我辅助学习；code policies 生成跨场景演示数据，用于训练 VLA 模型（如 π₀.₅）。

**关键结果**
在 RoboWorld 测试任务上，最强前沿模型平均 reward 仅 0.06，全部失败；引入上述改进方法后性能显著提升。代码、环境与基准已开源。
