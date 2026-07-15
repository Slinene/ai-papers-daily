---
title: Do AI Agents Know When a Task Is Simple? Toward Complexity-Aware Reasoning
  and Execution
title_zh: AI Agent 能否判断任务简单性？面向复杂度感知的推理与执行
authors:
- Junjie Yin
- Xinyu Feng
arxiv_id: '2607.13034'
url: https://arxiv.org/abs/2607.13034
pdf_url: https://arxiv.org/pdf/2607.13034
published: '2026-07-14'
collected: '2026-07-15'
category: Agent
direction: Agent 复杂度感知执行优化
tags:
- agent
- complexity-aware
- execution planning
- cost reduction
- redundancy
- llm
one_liner: 提出 E3 框架让 Agent 先估算任务难度，最小化执行，仅在验证失败时扩展，减少认知冗余
practical_value: '- **最小充分执行原则**：在构建推荐系统的多步 Agent（如数据分析、代码调试）时，先尝试用最少步骤完成任务，失败后再逐步扩展上下文，可避免过度检索或调用，显著降低
  token 消耗。

  - **复杂度感知调度**：为 Agent 增加任务难度估算模块，根据任务复杂程度动态分配上下文长度和工具调用次数，防止简单任务消耗过多资源，适合电商场景中大批量轻量查询的自动化处理。

  - **冗余度监控**：引入类似 ACRR（Agent 认知冗余比）的指标来度量 Agent 执行中的不必要操作，优化工作流设计，帮助我们识别并剪除重复的文件读取或无效推理环节。

  - **适应性验证机制**：E3 的「先执行、后验证、必要时扩展」策略可直接用于 Agent 驱动的搜索推荐调试、自动 A/B 测试分析等流程，在保证成功率的前提下大幅压缩执行成本。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：当前 LLM Agent 在多步任务中常采用“最大上下文优先”策略，重复读取无关文件，导致简单任务也耗用大量资源。缺乏对任务难度的预判和自适应执行规划，产生了大量认知冗余。

**方法**：将任务执行形式化为最小充分执行问题，定义 Agent 认知冗余比（ACRR）。提出 E3（Estimate, Execute, Expand）框架：先估算初始操作点，执行最小可行路径，然后验证；仅当验证失败时扩展上下文和步骤，循环直到成功。该框架不依赖特定模型，是对执行策略的控制。

**结果**：在包含 121 项确定性编辑任务的 MSE-Bench 基准上，E3 取得与最强基线相同的 100% 成功率，同时成本降低 85%，token 用量减少 91%，文件检查减少 92%，并比强自适应检索基线高出 16% 的成功率。在真实开源库的 gpt-4o 编辑测试中，E3 同样表现出最精简的执行策略和较高的任务成功率。
