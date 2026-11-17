---
title: 'SPILLWAY: Separating Target Admission from Sanitization to Defend Tool-Using
  Agents against Prompt Injection'
title_zh: SPILLWAY：分离目标准入与消毒以防御工具型智能体的提示注入
authors:
- Woosang Lim
- Yeseul Chang
- Jaewoo Lee
affiliations:
- SAINT Machines
- KAIST
- Chung-Ang University
arxiv_id: '2611.07222'
url: https://arxiv.org/abs/2611.07222
pdf_url: https://arxiv.org/pdf/2611.07222
published: '2026-11-03'
collected: '2026-11-17'
category: Agent
direction: Agent 工具调用安全 · Prompt Injection 防御
tags:
- Prompt Injection Defense
- Tool-Using Agents
- Deterministic Sanitization
- Target Admission
- Safety
one_liner: 利用工具返回的类型化字段与自由文本差异，构建确定性目标准入检查与消毒器，实现高可用、低开销的提示注入防御
practical_value: '- 在电商/支付/邮件类 Agent 中，将关键动作目标参数（如收款账户、收货地址、邮件接收人）的合法性绑定到用户任务中明确指定的值或只读工具类型化返回，禁止自由文本中的值覆盖目标，实现为无
  LLM 调用的确定性规则，降低延迟并缩小注入攻击面。

  - 采用“默认拒绝 + 白名单”模式：对工具调用中的目标字段检查其来源是否为用户任务、只读工具返回的类型化字段或预定义委托规则，否则拒绝。该模式可直接嵌入广告投放
  Agent 调整出价、搜索推荐 Agent 修改策略等高风险操作，防止恶意指令劫持交易目标。

  - 消毒器保留被删除的指令片段作为审计证据，本地判断器只恢复目标不在删除文本中的调用，提供可审计性。在需要合规审计的推荐/广告系统中，可记录所有被过滤的注入片段及其对决策的影响，便于事后追溯与合规证明。

  - 实验表明几乎不增加模型调用，适合线上 Agent 系统。可将 SPILLWAY 的检查置于工具调用前，无需重跑主模型，对时延友好，能低成本提升安全基线。'
score: 6
source: huggingface-daily
depth: abstract
---

工具使用智能体能操作邮件、文件、支付，网页或共享文档中的注入指令可能诱导其向攻击者转账或泄露数据。现有运行时防御常依赖语言模型对每个动作放行，既增加模型调用又让模型可能读取攻击文本；来源防御虽避免模型最终检查，但需要每个任务先做规划或路由。

SPILLWAY 观察到动作目标（如邮件发件人、支付账户）出现在工具的类型化返回字段，而注入指令以自由文本形式出现。由此构建两层防御：第一层是确定性目标准入检查，仅当每个出现在工具输出但不在用户任务中的目标值，是由只读工具在类型化字段中返回、或符合固定委托规则时，才放行该调用；第二层是确定性消毒器，在模型读取前删除匹配固定规则、类似指令的区域，并保留被删除片段作为证据。本地判断器可以恢复被拒绝的调用，但绝不恢复目标在被删除文本中的调用。

在三种骨干模型、七个任务套件上，标准模板注入无法将动作重定向到攻击者目标，同时达到所比较防御中最高的平均效用与综合评分（NRP、ERS）。伪造聊天模板产生原始零分，在发布的强化学习攻击者下平均范围内攻击成功率为 0.007。SPILLWAY 实现该安全底线时无防御触发的骨干重跑，几乎不增加模型调用。
