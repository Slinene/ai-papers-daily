---
title: 'Beneath the Surface of Chains-of-Thought: A Mechanistic Interpretation of
  Reasoning Operations in LLMs'
title_zh: 链式思维表象之下：LLM推理操作的机制性解释
authors:
- Seogyeong Jeong
- Jaehui Hwang
- Dongyoon Han
- Geonmo Gu
- Alice Oh
- Taekyung Kim
affiliations:
- KAIST
- NAVER AI Lab
arxiv_id: '2609.04753'
url: https://arxiv.org/abs/2609.04753
pdf_url: https://arxiv.org/pdf/2609.04753
published: '2026-09-03'
collected: '2026-09-08'
category: Reasoning
direction: 推理操作表示几何与机制分析
tags:
- mechanistic interpretability
- chain-of-thought
- representation geometry
- LLM reasoning
- attention masking
one_liner: 发现CoT中的问题表述、目标分解、演绎等操作在隐藏表示中可分离，中层最显著并依赖前文推理上下文
practical_value: '- 在 Agent / 搜索推理链路中，可以对 LLM 隐藏状态使用轻量线性探针识别当前是「问题表述 / 目标分解 / 演绎」阶段；中层特征最有效，可用于推理步骤质量监控、异常检测或动态路由，无需完整解析文本。

  - 如果做长 CoT 缓存 / 截断、KV cache 压缩，不能只保留最近片段或表层 token：前文推理上下文对后续 chunk 起始的 operation-aligned
  表示很重要，否则会破坏阶段一致性。

  - 相同表层 token 在不同推理操作中表示不同，说明下游使用 CoT 表示或 embedding 复用时，应按「推理操作上下文」而非字面 token 设计状态表示；这对多阶段推荐
  Agent 的 context 工程有参考价值。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：推理型 LLM 的优化目标越来越直接作用于 CoT 轨迹，但问题表述、目标分解、演绎等显式推理操作在表示空间中的内部结构仍不清楚。

方法要点：在隐藏表示上对多种推理操作做可分性分析，定位最佳分离层级；用词法与位置控制排除伪相关；分析 token 级 operation-alignment 的跨层分布；通过注意力掩码干预，检验当前 chunk 起始处表示是否依赖前文推理上下文。

关键结果：推理操作在 held-out 表示中可分离，中层最显著；该结构不由词法或位置信息解释；加深后操作对齐在 token 跨度上更分布式，相同表层 token 会随所在 chunk 的推理操作而改变表示；chunk onset 的 operation-aligned 表示依赖前文推理上下文。表明 LLM 的语言推理表达与内部几何结构存在对应关系。
