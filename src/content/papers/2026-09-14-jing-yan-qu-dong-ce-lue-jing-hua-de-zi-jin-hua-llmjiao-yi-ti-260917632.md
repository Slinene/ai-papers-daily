---
title: 'EvolveTrade: Experience-Driven Policy Refinement for Self-Evolving LLM Trading
  Agents'
title_zh: 经验驱动策略精化的自进化LLM交易智能体
authors:
- Sehee Kim
- Yumin Choi
- Minki Kang
- Sung Ju Hwang
affiliations:
- KAIST
- DeepAuto.ai
arxiv_id: '2609.17632'
url: https://arxiv.org/abs/2609.17632
pdf_url: https://arxiv.org/pdf/2609.17632
published: '2026-09-14'
collected: '2026-09-17'
category: Agent
direction: Agent 自进化策略优化
tags:
- LLM Agent
- Self-Evolution
- Text-as-Policy
- Tool Use
- Trading
- Policy Optimization
one_liner: 将Agent的system prompt视为文本参数化策略，由策略Agent基于决策轨迹和组合反馈迭代重写
practical_value: '- 将Agent的system prompt / 工具调用策略当作可优化的“文本参数”，通过定期基于历史交互trace和业务反馈（如转化率、收益）让策略Agent重写prompt，无需微调LLM即可实现策略迭代。适用于搜索/推荐中的Agent决策流程优化。

  - 借鉴其批量更新思想：在每轮更新间隔内收集决策动作和实际奖励，然后离线让策略Agent修订系统提示，再用于下一批决策。这样可形成闭环，尤其在非平稳的电商/广告环境中，定期调整信息获取和排序逻辑。

  - 行为分析可作为诊断工具：通过比较旧/新策略下的动作分布（如工具调用类型、代码执行比例）和归因分析（策略改动→动作变动→回报变动），找出哪些流程调整真正有效，可迁移到推荐Agent的可解释性分析。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM交易Agent通常由静态手写工具使用策略控制，难以在非平稳市场中自适应调整信息获取、工具调用、信号验证和风险管理行为。

**方法关键点**：EvolveTrade将tool-using Agent的system prompt视为文本参数化策略。在每个更新间隔，一个Policy Agent根据累积的决策轨迹和实际投资组合反馈（如收益、夏普比率）来修订策略，保持骨干LLM固定。更新后的策略用于下一批交易决策，使Agent能够迭代优化其信息获取和组合构建流程。

**关键结果**：在多个市场制度和两个LLM骨干上，EvolveTrade在大多数设置中提高了Sharpe Ratio和Cumulative Return。行为分析显示，自我进化的策略增加了代码介导的分析，并激活了与当前市场制度相关的计算；案例级策略到回报的归因追踪了策略引起的配置变化对实际回报差异的贡献。
