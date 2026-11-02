---
title: 'KITE: Retrieval as a Decision Procedure for Long-Term Conversational Memory'
title_zh: KITE：将检索构建为长期对话记忆的决策过程
authors:
- Feng Li
- Kailun Tan
- Zhibo Zhou
- Youxiang Wang
- Lejun Liu
- Huaigu Li
- Fei Du
- Huilong An
affiliations:
- Memoket AI Research
- Universität Stuttgart
- Georgia Institute of Technology
- Tsinghua University
arxiv_id: '2610.41521'
url: https://arxiv.org/abs/2610.41521
pdf_url: https://arxiv.org/pdf/2610.41521
published: '2026-10-30'
collected: '2026-11-02'
category: Agent
direction: Agent 长期记忆检索决策化
tags:
- LLM Agent
- Long-term Memory
- Retrieval
- Decision Procedure
- Conversational Memory
- Vector-free
one_liner: KITE将长期对话记忆检索变成受控主题索引上的可检查决策过程，LoCoMo/LongMemEval-S准确率93.5%/86.0%，仅约1.6k
  tokens
practical_value: '- 在电商客服/对话式推荐 Agent 里，长期记忆不要只依赖 embedding 相似度；可以维护一个受控的主题/商品/意图词汇表，把查询编译为显式检索计划，根据问题包含的时间、实体、主题条件去定位历史证据，提升可审计性。

  - 对结构化主题索引遗漏的表面细节，用 BM25 等稀疏词法检索兜底，适合找回订单号、SKU、地址、优惠码等精确字符串，避免 embedding 模糊匹配丢失关键信息。

  - 受控索引的动态扩展与合并可用于治理电商知识库和会话 topic；固定 lookup/ranking 执行路径可降低 LLM 调用成本，每题仅约 1.6k reader-context
  tokens，对高并发成本敏感的 Agent 场景有直接复用价值。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：现有 LLM Agent 长期记忆普遍用 embedding 相似度检索；它能做语义匹配，但无法判断检索到的记忆是否满足问题所隐含的条件，导致召回证据与查询条件脱节。

方法：KITE 不走向量检索，将多会话对话组织成受控主题词汇表（governed topic vocabulary）索引的结构化知识；主题通过受控扩展与合并演进。查询时先把问题编译为同一知识索引上的可检查检索计划，再用固定 lookup 和 ranking 操作执行；对结构化表示遗漏的表面细节用稀疏 lexical retrieval 兜底。

结果：在 LoCoMo 和 LongMemEval-S 上分别达到 93.5% 和 86.0% 准确率，每题 reader-context 只需约 1.6k tokens，说明记忆检索可超越相似度排序，成为确定证据是否满足问题的可检查决策过程。
