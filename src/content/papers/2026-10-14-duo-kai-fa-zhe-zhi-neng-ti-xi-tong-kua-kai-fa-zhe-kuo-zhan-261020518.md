---
title: 'The Wealth of Agents: Scaling Agentic AI Across Developers'
title_zh: 多开发者智能体系统：跨开发者扩展 Agent 能力
authors:
- Austin W. Hanjie
- Carlos E. Jimenez
- Zirui Wang
- Karthik Narasimhan
affiliations:
- Princeton University
- UC Berkeley
arxiv_id: '2610.20518'
url: https://arxiv.org/abs/2610.20518
pdf_url: https://arxiv.org/pdf/2610.20518
published: '2026-10-14'
collected: '2026-10-15'
category: MultiAgent
direction: 多开发者 Agent 生态协作与激励
tags:
- MDA
- routed-SDA
- agent routing
- specialization
- incentive design
- GAIA
one_liner: 提出多开发者 MDA：子任务分解路由组合专业 Agent，将≤35%单点准确率提至70%
practical_value: '- 如果你在做多商家/多服务商 Agent 平台或购物助手生态，不应只把整单路由给一个最强通用 Agent；采用 δ-MDA 式「请求分解
  → 子任务路由 → 结果组合」，让中尾部专业 Agent 在文件解析、网页理解、商品识别等子能力上竞争，可整体提质量并降低大模型成本。

  - 路由模型要建立「交互经验缓冲池 + update-agent」在线闭环：初始 Agent 描述常常夸大，必须用真实任务结果持续更新全局/上下文排序；这在电商场景中多
  Agent 能力重叠、服务商自述不可信时尤其重要。

  - 理论与实验一致：按整请求竞争的 routed-SDA 会激励开发者都做泛化系统；只有按子能力调度并以贡献/收益补偿时，才有动力做垂直专业 Agent。平台机制设计比单点模型优化更能决定生态能力上限。

  - 注意适用边界：当任务所需技能很窄如纯搜索时，任务分解/组合的协调成本可能高于收益，此时直接 route 到单个 SDA 更划算；建议先做能力宽度评估再决定是否启用
  MDA。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

动机：当前 Agent 系统多由单一开发者全权设计，小开发者被迫重建搜索、解析、编排等基础能力，难以用垂直数据或服务参与前沿能力建设。这篇工作提出多开发者智能体系统 MDA，把「跨开发者组合能力」作为新的 scaling axis，并用实验和理论比较 SDA、routed-SDA 与 δ-MDA。

方法关键点：
- 形式化三类系统：SDA 单开发者独立执行；routed-SDA 由 σ 路由整请求到单个 SDA；δ-MDA 先由 δγ-agent 把请求分解为子任务，再按子任务路由到不同 Agent，最后组合回复。
- 开发者建模：specification-agent 从无标签数据生成通用/专业开发者规格，meta-agent 在预算内迭代生成 ReAct agent；构建通用池 AG、专业池 AS、多 Agent 池 AMAS，并设置高/中/低三档模型能力层级。
- 路由机制：σ-agent 结合开发者 Agent 描述与真实交互经验 buffer，由 update-agent 生成全局和上下文相关排序，模拟多开发者竞争与不实能力宣称。
- 理论模型：用 Tullock contest 建模路由竞争，分析整请求竞争会诱导泛化均衡，而按子技能路由能支持专业化分工；交通份额补偿会诱导泛化，需要设计贡献对齐的收益机制。

关键实验：在 GAIA 上，专业池单 Agent 最高准确率 35%，δ-MDA 提升到 70.1%，超过最佳多 Agent SDA 的 67%，且成本约为其一半；去掉 high-tier 模型后 δ-MDA 仍达 67%/$9，优于中低端 SDA 的 60%/$8。一个 standalone 仅 19% 的互补 Agent，能让已有池从 40.4% 提升到 53.2%，说明单点指标会低估 Agent 在生态中的价值。但在纯搜索的 SealQA 上，δ-MDA 反而差于 rSDA 且成本更高，说明 MDA 并非普适。

最值得记住的一句话：MDA 的核心价值不在单个 Agent 的 standalone 分数，而在按子能力路由与激励设计能否让专业化供给持续对齐集体收益。
