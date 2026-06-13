---
title: The Cold-Start Safety Gap in LLM Agents
title_zh: LLM Agent 的冷启动安全差距现象
authors:
- Chung-En Sun
- Linbo Liu
- Tsui-Wei Weng
affiliations:
- University of California, San Diego
arxiv_id: '2606.07867'
url: https://arxiv.org/abs/2606.07867
pdf_url: https://arxiv.org/pdf/2606.07867
published: '2026-06-04'
collected: '2026-06-13'
category: Agent
direction: Agent 安全性 · 冷启动安全差距
tags:
- cold-start
- safety
- LLM agents
- benchmark
- representation analysis
- deployment strategy
one_liner: 发现 LLM Agent 在会话起始安全性最弱，通过预先完成少量常规任务可显著提升安全性 9-52%
practical_value: '- **Agent 部署预热策略**：在 Agent 正式接收用户请求前，先让它完成几个常规的无害工具调用任务（如查询天气、简单
  API 调用），可以显著降低后续面对恶意请求时的风险。这个预热步骤可直接嵌入 Agent 初始化流程，成本低且不影响模型功能。

  - **安全评估中加入对话深度维度**：现有安全评估往往只在首轮对话测试，遗漏了冷启动脆弱性。在设计内部 Agent 安全 Benchmark 时，应控制前置常规任务数量，模拟真实部署中上下文逐渐累积的场景，避免高估安全性。

  - **基于隐藏表示的在线安全监控**：论文发现模型隐藏状态会随前置任务增多向安全对齐区域迁移，这一动态特征可用来构建轻量级安全监控器——在 Agent 运行过程中持续检测状态偏离，预警潜在不安全行为。

  - **区分安全与效用的影响因素**：实验表明，Agent 先前的回答对安全影响较小但对保持效用至关重要，因此预热时若只施以安全指令而忽略实际任务执行，可能损害后续功能。部署预热应使用真实的常规任务，而非单纯的安全提示。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：具备工具调用能力的 LLM Agent 在实际部署中存在安全隐患，但现有评测通常假定 Agent 从零历史开始应对危险请求，忽略了会话长度对安全性的影响。该工作首次揭示“冷启动安全差距”——Agent 在对话初期危险性最高，随着前置常规任务数增加安全性逐渐提高。

**方法**：提出 SODA（Safety Over Depth for Agents）基准，控制 Agent 在遭遇安全威胁前已完成的前置常规任务数量（0 至 20），评估 7 款来自 4 个家族的模型。通过隐藏状态表示分析、消融实验（区分任务内容、模型自身回答、用户消息等）探究影响机制。并在 AgentHarm、Agent Safety Bench 等安全基准与 BFCL、API-Bank 等效用基准上交叉验证。

**关键结果**：
- 前置任务数从 0 增至 20 时，安全性提升幅度达 9–52%，几乎所有模型均表现出冷启动脆弱性。
- 表示分析证实隐藏状态逐步向安全对齐区域偏移。
- 消融发现：前置常规任务本身是安全提升的主要驱动，而 Agent 自己之前的回答对安全影响较小，但对保持后续功能性至关重要。
- 预热策略在不牺牲工具使用能力的条件下，能同时提升安全基准与效用基准上的表现。
