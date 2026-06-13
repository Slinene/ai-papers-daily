---
title: 'AgentBeats: Agentifying Agent Assessment for Openness, Standardization, and
  Reproducibility'
title_zh: 智能体评估的智能体化：用标准化协议实现开放、标准、可复现的评估
authors:
- Xiaoyuan Liu
- Jianhong Tu
- Yuqi Chen
- Siyuan Xie
- Sihan Ren
- Tianneng Shi
- Gal Gantar
- Evan Sandoval
- Donghyun Lee
- Daniel Miao
affiliations:
- UC Berkeley
- UC Santa Cruz
- EPFL
- IBM Research
- Carnegie Mellon University
arxiv_id: '2606.13608'
url: https://arxiv.org/abs/2606.13608
pdf_url: https://arxiv.org/pdf/2606.13608
published: '2026-06-11'
collected: '2026-06-13'
category: Agent
direction: Agent 评估标准化 · 多智能体评估
tags:
- Agent Evaluation
- Standardization
- A2A
- MCP
- Multi-Agent
- Reproducibility
one_liner: 将基准测试本身封装为 judge agent，通过 A2A 与 MCP 解耦评估逻辑，使任意智能体无需定制即可互操作
practical_value: '- **标准化评估接口**：用 A2A（任务分发）与 MCP（工具访问）解耦 benchmark 与待测 agent，消除 N×M
  集成成本，可直接复用到电商多智体评测（如客服 agent、推荐 agent、风控 agent），仅需实现 A2A wrapper 即可接入任何 judge agent。

  - **多种部署模式**：远程/托管/代理/CI 模式覆盖隐私与公开需求，电商团队可选择本地模式保护闭源 agent，或通过 CI 模式把评估嵌入 CI/CD，实现上线前自动化回归。

  - **可组合的 judge agent 设计**：judge agent 内部可灵活组合用户模拟器、LLM-as-judge 等子 agent，便于构建自定义评估流水线，如模拟买家行为、评估商品推荐
  agent 的多轮对话质量。

  - **降低评估门槛**：通过自然语言描述评估逻辑（semantic internalization）即可快速创建新 benchmark，无需硬编码，适合业务快速验证新场景下的
  agent 行为。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：LLM 驱动的智能体系统快速发展，但评估生态严重碎片化。现有基准测试与目标智能体紧耦合，每一对 benchmark-agent 组合都需要定制化集成（N×M 工作量），且评估环境与生产部署环境差异大，难以公平比较异构 agent 设计。根本原因在于缺少开放、与 agent 无关的评估接口。

**方法关键点**：
- 提出 **Agentified Agent Assessment (AAA)** 范式：将 benchmark 本身实现为一个 judge agent，通过标准化协议 A2A（任务管理与交互）和 MCP（工具与环境访问）与 subject agent 通信，实现评估逻辑与 agent 实现的完全分离。
- judge agent 内部可嵌入数据集、环境模拟、LLM judge 等组件，支持程序化或语义化定义评估流程。AAA 原生支持多智能体对抗/协作场景。
- 基于 AAA 构建 **AgentBeats** 系统，提供五种操作模式（本地、远程、托管、代理、CI）以满足开放性、隐私、可复现性的现实约束。
- 给出 judge agent 与 subject agent 的开发指南，降低适配成本，并设计了 agent 控制平面、MCP 网关、沙箱管理等扩展组件。

**关键结果**：
- 五个月开放竞赛吸引 298 个 judge agents（覆盖编码、网页浏览、医疗等 12 个类别）和 467 个 subject agents，证明 AAA 具有广泛的覆盖性。
- 编码 agent 案例研究表明，AAA 评估结果与公开记录一致，且能揭示以往缺失的 agent 与原生 harness 之间的协同适应效应。
- 标准化将集成量从 N×M 降至 N+M，降低迁移成本，且未引入显著评估偏差。
