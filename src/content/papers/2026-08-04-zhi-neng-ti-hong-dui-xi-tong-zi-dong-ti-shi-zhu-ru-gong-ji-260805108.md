---
title: 'Agent Against Agent: An Agentic System for Automatic Prompt Injection Red
  Teaming'
title_zh: 智能体红队系统：自动提示注入攻击
authors:
- Yanting Wang
- Chenlong Yin
- Runpeng Geng
- Jinyuan Jia
affiliations:
- The Pennsylvania State University
arxiv_id: '2608.05108'
url: https://arxiv.org/abs/2608.05108
pdf_url: https://arxiv.org/pdf/2608.05108
published: '2026-08-04'
collected: '2026-08-08'
category: Agent
direction: Agent 红队测试与安全攻击
tags:
- Prompt Injection
- Red Teaming
- Agentic System
- Attack
- LLM Security
- Strategy Library
one_liner: 提出PIMiner，通过多任务训练构建可迁移策略库，实现跨LLM的高效提示注入红队测试。
practical_value: '- 对 Agent 推荐系统做安全评估时，可借鉴策略库思路：收集历史攻击成功案例，沉淀为可复用的策略模板，对新上线的 Agent
  模块快速进行鲁棒性测试。

  - 高度稀疏查询（每个样本仅需约 10 次查询）的做法，适合在线上生产环境以极低采样成本持续探测 Agent 是否有注入漏洞，避免大量无效请求影响服务。

  - 跨模型迁移能力表明：可以基于少数开源模型训练出一套通用攻击策略库，再迁移到闭源商业模型（如 GPT-4）上做红队测试，业务中不必强行获取目标模型内部信息。

  - 攻击成功样本可直接用于构造对抗训练数据，强化防御，从而让电商搜索 / 推荐 Agent 更稳健地处理不可信的外部内容（如商品描述、用户评价、工具返回结果）。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有基于强化学习的提示注入红队方法泛化性差，训练的 attacker 模型难以迁移到未见过的目标 LLM Agent，且需要大量查询，效率低下。

**方法关键点**：设计 PIMiner，一个自动红队 Agent 系统。训练阶段，它在多个 (数据集, 目标模型) 对上迭代攻击，从 scratch 构建一个可复用的**策略库**，每条策略对应一种成功注入模式。测试阶段，对于全新的目标 LLM，PIMiner 直接调用策略库，结合极少量的在线试探（每样本仅约 10 次查询）快速适配，无需任何额外训练。

**关键结果**：在严格协议下，IPIArena 上对 Gemini-2.5-Pro 的 ASR 达 76.2%，GPT-5.1 达 61.9%，Claude-Sonnet-4.5 达 42.9%；在 AgentDojo 上分别达到 86.7%、53.3%、40.0%。证实了策略库的强迁移能力和高效攻击性能。
