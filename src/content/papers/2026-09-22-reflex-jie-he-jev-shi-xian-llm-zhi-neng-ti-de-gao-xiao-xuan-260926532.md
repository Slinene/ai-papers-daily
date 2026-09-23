---
title: REFLEX with Jev for Efficient Selective Control in LLM Agents
title_zh: REFLEX 结合 Jev 实现 LLM 智能体的高效选择性控制
authors:
- Tiantong Wu
- Wei Yang Bryan Lim
affiliations:
- Nanyang Technological University
arxiv_id: '2609.26532'
url: https://arxiv.org/abs/2609.26532
pdf_url: https://arxiv.org/pdf/2609.26532
published: '2026-09-22'
collected: '2026-09-23'
category: Agent
direction: Agent 选择性控制与强模型调用优化
tags:
- Agent
- Selective Control
- LLM Routing
- Jev
- Tool Use
- Efficiency
one_liner: REFLEX 用 Jev 做快速类型决策层，低置信或需生成时调强 LLM，100 任务基准上 95% 成功并减少 72.7% 强模型调用
practical_value: '- 架构拆分：在电商导购/广告投放 Agent 中，把“选哪个工具、参数是否合法、是否继续”等有限集合决策从生成式 LLM 中剥离，用轻量分类器或
  Jev 类模型先做 typed decision；仅当置信度低于阈值或需要自由文本生成时再调用强模型，可省 70%+ 强模型调用，降低延迟与成本。

  - 回退设计：对边界场景（如退款/价格修改等高风险动作）要保守，即便轻量模型置信度不低，也设置 authorization boundary 附近强制回退或人工/强模型复核；因为论文显示授权边界附近的
  near-valid alternatives 是主要失败来源。

  - 动作空间控制：候选工具/动作数量不要过大，尽量合并语义相近的 action；论文指出可靠性依赖 action-set size，过大会削弱 Jev 选择质量，可先在业务数据上测
  action-set size 的影响曲线。

  - 先做基线：如果已有便宜生成式模型（如 GPT-4o mini/Gemini Flash）的 cascade 路由准确率已经很高，typed decision
  layer 可能收益有限；建议先做离线对比实验，再决定是否引入 Jev，而不是直接上。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

动机：LLM agents 在每一步都调用生成式强模型，但很多步骤只需从固定集合中选择（工具、参数、是否继续），造成计算浪费。核心问题是专用决策模型能否处理有界选择并保持成功率，以及何时优于廉价生成级联。
方法：REFLEX 架构使用 Jev 作为快速 typed 决策层，输出类型化概率决策；当置信度低或需要生成时回退调用强 LLM。在冻结的 100 任务基准上评估，使用多种 fallback 家族；通过受控干预分析 action-set 大小和授权边界附近 near-valid alternatives 对可靠性的影响；同时用外部 BFCL 和 τ 风格评估与廉价生成级联对比。
结果：在 100 任务基准上，REFLEX 达到 95% 成功率，同时比仅用强模型智能体减少 72.7% 强模型调用；减少在三种 fallback 家族中持续。受控实验显示可靠性依赖动作集大小和授权边界附近的 near-valid alternatives。外部 BFCL 和 τ 风格评估中，当普通路由已经高度准确时，对廉价生成级联的优势有限。
