---
title: Reliable AI-Assisted Decisions via Selective Auditing
title_zh: 通过选择性审计实现可靠的 AI 辅助决策
authors:
- Isaac Gibbs
- Elise L. Han
- Ryan J. Tibshirani
- Tijana Zrnic
affiliations:
- University of Toronto
- Stanford University
- University of California, Berkeley
arxiv_id: '2610.31662'
url: https://arxiv.org/abs/2610.31662
pdf_url: https://arxiv.org/pdf/2610.31662
published: '2026-10-22'
collected: '2026-10-24'
category: Other
direction: 在线决策监控 · 选择性人工审计
tags:
- selective auditing
- online error control
- human-in-the-loop
- confidence scores
- LLM safety
one_liner: 提出在线选择性审计框架，在控制未审计 AI 错误比例低于阈值的同时最小化人工审计频率
practical_value: '- 在电商/推荐场景中，AI 生成的商品描述、推荐理由或 Agent 操作常带有 confidence score；可借鉴该框架做选择性人工审核：设定业务可接受的未纠错比例
  α，用在线阈值动态决定哪些 case 送审，减少全量审核。

  - 算法无分布假设，对 i.i.d. 和对抗性流量都有理论保证，适合电商大促、恶意刷单等非平稳流量下的审核策略。

  - 若系统由“生成 Agent + 校验 Agent”组成，可把校验分数作为 confidence score，接入该方法自动升级高风险决策；阈值无需重新训练，直接在线调整。

  - 工程上可作为轻量级后处理模块：不改变原有模型，只需输出 score，与现有规则/模型融合成本低；实验表明在 LLM 有害请求过滤、数据标注等任务中能显著降低人工审核量。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：AI 决策规模扩大，专家逐条审查成本过高，需要自动决定何时信任 AI、何时升级人工审计。

方法关键点：把在线监测建模为约束优化：在保证未审计 AI 错误比例不超过预设阈值 α 的前提下，最小化审计频率。算法仅利用每轮的决策与 confidence score（可来自独立 verifier agent），无需分布假设，并给出对抗与 i.i.d. 数据流下渐近最优的审计率。

关键结果：在 LLM 有害请求筛查、定性文本标注、数据标注等实验中，方法实现有效的错误控制，同时相比基线大幅减少人工审计量。
