---
title: 'When Tomorrow Becomes Today: Self-Evolving Policies for Agentic Time-Series
  Forecasting'
title_zh: 当明天成为今天：自进化策略用于智能体时序预测
authors:
- Yifan Hu
- Xilin Dai
- Zhiyuan Qu
- Yiding Liu
- Zewei Dong
- Jiang-ming Yang
- Qiang Xu
affiliations:
- Ant International
- Tsinghua University
- The Chinese University of Hong Kong
arxiv_id: '2609.24862'
url: https://arxiv.org/abs/2609.24862
pdf_url: https://arxiv.org/pdf/2609.24862
published: '2026-09-21'
collected: '2026-09-22'
category: Agent
direction: Agent 自进化 · 延迟反馈策略
tags:
- Time-Series Forecasting
- Agentic AI
- Self-Evolving Policy
- Delayed Feedback
- Orchestration
one_liner: 将时序预测智能体的延迟反馈转化为专家信任、路径选择与干预强度的持久联合更新
practical_value: '- 延迟反馈无需额外标注：在电商推荐 Agent 中，每次请求同时记录多路召回/排序/策略路径的预测结果，待真实转化/点击回流后用
  realized outcome 评估整个候选集，为在线策略更新提供免费监督信号。

  - 自进化策略分层更新：借鉴 frozen backbone + 外层策略微调，只更新专家信任权重、路径路由概率、干预强度等轻量参数，避免频繁更新 LLM/大模型
  backbone，工程上更稳定且易回滚。

  - predict-reveal-update 协议可嵌入推荐 Agent 编排：如搜索推荐中由 LLM 调度多个模型（语义召回、协同过滤、生成式推荐），通过每轮真实反馈持续调整各专家贡献度，自动适应流量/季节/活动变化。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：时序预测智能体面临机制演化，数值模型、推理策略、干预规则的有效性随时间变化，需同时适应预测结果与编排策略。部署过程天然提供监督：预测时界过后，真实目标揭示早期决策有效性。但现有方法仅通过 forecast refinement、reflection 或 retrieval 利用历史经验，未系统地将 realized outcome 转化为对联合编排策略的持久更新。

方法：提出 TimEvolve，一个 frozen-backbone 时序智能体。在预测前 commit 所有数值专家预测和候选 agent path；目标观测后，用 realized outcome 评估整个 alternative set，获得无需额外标注的延迟反馈。关键是将每个 realized outcome 转化为三方面持久联合更新：expert trust、agent path selection、intervention strength。采用 temporally ordered predict-reveal-update 协议，将延迟反馈应用于后续预测。backbone 冻结，仅更新轻量策略参数。

结果：在八个 Time-MMD 领域、十五个方法中，TimEvolve 取得最佳平均 MSE 与 MAE rank，并在七个领域上两项误差指标均最低，验证了从部署中未来学习预测策略的价值。
