---
title: 'StartupBench: Benchmarking General-Purpose Agents on Market-Validated End-to-End
  Workflows'
title_zh: StartupBench：基于市场验证的端到端工作流评测通用智能体
authors:
- Liya Zhu
- Xin Ma
- Tao Liu
- Haodong Wang
- Ge Zhang
- Jingzhe Ding
- Qingshui Gu
- Yongjie Zhong
- Jinxiang Meng
- Yuan Gao
affiliations:
- ByteDance Seed
- Nanjing University
- M-A-P
- TokenWave.AI
arxiv_id: '2608.17800'
url: https://arxiv.org/abs/2608.17800
pdf_url: https://arxiv.org/pdf/2608.17800
published: '2026-08-17'
collected: '2026-08-20'
category: Eval
direction: Agent 端到端真实工作流评测
tags:
- Agent Benchmark
- E2E Workflows
- Market-Validated
- LLM Agents
- Evaluation
one_liner: 构建首个基于市场验证 AI 创业产品工作流的端到端 Agent 基准，最强模型完成率仅约30%
practical_value: '- 构建内部 Agent 评测集时，不要只依赖公开基准或研究者自选任务，可以从已上线且有稳定用户的产品工作流中提取真实任务，例如电商运营中的选品分析、商品文案生成、营销活动策划、客服工单处理等，让评测更贴近业务真实需求。

  - 采用 deliverable-oriented 的任务定义：要求 Agent 产出完整可交付物（如报告、代码、设计文档），并用细粒度 rubric 对多个维度打分。这样可以捕捉部分正确但不可交付的中间进展，比简单的
  pass/fail 更能区分模型能力。

  - 论文发现复杂指令遵循和领域专业知识是主要失败点。在电商/广告场景落地 Agent 时，建议通过领域知识注入（如 RAG 挂载商品知识库、行业规则库）和约束检查模块来强化这些薄弱环节，而不是单纯依赖通用大模型。

  - 评估时要使用统一的 agent harness，避免不同框架差异干扰模型能力判断；同时关注模型在部分进展上的表现，为迭代优化提供信号。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 Agent 基准大多由研究者选定任务，难以判断模型能力的进步是否对应真实用户需求。StartupBench 选取已被市场验证的 AI 创业产品作为任务来源，以产品采用度作为“真实需求”的代理信号。

**方法关键点**：系统梳理多个有实际用户的 AI 产品及其工作流，将产品核心工作流转化为端到端、以交付物为导向的任务（如生成报告、代码、设计文档等），覆盖多个专业领域。评估采用与任务复杂度匹配的细粒度 rubric，并在统一 agent harness 下评估代表性模型。

**关键结果**：在统一评测框架下，最强模型仅成功完成约 30% 的任务，尽管在许多任务上取得了可观的局部进展。进一步分析显示，复杂指令遵循和领域专业知识是失败的主要来源。该结果表明，许多已被市场验证的工作流仍超出当前通用 Agent 的可靠能力边界，StartupBench 可作为衡量真实用户任务端到端完成度的实证基准。
