---
title: PersonalQuery-Benchmark:Evaluating Retrieval Robustness to Personalized User
  Expression Differences
title_zh: 个性化查询基准：评估检索对用户表达差异的鲁棒性
authors:
- Wenyu Liang
- Hongzhi Yin
- Tongtong Wu
- Fan Liu
- Kexin Dai
- Weiqing Wang
affiliations:
- Monash University
- University of Queensland
- Southeast University
arxiv_id: '2610.32164'
url: https://arxiv.org/abs/2610.32164
pdf_url: https://arxiv.org/pdf/2610.32164
published: '2026-10-23'
collected: '2026-10-26'
category: Eval
direction: 个性化检索鲁棒性评测基准
tags:
- Personalized Retrieval
- Query Robustness
- Benchmark
- Syntactic Variation
- Writing Errors
- LLM Ranking
one_liner: 构建首个个性化查询表达差异基准 PQB，揭示检索效果高不等于对句法与书写错误鲁棒
practical_value: '- **构建用户表达差异测试集**：从真实用户历史文本中挖掘个性化句法习惯和常见书写错误，生成同一信息需求的多版本 query，用于评估检索/排序模型在真实用户表达波动下的稳定性。

  - **评估模型鲁棒性与效果分离**：不要只看整体 nDCG/MRR，需单独报告模型对句法变化和拼写错误变化的敏感度；高效果模型可能对用户表达变化更脆弱，在电商搜索中直接导致长尾用户流失。

  - **用 LLM 生成 query 变体 + 人工校验**：可用 LLM 基于用户历史文本生成个性化句法改写和拼写错误变体，再用 LLM 评估与少量人工标注做质量校验，低成本构造大规模鲁棒性测试集。

  - **检索架构选择参考**：论文覆盖 lexical、learned sparse、dense bi-encoder、late-interaction、hybrid
  五类检索架构，其鲁棒性差异可作为电商搜索技术选型的参考——需根据业务对用户输入噪声的容忍度选择合适架构。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：个性化信息检索主要建模用户偏好和查询意图，但忽略了不同用户表达同一信息需求时的个性化表达差异。现有真实查询数据缺乏稳定的用户身份、长期表达历史和意图匹配对照，难以系统评估表达差异对检索结果的影响。

**方法关键点**：提出 PersonalQuery-Benchmark (PQB)。从用户历史文本中建模两类个性化表达：个性化句法表达（如词序、句式习惯）和个性化书写错误（如拼写、打字错误）。基于这些模式构造同一信息需求下的个性化句法查询和个性化书写错误查询，并通过 LLM 评估和独立人工评估验证基准质量。PQB 覆盖 Amazon 三个产品域，共包含 6516 个查询实例。在五类代表性检索模型（lexical、learned sparse、dense bi-encoder、late-interaction、hybrid）和两个 LLM-based ranking 模型上进行评估。

**关键结果**：在固定信息需求的情况下，个性化表达差异仍导致可测量的排序变化；不同检索模型对句法变化和书写错误变化的敏感度差异明显；整体检索效果更高的模型未必对表达变化具有更强的鲁棒性。PQB 为系统研究个性化表达鲁棒性提供了新基准和评估框架。
