---
title: 'IQuest-Q1: Advancing Foundation Capabilities for Agentic CLI Systems'
title_zh: IQuest-Q1：面向 Agentic CLI 系统的稀疏 MoE 基础模型
authors:
- A. Jian Yang
- An Huang
- Bo Dan
- Chen Mu
- Chengran Yang
- Chuan Shi
- Feng Chang
- Hongxin Li
- Hongyuan Tao
- Jinxing Zhang
affiliations:
- IQuest Research
arxiv_id: '2610.30949'
url: https://arxiv.org/abs/2610.30949
pdf_url: https://arxiv.org/pdf/2610.30949
published: '2026-10-21'
collected: '2026-10-24'
category: Agent
direction: Agentic LLM 训练 · MoE 与多阶段后训练
tags:
- MoE
- Agentic LLM
- Post-training
- RL
- Model Merging
- CLI Systems
one_liner: 320B 稀疏 MoE 模型，通过多阶段训练和模型合并强化 CLI agent 编码能力
practical_value: '- 稀疏 MoE 架构（320B 总参、15B 激活）在保持大模型容量的同时控制推理成本，适合需要实时响应的搜索/推荐 Agent
  场景，可参考其专家路由设计，减少线上 latency。

  - 多 scaffold + 多版本后训练策略（SFT + 领域 RL + MOPD 跨多种脚手架）能整合互补训练信号，在电商 Agent 中可借鉴：针对商品知识、会话策略、API
  调用等不同子任务分别设计 scaffold 和奖励，再合并训练，提升整体鲁棒性。

  - 模型合并技术（merge 不同 expert 和 checkpoint 并缓解参数冲突）可直接迁移到多任务推荐模型融合，例如把单品推荐、query 改写、对话策略等专家模型合并为统一模型，降低维护成本。

  - 两阶段课程学习先通用后增加 coding 数据，可用于垂直领域 LLM 微调：先在大规模通用语料上稳定训练，再逐步增加电商/广告领域数据，避免灾难性遗忘。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM-based agents 需要在 CLI 环境中进行迭代推理、行动和交互，现有基础模型在编码与通用能力上仍有不足，且大模型推理成本高。

**方法关键点**：IQuest-Q1 是一个 sparse MoE agentic foundation model，总参数 320B、激活 15B。训练分三阶段：(1) 预训练结合 Stable SplitNorm、Muon、muP 与两阶段课程（第二阶段增加 coding 数据比例），保持安全学习率与最优学习率之间的稳定裕度；(2) 精细化 mid-training，扩展领域和格式数据混合，逐步延长上下文；(3) multi-scaffold 与 multi-version 后训练，跨多种脚手架组合 SFT、领域定向 RL 与 MOPD，整合互补信号。最后通过 model merging 融合不同专家与 checkpoint，缓解参数更新冲突。

**关键结果**：在多个 CLI 与通用 benchmark 上达到领先水平：DeepSWE v1.1 74.2，NL2Repo 75.3，CyberGym 88.1，Terminal-Bench 2.1 89.1，JobBench 65.7，Agents' Last Exam 32.2，Humanity's Last Exam 43.4（无工具），自建 IQuest-CLIBench 58.5。
