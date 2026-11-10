---
title: 'Safe Reinforcement Learning for Multi-Turn Clinical Agents: When Dense Rewards
  Beat Outcome Rewards'
title_zh: 安全强化学习训练多轮临床智能体：稠密过程奖励优于结果奖励
authors:
- Brendan P. Murphy
- Agustina Saenz
affiliations:
- Stanford University
arxiv_id: '2611.12728'
url: https://arxiv.org/abs/2611.12728
pdf_url: https://arxiv.org/pdf/2611.12728
published: '2026-11-09'
collected: '2026-11-10'
category: Agent
direction: LLM Agent 多轮决策奖励设计
tags:
- RLHF
- GRPO
- reward shaping
- multi-turn agents
- process reward
- safety
one_liner: 在可控多轮临床决策中证明仅结果奖励会导致过早停止和单提问塌缩，密集过程奖励更稳健
practical_value: '- 多轮导购/推荐 Agent 若只按最终转化或成交 reward 优化，容易出现“只问一个澄清问题就推商品”或过早结束对话；可借鉴论文思路，对能显著降低用户意图不确定性的提问/澄清动作赋予中间过程奖励。

  - 评估不能只看总体 GMV 或成功率，应单独看信息收集效率、对话轮次/查询成本，以及高风险/复杂用户群上的表现，否则 RL 可能靠牺牲尾部用户提高均值。

  - 在已有较好 SFT 冷启动后直接跑 GRPO，容易通过删减澄清问题提升短期指标但损害复杂或高风险 case；建议在 RL 阶段保留过程奖励或轮次约束，并分人群评估。

  - 有偏 SFT 数据造成的罕见行为缺口，RL 不一定能修复，甚至可能放大捷径；训练前要先治理数据覆盖和初始化行为分布，不能指望 RL 自动纠偏。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：可验证奖励的 RL 越来越多用于提升 LLM 推理，但对多轮顺序决策过程的影响仍不清晰；临床多轮 Agent 需要决定问什么、何时停止、采取什么动作，偏差会带来安全风险。

方法关键点：构建三类受控环境——药物续方分诊、急性诊断检查、剂量滴定，均含隐状态、查询成本、精确自适应 oracle 和确定性结果验证器。比较仅结果奖励的 GRPO 与给减少不确定性的提问赋予密集过程奖励；进一步测试探索/利用分离、过程奖励强度、监督暖启动后的 RL，以及有偏 SFT 数据下的 RL。

关键结果：仅结果奖励常提高总奖励，但产生过早承诺、单提问塌缩和罕见高风险失败。诊断任务中，密集奖励在 3 个训练种子下提升 held-out 价值和中风险支持，避免仅结果奖励的高风险种子塌缩。分离探索与利用在最优 ckpt 提高高风险支持，但低危病例过度问询。RL 在已仔细收集信息的 SFT 初始化后会通过删问题提高总奖励，却降低高风险表现；RL 也无法可靠修复有偏 SFT 的罕见行为缺口。

结论：可验证最终结果不足以训练可靠的多轮 Agent，奖励设计必须考虑过程，评估必须区分自适应信息收集与奖励捷径。
