---
title: Report on The 1st Workshop on Human-Centered Proactive and Personalized Agents
  for Interactive Information Access at CHIIR 2026
title_zh: CHIIR 2026 以人为本的主动式个性化信息访问代理研讨会报告
authors:
- Kirandeep Kaur
- Vinayak Gupta
- Tanya Roosta
- Madhura Raju
- Grace Hui Yang
- Chirag Shah
affiliations:
- University of Washington
- AMD & UC Berkeley
- TikTok
- Georgetown University
arxiv_id: '2608.18638'
url: https://arxiv.org/abs/2608.18638
pdf_url: https://arxiv.org/pdf/2608.18638
published: '2026-08-19'
collected: '2026-08-23'
category: Agent
direction: 人本主动式 Agent 设计原则
tags:
- Proactive Agents
- Personalization
- Human-Centered AI
- Interactive Information Access
- Trust
- Evaluation
one_liner: 系统梳理主动式信息访问Agent的人本设计议题，强调主动性须时机恰当、透明、可争议且对齐用户目标
practical_value: '- 主动推荐/导购 Agent 的触发策略不能只依赖点击预测分数，应引入 **calibrated initiative**：结合用户上下文、可中断性与任务阶段判断何时推送，降低打扰成本。

  - 在搜索/推荐 Agent 提供主动建议时，需要内置**透明与可争议机制**：给用户解释“为什么此时给出该建议”，并提供快速纠正/关闭入口，避免 agent
  自动化侵蚀用户控制感。

  - 跨会话个性化应区分**短期会话状态与长期记忆**，用 memory 架构累积偏好，但必须允许用户查看、修改或删除记忆，否则信任会快速下降。

  - 评估不能只看任务准确率或点击率，要加入**用户福利、信任、agency/控制感**等指标，尤其在电商导购、智能客服等高频交互场景中更关键。'
score: 6
source: arxiv-cs.HC
depth: abstract
---

动机：信息访问正从被动 query-response 范式转向能个性化交互、保留上下文、推断潜在需求并主动发起支持的 Agent 系统，但主动性带来自主性、隐私、信任、透明度和评估等新问题，缺乏跨学科梳理。

方法关键点：这是 CHIIR 2026 首届 Workshop 报告，汇总了信息检索、HCI、对话系统、AI 伦理、认知科学等领域的 invited talks、论文与开放讨论，涵盖 calibrated initiative、knowledge-gap navigation、long-term memory、value-sensitive design、implicit personalization、AI-mediated care、proactive dialogue 以及超越任务准确率的评估。

关键结果：没有量化实验，核心结论是——**主动性不应被简单理解为更早行动或更准预测，而是一种必须时机恰当、透明、可争议并与用户目标对齐的介入形式**。报告进一步归纳了设计主动式个性化 Agent 的研究挑战，指向任务目标与用户代理权之间的张力。
