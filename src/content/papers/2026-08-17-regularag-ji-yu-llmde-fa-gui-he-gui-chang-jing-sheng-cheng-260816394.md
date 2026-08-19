---
title: 'Think Inside the Chunk: RegulaRAG for Regulation-Compliant Scenario Generation
  using LLMs: A Case Study of UN Regulation No. 152'
title_zh: RegulaRAG：基于LLM的法规合规场景生成（以UN第152号法规为例）
authors:
- Vahid Zolfaghari
- Nenad Petrovic
- AndrÉ Schamschurko
- Alois Knoll
arxiv_id: '2608.16394'
url: https://arxiv.org/abs/2608.16394
pdf_url: https://arxiv.org/pdf/2608.16394
published: '2026-08-17'
collected: '2026-08-19'
category: RAG
direction: RAG 检索增强生成优化
tags:
- RAG
- Chunking
- Graph Traversal
- Reranking
- LLM
- Regulation
one_liner: RegulaRAG结合SmartChunking、图遍历参考感知增强与Smart Retrieve & Rerank，在法规场景生成中Meta-Score
  82.99，领先43%
practical_value: '- **结构感知切片（SmartChunking）**：对法规、商品说明书、活动规则等长文档RAG，保留标题/章节/条款层级，避免简单固定长度切片导致上下文断裂，可显著提升LLM回答准确性。

  - **参考感知增强**：通过图遍历自动关联段落与表格（例如电商SKU参数表与正文描述），解决表格信息在RAG中检索不到或割裂的问题，可直接用于商品详情页问答、售后政策查询。

  - **三步渐进式参数搜索**：不依赖暴力网格搜索，快速找到chunk大小、top-k等检索参数，降低调参成本，适合快速迭代的电商RAG系统。

  - **鲁棒性压力测试**：用干扰文档扩充语料库评估RAG稳定性，可作为上线前评测标准，防止因知识库膨胀导致检索质量急剧下降。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：LLM在生成法规合规测试场景时，难以将输出锚定在长而层级化的标准文档中，导致幻觉和遗漏。
**方法**：RegulaRAG 采用 SmartChunking 保留法规结构；通过图遍历对段落和表格进行参考感知增强，建立引用关系；在增强单元上使用 Smart Retrieve & Rerank 进行检索。输出用自定义惩罚评分指标评估。实验包括三步渐进式搜索确定近似最优检索参数、与5个基线RAG对比、以及用干扰内容扩充语料库的鲁棒性测试。
**结果**：RegulaRAG 平均 Meta-Score 82.99，比第二好的系统高43%（NoRAG 57.94），每个查询token消耗14k-25k，远低于图中心基线高达500k。语料库规模增长时性能保持稳定，而竞争RAG系统质量和鲁棒性急剧下降。
