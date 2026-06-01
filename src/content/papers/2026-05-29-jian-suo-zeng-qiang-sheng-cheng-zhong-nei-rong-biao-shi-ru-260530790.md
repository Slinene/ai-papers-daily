---
title: On the impact of retrieved content representations in RAG Pipelines
title_zh: 检索增强生成中内容表示如何影响答案保留与生成准确性
authors:
- Jonathan J Ross
- Bevan Koopman
- Anton van der Vegt
- Guido Zuccon
affiliations:
- The University of Queensland
- CSIRO
arxiv_id: '2605.30790'
url: https://arxiv.org/abs/2605.30790
pdf_url: https://arxiv.org/pdf/2605.30790
published: '2026-05-29'
collected: '2026-06-01'
category: RAG
direction: RAG 检索内容表示对 LLM 生成的影响
tags:
- RAG
- Document Representation
- Answer Retention
- LLM
- QA
one_liner: 在RAG中，答案保留是决定生成器准确性的主导因素，其他表示属性影响有限
practical_value: '- 在电商搜索/推荐RAG场景中，优先保证检索片段经压缩或改写后仍 **保留答案关键信息**（如产品属性、参数），而非盲目追求简练或语义对齐。

  - 引入 **答案保留** 作为离线评估指标，可快速筛选文档处理策略，避免每次变更都需昂贵生成评估。

  - 实验中的13种转换（选择、摘要、重写等）可作为多臂老虎机策略的候选臂，但对每种臂需监控保留率，当保留率低于阈值时自动回退到原始表示。

  - 对于多轮Agent对话中上下文有限的情形，采用保留率高的 **选择关键句** 策略比单纯生成摘要更稳定，能减少幻觉并提升工具调用准确性。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有RAG管道大多沿用为人类设计的检索结果表示（如文档全文、片段），当消费者变为LLM时，何种表示形式能最大化生成质量尚缺乏系统理解。以往工作孤立地考察单一转换（如摘要或重写），无法揭示决定生成准确性的核心因素。

**方法**：固定检索引擎，在NQ和TriviaQA等问答数据集上，将同一批检索文档转换为14种不同表示（原始基线、选择、摘要、重写等，含查询依赖/独立变体），分别馈入GPT-4、Llama-3等四个生成器。对每种表示，除测量生成准确率外，还定义并测量 **答案保留**：转换后的文档是否仍包含正确答案。

**关键结果**：答案保留是生成准确率的最强预测因子；当保留率高时，表示的措辞、长度、结构、是否依赖查询等属性对准确率影响甚微。这表明先前工作中归因于特定机制的增益，可能主要由该机制对答案内容的保留能力决定，而非机制本身。控制保留变量后，各表示间的性能差异大幅缩小。
