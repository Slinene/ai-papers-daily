---
title: Trust Guided Decision Transformer
title_zh: 信任引导的决策 Transformer
authors:
- Chainesh Gautam
- Raghuram Bharadwaj Diddigi
- Chandramouli Kamanchi
- Pankaj Dayama
- Sumanta Mukherjee
- Kameshwaran Sampath
affiliations:
- International Institute of Information Technology Bangalore
- IBM Research Bangalore
arxiv_id: '2609.31586'
url: https://arxiv.org/abs/2609.31586
pdf_url: https://arxiv.org/pdf/2609.31586
published: '2026-09-25'
collected: '2026-09-28'
category: Other
direction: 离线强化学习 · 决策 Transformer 上下文选择
tags:
- Decision Transformer
- Offline RL
- Conformal Prediction
- Context Selection
- State Prediction Error
- Value Guidance
one_liner: 用模型自身状态预测误差加保形校准筛选可信上下文，再让 critic 选动作，缓解长 rollout 分布漂移
practical_value: '- 在长程 Agent / 对话式推荐中，自回归生成的上下文容易偏离训练分布；可以复用「下一步状态/Token 预测误差」作为
  OOD 信号，而不只依赖 reward 或 critic 分数。

  - 用 split conformal prediction 在离线验证集上标定预测误差阈值，能获得覆盖率保证，避免人工拍阈值；适合对会话状态转移模型或用户序列模型做在线可信度过滤。

  - 先做 trust filtering 再做 value/critic 选择：不要从不可靠 context 生成的动作里用 critic 选高价值动作；应当让
  critic 只在可信 context suffix 集合内打分，能降低 OOD 动作风险。

  - 对长序列推荐或 Agent 轨迹，可维护多个最近 context suffix，逐段做误差检查，只保留可信历史片段，实现类似软 reset 的上下文控制，避免硬
  reset 丢失重要信息。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：Decision Transformer（DT）在长 rollout 中表现下降，因为自回归生成的条件上下文逐渐偏离离线训练分布，但模型仍被要求基于未见过的历史做决策。

方法关键点：TGDT 用模型自身的下一步状态预测误差作为漂移信号；滚动计算多个最近 context suffix 的误差，通过 split conformal prediction 在离线验证集上校准阈值，只保留误差在阈值内的可信 suffix；之后用冻结 critic 在可信 suffix 中选择价值最高的动作。这个顺序与纯 value-only 弹性选择相反：先信任筛选、后价值选择，避免 critic 从不可靠上下文生成的动作里选优。

关键结果：在 D4RL navigation 和 locomotion 任务上，状态预测误差、critic 引导和硬 context reset 各自只能解决部分问题；TGDT 减少持续高误差 run，并在 return 上超过 vanilla DT、reset-based context control 和 value-only context selection。
