---
title: 'FootprintRAG: Visual Analytics for Evidence Context Refinement in RAG-based
  Scientific Literature Exploration'
title_zh: FootprintRAG：科学文献探索中RAG证据上下文精炼的可视化分析系统
authors:
- Xingyu Liu
- Yu Dong
- Qizhen Yu
- Shiyu Cheng
- Zhe Wang
- Guan Li
- Guihua Shan
- Dong Tian
- Christy Jie Liang
- Quang Vinh Nguyen
affiliations:
- Computer Network Information Center, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
- Hangzhou Institute for Advanced Study, UCAS
- University of Technology Sydney
- Western Sydney University
arxiv_id: '2609.19601'
url: https://arxiv.org/abs/2609.19601
pdf_url: https://arxiv.org/pdf/2609.19601
published: '2026-09-17'
collected: '2026-09-19'
category: RAG
direction: RAG 证据上下文可视化精炼
tags:
- RAG
- Visual Analytics
- LLM Agent
- Evidence Refinement
- Scientific Literature
- Provenance
one_liner: 将RAG证据上下文显式化为可检查、可修订对象，通过LLM-agent与可视化视图支持多轮检索、证据精炼与溯源摘要生成
practical_value: '- 在商品知识库问答或客服 RAG 场景，把检索到的证据片段（商品属性、用户评论、政策条款）显式呈现为可勾选/排除的候选列表，生成前允许业务人员修正证据上下文，减少隐式过滤导致的错误答案。

  - 引入多轮检索轨迹可视化：记录每轮 query 变体、召回、重排和采纳/丢弃状态，便于调试 RAG pipeline，定位漏召回或误排序原因，类似检索评估矩阵。

  - 用 LLM-agent 自动化证据评估与补充候选生成：对每条证据打分并基于语料级证据空间推荐 ERS 排名补充候选，可迁移到广告文案生成中的素材/卖点证据挖掘与推荐。

  - 摘要生成支持 provenance-aware，每条结论可追溯到来源证据单元，适用于电商导购内容合成或商品推荐理由解释，增强可信度与合规性。'
score: 6
source: arxiv-cs.HC
depth: abstract
---

**动机**：RAG 在科学文献探索中用于 grounding LLM 输出，但证据上下文通常通过隐式检索、重排序、评估、过滤步骤产生，用户不清楚证据如何被构建、哪些被保留或丢弃，可能遗漏潜在有用证据。

**方法关键点**：FootprintRAG 将 RAG 证据上下文视为生成前可显式检查、修订的分析对象。系统解析科学文献为文本和图表的证据单元；将初始查询扩展为并行 query 变体；在迭代轮次中检索与评估证据；从语料级证据空间中通过 ERS 排名呈现补充候选。协调视图将检索轨迹、证据状态修订与溯源摘要生成连接成用户可操控的工作流，允许用户比较检索方向、修正证据状态并重新生成摘要。

**关键结果**：通过两个案例研究、用户研究以及与代表性 RAG 系统的流程级对比，验证系统能帮助用户比较检索方向、修订候选证据、恢复可能被忽略的证据，并将生成摘要追溯到支撑证据单元。
