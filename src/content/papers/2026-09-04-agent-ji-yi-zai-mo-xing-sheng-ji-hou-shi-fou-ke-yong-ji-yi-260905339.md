---
title: Does Your Agent's Memory Survive a Model Upgrade? A Controlled Study of Memory
  Portability
title_zh: Agent 记忆在模型升级后是否可用：记忆可移植性对照研究
authors:
- Ankit Goyal
- Jaideep Ray
affiliations:
- LinkedIn
arxiv_id: '2609.05339'
url: https://arxiv.org/abs/2609.05339
pdf_url: https://arxiv.org/pdf/2609.05339
published: '2026-09-04'
collected: '2026-09-07'
category: Agent
direction: Agent 记忆可移植性评测
tags:
- Agent Memory
- Model Upgrade
- RAG
- Knowledge Graph
- Memory Portability
- Evaluation
one_liner: 对照评测四种 Agent 记忆格式在模型升级后的可移植性，证明固定 schema 知识图谱最稳，NOTES 与 RAG 需重建或保留原始历史
practical_value: '- 生产级 Agent 记忆若可能经历模型升级，优先用固定 schema 的 KG 而非自由文本 NOTES；KG-fixed
  在 writer swap 下 accuracy 几乎不变，能避免模型耦合导致的隐性遗忘。

  - RAG 记忆系统升级 embedding 模型时，不要在同一个索引里混用新旧 embedding：50/50 混合只拿到 4.96pp 增益，会丢掉全量 re-embedding
  的 11.90pp 大部分收益。应隔离版本化 embedding 空间，新模型向量写入独立索引。

  - 只保留压缩后的 NOTES 不够：模型升级后 store-only repair 在 48 个用例中全都达不到 90% 恢复目标；必须同时保留原始 source
  history，才能在检索或解读出错时重新构建记忆。

  - 记忆迁移评估必须做方向特异性测试：NOTES 迁移出现 +9.91 与 -13.28pp 的非对称变化。训练/评测 pipeline 里不要只测 A→B，要把
  B→A 也纳入回归项。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：Agent 长期记忆在模型升级时面临隐性遗忘风险：同一份 memory store 不迁移，新模型可能对旧自然语言笔记解读不同；混合 embedding 版本会破坏检索；只修 store 而无原始证据难以有效修复。因此需要量化不同记忆存储格式在 writer swap 时的可移植性。

方法：构造 48 个 synthetic histories，采用随机答案码和 exact scoring，比较 4 种记忆格式：LC-RAW（完整原文长上下文）、RAG（分块检索增强）、NOTES（模型压缩的自然语言笔记）、KG-fixed（固定 schema 知识图谱）；使用两个 <10B open-weight 模型做互换测试。

结果：KG-fixed 最稳，writer swap 后 accuracy 仅变化 +0.0004±0.0020；NOTES 高度耦合模型，accuracy 随迁移方向偏移 +9.91 或 -13.28pp；RAG 使用 50/50 混合 embedding 索引仅提升 4.96pp，远低于全量 re-embedding 的 11.90pp。分解诊断显示：NOTES 精度损失 80% 来自构建期信息丢失；RAG 损失 81% 来自检索失败。仅修 store 的 NOTES 修复在 48 个用例中无一达到 90% 恢复目标，而保留原始 source history 可在某个测试方向 34/48 成功恢复。结论指向方向特异性迁移测试、严格 embedding 空间隔离，以及保留 source histories 进行记忆修复。
