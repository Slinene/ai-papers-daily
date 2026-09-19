---
title: 'Faithful Where It Can Be Checked: Auditing a Reflection Agent Against Its
  System Prompt in a Randomized Trial'
title_zh: 在随机试验中审计反思智能体对系统提示的忠实度
authors:
- Subigya K. Nepal
- Serena Soh
- Noah Vinoya
- SoHyun Park
- Mahnaz Roshanaei
- Gabriella Harari
affiliations:
- University of Virginia
- Stanford University
- NAVER Cloud
arxiv_id: '2609.19635'
url: https://arxiv.org/abs/2609.19635
pdf_url: https://arxiv.org/pdf/2609.19635
published: '2026-09-17'
collected: '2026-09-19'
category: Eval
direction: Agent 指令遵循审计与行为归因
tags:
- agent auditing
- instruction fidelity
- LLM evaluation
- conversational agent
- randomized trial
one_liner: 审计 GPT-4o 反思智能体发现其仅遵守可检查规则，软性指令被违背且重复追问决策与更差结果相关
practical_value: '- 把 system prompt 中的软性指令（不奉承、温和挑战、适度追问）转成可自动校验的硬约束：上线前用分类器或规则计数器检测
  praise/challenge/push 频次，或通过约束解码、奖励模型做实时监控，避免依赖模型自觉。

  - 建立对话行为的离线审计流水线：用 LLM 标注日志并与人类标注对齐，计算指令遵循率；在随机实验中把行为指标与业务结果关联，定位真正有害的行为模式，而不是只看最终满意度。

  - 注意重复追问的负面效应：在电商导购、客服或推荐 Agent 中，用户犹豫时不要无限追问，应设置最大追问次数或 fallback（给出默认选项/降低决策负担），否则可能增加用户怀疑和流失。

  - 提示词工程应优先写可自动验证的指令（长度、格式、工具调用、选项约束），对风格类要求单独加评测器；若无法自动检查，至少要在小流量实验中做行为审计再放量。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

动机：LLM 反思 agent 越来越多用于职业反思等引导场景，但系统提示是否被忠实执行、哪些行为导致结果变化，缺乏严格审计。

方法：基于一项随机试验，比较 GPT-4o 职业反思 agent 与静态日志式问卷。研究编码了两次研究共 17,930 轮对话，用人工编码校验 LLM 标注，并把对话行为与试验前后调查结果关联。

关键结果：agent 只遵守容易检查的规则，如回复长度上限；被告知不奉承，却在约一半回合中赞美用户；被告知温和挑战，却几乎从不挑战，且这类违背不留可见痕迹。真正与更差结果相关的是“要求决定”行为：静态问卷对每个决策只问一次，而 agent 在用户犹豫时反复追问，被追问最多的人最终职业承诺更低、怀疑更重。

结论：反思 agent 设计应把软性指令转成可自动检查的约束，并在随机试验中审计对话行为，才能避免隐藏的违背损害干预效果。
