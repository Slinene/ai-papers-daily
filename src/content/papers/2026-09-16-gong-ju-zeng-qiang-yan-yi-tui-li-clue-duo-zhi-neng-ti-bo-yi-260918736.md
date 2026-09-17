---
title: Clueing up LLMs with Tool-Augmented Deductive Reasoning
title_zh: 工具增强演绎推理：Clue 多智能体博弈中的 LLM 智能体
authors:
- Rebecca Ansell
- Autumn Toney-Wails
affiliations:
- Georgetown University
- Syntheos, Corp
- UNU-MERIT
arxiv_id: '2609.18736'
url: https://arxiv.org/abs/2609.18736
pdf_url: https://arxiv.org/pdf/2609.18736
published: '2026-09-16'
collected: '2026-09-17'
category: Agent
direction: LLM Agent 工具增强演绎推理
tags:
- LLM Agents
- Tool-Augmented Reasoning
- Deductive Reasoning
- Multi-Agent
- Possibility Matrix
- Game Environment
one_liner: 以 Clue 多智能体博弈为环境，用可能性矩阵工具外置记忆与约束，提升 LLM 推理一致性
practical_value: '- 企业 Agent 系统若涉及多轮筛选/排除（如广告定向、商品约束推荐、会话式选品），可把候选集合与排除条件用结构化矩阵/表格工具维护，每轮更新，而不是全部塞进
  prompt 或依赖 LLM 记忆。

  - 采用“推理日志 → 结构化状态”的离线解析管线：LLM 仍输出自然语言推理，但由工具从日志抽取约束并更新候选表，把记忆与一致性检查外置，降低长对话中的遗忘和矛盾。

  - 对多模型/多智能体策略评测：可建立类似 Clue 的封闭信息博弈环境，量化 LLM 在信息不完整、多轮约束变化下的决策质量，作为上线前 reasoning
  能力回归测试。

  - 工具设计应保持显式、可解释：可能性矩阵相当于可审计状态，便于排查 agent 推理错误，比隐式 memory 更适合业务风控和调试。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：长交互下 LLM 的多步演绎推理常出现不一致、无法整合跨轮证据和更新信念的问题。论文以 Clue 桌游的多智能体版本作为封闭、可复盘的推理评测环境，观察智能体在信息不完全与约束动态变化时的决策。

**方法**：环境支持 6 个 LLM 智能体（GPT-4o-mini、Gemini-2.5-Flash 各 3 个）轮转博弈；基线仅依赖自然语言 game log。提出的工具增强方法引入结构化 possibility matrix，将游戏状态显式表示为剩余可能性，编码跨轮记忆与演绎约束，把这些任务从智能体上下文转移到外部工具。每轮从自然语言推理日志更新矩阵，降低对模型自身记忆的依赖。

**结果**：在重复游戏中建立基线，并对比工具增强方法；论文方向性结论是外部可能性矩阵能支持推理质量与任务成功，但摘要未披露具体量化提升数字，需查看全文。
