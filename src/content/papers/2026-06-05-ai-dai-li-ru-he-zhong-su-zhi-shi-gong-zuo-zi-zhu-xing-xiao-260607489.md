---
title: 'How AI Agents Reshape Knowledge Work: Autonomy, Efficiency, and Scope'
title_zh: AI 代理如何重塑知识工作：自主性、效率与范围
authors:
- Jeremy Yang
- Kate Zyskowski
- Noah Yonack
- Jerry Ma
affiliations:
- Harvard University
- Perplexity
arxiv_id: '2606.07489'
url: https://arxiv.org/abs/2606.07489
pdf_url: https://arxiv.org/pdf/2606.07489
published: '2026-06-05'
collected: '2026-06-08'
category: Agent
direction: AI Agent 自主任务执行与效率分析
tags:
- AI agents
- knowledge work
- autonomy
- efficiency
- task scope
- natural experiment
one_liner: 基于 Perplexity 生产数据，用匹配对自然实验证明代理将任务时间减少 87%、成本降低 94%，并扩展了工作广度与深度
practical_value: '- **任务路由决策**：代理的高固定成本、低边际成本特性（f_Agent > f_Conversational, m_Agent
  < m_Conversational）可指导电商智能客服或 Agent 系统设计——对简单查询（如 FAQ）使用对话式，对多步复杂任务（如售后处理、跨系统操作）自动切换为代理执行，平衡体验与成本。

  - **匹配对评估范式**：利用同一用户提交近似查询到两个产品（相似度 >0.99）作为自然实验，消除了任务和用户异质性，能干净地衡量新功能的增量价值。在推荐系统或
  Agent 迭代中，可设计类似 A/B 测试，用近似上下文配对评估效果。

  - **代理解锁新生需求**：Computer 用户在代理模式下尝试了更多跨领域、高认知复杂度的任务，且 23% 的查询涉及全新任务类型。生成式推荐系统可借鉴此发现，在用户授权下，主动生成超出历史兴趣的商品或内容，扩大用户探索边界。

  - **自主性与质量共存**：代理的自动执行并未导致不满意率上升（反而降低 55%），验证了自主性不必然牺牲输出质量。对于多智体系统，可在编排设计中嵌入校验步骤，如自动复核、用户确认点，确保长链路任务可靠性。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**：AI 系统正从对话式助手向能端到端执行任务的自主代理演进，但缺乏大规模生产数据证明其对现实工作的影响。本文利用 Perplexity 的 Search（对话式）和 Computer（代理式）产品，研究这一转变如何改变知识工作的完成方式。

**方法关键点**：
- 构建个体级任务模型，假定代理固定委托成本更高、边际执行成本更低，推导出代理会扩展可负担任务边界、增加总价值和剩余。
- 匹配对自然实验：从 100,000 双产品用户中抽取 10,000 对初始查询余弦相似度 >0.99 的会话，控制任务内容，对比自主性、效率和范围。
- 自主性衡量：机器执行时间（Computer 记录工具调用墙钟时间）、跟进查询分类、用户不满意度信号。
- 效率估计：工具推算、LLM 估算、用户访谈三角度量化 Search+Human 与 Computer+Human 的时间成本，人工时薪映射至 BLS 职业工资数据。

**关键实验与结果**：
- 自主性：Computer 平均每会话自主工作 26 分钟，Search 仅 33 秒（48×），跟进查询从指令式转向验证/扩展；Computer 的中高不满意度率比 Search 低 55%（1.3% vs. 2.9%）。
- 效率：匹配任务上，Search+Human 平均需 269 分钟，Computer+Human 仅需 36 分钟，时间节省 87%，成本节省 94%；盈亏平衡分析显示，人类若要匹配代理成本，需在 20 分钟内手动完成所有非检索步骤。
- 范围扩展：横向，Computer 查询跨职业边界比例高出 9 pp；纵向，认知复杂度（高阶 Bloom 思维 76% vs. 55%）、知识广度（所需 O*NET 领域数 2.40 vs. 1.74）、任务复合度（单查询涉及详细工作活动数 +59%）均显著更高；23% 的 Computer 查询涉及用户 Search 历史中从未出现的新任务。

**核心结论**：自主代理通过自动化多步执行，大幅压缩知识工作的时间和成本，同时提升了输出质量，并引导用户涉足更复杂、更跨领域的工作，揭示了 AI 代理重塑工作结构的经济学证据。
