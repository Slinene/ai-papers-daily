---
title: 'OpenART: Scaling Agent Red Teaming via Open-Ended Environment Evolution'
title_zh: OpenART：基于开放式环境演化的 Agent 红队规模化评测
authors:
- Yunhao Chen
- Xin Wang
- Yixu Wang
- Yi Liu
- Jie Li
- Yan Teng
- Xingjun Ma
- Xia Hu
- Yu-Gang Jiang
affiliations:
- Fudan University
- Shanghai Artificial Intelligence Laboratory
- XSafeAI
arxiv_id: '2608.00677'
url: https://arxiv.org/abs/2608.00677
pdf_url: https://arxiv.org/pdf/2608.00677
published: '2026-07-31'
collected: '2026-08-14'
category: Agent
direction: Agent 安全红队 · 环境演化
tags:
- Agent Safety
- Red Teaming
- Environment Evolution
- Black-box Attack
- Markov Hypergraph
- Benchmark
one_liner: 提出开放式环境演化基准 OpenART 与黑盒攻击策略 EMHA，在 75 种 Agent-模型配置上取得 85.0% 攻击成功率
practical_value: '- 在电商/广告等长会话 Agent 场景中，可借鉴「环境状态演化」思路：不直接攻击模型输入，而是通过授权状态转移逐步污染共享上下文，测试推荐/搜索
  Agent 在累积状态下的鲁棒性。

  - 多工具调用（如商品检索、订单查询、广告投放）中，可建立状态转移超图，识别高风险路径，提前限制敏感状态变更，防止攻击链通过多个合法工具组合放大风险。

  - 评估 Agent 安全时，除了模型能力，需重点关注 runtime 框架选择：文中发现目标 Agent 身份可解释额外 7.6% ASR 变异，提示生产中应测试不同
  Agent 运行时的安全性差异，避免仅依赖模型层防御。

  - 对于长链路任务（如电商导购 Agent 执行 97 次工具调用），可引入动态环境监控，检测偏离任务目标的异常状态演化，作为红队预警机制。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 Agent 安全评测集中于短时静态任务，忽略持久环境中早期状态变化对后续决策的累积影响，且各 benchmark 接口不统一，难以横向比较不同 Agent runtime。

**方法关键点**：构建 OpenART 基准，包含超过 10,000 个验证过的有状态场景，覆盖 50 个领域，源自 500K+ 工具/MCP/Skills，任务中位需要 97 次工具调用；通过目标适配器投影到 15 个已部署 Agent、5 个基础模型、8 种攻击向量，统一评估 75 个 Agent-模型配置。提出 Evolutionary Markov Hypergraph Attack (EMHA)，一种黑盒策略，在超图路径上协调授权状态转换实现反馈驱动的环境演化，无需参数更新，任务目标与安全约束保持不变，仅环境状态变化。

**关键结果**：在所有 75 个配置上，EMHA 汇总严格 Attack Success Rate (ASR) 达 85.0%；相比仅指令演化的优势从简单环境约 2% 扩大到最复杂环境超过 17%；引入目标 Agent 身份额外解释 7.6% ASR 变异，表明运行时实现对安全有显著影响，不仅取决于底层模型能力。
