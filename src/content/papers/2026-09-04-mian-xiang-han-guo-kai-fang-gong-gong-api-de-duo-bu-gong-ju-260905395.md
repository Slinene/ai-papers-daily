---
title: 'Multi-Step Tool-Calling over Korean Open Public APIs: A Benchmark and a Data-Synthesis
  Recipe'
title_zh: 面向韩国开放公共 API 的多步工具调用基准与数据合成
authors:
- Dain Kim
- Eungi Cho
- Kyumin Kim
- Shinyeong Noh
- Kyuseong Lim
affiliations:
- LG CNS
arxiv_id: '2609.05395'
url: https://arxiv.org/abs/2609.05395
pdf_url: https://arxiv.org/pdf/2609.05395
published: '2026-09-04'
collected: '2026-09-07'
category: Agent
direction: Agent 工具调用 · 执行验证数据合成
tags:
- tool-calling
- data-synthesis
- GRPO
- execution-grounded
- API-agent
- benchmark
one_liner: 执行验证动态图合成多步工具调用数据，9B 模型经 GRPO 微调接近 27B
practical_value: '- 构建多步 tool-calling 训练数据时，用真实 API 执行验证 schema 间的参数传递链（output→input），只保留实际跑通的边，可避免合成不可执行轨迹；电商/搜索
  Agent 接内部商品、订单、营销 API 也能复用这一 graph 验证思路。

  - 将工具流建模为动态执行图，节点是工具/参数，边是数据依赖；可把常用 API 组合沉淀成可遍历子图，自动扩展长尾 multi-step 任务，适合 query-商品-优惠券-物流等串行调用场景。

  - 用 GRPO 在合成轨迹上做 RL 微调，小模型 9B 可逼近大 27B untuned；预算受限的本地化 Agent 可优先考虑 execution-grounded
  合成 + RFT/GRPO，而不是盲目换大模型。

  - 评估时增加真实 API 调用成功率/轨迹可执行率，而不只看格式正确率；对推荐 Agent 的 task completion 指标设计有参考。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：数据主权法规要求公共机构本地部署开源 LLM agent，但开源模型在多步 live government API tool-calling 上表现差，且缺少专门 benchmark。

**方法关键点**：
- 提出 KOPA-Bench，包含 145 个基于韩国真实公共 API 的任务，覆盖实体代码查询、分页取数等多步调用。
- 提出 EDGE：Execution-grounded Dynamic Graph。先构建工具间输出→输入的参数依赖图，再直接调用真实 API 筛选出实际执行成功的边，最后沿验证过的边遍历合成可执行多步轨迹。
- 用合成数据对 9B 模型做 GRPO 强化微调。

**关键结果**：
- 经 GRPO 微调的 9B 模型在 KOPA-Bench 上接近同系列未微调 27B 模型。
- 在 BFCL benchmark 上也显著提升，验证了 execution-grounded 数据合成的跨场景可迁移性。
