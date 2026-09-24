---
title: 'JEV-as-a-Judge: Accept When Confident, Escalate When Unsure'
title_zh: JEV 评判器：置信时接受，不确定时升级
authors:
- Yubo Li
- Yidi Miao
- Ramayya Krishnan
- Rema Padman
affiliations:
- Carnegie Mellon University
arxiv_id: '2609.26550'
url: https://arxiv.org/abs/2609.26550
pdf_url: https://arxiv.org/pdf/2609.26550
published: '2026-09-21'
collected: '2026-09-24'
category: Eval
direction: LLM-as-a-Judge 置信度级联评估
tags:
- LLM-as-a-judge
- confidence estimation
- cascade
- evaluation cost
- reward models
- factuality
one_liner: 用判别式 JEV 做低成本一阶段评判，低置信时级联大模型，在偏好/事实性任务上以 0.36% 成本接近 SOTA 精度
practical_value: '- 在大规模评估生成结果（搜索相关性、广告文案、商品描述、Agent 回答质量）时，可先上轻量判别式 judge 输出 label
  probabilities，不让大模型生成 rationale；低置信样本路由给强 LLM 或人工复核，显著降低 token 与费用。

  - 优先采用冻结的级联策略而非重训：用轻量 judge 的置信度卡阈值，接受高置信判断、升级低置信判断；论文在多个 benchmark 上保留 99% 的 strong
  judge 精度，适合线上质量监控和批量评估。

  - 业务中常见的 pairwise preference / evidence-grounded factuality 评估，可先试 JEV 这类 reward-model
  judge；对需要复杂推导或识别“写得漂亮但错误”的样本，不要省成本，应直接升级到强 LLM 或人工。

  - 将评估输出契约设计为 decision + probability，而不是自然语言理由；便于服务化、监控、校准，也能按业务风险设置不同阈值。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：LLM-as-a-judge 能覆盖开放任务评估，但推理成本和置信可靠性在大规模场景下成为瓶颈。需要判断是否能用一个只输出决策的轻量 judge 先做经济的一轮筛查，并在不确定时升级更强的评估。

方法关键点：引入 JEV-as-a-judge 作为决策型判别式 judge，直接暴露 typed decision 和 label probabilities，以概率作为置信度；与 16 个生成式 / reward-model judge 对比，并使用盲评人类裁决。冻结级联策略：高置信判决直接接受，低置信判决升级给 state-of-the-art LLM judge。

关键结果：在普通偏好和 evidence-grounded factuality 上，JEV 与最强 LLM judge 的差距在 3 个百分点以内，但费用仅为后者 0.36%；差距主要集中在低置信决策上。冻结级联可保留最强 judge 99% 的精度，同时降低总成本。当判断需要检查推导过程或抵抗细节丰富但错误的答案时，JEV 与强 judge 的差距会更大，说明这类样本更适合直接升级。
