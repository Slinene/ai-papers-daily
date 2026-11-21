---
title: 'System 1 agents: a method for local, reliable and fast agentic AI'
title_zh: System 1 智能体：本地、可靠、快速的工具调用方法
authors:
- Eleftherios Tzanis
- Michail E. Klontzas
arxiv_id: '2611.21053'
url: https://arxiv.org/abs/2611.21053
pdf_url: https://arxiv.org/pdf/2611.21053
published: '2026-11-15'
collected: '2026-11-21'
category: Agent
direction: Agent 工具调用本地化与防幻觉
tags:
- System 1
- Tool Calling
- Hallucination
- Local LLM
- Schema Compiler
one_liner: 将工具 schema 与请求编译为选择题，由单次决策模型作答，实现零幻觉工具调用
practical_value: '- 在电商导购 Agent 调用商品搜索、优惠券查询、订单 API 时，可把工具选择与参数填充从自回归生成改为「确定性编译 +
  选择题/填空题」，所有候选值只能来自用户请求或 schema 枚举，天然杜绝 LLM 编造商品 ID、价格、优惠码。

  - 对需要本地化或高 QPS 在线链路（如实时搜索建议、广告素材选择）的场景，用一次前向的轻量决策模型替代 LLM 逐 token 生成，能显著降低延迟和 token
  成本，同时避免非法工具名和不存在参数。

  - 可借鉴其评估方式：统计工具调用中“发明内容”的比例作为 Agent 可靠性指标，上线前与本地 LLM agent 基线对比，重点检查用户未提供但被模型补齐的参数值。

  - 当请求中缺少必要参数时，让 Agent 显式“正确拒绝调用”，而不是让 LLM 猜值执行，这对交易链路（下单、支付、发券）尤其重要。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**
临床等敏感场景不能把数据传上云，但本地 LLM agent 做工具调用时会逐 token 生成工具名和参数，可能调不存在的工具、用不存在的参数，或填一个用户从未给出的值。一个幻觉值会沿分析流水线传播到后续每一步，且难以被发现。

**方法关键点**
设计 System 1 agents：完全不做文本生成。一个确定性编译器把每个工具的 schema 和当前请求转成多道多项选择题，所有选项均来自请求原文或 schema 定义；再由一个单次前向的决策模型直接输出答案，根据答案完成工具选择、参数填充或拒绝调用。该架构把工具调用变成封闭世界里的分类/抽取问题，而不是开放生成。

**关键结果数字**
在 1,952 条请求、157 个影像与生物医学工具上，最佳 System 1 agent 选对工具或正确拒绝的比例为 97.0%，显著超过 18 个本地 LLM-agent 配置中的最好成绩 95.2%。在 6,056 个已声明参数值上，填充准确率为 97.0%。System 1 调用中没有出现任何发明内容，而 LLM 调用中发明内容占比为 5.5–19.7%。代码已开源。
