---
title: 'AdsWorldEngine: A Self-Evolving Conversational Advertising Agent through Orchestrator
  and Tool Coevolution'
title_zh: AdsWorldEngine：编排器与工具协同进化的对话广告 Agent
authors:
- Simiao Zuo
- Chenhui Xu
- Yimeng Jia
- Qiang Lou
- Jian Jiao
- Denis Charles
affiliations:
- Microsoft
arxiv_id: '2608.13833'
url: https://arxiv.org/abs/2608.13833
pdf_url: https://arxiv.org/pdf/2608.13833
published: '2026-08-13'
collected: '2026-08-17'
category: Agent
direction: 对话广告 Agent 与工具协同进化
tags:
- conversational advertising
- agent
- GRPO
- DPO
- judgment model
- tool coevolution
one_liner: 用 Actor-Tool 协同进化与标签锚定判断建模构建对话广告 Agent，取得显著离线与在线收益
practical_value: '- 把“是否出广告/推荐/消息”从“出什么”里拆开：用 Opportunity Gate + asymmetric cost-sensitive
  GRPO 控制误触发。false positive 惩罚设为 -2、false negative 设为 -1，直接按业务损失编码；不要做 group std scaling，避免抹掉不对称
  gap。适合电商 push、对话推荐插入、搜索广告位决策。

  - Actor-Tool 协同进化：先用 final slate 的 relevance/diversity 奖励训练 Orchestrator，再用 high/low
  reward rollouts 构造 (intent, 正样本 ad, 负样本 ad) preference 对，以 DPO 式目标训练 retrieval/relevance/ranking
  tool。能把端到端业务奖励传导到召回/排序工具，适合已有检索/排序模型的团队。

  - Orchestrator 的 GRPO 奖励要看最终 slate 的 relevance/diversity，而不是看生成 query 的表面多样性。训练后模型会从“2026
  Honda Pilot vs Toyota Grand Highlander comparison”这种重叠 query 变成两个产品名 query，检索候选更不重叠。搜索
  query 生成/改写可复用：评估 query 质量要用下游召回结果。

  - Label grounded judgment modeling：用 human label + 生产 guideline 生成思维链，再用 reflection
  过滤标签不一致的 rationale，能减少“流畅但违背 label”的监督噪声；适合做主观 relevance/机会判断模型。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**

对话广告需要从多轮对话、助手回复中推断隐含商业意图，并判断是否出广告、选哪几个广告。这是一个完整 ad serving 问题，而非单纯检索排序；现有工作多只做单点组件。需要一个可生产的 agentic 框架，并且让 agent 与下游工具一起优化。

**方法关键点**

- AdsWorldEngine 由 Opportunity Gate、Orchestrator、Tool Set、Evaluator 组成：Gate 先判断该轮是否适合展示；Orchestrator 完成状态解析、约束提取、intent 生成、工具调用与 reflection 后选 top-3；Evaluator 离线给 relevance/diversity 奖励。
- Label grounded judgment modeling：用生产 guideline 和 human labels 生成 thinking trace，再通过 reflection 过滤 label 不一致的 rationale；用 SFT 加 cost-sensitive GRPO，去掉 group std scaling 以保留不对称误差成本。用于 Gate 和 conversation-to-ad relevance 模型。
- Iterative actor-tool optimization：先 SFT warm up Orchestrator；每轮用 GRPO 优化 final slate 奖励，再用 high/low reward rollouts 构造 (intent, ad+, ad-) preference 对，以 DPO 式目标更新 retrieval/relevance/ranking tools，交替 3 轮。

**关键结果**

- 判断模型：Gate 在 SFT 后太保守，TPR -17.19%；加入 cost-sensitive GRPO 后 TPR 不降，FPR -39.07%，BalAcc +2.51%。Relevance 模型 FPR -12.71%，TPR -0.78%，BalAcc +7.51%。
- 全链路相对现网 Production System：SFT 后 diversity +15.31%、relevance +49.37%；3 轮迭代后 diversity +62.87%、relevance +82.26%。
- 20 天在线 A/B：RPM +22%，广告覆盖率 +74%。

**最值得记住的一句话**

用最终 slate 奖励同时优化 actor 和下游工具，能形成自我进化闭环，比只训 LLM agent 或只改工具更有效。
