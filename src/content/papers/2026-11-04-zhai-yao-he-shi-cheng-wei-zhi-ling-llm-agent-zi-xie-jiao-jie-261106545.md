---
title: When Do Summaries Become Instructions? Unsupported Policy in LLM Agents' Self-Written
  Handoff Summaries
title_zh: 摘要何时成为指令？LLM Agent 自写交接摘要中的无依据策略
authors:
- Wenhui Chu
affiliations:
- University at Albany, State University of New York
arxiv_id: '2611.06545'
url: https://arxiv.org/abs/2611.06545
pdf_url: https://arxiv.org/pdf/2611.06545
published: '2026-11-04'
collected: '2026-11-05'
category: Agent
direction: Agent 上下文压缩交接摘要的可靠性审计
tags:
- LLM agents
- handoff summaries
- context compaction
- policy drift
- evaluation
- unsupported permissions
one_liner: 审计 LLM Agent 上下文压缩摘要中的无依据权限与限制，并验证其影响继任行为及来源
practical_value: '- 在电商/客服等长时运行 Agent 中，上下文压缩交接摘要可能引入原记录不支持的权限/限制。建议对交接摘要中涉及“允许/禁止/需审批”的句子做规则或
  LLM 审计（类似 AI reader），标记疑似无依据策略，人工或自动复核。

  - 系统提示的措辞影响策略漂移：明确说明“权限/需求必须来自权限账本”比笼统说“某些操作需审批”能大幅减少无依据限制（5.0%→1.8%，held-out 1.8%→0.3%），且不削弱必要审批。在
  Agent 系统提示中可尝试将策略来源显式化。

  - 对疑似无依据策略句子的影响评估可用 same-snapshot replay：将原摘要中的策略句替换为中性填充后重跑后继 Agent，对比行为变化；若影响脆弱，说明继承效应可能被高估，需谨慎解读。

  - 权限账本、工具使用场景（如广告投放、商品上架审批）下，可在压缩后自动比对账本与摘要中的权限陈述，避免虚假授权导致未授权操作。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：长时运行的 LLM Agent 通过压缩上下文节省空间，但交接摘要中常包含权限、审批要求等政策性句子，若与原始记录不符，会被后继 Agent 继承并改变行为。

方法：用合成工具使用任务构建带 ground-truth permission ledger 的环境；same-snapshot replay 将摘要中疑似无依据策略句替换为中性填充，测试行为影响；两个 AI reader 对规则标记的 held-out 摘要进行确认。

结果：两个开放权重模型中分别有 1.2% 和 2.4% 的摘要包含无依据限制，0.1% 和 1.3% 包含无依据授权。针对限制的预先设定 replay 测试不显著（p=0.58），后续探索性分析发现脆弱效应（p=0.027）。中和虚假批准后，未授权动作从 120 次中的 24 次降至 7 次（事后分析；后续集合 48 次中从 17 降至 11）。多数开发集限制源于 Agent 早先推理认为某操作需要批准（事后分析）。在预先设定测试中，将系统提示从“有些操作需要审批”改为说明需求来源，使无依据限制从开发总结的 5.0% 降至 1.8%，在 held-out 模板上从 1.8% 降至 0.3%（p<10^-9），而账本要求的审批请求几乎不变。代码与数据开源。
