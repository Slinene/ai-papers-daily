---
title: 'Never the Number: Structural Abstention for AI Systems Whose Answers Are Consumed
  as Fact'
title_zh: 永不碰数字：面向事实型答案 AI 系统的结构化弃权架构
authors:
- Zhelun
- Wu
arxiv_id: '2608.13926'
url: https://arxiv.org/abs/2608.13926
pdf_url: https://arxiv.org/pdf/2608.13926
published: '2026-08-14'
collected: '2026-08-17'
category: LLM
direction: LLM 可靠性 · 结构化弃权
tags:
- trustworthy AI
- LLM reliability
- abstention
- text-to-SQL
- deterministic execution
- agent safety
one_liner: 用确定性内核与生成外壳解耦，生成组件只影响问题解释不碰返回值，无法表达请求直接拒绝，从结构上避免 LLM 事实性幻觉
practical_value: '- 在电商/广告的自然语言数据问数、指标看板、运营机器人中，把“数值/聚合结果”与“自然语言解释”拆开：生成模块只负责 paraphrase、确认语义，数值由确定性
  SQL/指标内核计算，避免 fluent wrong answer。

  - 建立 bounded set of answerable question shapes，把 LLM 的输入映射到有限查询模板；不能映射的请求直接拒绝或让用户重新表述，而不是让
  LLM 兜底生成近似答案，尤其适用客服、价格/库存/预算等高风险查询。

  - Agent 系统中可复用到工具调用与策略动作：LLM 只负责路由、生成确认问题和措辞，不参与最终执行参数计算；对写操作/策略参数使用确定性决策层，降低工具误用与事实性污染。

  - 五决策配方可作为 human-in-the-loop confirmation 设计参考：在展示数值前先让用户确认问题语义，把不可结构化表达的需求排除在计算之前，提升生产系统可信度。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 让自然语言查库（NLIDB）可用，但 text-to-SQL 幻觉列名或聚合错误会产生流畅却错误的答案，消费端无法在回答处分辨。在企业管理驾驶舱、指标看板以及工具型 Agent 消费答案时，可靠性先于准确率。

**方法关键点**：提出“可信内核 + 生成外壳”的架构模式。核心不变量是：可虚构的组件可以影响系统回答哪个问题，但不能影响系统返回哪个值。生成外壳负责解释模糊输入、生成确认问题和措辞；确定性内核把完全指定的问题匹配到有限的可答问题形状，并通过确定性执行编译为查询。两者在用户确认后才会计算值；内核无法表达的需求直接拒绝而非近似，称为 structured abstention，区别于基于置信度的 selective prediction / calibrated confidence。文章给出实现无关的规范、五决策配方，并扩展到 agentic 系统的动作。

**结果**：报告两年生产案例，与 fine-tuned parser 和 tool-retrieval agent 两个生成式替代方案对比，后两者会输出流畅但错误的值，本架构通过不变量从结构上避免该失败；后续企业可靠性与基准工作也验证了该模式。
