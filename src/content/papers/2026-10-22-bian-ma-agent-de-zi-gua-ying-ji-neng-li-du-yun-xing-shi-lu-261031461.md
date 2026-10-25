---
title: 'Adaptive Skill Granularity for Coding Agents: Runtime Routing and Macro-to-Micro
  Recovery'
title_zh: 编码 Agent 的自适应技能粒度：运行时路由与宏到微恢复
authors:
- Dingxuan Zhang
- Yanhui Jiang
- Jun Wang
- Hefeng Zhou
affiliations:
- Shanghai Jiao Tong University
- Kuaishou Technology Co., Ltd.
- University of Warwick
arxiv_id: '2610.31461'
url: https://arxiv.org/abs/2610.31461
pdf_url: https://arxiv.org/pdf/2610.31461
published: '2026-10-22'
collected: '2026-10-25'
category: Agent
direction: Agent 技能粒度自适应与恢复执行
tags:
- LLM agent
- skill granularity
- runtime routing
- macro-to-micro recovery
- coding agent
- finite-state executor
one_liner: 将技能粒度作为条件化动作抽象策略，通过特征控制器与宏到微恢复提升编码 Agent 鲁棒性
practical_value: '- 在推荐/搜索 Agent 工作流中，把“宏技能”（如一次生成完整推荐理由+商品卡片+优惠文案）与“微工具”（分别调用召回、排序、文案模型）纳入同一路由策略，根据
  query 复杂度、用户状态和上下文选择执行粒度；若宏技能失败或不符合预期，自动降级到微工具补齐，避免整链路失败。

  - 可借鉴其 feature-based 控制器思路：不依赖 LLM 做每个步骤的粒度判断，而是用用户/任务/状态特征（如 query 长度、类目数、历史是否出现矛盾信号、置信度）训练轻量分类器或规则，决定走宏模板还是微调用，降低延迟和成本，适合高
  QPS 电商搜索/推荐消息场景。

  - 引入有限状态执行器和显式的 transition correctness / route match 过程指标，对业务 Agent 做可观测、可回滚的执行管理；在
  push 文案生成、搜索 query 改写等场景中，可以跟踪“宏采纳率”“失败恢复率”来评估系统鲁棒性而非只看最终转化。

  - 局限：论文面向 coding agents，缺少电商语料和在线指标；迁移时需重定义技能库和 verifier，但执行抽象与回退机制可复用。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM coding agent 常以可复用技能封装流程，但实际执行中同一任务可用原子工具调用、宏技能或混合执行；固定宏执行在匹配时高效，遇到任务结构或状态不匹配时脆弱，缺乏运行时控制和失败恢复。

**方法关键点**：提出 Adaptive Skill Granularity 框架，将技能粒度视为条件化动作抽象策略，取决于任务结构、执行状态和宏技能失败；系统由基于特征的粒度控制器（feature-based granularity controller）和有限状态恢复执行器（finite-state recovery executor）组成，控制器决定宏/微/混合路由，执行器在宏技能失败后显式触发宏到微恢复。

**关键结果**：在确定性 coding-agent 协议上评估，指标包括 verifier 定义的成功率、总成本，以及宏采纳率、失败恢复、路由匹配和转换正确性等过程指标。结果显示固定宏执行在适用时高效但在不匹配时脆弱；运行时路由和显式宏到微恢复提高了鲁棒性，并可恢复固定粒度执行无法解决的受控宏失败。论文未报告具体数值，以定性对比为主。
