---
title: 'Atria Dawn: The Dawn of Agentic Superintelligence'
title_zh: Atria Dawn：智能体超级智能的黎明
authors:
- Honglin Guo
- Tao Gui
- Yicheng Chen
- Guanting Dong
- Qiming Ge
- Yuyang Hu
- Zixian Huang
- Jiajie Jin
- Alexander Lam
- Yining Li
affiliations:
- Atria Team
- Fudan University
arxiv_id: '2609.15818'
url: https://arxiv.org/abs/2609.15818
pdf_url: https://arxiv.org/pdf/2609.15818
published: '2026-09-13'
collected: '2026-09-15'
category: Agent
direction: 智能体基础模型与可验证经验训练
tags:
- Agentic LLM
- Verifiable Experience Pipeline
- Tool Use
- Human-AI Collaboration
- Research Agents
one_liner: 推出 Atria Dawn Preview：基于可验证经验管道训练的智能体基础模型，16个基准中5个达最高分，并揭示人机协作转向项目级伙伴关系
practical_value: '- 可验证经验管道：在电商/推荐 Agent 场景中，可以把模型输出接入可执行环境（线上沙箱、模拟器、规则引擎）或外部验证信号（转化、GMV、AB
  实验结果），将工具调用、策略生成转化为可验证经验，减少不可执行动作和幻觉。

  - 人机协作模式：让 Agent 频繁提出方法和实现修改，人类保留最终决策与反馈，适合电商 Agent 工作流（选品、出价、文案生成）中设置 human-in-the-loop
  决策门，提升效率且保持风险可控。

  - 任务记录分析：借鉴其 769 条任务记录的量化方法，用 Agent 日志评估哪些环节“无 AI 不可行”，识别高杠杆场景，指导资源分配。

  - 适用边界：论文聚焦科研与工程 Agent，非直接推荐系统；但可复用“可执行验证 + 工具交互”的建模思路到生成式推荐或策略 Agent，强化外部奖励闭环。'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
AI agents 开始参与开发其后继模型，改变智能生产方式和研究者角色。真实科研/工程任务要求 agent 不仅会聊天，还要可靠地调用工具、在可执行环境中完成工作并接受外部验证。

### 方法
Atria Dawn Preview 是面向科研与工程工作流的 foundation agentic language model。核心训练机制是 Verifiable Experience Pipeline：把 tool-mediated interactions 连接到 executable environments，用 externally verified outcomes 作为优化信号，使模型从可验证经验中学习。

### 关键结果
在 16 个真实科研、工程、数字工作基准上，模型达到 frontier agent 水平，其中 5 个取得最高分。同时，作者把自身研发过程作为人机协作案例：分析 56 位参与者的 769 条任务记录和 agent logs；约 1/3 的 AI 辅助任务被评估为无 AI 不可行；agent 频繁提出方法并实现修改，人类保留最终决策、通过判断和反馈引导探索，协作从 task-level execution 转向 project-level partnership。结论强调未来自主 AI 研究需同步提升发现能力与人类监督质量。
