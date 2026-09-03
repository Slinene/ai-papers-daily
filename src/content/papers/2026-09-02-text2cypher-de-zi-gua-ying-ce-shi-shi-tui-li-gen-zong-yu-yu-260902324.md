---
title: Adaptive Test-Time Inference for Text2Cypher with Trace Budgeting and Selective
  Refinement
title_zh: Text2Cypher 的自适应测试时推理：跟踪预算与选择性精炼
authors:
- Makbule Gulcin Ozsoy
affiliations:
- Neo4j, London, UK
arxiv_id: '2609.02324'
url: https://arxiv.org/abs/2609.02324
pdf_url: https://arxiv.org/pdf/2609.02324
published: '2026-09-02'
collected: '2026-09-03'
category: LLM
direction: LLM 测试时推理优化 · Text2Cypher
tags:
- Text2Cypher
- test-time inference
- adaptive budget
- execution-guided refinement
- cost efficiency
one_liner: 提出自适应 trace 预算与选择性执行引导精炼，在 Text2Cypher 上降低 30.7% 生成预算、21-25% 推理时间且质量持平
practical_value: '- 在电商/搜索的文本生成场景（query 改写、商品标题、广告文案、推荐理由）中，可先做难度/置信度评估，动态分配采样与精炼预算：简单请求少生成少校验，复杂请求多候选+执行级验证，降低
  LLM 成本与延迟。

  - 执行引导精炼可迁移到业务规则校验：对生成结果做 schema、库存、价格、广告法违禁词等可执行检查，仅在失败或低置信时触发强模型 refinement，而不是全量二次生成。

  - 跨模型族精炼结果表明，可保留现有轻量/低延迟主模型，用另一个强模型作为统一精炼服务做兜底，兼顾效果与成本，便于在推荐链路中逐步引入 LLM 精炼。

  - 动态 budget 分配思路类似推荐系统的粗排/精排分级算力：可按 query 复杂度或用户价值分层，对高价值/复杂流量给予更多推理资源。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：LLM 让自然语言查询结构化数据库成为可能，但生成的 Text2Cypher 查询仍可能语法错误、违反 schema 或执行失败。现有测试时推理虽无需重训即可提升可靠性，却普遍使用固定候选预算和统一精炼策略，对不同难度问题浪费计算。

方法关键点：提出两种自适应测试时策略——adaptive trace budgeting，根据问题难度动态调整候选生成预算；selective execution-guided refinement，仅在额外推理预计有益时触发修正。两者结合可在保持质量前提下减少不必要推理。

关键结果：在 Gemma-2-9B 与 Qwen-2.5-7B 上，adaptive trace budgeting 将平均生成预算降低 30.7%，墙钟推理时间下降 21–25%，生成质量与固定预算相当；selective refinement 几乎保留全部执行成功增益，执行成功仅下降 0.2–0.5%，并跳过简单问题的不必要精炼；此外，单个修正模型 Gemma-4 可有效精炼不同模型族的输出，显示 refinement 可跨模型族迁移。
