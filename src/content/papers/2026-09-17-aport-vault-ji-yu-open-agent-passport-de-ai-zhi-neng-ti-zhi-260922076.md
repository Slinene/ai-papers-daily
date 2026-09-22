---
title: 'APort Vault: Benchmarking AI Agent Payment Authorization with the Open Agent
  Passport'
title_zh: APort Vault：基于 Open Agent Passport 的 AI 智能体支付授权基准
authors:
- Uchi Uchibeke
affiliations:
- APort Technologies Inc.
arxiv_id: '2609.22076'
url: https://arxiv.org/abs/2609.22076
pdf_url: https://arxiv.org/pdf/2609.22076
published: '2026-09-17'
collected: '2026-09-22'
category: Eval
direction: Agent 工具调用授权与安全评估
tags:
- AI Agent Security
- Payment Authorization
- Benchmark
- Tool Use
- Policy Enforcement
- Open Agent Passport
one_liner: 回放 4371 条人类攻击，证明确定性预执行检查可将未授权支付转账从 140 次降至 0 次
practical_value: '- 在 Agent 执行支付、退款、优惠券发放等高风险工具调用前，增加一个确定性的预执行策略层（如 Open Agent Passport），用白名单校验接收方/账户，而不是依赖
  LLM 自身的判断，可显著降低越权操作。

  - 评估 Agent 安全或工具调用时，不要只统计“请求率”或“成功率”，应分解为请求、成功支付、授权决定、成员资格、未授权转账等多个事件，否则指标会掩盖真正的失败模式。

  - 攻击回放与分层 policy 配置（Level 1-4）的思路可迁移到电商 Agent 测试集构建：按风险等级设计不同允许操作范围，在不同配置下回放攻击，并公开数据集以复现结果。

  - 业务中更应投入精力设计清晰的授权边界和确定性执行，而非单纯比较 LLM 能力：本研究发现请求率差异主要来自 policy 配置而非模型本身。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：工具使用型 AI 智能体如果拥有支付工具，容易被人类攻击诱导执行未授权转账；需要基准评估授权边界，而非仅看模型生成请求率。

方法：APort Vault 回放公开夺旗赛中 4371 条人类编写的攻击，在 14 个模型（8 个实验室）、5 种策略配置、两个重放轨道（有/无确定性预执行检查实现 Open Agent Passport）下完成 225,964 次评估。每次评估报告 5 类事件：支付请求、成功支付、授权决定、接收方成员资格、未授权接收方转账。

关键结果：请求率因配置差异远大于模型差异，模型单独在 Level 1 为 10.9%，Level 2 为 3.0%，Level 3 为 0.1%，Level 4 为 79.4%。Level 4 的 1293 个 prompt 上请求率 71.2%-84.3%，809 个 prompt 在所有 14 个模型都产生请求并成功支付给白名单接收方，说明这是共享行为而非攻破。授权边界才是差异点：在 Level 2-4，模型单独未授权转账 140/76,842，加 OAP 层后 0/69,297；匹配三元组上 105 vs 0；0 未授权转账跨越 790 个源会话，每会话上界 0.38%。该层未通过拒绝支付达成：层后执行 25,370 笔支付，策略仅拒绝了 25,640 次转账调用中的 187 次，其中 148 次因禁止接收方。

数据集、评分代码与分析脚本已在 Hugging Face 发布。
