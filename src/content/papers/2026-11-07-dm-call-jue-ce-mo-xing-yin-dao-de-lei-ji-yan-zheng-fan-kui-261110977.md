---
title: 'DM-Call: Decision-Model-Guided Function Calling with Cumulative Verification
  Feedback'
title_zh: DM-Call：决策模型引导的累积验证反馈函数调用
authors:
- Minhyeong Yu
- Wonduk Seo
- Seunghyun Lee
affiliations:
- Enhans
- University College London
arxiv_id: '2611.10977'
url: https://arxiv.org/abs/2611.10977
pdf_url: https://arxiv.org/pdf/2611.10977
published: '2026-11-07'
collected: '2026-11-10'
category: Agent
direction: LLM 函数调用验证与迭代优化
tags:
- function calling
- decision model
- verification feedback
- LLM Agent
- tool use
- schema validation
one_liner: 用独立决策模型校验函数选择与参数正确性，并累积多轮验证信号作为混合反馈迭代修正，提升函数调用准确率
practical_value: '- 在电商/广告 Agent 中，可在执行真实工具（如下单、扣费、投放 API）前增加一层轻量决策模型做语义校验，拦截函数选择错误和参数不匹配，避免副作用与资损。

  - 累积多次尝试的校验信号（概率、二元判断、schema 错误）作为反馈，比单次错误提示更稳定，可提升 LLM 自我修正成功率。

  - 反馈表示采用「数值概率 + 文本正确性标签」混合形式，比纯文本或纯数值更有效，可直接用于 prompt 模板设计。

  - 无需执行外部工具即可迭代修正，适合高价值 API 调用场景，降低在线成本与风险；但需权衡额外决策模型调用带来的延迟和成本。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：LLM 函数调用不仅要求语法正确，还必须语义正确——选择恰当函数并生成符合用户意图的参数。现有方案多关注语法校验，对函数选择错误和参数不匹配等语义问题覆盖不足。

**方法关键点**：DM-Call 将局部 schema 校验与独立决策模型验证结合。决策模型分别判断函数选择和参数正确性；候选被拒后，系统累积多轮校验信号，包括验证概率、二元判断和 schema 错误。混合反馈表示同时利用数值概率和语言正确性标签，引导 LLM 迭代细化，全程不执行外部工具。

**关键结果**：在 BFCL 和 API-Bank 评估中，DM-Call 相比直接生成显著提升函数调用准确率，额外成本适中。
