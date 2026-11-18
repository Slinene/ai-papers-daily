---
title: Invariant-Aware Harness Enforcement to Protect LLM Agents from Silent API Failures
title_zh: 基于不变量感知的 Harness 强制保护 LLM Agent 免受静默 API 失败
authors:
- Sajib Acharjee Dip
- Brian Ouyang
- Lala Motlhabi
affiliations:
- Virginia Tech
- Genentech
arxiv_id: '2611.20595'
url: https://arxiv.org/abs/2611.20595
pdf_url: https://arxiv.org/pdf/2611.20595
published: '2026-11-15'
collected: '2026-11-18'
category: Agent
direction: Agent 工具调用可靠性
tags:
- LLM Agent
- API Failure
- Invariant Checking
- Tool Calling
- Reliability
- Enforcement
one_liner: SilentGuard 在工具调用 harness 层用 API 不变量强制拦截静默失败，将 LLM Agent 错误答案从七成降至接近零
practical_value: '- 在电商/广告/搜索推荐 Agent 接入搜索、推荐、商品统计等内部 API 时，别只依赖 prompt 自检或 LLM reviewer；把校验逻辑放进
  tool-calling harness，对返回结果做硬性 invariant 检查，例如请求了 category 过滤，返回条目必须全部匹配该 category；请求两个条件计数，结果不能大于任一单条件计数。

  - 强制拦截比警告有效：论文实测用相同检查但只给 warning，错误答案仍有 70.1%；因此对关键数据接口应直接 withhold 结果或让 agent 返回
  abstain，而不是把可疑结果继续传给模型。

  - 公共研究 API 中 11/15 存在静默失败，说明业务 API 也可能无声地忽略 filters 返回看似正常的错误结果；可在工具调用层记录 invariant
  violation 作为监控指标，识别不可靠 API 并推动修复，避免污染下游推荐/广告归因。

  - 对计数、统计类 API 的静默失效尤其敏感，可设计 cross-field 不变量，如请求多个 filter 时，结果数必须小于等于去掉任一 filter
  后的 cardinality；这类检查成本低，能大幅降低静默错误传播。'
score: 7
source: huggingface-daily
depth: abstract
---

## 动机
LLM Agent 大量通过 API 获取搜索结果、商品统计等信息，再据此作答。很多 API 会静默失败：例如文档里 filter 名写错，API 直接忽略该 filter，仍返回 HTTP 200 和看似合理但错误的数据。当前方案如 checklist、reviewer model、LLM judge 依赖模型自我纠错，但模型往往看到问题仍继续回答。

## 方法关键点
SilentGuard 把判断从模型移到执行工具调用的 harness 层。它对每个 API 返回结果测试必须满足的 invariants，例如请求的过滤条件必须被满足、返回数量必须符合约束。一旦违反 invariant，就 withhold 结果，不传给模型，通过 abstaining 而非恢复来避免错误答案。关键结论是强制 enforcement 远好于仅给 warning。

## 关键结果
- 15 个公共研究 API 中 11 个存在静默失败，计数最多膨胀 691 倍。
- 现有修复方法留下超过 70% 错误答案，LLM judge 只标记 77.4% 的虚假计数。
- 在 7 个开源模型上，SilentGuard 将目标故障上的错误答案从 74.0% 降到 1.7%，且无故障任务性能不下降。
- 在 3 个前沿模型上，错误答案从 70.2% 降到 0.5%。
- 仅给警告仍导致 70.1% 错误答案，强制拦截是关键。
- 对新类型的故障，harness 单独将错误答案从 61.1% 降至 24.5%。
