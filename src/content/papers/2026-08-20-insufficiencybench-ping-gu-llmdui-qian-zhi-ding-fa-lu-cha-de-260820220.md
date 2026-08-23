---
title: 'InsufficiencyBench: Evaluating LLM legal advice on underspecified user queries'
title_zh: InsufficiencyBench：评估LLM对欠指定法律查询的处理能力
authors:
- Samuel J. Vincent
- Daniel Calloway
- Fangyi Yu
- Andrew M. Bean
- Nabeel Seedat
affiliations:
- Thomson Reuters Foundational Research
- Imperial College London
arxiv_id: '2608.20220'
url: https://arxiv.org/abs/2608.20220
pdf_url: https://arxiv.org/pdf/2608.20220
published: '2026-08-20'
collected: '2026-08-23'
category: Eval
direction: LLM欠指定查询处理评估
tags:
- InsufficiencyBench
- Legal AI
- Query Understanding
- Benchmark
- LLM Evaluation
- Underspecified Queries
one_liner: 首个法律查询信息不足基准，衡量LLM识别缺失要素并避免臆测回答的能力
practical_value: '- 在电商客服/对话式推荐Agent中，先对用户query做信息充分性分类，识别缺失的决策关键属性（如尺码、配送地址、预算、使用场景），在推荐前主动追问，避免用模型臆测补全。

  - 构建类似“完整 vs 缺失变体”的评估集，监控模型是否对信息不足请求无差别回答或过度拒绝；用F2/召回等指标平衡漏判与过度追问。

  - 借鉴缺失元素分类法（switch/gating/fatal prerequisite）设计对话状态机：不同缺失类型对最终决策影响不同，可配置强制追问、条件追问或默认假设。

  - 对搜索query改写/推荐召回场景，先判断query是否信息不足，避免用LLM幻觉补全用户意图产生错误召回；同时保留对完整query直接执行的能力。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

动机：现有法律LLM基准假设用户查询信息完整，但实际用户常遗漏影响法律结果的关键事实，模型可能基于臆测给出置信错误答案。

方法关键点：构建InsufficiencyBench，首个针对查询侧信息不足的基准。正式化8类缺失元素，归入switch、gating、fatal prerequisite三类结构失败模式；包含202项（58个完整查询，144个缺失变体），覆盖6个法律领域、24个美国司法辖区，由执业律师标注。评估十个前沿模型在缺失元素识别、追问与回答限定上的表现。

关键结果数字：没有任何模型在缺失元素识别上F2超过0.46，中位召回仅0.44；模型要么无差别保留意见，要么在捏造假设下悄然回答；没有模型能同时做到对缺失查询限定回答、对完整查询直接回答。
