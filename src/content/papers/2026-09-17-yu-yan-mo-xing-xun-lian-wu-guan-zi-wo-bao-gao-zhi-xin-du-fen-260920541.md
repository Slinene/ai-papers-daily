---
title: An Analysis of Training-Free Self-Reported Confidence in Language Models
title_zh: 语言模型训练无关自我报告置信度分析
authors:
- Lukas Meyer
- Sofia Rossi
- Wei Chen
- Thomas Laurent
- Yiming Li
affiliations:
- DreamAI
arxiv_id: '2609.20541'
url: https://arxiv.org/abs/2609.20541
pdf_url: https://arxiv.org/pdf/2609.20541
published: '2026-09-17'
collected: '2026-09-19'
category: Eval
direction: LLM 置信度估计与校准分析
tags:
- confidence estimation
- calibration
- self-consistency
- verbalized confidence
- uncertainty
- LLM evaluation
one_liner: 直接口头置信度是强基线，但自我报告对提示词敏感且自洽性会放大共享误解
practical_value: '- 在生成推荐理由、广告文案、商品属性或搜索 query 时，可直接用 verbalized confidence 做不确定性初筛，但不要把它当成稳定分数直接做硬阈值路由：同一答案等效重问会带来
  0.043–0.084 的分数波动，并翻转 4%–9% 的 0.8 阈值决策。

  - 在需要人工审核的生成内容（如合规文案、事实性描述）上，可以用自报置信度对审核队列排序，优先检查低置信样本；但上线前必须做领域内校准审计，因为基准噪声和提示词差异会明显影响
  AUROC。

  - 对 Agent 多智能体投票或自洽性路由要谨慎：三样本一致性在该实验中显著弱于直接口头置信度，而且错误答案也可能获得一致支持，说明共享先验会放大系统性误解，建议引入外部证据或独立校验器。

  - 如果业务依赖 closed model 的 API，无法拿到 token probability，口头置信度仍然是可用的训练无关信号，但需要设计更鲁棒的 elicitation
  协议，例如多次采样、多样化提示或校准映射。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：LLM 在生成内容时可以同时给出数值置信度，但不确定这是真实的不确定性估计还是只是修辞。对于电商、广告、搜索等需要分配有限人工验证资源的场景，可靠的置信度信号很有价值。

方法：在 100 个 TriviaQA 问题上，对两个模型家族分析了三种无需训练的置信度信号：与答案一起口头给出的置信度、事后 P(True)、以及三次额外生成的一致性。还做了复问实验和 100 条传记声明的审计。

关键结果：直接口头置信度是出乎意料的强基线，在审计基准错误后 AUROC 达到 0.956 和 0.937。三样本一致性明显更弱，AUROC 仅为 0.765 和 0.790，与口头置信度的固定插值没有统计上可靠的好处。一个模型 9 个错误中有 4 个、另一个模型 8 个错误中有 2 个获得了一致的样本支持，说明自我一致性会放大共享误解。用等效提示重新询问同一固定答案时，平均分数变化 0.043 到 0.084，在 0.8 阈值下翻转 4% 到 9% 的决策。传记声明审计只发现支持与矛盾声明之间存在适度的置信度差距。结论：有用的自我报告对诱发方式、相关错误和基准噪声仍然敏感。
