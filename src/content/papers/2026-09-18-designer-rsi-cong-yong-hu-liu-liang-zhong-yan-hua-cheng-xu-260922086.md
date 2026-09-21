---
title: 'Designer-RSI: Evolving Procedural Memory from User Traffic for Agentic Graphic
  Design'
title_zh: Designer-RSI：从用户流量中演化程序性记忆用于智能平面设计
authors:
- Hongyang Du
- Lan Yan
- Christian Flores
- Asim Kadav
affiliations:
- Adobe
- Brown University
arxiv_id: '2609.22086'
url: https://arxiv.org/abs/2609.22086
pdf_url: https://arxiv.org/pdf/2609.22086
published: '2026-09-18'
collected: '2026-09-21'
category: Agent
direction: Agent 外部程序性记忆持续进化
tags:
- Procedural Memory
- Continual Adaptation
- Agentic Design
- LLM Agents
- Self-Improvement
- Tool Use
one_liner: 冻结大模型加外部程序性记忆持续适应，通过拓宽与深化技能库将设计智能体执行成功率从72.7%提升至99.3%
practical_value: '- 可复用外部程序性记忆库：电商/广告场景中涉及多步工具调用的 Agent（如自动生成商品详情页、广告投放流程调整）可将常用操作流程沉淀为自然语言技能，通过执行经验自动扩充和修订，无需微调模型。

  - 拓宽+深化双机制：遇到重复出现的未覆盖子任务时提取新技能（widening）；对已有技能用成功/失败轨迹对比修订（deepening），并设置匹配重放门（matched
  replay gate）作为自动化回归测试，确保新技能不破坏已有成功案例，可直接复用于业务 Agent 的技能迭代。

  - 冻结前沿模型 + 外部记忆适应：避免频繁更新大模型权重，降低成本和风险；适合模型无法频繁重训但需要快速适应新任务流的在线系统，如搜索推荐中的 Agent 策略调整。

  - 噪声反馈下的持续学习：设计任务无可靠程序化评估 oracle，但通过自动评分轨迹和真实用户 brief 仍能有效演化技能；对电商中大量弱监督/无监督反馈场景有借鉴意义。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：专业平面设计是长周期 agentic 任务，结构化可编辑产物来自众多相互依赖的操作，但结果缺乏可靠的程序化评估 oracle，传统静态 agent 难以持续适应复杂多样的用户需求。

**方法关键点**：冻结前沿模型通过 230+ 工具操作专业设计软件，外部程序性记忆以自然语言技能形式存储可复用设计流程。记忆通过两种机制演化：拓宽（widening）为重复出现的未覆盖子任务采集新流程；深化（deepening）根据自身成功与失败的执行修订现有技能。引入匹配重放门（matched replay gate），只接受能修复失败且不回归已观察成功案例的修改，确保记忆更新安全。整个过程无权重更新、无人工标签。

**关键结果**：在 1,406 个真实用户 brief 和 1,869 个自动评分轨迹上经过 5 轮迭代，技能库从 76 个文档衍生技能增至 139 个；GenEval2 执行成功率从 72.7% 提升至 99.3%，生成质量提高 11.99 分。在四个专项设计基准上，对无技能 agent 的胜率分别达到 61.8%（Claude-Sonnet-4）和 67.6%（Claude-Opus-4.6）。在 200 个留出 brief 上，单独拓宽或深化的胜率为 49.4% / 48.6%，组合使用达到 58.5%（p=0.025），证明双机制协同有效。
