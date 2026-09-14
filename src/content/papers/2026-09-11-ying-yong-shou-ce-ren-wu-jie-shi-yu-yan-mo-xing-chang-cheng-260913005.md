---
title: 'Tasks over Application Manuals: Revealing Gaps in Long-Horizon Procedural
  Reasoning for Language Models'
title_zh: 应用手册任务：揭示语言模型长程程序推理的缺陷
authors:
- Utkarsh Soni
- Syed Shariyar Murtaza
- Yifan Nie
- Sachin Chandrasekhar
- Eugene Wen
affiliations:
- Manulife
arxiv_id: '2609.13005'
url: https://arxiv.org/abs/2609.13005
pdf_url: https://arxiv.org/pdf/2609.13005
published: '2026-09-11'
collected: '2026-09-14'
category: Eval
direction: 长程程序推理评测
tags:
- benchmark
- long-horizon reasoning
- RAG
- agent
- GPT-5
- procedural reasoning
one_liner: 构建 TAM 基准，用两类真实手册任务评估 GPT-5，发现精确匹配仅 1% 和 15.5%
practical_value: '- 业务中高度规则化、需要跨文档查询的任务（广告政策、促销/优惠券规则、售后条款）不要直接交给 GPT-5 端到端生成最终判定；应拆成可校验的子步骤，每步做精确匹配或规则引擎兜底，LLM
  只做信息抽取/语义匹配。

  - RAG 和 ReAct 在长程手册任务上没解决根本问题，说明长文档检索准确率是瓶颈；可先做语义切分、section-level 索引、规则预先结构化（如将条款转成可执行
  DSL/知识图谱），把“翻手册”转化为确定性查表。

  - 建立内部评测时，用逐条人工验证的 exact-match 指标，不要只看模型输出“像不像”；TAM 的构建方法可复制到自己的业务手册/政策库上，先测 GPT-5
  类模型的基线。

  - Agent harness 可能因循环步骤长而累积错误，建议设置中间状态校验点、限制 ReAct 步数，并把高置信度规则提前缓存到上下文。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

动机：现有 LLM 多跳推理评测多为短程，无法反映真实场景中需要翻阅数百页手册、执行依赖规则链的任务。

方法关键点：构建 TAM 基准，覆盖 ICD-10-CM 临床编码和美国联邦量刑两个领域；每个任务要求从数万条规则中查找并执行跨章节步骤，输出精确答案。用 GPT-5 评估 RAG、ReAct 风格提示和 agent-harness 等通用方法。

关键结果：最好精确匹配率 ICD-10-CM 仅 1%，量刑 15.5%，显示当前评测高估了模型长程规则遵循能力，检索与推理循环带来错误传播。数据与代码已公开。
