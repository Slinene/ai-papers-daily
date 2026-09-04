---
title: 'RuleMem: Active Rule Memory for Long-Term Conversational Agents'
title_zh: 规则记忆：对话代理的主动规则归纳与推理
authors:
- Xingyuan Zeng
- Zuohan Wu
- Quanming Yao
- Yue Wang
- Wei Liu
- Libin Zheng
- Jiuke Wang
- Jian Yin
affiliations:
- Sun Yat-sen University
- The Hong Kong University of Science and Technology (Guangzhou)
- Shenzhen Institute of Computing Sciences
- The Hong Kong Polytechnic University
- Tsinghua University
arxiv_id: '2609.03915'
url: https://arxiv.org/abs/2609.03915
pdf_url: https://arxiv.org/pdf/2609.03915
published: '2026-09-03'
collected: '2026-09-04'
category: Agent
direction: Agent 长对话记忆规则化推理
tags:
- Rule Induction
- Long-term Memory
- Conversational Agent
- RAG
- Horn Clause
- Perplexity Filtering
one_liner: 将对话历史归纳为自然语言 Horn 子句规则，用 perplexity 一致性过滤并指导证据召回与推理，显著提升长对话 QA 准确率
practical_value: '- 从用户历史交互中归纳行为规则（如“用户买过 A 后常会买 B”），作为可复用推理模板，可指导召回和排序，缓解语义鸿沟。

  - RPC 验证机制可用于任何 LLM 生成的规则/知识，通过 perplexity 降低评估支持度，过滤幻觉和过泛化规则。

  - 将 Horn 子句作为推理骨架，与事实分离，可在推荐解释或对话式推荐中提供显式逻辑链，增强可信度。

  - 工程上可以将事实存储与规则存储分层，规则层承担“抽象先验”，在查询时先激活规则再召回事实，降低无关噪声。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
长期对话中的问答需要跨大量时间分散的历史推理，现有记忆机制要么被动存储事实（similarity retrieval），要么构建实例级结构（知识图谱、Zettelkasten），都面临语义鸿沟导致的召回失败和复杂上下文中的推理失败。需要更高层次的抽象：从实例中归纳规则，像人类认知一样用规则指导记忆和推理。

## 方法关键点
- **规则归纳**：从对话提取时序四元组 (subject, relation, object, time) 构建事实记忆库；通过随机游走采样推理路径，LLM 筛选并重构；对相似关系路径分组，归纳为自然语言 Horn 子句规则（B1 ∧ ... ∧ Bn ⇒ H），其中原子用类型占位符（如 [Person], [Event]）抽象。
- **RPC 验证**：用条件困惑度降低衡量规则质量。内部一致性：规则头相对规则体的 perplexity 降低；外部事实一致性：加入相关事实后规则头 perplexity 进一步降低。两者加权得分超过阈值才存入规则记忆库。
- **推理时**：先匹配规则头激活候选规则，以规则体为前提生成检索线索，召回候选事实；再用 LLM 作为语义统一算子过滤不满足变量绑定的事实；最后将问题、激活规则、证据组织成结构化 prompt 生成答案。

## 关键实验
- 数据集：LoCoMo（5,882 对话轮，1,986 问题）和 LongMemEval_s*（5 个超长对话，约 1.82M tokens，300 问题）。
- 基线：对比 14 个主流记忆与 RAG 方法，包括 Mem0, Letta, LangMem, A-MEM, Mem0g, MemoryBank, MemInsight, Zep, SCM, BM25, ReAct, MetaKGRAG, LightRAG, GraphRAG。
- 结果：在 LoCoMo 上，平均 BLEU 36.90，Acc 78.05，超过基线平均 27.47 分（相对 54.3%）；多跳 Acc 82.43，开放域 78.37。消融显示去除规则和 RPC 均显著下降。Guided Recall 平均召回率从 0.56 提升到 0.79（+41.1%）；Explicit Reasoning 平均推理失败减少 12%。

**最值得记住的一句话**：用可复用的抽象规则作为记忆，能同时缓解语义鸿沟和推理不确定性，将被动记忆变为主动推理骨架。
