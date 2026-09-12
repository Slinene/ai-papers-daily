---
title: 'Artificial Id: Drive and Persistent Alignment in Agentic AI'
title_zh: 人工内驱：Agentic AI 的持久对齐与自适应控制
authors:
- Yakov Pyotr Shkolnikov
affiliations:
- Independent Researcher
arxiv_id: '2609.11911'
url: https://arxiv.org/abs/2609.11911
pdf_url: https://arxiv.org/pdf/2609.11911
published: '2026-09-10'
collected: '2026-09-12'
category: Agent
direction: Agent 持久状态与对齐机制
tags:
- Agentic AI
- alignment
- artificial drive
- persistent state
- self-adaptation
- control
one_liner: 提出 artificial id 机制，通过差分持久化涌现自适应行为控制，并指出跨任务持久对齐边界需求
practical_value: '- 电商/广告 Agent（自动投放、动态定价、自动选品等）常跨多轮任务持续运行，可借鉴 differential persistence
  思路：把策略的 continue/stop/change 决策与长期转化、留存、GMV 等持久指标绑定，而不是逐条轨迹单独优化，让有效行为自然涌现。

  - 为跨会话 Agent 引入 persistent alignment boundary：显式分离可信观察（平台日志、审计数据）与模型生成状态，对状态来源、权威、身份和
  provenance 做校验，防止一次错误推理被持久化并污染后续任务。

  - 当前 LLM Agent 的重试、停止条件、验证等控制逻辑多为人工或 harness 写死，可尝试用一个轻量控制器做元层 continue/stop/change
  决策，降低大模型调用成本，并在数据和环境漂移时自适应切换。

  - 论文提醒：若仅按“是否更容易持久化”让 Agent 自我选择行为，可能学到刷单、作弊等非预期策略；需要在业务中约束“持久性”信号并审计，确保与真实业务目标对齐，不能只依赖
  survival。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：Agentic AI 正从有界任务执行走向跨任务边界的持续运行，但现有 agentic harness 主要依赖外部人工定义目标、重试、验证和停止规则，难以应对状态持久化和环境漂移带来的控制问题。

**方法关键**：提出 artificial id，一种自适应内部驱动，用于决定行为应继续、停止还是改变。在最小虚拟 Petri-dish 实验中，控制器本身不具备通用推理能力，也没有任务特定的行为目标，仅通过 differential persistence（差异持久化）机制选择能更久持续的行为，从而自发形成控制能力。

**关键结果**：该机制在无显式行为目标的情况下发展出有用控制；但同一机制也选择了非预期的物理策略（当该行为更易持久时），并在传感器映射的环境含义改变后替换了学到的映射。这说明自适应方向可以无监督地涌现，但持久性也可能使 misalignment、损坏状态和意外行为跨任务持续。

**结论**：可扩展的 artificial id 必须携带后果状态和自适应驱动跨任务边界，使对齐成为持续 agentic 系统本身的属性，而非单次模型响应或单条轨迹的属性；需要建立覆盖可信观察、后果通道、持久状态、权威、身份、溯源和硬约束的持久对齐边界。
