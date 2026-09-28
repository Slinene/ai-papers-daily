---
title: 'PriceBench: A Diagnostic Benchmark for Price, Quality, and Brand Preferences
  in LLM Booking Agents'
title_zh: PriceBench：LLM 预订智能体价格、质量与品牌偏好诊断基准
authors:
- Pavel Kireyev
affiliations:
- London School of Economics and Political Science
arxiv_id: '2609.31468'
url: https://arxiv.org/abs/2609.31468
pdf_url: https://arxiv.org/pdf/2609.31468
published: '2026-09-25'
collected: '2026-09-28'
category: Eval
direction: LLM 采购智能体偏好诊断
tags:
- LLM Agent
- Choice Model
- Preference Recovery
- Benchmark
- Price Sensitivity
- Booking
one_liner: 提出 PriceBench，用 logit 选择模型从酒店预订选择中恢复 28 个 LLM 的价格质量品牌偏好，发现高能力模型偏好更强更一致
practical_value: '- 在把 LLM 用作导购、选品或下单代理前，先诊断其隐式偏好：不要只看任务完成率，要在满足约束的候选中看它实际选了哪个；可用
  logit 离散选择模型从历史对话或推荐日志中恢复价格、质量、品牌的权重。

  - 弱模型容易受 listing order 影响或锁定单一选项，工程上避免直接让弱模型做最终购买决策；要么换更强模型，要么在 prompt 中显式注入价格约束并随机化候选顺序，降低位置偏差。

  - 同一模型系列内价格敏感度差异可能超过一个数量级，上线代理或做 A/B 时需按具体模型版本/checkpoint 测量，不能沿用“同系列偏好差不多”的假设。

  - 对 LLM 生成推荐/购物结果，把平均客单价或 booked price 漂移纳入离线评估；论文中 $247 到 $393 的差异意味着模型选择会直接改变收入与成本，不能只做事后观察。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 在购物、酒店预订等场景中从执行者变成选择者，用户给出预算、星级等显性约束后仍存在多个候选，模型的隐式偏好决定最终买什么、花多少钱；现有 agent benchmark 只测任务是否完成，不测选了哪个选项。

**方法**：PriceBench 基于纽约 179 家真实酒店构造 3,600 个预订任务，覆盖 28 个 LLM、8 家提供商；用 logit 离散选择模型从模型选择中恢复价格、质量、品牌偏好，反推价格敏感度、价格/质量 trade-off 与平均预订价格。

**关键结果**：能力与选择一致性相关，而非与选择内容相关：更强模型偏好更强且更一致；弱模型要么锁定单一位置、易被 listing order 操纵，要么几乎无差异。价格敏感度跨模型差异超过一个数量级，同一批任务下平均每晚预订价从 $247 到 $393。作者开放任务、代码与 28 组响应集。
