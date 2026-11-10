---
title: 'WorkflowArena: Benchmarking Executable Workflow Orchestration in LLM-Based
  Multi-Agent Systems'
title_zh: WorkflowArena：LLM 多智能体系统可执行工作流编排基准
authors:
- Zheng Jiang
- Fang Niu
- Bo Peng
- Houde Qian
- Wenyi Li
- Deyao Hong
- Mingju Gao
- Yizhe Chi
- Youjie Zheng
- Kaisen Yang
affiliations:
- Navers Lab
- Einsia.AI
- Tsinghua University
arxiv_id: '2611.12856'
url: https://arxiv.org/abs/2611.12856
pdf_url: https://arxiv.org/pdf/2611.12856
published: '2026-11-09'
collected: '2026-11-10'
category: MultiAgent
direction: 多智能体工作流编排评测
tags:
- Workflow Orchestration
- Multi-Agent Systems
- LLM Agents
- Benchmark
- Delegation
- Evaluation
one_liner: 提出 WorkflowArena 基准，评估多智能体系统中自主工作流编排与交付物质量的联合表现
practical_value: '- 评估 Agent 系统时不要只看最终任务完成，应记录 delegation 结构：在电商导购、广告投放等长程任务中，可借鉴
  WorkflowArena 思路，同时评测交付物质量和底层工作组织，避免只看结果掩盖编排缺陷。

  - 不同 orchestrator 有不同 delegation 策略：Claude 模型倾向低频调用但更大 worker 组，GPT 模型倾向高频小单元 delegate。在业务中选择
  orchestrator 时，可据此决定是集中式大组协作还是细粒度流水线，例如搜索推荐 Agent 的召回-排序-解释链路可尝试不同粒度拆分。

  - 工作流编排能力可迁移：固定 executor 时，强 orchestrator 生成的工作流能显著提升弱 executor，说明业务中可分离 planner/orchestrator
  与 executor 模型，用强模型生成工作流、弱模型执行，降低成本。

  - 长程任务中工作流组织本身是性能决定因素：在设计商品推荐、广告创意生成等多步骤 Agent 系统时，应显式把工作流生成和审查作为独立模块，而不是隐含在 prompt
  链里。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 智能体越来越多以多智能体系统部署，系统结构由开发者设计转为运行时由模型生成可执行工作流。现有基准只测端到端任务完成或预设结构下的协调，缺少对工作流编排能力的独立评估。

**方法关键点**：提出 WorkflowArena，包含 145 个长程任务，覆盖软件工程、形式数学、法律分析、3D 制作等 8 个专业领域。每个任务给定初始工作区和由相互依赖组件组成的交付物，由隐藏 verifier 评估。Agent 自主决定是否及如何 delegation，所有 delegation 被记录，联合评估交付物质量与工作组织。

**关键结果**：测试 9 个模型，没有单一配置在所有领域最优。系统呈现不同 delegation 策略：高 effort 下 Claude Code 中 Claude 模型调用工作流频率较低但 worker 组更大，GPT 模型在 Codex 中更频繁以更小单元 delegate。在固定 executor 的挑战子集上，Claude Opus 5.5 编写的工作流显著提升较弱 executor，表明工作流编排本身是可测量的任务性能决定因素。
