---
title: 'Shopping by algorithm: How agentic AI deploys human heuristics as a surrogate
  consumer'
title_zh: 算法购物：代理式 AI 如何将人类启发式部署为代理消费者
authors:
- Davood Wadi
- Yu Ma
affiliations:
- Desautels Faculty of Management, McGill University
arxiv_id: '2609.28372'
url: https://arxiv.org/abs/2609.28372
pdf_url: https://arxiv.org/pdf/2609.28372
published: '2026-09-23'
collected: '2026-09-24'
category: Agent
direction: Agent 代理消费者决策与信息搜索
tags:
- LLM agents
- consumer behavior
- bounded rationality
- pricing cues
- tool calls
- information search
one_liner: 通过 Tool-Lab 实验发现，在模糊目标与信息获取成本下，LLM 购物代理会像人类一样省略诊断属性并做出次优选择。
practical_value: '- 目标 prompt 要具体：明确要求比较单位价格等诊断属性，可显著减少 LLM 购物代理在成本约束下省略关键信息的行为。

  - 信息获取成本设计需谨慎：工具调用成本会放大营销定价线索的误导性，建议接口层默认暴露单位价格等高诊断价值属性，或强制计算。

  - 监控定价线索交互：just-below pricing 与促销框架在零成本下几乎无害，但在模糊目标+成本条件下会触发启发式捷径，需在代理决策链路中加入单位价格校验。

  - 信息架构比模型本身更关键：营销启发式漏洞来自店面信息架构而非 LLM 不可变缺陷，可通过工具/接口设计缓解。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：消费者日益将购买决策委托给 LLM 代理，但代理是否也会像人类一样被营销定价启发式误导尚不明确。作者构建 Tool-Lab 实验，将产品属性置于昂贵的工具调用之后，追踪 AI 购物代理的信息获取过程。

**方法关键点**：在八个商业 LLM（三个提供商）上测试 just-below pricing 与促销框架两种定价线索；操纵信息获取成本（零成本 vs 高成本）与目标 prompt 模糊度（模糊 vs 具体）；记录代理在做出选择前调用的属性，判断其是否获取了计算单位价格所需的诊断属性。

**关键结果**：零成本下定价线索几乎不误导；但施加获取成本且目标模糊时，LLM 会省略单位价格计算所需的诊断属性，做出类似人类启发式的次优选择；具体目标 prompt 则能保持诊断搜索与选择最优性。研究表明，委托式 AI 购物中的营销启发式受店面信息架构支配，而非 LLM 固有缺陷。
