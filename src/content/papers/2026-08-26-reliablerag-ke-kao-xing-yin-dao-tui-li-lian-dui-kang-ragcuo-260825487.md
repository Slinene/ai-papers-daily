---
title: 'ReliableRAG: Combating Misinformation in Retrieval-Augmented Generation via
  Reliability-Guided Reasoning Chains'
title_zh: ReliableRAG：可靠性引导推理链对抗RAG错误信息
authors:
- Jinpu Jiang
- Xuan Wu
- Wenhao Song
- Bo Yang
- You Zhou
- Hongwei Ge
- Heow Pueh Lee
- Yanchun Liang
- Chunguo Wu
affiliations:
- Jilin University
- Dalian University of Technology
- National University of Singapore
- Zhuhai College of Science and Technology
arxiv_id: '2608.25487'
url: https://arxiv.org/abs/2608.25487
pdf_url: https://arxiv.org/pdf/2608.25487
published: '2026-08-26'
collected: '2026-08-27'
category: RAG
direction: 多跳QA · 细粒度可靠性评估
tags:
- RAG
- Multi-hop QA
- Misinformation
- Reasoning Chains
- Triple Extraction
- Reliability
one_liner: 首个面向多跳QA的可靠性驱动RAG框架，通过细粒度三元组评估与推理链生成对抗欺骗性错误信息
practical_value: '- 借鉴“信息段→结构化三元组→可靠性打分”的管线：在电商商品问答或导购场景中，把商品详情、评论、UGC转为三元组，结合 query
  相关性与三元组可信度（来源权威度、事实一致性）过滤不可靠内容，降低错误信息对答案的影响。

  - 采用 top-K 非冗余三元组压缩上下文：RAG 检索大量文本易含噪声，先抽取三元组并去冗余，能减少 token 消耗、提高生成准确性，适合实时推荐文案生成或客服Agent场景。

  - 自回归构建推理链而非一次性生成：在多跳决策场景（如“为何该商品适合油皮？”需综合成分、评价）中，逐跳纳入可靠三元组，提高推理可解释性与鲁棒性，可参考用于购物决策Agent。

  - 显式区分语义相关性与事实可信度：推荐/搜索中只做语义匹配易被“看起来相关但事实错误”的内容误导，建议增加可靠性评估模块（来源权威度、跨源验证等）。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：RAG 在新闻、社交媒体等含错误信息场景中易受欺骗，多跳QA中单个语义相关但事实错误的片段就足以误导多步推理。现有方法依赖隐式对齐或显式规则，缺乏细粒度信息可靠性评估，难以应对伪装成相关信息的欺骗内容。

**方法**：ReliableRAG 先从源文档抽取信息片段并表示为结构化三元组。对每个三元组计算可靠性分 = 查询-三元组语义相关性 + 三元组可信度，并保留 top-K 可靠且非冗余的三元组。基于这些三元组自回归构建推理链，逐步整合可信证据、过滤误导信息，最终生成忠实于可靠信息的答案。该框架以三元组为最小评估单元，是首个可靠性驱动的 RAG 抗错误信息方案。

**结果**：在三个多跳QA数据集上的实验表明，ReliableRAG 在欺骗信息注入条件下显著优于现有方法，提升了 RAG 系统的事实可靠性和鲁棒性。
