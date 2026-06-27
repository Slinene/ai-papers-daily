---
title: Tracing Target Answers in Poisoned Retrieval Corpora via Token Influence Attribution
title_zh: 基于令牌影响归因检测RAG中毒攻击并追踪目标答案
authors:
- Yan-Lun Chen
- Pin-Yu Chen
- Chia-Mu Yu
- Ying-Dar Lin
- Yu-Sung Wu
- Wei-Bin Lee
affiliations:
- National Yang Ming Chiao Tung University
- IBM Research
- Hon Hai Research Institute
arxiv_id: '2606.25721'
url: https://arxiv.org/abs/2606.25721
pdf_url: https://arxiv.org/pdf/2606.25721
published: '2026-06-24'
collected: '2026-06-27'
category: RAG
direction: RAG安全性 · 令牌影响归因
tags:
- RAG
- corpus poisoning
- detection
- token influence attribution
- lightweight
one_liner: TRACE利用令牌影响归因轻量检测RAG语料中毒，同时还原攻击者预设的错误答案
practical_value: '- 电商客服或知识库RAG场景中，可将TRACE作为轻量安全层，无需额外LLM校验，仅通过高频高影响关键词检测中毒文档，降低计算开销和延迟。

  - 方法依赖的令牌影响归因（如梯度×嵌入）可直接集成到现有RAG推理流程，对检索到的文档进行实时评分，用于过滤可疑内容。

  - 论文揭示中毒文档中反复出现的高影响令牌会泄露攻击者预设的错误答案，这一特性可用于安全审计：通过追踪此类关键词发现攻击意图和候选恶意文档。

  - 在推荐系统的评论问答或商品描述生成中，若使用RAG，同理可借鉴TRACE防止恶意语料篡改生成结果，提升系统鲁棒性。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：RAG系统通过外部知识增强LLM，但易受语料中毒攻击——攻击者预先注入误导文档，使LLM生成错误答案。现有检测方案依赖辅助分类器或额外LLM校验，计算开销大，不适用于实时业务。

**方法**：TRACE（Tracing Target Answers in Poisoned Corpora via Token Influence Attribution）是一种轻量检测框架。它首先利用令牌影响归因（如梯度×输入词嵌入）定位对模型输出影响最大的关键词；然后在多个检索文档中寻找重复出现的高影响关键词，认为这些词是攻击者刻意注入的“目标答案碎片”；最后通过二次验证（检查这些关键词是否确实驱动模型输出特定错误答案）确认中毒行为。整个过程无需额外模型训练或LLM自检，仅依赖推理时的归因分析。

**结果**：在三个QA基准（NQ、HotpotQA、MS MARCO）和六个LLM（包括Llama-2、Mistral等）上，TRACE检测中毒攻击的F1均超过0.9，同时能高准确率还原攻击者预设的错误答案（如“50岁”对于“医疗保险生效年龄”的问题），验证了关键词与目标答案的强关联。
