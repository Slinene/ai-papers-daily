---
title: 'OptionWorld: A Benchmark for Diagnosing Failures of LLMs as Long-Term Personal
  Assistants'
title_zh: OptionWorld：诊断 LLM 长期个人助手失败环节的基准
authors:
- Ruoyu Zhang
- Zhaocen Liu
- Weiyi Tian
- Melissa Feng
- Shilong Liu
affiliations:
- University of British Columbia
- University of Chicago
- Independent Researcher
- Princeton University
arxiv_id: '2610.28491'
url: https://arxiv.org/abs/2610.28491
pdf_url: https://arxiv.org/pdf/2610.28491
published: '2026-10-20'
collected: '2026-10-21'
category: Eval
direction: Agent 长期任务失败诊断基准
tags:
- LLM Agents
- Long-term Memory
- Failure Analysis
- Benchmark
- Personal Assistants
one_liner: 提出 OptionWorld 基准，追踪从信息获取到行动结果的完整链路，定位 LLM 长期助手跨天任务失败环节
practical_value: '- 在构建长期 Agent（如电商售后助手、广告投放优化助手）时，应显式维护“未完成任务清单”，为每个任务记录已获取事实、下一步行动、截止时间和阻塞条件，而非仅依赖对话记忆。可借鉴论文中的
  Task State 概念，将“已获取事实”与“已执行干预”分开跟踪。

  - 失败分析显示 Agent 常将临时障碍（如等待某条记录）误当作永久限制，导致自我设限而停止行动。可在系统层面加入定期校验机制：对等待条件设置有效期，过期自动重试或升级，避免
  Agent 永久等待。

  - 提示词或工具设计中明确区分“允许询问”和“允许承诺/执行”，避免 Agent 因权限边界不清而放弃可采取的行动。可参考论文的权限说明纠正实验：仅澄清“禁止联系”是指禁止最终承诺而非禁止询问，即可恢复正确行为。

  - 对于长期任务，采用 checkpoint 回放和最小干预（补充事实、行动提醒、权限澄清）进行诊断，帮助定位失败发生在信息获取、判断还是行动环节，从而针对性优化
  prompt 或 memory 结构，而不是盲目增加上下文长度。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
长期个人助手需要跨天跟踪未完成任务，随着信息和环境变化持续跟进。现有 benchmark 大多只给任务完成率或阶段分数，无法区分失败是因为缺少事实、保留了事实但未有效使用、还是后续行动停滞。OptionWorld 通过模拟日常事务，将信息获取、判断、行动和结果串联起来，定位 LLM 在哪个环节断掉。

**方法关键点**  
- 8 个模拟世界（住房、工作、独立生活、家庭协调），每个 60 天、24 个隐藏目标，共 192 个目标。Agent 只能通过日常事件和工具发现需求，不能看到目标列表。  
- 工具包括读取来源、检查对象、比较记录、保存笔记、注册监控条件、联系相关人员、请求授权、执行操作。  
- 每个目标有六项二元评分：Observed (O)、Risk hypothesis (H)、Grounded discovery (G)、Timely grounded (T)、Intervention delivered (I)、Simulated outcome (Y)，形成依赖链 H≥G≥T≥I≥Y。主指标 OPR 即目标成功率。  
- 额外分析事实获取与决策输入中事实可用性：统计失败实例中主要事实是否已在截止前获得，以及是否仍存在于最后一次有效决策输入中。

**关键结果数字**  
- 6 个系统（DeepSeek, Fable, Gemini, Grok, Qwen, Astra/Codex）在相同 8 个世界上各跑 3 次，共 144 条轨迹、3456 个目标实例。  
- 目标成功率：Astra 61.6%，DeepSeek 48.3%，Grok 23.6%。  
- 49.5% 的失败发生在及时获得主要事实之后；35.5% 的失败案例中事实仍存在于最后有效决策输入中。  
- 最主要失败原因：信息缺口（30.2%）、行动选择/调整失败（21.3%）、自我设限（18.9%）。  
- 补充实验：添加缺失事实可在部分检查点恢复成功；行动提醒可重启行动但可能错过截止时间；更正错误的禁止联系说明可恢复允许的询问。

**最值得记住的一句话**  
长期 Agent 的失败不只在信息获取，更在于把已获取的事实与未完成的任务连接起来、在截止前采取有效行动，以及区分实际限制和 Agent 自身的错误假设。
