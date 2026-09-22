---
title: 'DolphinBench: Mapping the Pareto Frontier of Agent Memory'
title_zh: DolphinBench：刻画智能体记忆的帕累托前沿
authors:
- Soumil Rathi
- Deshraj Yadav
- Taranjeet Singh
affiliations:
- Mem0
arxiv_id: '2609.24971'
url: https://arxiv.org/abs/2609.24971
pdf_url: https://arxiv.org/pdf/2609.24971
published: '2026-09-21'
collected: '2026-09-22'
category: Eval
direction: Agent 记忆评估基准
tags:
- Agent Memory
- Benchmark
- Task Completion
- Cost-Latency
- Long-term Memory
one_liner: 首个通过任务完成直接评估智能体记忆，并要求报告成本与延迟的基准
practical_value: '- **任务完成式记忆评估**：在电商客服/导购 Agent 中，不要只测“用户偏好是什么”，而让 Agent 执行修改未支付订单、按用户历史沟通风格回复等任务，考察隐式的记忆触发与检索能力。

  - **强制成本与延迟上报**：上线 Agent 记忆模块时，同时记录 token 成本、检索步数、p50/p95 延迟，避免通过全量回放上下文或无限检索刷准确率。

  - **用 with/without history 验证任务依赖**：构建评测集时，删除相关历史后任务应无法完成，才能确认评测的是 memory 模块，而非
  prompt 推理或通用能力。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有 Agent 记忆基准多为 QA 形式，问题本身会暗示需要检索某类事实，且通常只看准确率，忽视成本与延迟，导致记忆系统可通过不合理资源消耗刷分。

**方法关键点**：DolphinBench 直接通过任务完成评估记忆。包含 3 个知识工作 persona，每个约 500k tokens 用户消息历史，每个 persona 200 个任务，任务依赖历史信息才能完成。每个任务都用带/不带相关历史各跑一次 agent 进行验证：要求带历史成功、不带历史失败。所有提交必须报告总成本和延迟，与准确率共同构成帕累托前沿。

**关键结果**：这是首个同时具备“任务完成式评估、历史依赖验证、成本+延迟+准确率联合上报”三要素的 Agent 记忆基准。数据集与评估代码已公开。
