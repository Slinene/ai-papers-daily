---
title: 'A Decade in a Day: Synthesizing Agent-Native Interfaces from Human-Oriented
  Software Evolution'
title_zh: 一日合成十年：从人本软件演化构建 Agent 原生接口
authors:
- Alan Wu
- Wei Tao
- Yiwen Guo
affiliations:
- Independent Researcher
- LIGHTSPEED
arxiv_id: '2610.15765'
url: https://arxiv.org/abs/2610.15765
pdf_url: https://arxiv.org/pdf/2610.15765
published: '2026-10-10'
collected: '2026-10-14'
category: Agent
direction: LLM Agent 接口设计与评估
tags:
- LLM Agents
- Interface Design
- Benchmark
- Token Efficiency
- Tool Use
one_liner: 提出 DeskIF-Bench 基准并依据可发现性、粒度、可观察性合成原子接口，提升 LLM Agent 桌面任务成功率并降低约73% token
  消耗
practical_value: '- 业务中构建 Agent 操作内部系统（如广告投放、推荐配置后台）时，不要直接让 Agent 调用低层 SDK 或点击 GUI，而是抽象出“原子操作”（如设置预算、创建计划、查询报表）并组合成“目标级命令”（如“暂停超预算广告”），可显著提高成功率并降低
  token 消耗（论文中约降低 73%）。

  - 设计给 Agent 使用的工具/API 时，重点优化三个属性：可发现性（discoverability）——让 Agent 能快速找到可用操作；粒度（granularity）——操作粒度与任务目标匹配，避免过细或过粗；可观察性（observability）——返回结构化、明确的状态反馈，便于
  Agent 决策。这些属性可通过轨迹分析识别。

  - 评估 Agent 在不同版本或不同工具接口下的表现时，可借鉴“固定任务、Agent、验证器，只改变接口”的对照方法，定量归因接口设计的影响，指导内部工具迭代。

  - 若在电商搜索推荐中引入 Agent 调用推荐引擎或搜索服务，可提供高层命令式接口（如“重排序候选集”），而非暴露底层模型推理细节，提高 Agent 决策效率。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：LLM agents 正成为桌面应用的新用户，但现有 GUI 和 SDK 均面向人类设计，要求代理解释视觉控件或发现并组合底层软件操作，阻碍了代理性能。

方法关键点：将软件演化视为界面变化的自然来源，构建 DeskIF-Bench 基准，含 255 个经过工件验证的任务，覆盖 6 个桌面应用。固定任务、代理和验证器，仅改变软件版本，量化界面变化对代理性能的影响。轨迹分析识别出三个关键界面属性：可发现性（discoverability）、粒度（granularity）和可观察性（observability）。据此开发 ANIS 框架，从已安装应用的能力合成 agent-native 接口，将操作抽象为原子接口，再组合为目标级命令。

关键结果：在两个模型和六个应用上，最新版本软件的性能一致优于最旧版本。在扩展的 368 个任务、8 个应用上，原子接口相较原生 SDK 使用将成功率提升 3.8 个百分点（DeepSeek V4 Flash）和 3.5 个百分点（Claude Haiku 4.5），在线 token 使用降低约 73%；目标级命令进一步将成功率提高到 74.5% 和 67.4%。
