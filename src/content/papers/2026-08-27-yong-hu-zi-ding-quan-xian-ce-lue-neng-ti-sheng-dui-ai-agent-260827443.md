---
title: Do User-Authored Permission Policies Improve Protection Against AI Agent Overreach?
title_zh: 用户自定权限策略能提升对 AI Agent 越权的防护吗？
authors:
- Ting Yan
arxiv_id: '2608.27443'
url: https://arxiv.org/abs/2608.27443
pdf_url: https://arxiv.org/pdf/2608.27443
published: '2026-08-27'
collected: '2026-08-30'
category: Agent
direction: Agent 权限控制与人机协作
tags:
- AI agents
- permission systems
- user-authored policies
- human-in-the-loop
- overreach
- user study
one_liner: 用户预设 allow/ask/never 规则反而比逐动作审批和模型审查放过更多越权动作，主因是用户大量选 ask
practical_value: '- 在电商/Agent 权限系统里，不要把“用户预设规则”当作自动降低越权风险的手段：用户倾向选 ask，把决策推回运行时，总干预成本未必下降。默认策略应更保守，例如高风险动作默认
  never 或需主动开启 allow。

  - 将 Agent 动作按后果类别（资金、隐私、不可逆操作等）映射为自然语言 allow/ask/never 规则，可以减少运行时 prompt 次数（18→10.9），但前提是规则设置成本可控。可提供预设安全策略模板，避免用户逐条从零配置。

  - 越权动作大部分在用户批准后执行，说明仅靠“规则+人工确认”不够。批准界面应突出风险信号、变更摘要和不可逆提示，不能只列动作名称。

  - 对自动下单、改价、群发消息等电商场景，建议把动作后果分级与实时风控结合：规则负责减少常规打断，风控/模型审查负责捕获异常越权，而不是依赖用户预设规则兜底。'
score: 6
source: arxiv-cs.HC
depth: abstract
---

动机：AI Agent 正在成为邮件、支付、文件、个人数据等数字服务的主要入口，需要一种非专业用户也能理解、可复用的权限控制方式。研究比较三种机制：逐动作人工审批（HITL）、模型自动逐动作审查（AUTO）、以及用户按动作后果类别预设 allow/ask/never 规则（POLICY）。

方法：113 名无专业软件背景的参与者被分到三种条件。所有人在 4 个后果类别中先判断 2 个示例，POLICY 组再为每个类别设置一条常驻规则。随后所有人监督同一个包含 18 个动作的模拟一天，其中 7 个为越权动作。

关键结果：POLICY 拦截越权的比例低于 HITL（−20.1 个百分点，95% CI [−32.1, −8.1]）和 AUTO（−14.5 个百分点，95% CI [−25.8, −3.2]），但必需动作完成率仍高。POLICY 将运行时 prompt 从 18.0 降到 10.9，然而计入规则设置时间后，总干预时间没有可靠降低。探索性分析显示，140 条 POLICY 规则中有 114 条选了 ask，导致大多数越权动作被返回运行时人工确认。POLICY 下执行的 148 个越权动作中，133 个来自用户批准，15 个在 allow 规则下自动执行。用户自定规则并未自动提供更强防护，反而暴露了偏好与承诺之间的差距：反复选 ask 保留了逐案选择权，却使常驻策略无法提前固化决策。
