---
title: 'AutoPILOT: A Visual Agent Harness for Real-Time Gameplay'
title_zh: AutoPILOT：实时游戏视觉 Agent 执行框架
authors:
- Mark Zhao
- Pengcheng Wang
- Rui Yang
- Jiarui Yao
- Xirui Jiang
- Yuxi Chen
- Bingxuan Li
- Hanyang Chen
- Ke Yang
- Manling Li
affiliations:
- University of Illinois Urbana-Champaign
- Georgia Institute of Technology
- Northwestern University
arxiv_id: '2611.28202'
url: https://arxiv.org/abs/2611.28202
pdf_url: https://arxiv.org/pdf/2611.28202
published: '2026-11-19'
collected: '2026-11-24'
category: Agent
direction: Agent 实时控制与动作执行优化
tags:
- Real-time Agent
- Harness
- Macro
- Closed-loop Controller
- Game AI
- Cost Efficiency
one_liner: 让模型单次调用生成宏或闭环控制器，在无模型调用期间自主执行动作，大幅提升实时游戏成功率并降低成本
practical_value: '- 分层执行架构：将 LLM 决策与执行解耦，允许模型输出可执行代码或策略在本地闭环运行，减少对模型调用的依赖，适用于需要低延迟的实时推荐/广告竞价场景，如生成规则或小型模型在流式数据上执行，LLM
  仅在触发事件时介入。

  - 唤醒事件设计：定义清晰的 handoff 条件，例如预测置信度下降、数据漂移、性能异常等，用于自动交还控制权给 LLM，可借鉴到在线推荐系统的模型更新或策略切换。

  - 成本控制：通过宏/控制器减少高频 API 调用，实验中达到同等效果只需 1/5 成本，对大规模推荐/搜索 Agent 有直接成本收益。

  - 离线评估设计：AFK-Bench 按系统对“无响应”的容忍度划分任务，建议构建类似实时交互基准，评估 Agent 在用户不耐受延迟下的表现，可指导电商搜索/推荐的实时性设计。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：多模态基础模型在等待型游戏中表现好，但实时游戏中因模型推理延迟而失败，关键在于 harness 如何将模型输出转化为随时间执行的动作。现有 harness（如 VISTA）每次模型调用最多产生一个动作，导致 agent 只能以模型思考频率行动。

**方法关键点**：提出 AutoPILOT，改变动作执行方式：每次模型调用，模型可以选择发送一个原始动作、启动开环宏、或编写一个闭环控制器。控制器从屏幕读取状态并在无模型调用的情况下持续执行动作，直到触发唤醒事件交还控制权。同时构建 AFK-Bench，包含 120 个多样化浏览器游戏，按对无响应的反应分组，支持实时和暂停时钟两种模式。

**关键结果**：使用 GPT-6.1 Sol，在相同预算下，AutoPILOT 实时成功率 68.6%，对比 VISTA 的 38.3%；在 GameWorld 上实时保持 80.0%，而 VISTA 从暂停时的 84.1% 下降到实时 42.9%。增益跨模型保持，且达到 VISTA 最终成功率仅需其 API 成本的五分之一。
