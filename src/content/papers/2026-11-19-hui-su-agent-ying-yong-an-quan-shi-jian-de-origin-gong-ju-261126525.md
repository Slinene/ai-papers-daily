---
title: Backtracking Agent Applications Security Incidents
title_zh: 回溯 Agent 应用安全事件的 Origin 工具
authors:
- Yicheng Cai
- Taegyu Kim
- Peng Liu
affiliations:
- Pennsylvania State University
arxiv_id: '2611.26525'
url: https://arxiv.org/abs/2611.26525
pdf_url: https://arxiv.org/pdf/2611.26525
published: '2026-11-19'
collected: '2026-11-21'
category: Agent
direction: Agent 安全回溯 · 跨层依赖图
tags:
- Agent Security
- Backtracking
- LLM
- Trajectory Logs
- Taint Analysis
- Cross-layer Graph
one_liner: 提出 Origin 工具，通过跨层依赖图与区域推断算法，让分析师用少量查询准确定位 Agent 攻击入口点
practical_value: '- **Agent 可观测性与审计：** 借鉴 CLDG 思想，在电商/客服 Agent 系统中构建轨迹日志与底层代码执行/数据流的映射，用于快速定位业务故障、推荐链路异常或安全事件归因。

  - **Region 推断可迁移到性能诊断：** 将 agent 功能分组（region）并自动关联代码区域，可减少人工排查，用于内部诊断平台或根因分析工具。

  - **安全防御前置：** 随着电商购物助手、广告投放 Agent 使用 LLM，间接提示注入、memory poisoning 等风险增加，部署时需考虑回溯能力，Origin
  的查询接口设计可参考。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机：** Agent 应用大规模部署，安全事件发生后需回溯定位 compromise entry point (CEP)。可用 artifacts 为 trajectory logs 与源代码，但 trajectory logs 在 agent 功能抽象层，而 CEP 候选是代码执行层函数调用，语义鸿沟导致分析师需手工检查代码。

**方法关键点：** Origin 工具让分析师提交少量查询来识别 CEP。核心是定义中间抽象：cross-layer dependency graph (CLDG) 连接语义层的 region-inferred functions 与低层 taint propagation subgraph 中的变量；配套 region inference algorithm 确定 region-to-variable mapping，构建跨层图。Region 是特定 agent 功能组。

**关键结果数字：** 在 5 个流行 agent 应用、8 个攻击事件的案例研究中，分析师使用 Origin 正确识别所有 CEP，而现有工具无法提供。
