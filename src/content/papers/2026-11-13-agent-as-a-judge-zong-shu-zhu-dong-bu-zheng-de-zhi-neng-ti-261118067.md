---
title: Agent-as-a-Judge
title_zh: Agent-as-a-Judge 综述：主动补证的智能体评估
authors:
- Runyang You
- Hongru Cai
- Caiqi Zhang
- Qiancheng Xu
- Meng Liu
- Tiezheng Yu
- Yongqi Li
- Wenjie Li
affiliations:
- The Hong Kong Polytechnic University
- University of Cambridge
- Shandong University
- Huawei Technologies
arxiv_id: '2611.18067'
url: https://arxiv.org/abs/2611.18067
pdf_url: https://arxiv.org/pdf/2611.18067
published: '2026-11-13'
collected: '2026-11-16'
category: Eval
direction: Agent 评估机制综述
tags:
- Agent-as-a-Judge
- LLM-as-a-Judge
- Agentic Evaluation
- Multi-Agent
- Tool Integration
one_liner: 系统梳理 Agent-as-a-Judge 设计空间，涵盖多智能体协作、工具集成、记忆与规划，并复现关键评测结果
practical_value: '- 评估电商/搜索 Agent 时，不用静态日志当唯一依据；让 judge 能回放或查询商品库、库存、广告策略、UI 状态，再对推荐轨迹/工具调用打分。可先把「列出缺失证据并补证」设为
  judge 的前置步骤。

  - 采用多智能体分工：一个 agent 生成检查项并做外部事实核查，另一个按 rubric 打分，第三个做政策合规检查（广告披露、价格真实性、隐私）。这比单次
  LLM judge 更稳，尤其适合多轮购物助手和 query 改写评估。

  - 给 judge 增加 memory，把同一 session 中已经核实过的 item/query/用户意图缓存，避免重复工具调用；对长轨迹用结构化 workflow
  + early exit，只对关键步骤深查，控制成本。

  - 上线前用小规模业务数据复现 agentic judge 的收益；本文复现发现 agentic 提升不均衡，盲目上 agentic evaluator 可能只增加成本。可先在低风险任务（搜索建议、商品推荐理由）试点。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：LLM-as-a-Judge 在固定上下文下只能依据给定材料打分，难以处理评估智能体轨迹、可执行产物或领域报告时的证据缺口：环境状态未记录、事实声明需外部核实。被动判定会误判，因此需要能主动检查、补证后再下结论的 Agent-as-a-Judge。

方法关键点：用 evaluation-directed checks 定义范围，覆盖结构化工作流与观察驱动控制；按多智能体协作、工具集成、记忆、规划四个机制组织设计空间；这些机制共同提供判定所需的检查与证据。还整理并复现了代表性 agentic judge 的公开分数。

关键结果：工具和记忆是主动补证的核心；复现显示不同 agentic judge 在任务上的提升不一致，说明需要面向专门任务的 agentic evaluation。
