---
title: 'SIMMER: Benchmarking Latent Failures in LLM Executable Planning with a World
  Model'
title_zh: SIMMER：基于世界模型的LLM可执行规划潜在失败基准测试
authors:
- Xiaoxin Lu
- Ranran Haoran Zhang
- Rui Zhang
affiliations:
- The Pennsylvania State University
arxiv_id: '2606.14574'
url: https://arxiv.org/abs/2606.14574
pdf_url: https://arxiv.org/pdf/2606.14574
published: '2026-06-12'
collected: '2026-06-15'
category: Agent
direction: Agent 规划可靠性评估 · 潜在失败检测
tags:
- LLM Planning
- Latent Failures
- World Model
- Agent Evaluation
- Safety
one_liner: 提出符号化厨房世界模型与状态机执行器，系统评估并缓解LLM智能体规划中的潜在与不可逆失败。
practical_value: '- 借鉴“潜在失败”概念，在多步决策流程（如促销路径规划、智能客服对话策略）中引入隐性错误检测，避免最终目标被无声破坏。

  - 使用符号化状态机执行器 + 世界模型进行离线仿真，可精确审计计划中的状态传播（如库存变化、用户意图漂移）导致的不可逆错误。

  - 采用反事实前瞻模拟（Counterfactual Foresight），让模型在生成每一步时主动预测并修正潜在的隐性危害，显著提升规划安全性。

  - 在序列推荐或 Agent 交互中，不应只检查即时前置条件，需定义后执行审计规则，捕捉全局安全违规（如资源耗尽、死锁）。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：LLM 规划评估长期关注执行时的即时失败，却忽略了一类更隐蔽的错误——潜在失败。这些错误不立即导致执行中止，而是通过隐式状态传播（如交叉污染）无声破坏最终目标，甚至造成不可逆后果。针对该评估盲区，本文提出 SIMMER 基准，旨在系统检测和缓解 LLM 智能体在物理任务规划中的潜在失败。

**方法**：
- 构造了一个厨房领域的符号化世界模型，包含从 wikiHow、Instructables 等提取的 77 个动作、262 个对象和约 46,800 种真实交互，能精细跟踪污染、温度等隐式状态变化。
- 定义了三级失败分类：**即时失败**（违反动作前置条件）、**潜在失败**（状态传播错误、隐含前置条件遗漏、后目标忽略）以及**不可逆失败**。
- 实现了状态机执行器，分两阶段审计：逐步执行时捕捉即时失败，执行后扫描全局状态（如食品污染、电器未关）以发现潜在与不可逆失败。
- 在 100 个覆盖 12 种烹饪技法、平均每任务含 26.6 个动作的任务上，评估了 GPT-5.4、Claude Opus 4.6、Gemini 3 Flash 等 6 个前沿与开源模型，并测试了 **Self-Refine** 和 **反事实前瞻模拟**（生成每一步前模拟状态并自检）两种缓解策略。

**关键结果**：
- 即使最强模型，无错误计划最高仅 **17%**；整体平均仅 7.2%。
- 潜在失败影响 **29–56%** 的计划，其中大部分为不可逆的错误（最高 45%）。
- 反事实前瞻模拟可将前沿模型的潜在失败降低 **72%**，不可逆失败降低 **75%**，而简单的全计划自纠效果较差。
- 错误分布显示：即时失败主要源于具身推理缺陷和状态跟踪错误；潜在失败集中在状态传播失控、隐含前置条件无知和事后疏忽。

**核心启示**：LLM 规划评估必须超越表面执行成功，显式跟踪隐式状态并强制步骤级自检方能大幅减少危害性潜在失败。
