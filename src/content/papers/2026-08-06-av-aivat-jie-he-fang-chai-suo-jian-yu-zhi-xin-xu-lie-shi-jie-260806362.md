---
title: 'AV-AIVAT: 74x Cheaper Agent Evaluation with Certified Anytime-Valid Stopping
  in Imperfect-Information Games'
title_zh: AV-AIVAT：结合方差缩减与置信序列实现74倍廉价Agent评估及保证的随时停止
authors:
- Boning Li
- Yu Chen
- Longbo Huang
arxiv_id: '2608.06362'
url: https://arxiv.org/abs/2608.06362
pdf_url: https://arxiv.org/pdf/2608.06362
published: '2026-08-06'
collected: '2026-08-09'
category: Eval
direction: Agent评估 · 随时有效停止
tags:
- Agent Evaluation
- Confidence Sequences
- AIVAT
- Variance Reduction
- Anytime-Valid Stopping
- LLM Agents
one_liner: 融合方差缩减AIVAT与置信序列，实现证据充分即停的有保证评估，成本降低74倍
practical_value: '- 在线A/B测试或Agent对战评估中，可使用控制变量法（类似AIVAT）降低方差，结合置信序列（CS）实现随时停止，显著节省推理/人力成本，同时保持统计保证。

  - 避免固定样本量或窥视p值带来的风险：采用任何时间有效推断，可在证据充足时立即决策，加速实验迭代。

  - 对于LLM agent在线评估，可训练一个仅依赖历史数据的价值模型，生成零均值修正项，确保修正因子独立于当前对局，正确实现方差缩减。

  - 在推荐系统广告实验中，可借鉴分层结构（渐近CS快速筛选，经验伯恩斯坦CS严格认证），将早期停止流程标准化、可审计化。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：Agent对战评估昂贵且受随机性影响，固定预算要么在结论已定后浪费资源，要么提前结束导致统计功效不足。传统可选停止会破坏置信度，而方差缩减方法AIVAT虽能大幅降低噪声，却未提供停止规则。

**方法**：将AIVAT与连续监测的置信序列（CS）结合为AV-AIVAT：在线价值模型仅用历史数据学习校正项，避免使用自身信息。两种CS配合——渐近CS用于快速筛选，经验伯恩斯坦CS提供有限样本精确认证，并给出校正后收益的结构化上界。

**结果**：在15种LLM agent的71,439手无限注德州扑克中，AIVAT方差缩减中位数54倍；在95%置信、±1大盲注精度下，原始结果所需手数是AIVAT修正后的74倍（渐近停止），经验伯恩斯坦CS停止时间中位数比仅为1.37倍。
