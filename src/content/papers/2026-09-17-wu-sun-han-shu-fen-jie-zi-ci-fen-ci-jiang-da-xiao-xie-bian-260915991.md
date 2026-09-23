---
title: 'The Functionalizer: Lossless Functional Decomposition for Subword Tokenization'
title_zh: 无损函数分解子词分词：将大小写/变音/重复编码为可逆操作符
authors:
- Connor Makowski
- Willem Guter
affiliations:
- Center for Transportation & Logistics, Massachusetts Institute of Technology
arxiv_id: '2609.15991'
url: https://arxiv.org/abs/2609.15991
pdf_url: https://arxiv.org/pdf/2609.15991
published: '2026-09-17'
collected: '2026-09-23'
category: LLM
direction: 子词分词 · 函数分解
tags:
- Subword Tokenization
- Lossless Decomposition
- Orthographic Variation
- Vocabulary Efficiency
- GPT-2
one_liner: 提出 Functionalizer 预分词框架，将大小写、变音、字符重复无损分解为 Unicode 操作符前缀，显著减小词汇量并提升代码生成质量
practical_value: '- 面向多语言或 UGC 场景（跨境电商商品标题、评论、搜索 query），将大小写、重音、字符重复等表面变化从词汇表中剥离，用可逆操作符编码，可显著压缩词汇表、降低嵌入参数，且不丢失信息。

  - Functionalizer 是可插拔的预分词器，能无缝接入现有 BPE/WordPiece 流程，工程实现成本低；可先在离线语料上验证词汇压缩率和下游任务（如
  query 理解、CTR 模型）的 AUC 变化。

  - 字符重复操作符对 UGC 中常见的情感强调（如“好好好”“赞赞赞”）有直接借鉴意义，可减少不同重复次数 token 的数量，避免词汇碎片化。

  - 对代码生成或结构化文本任务，该方法通过保留结构信息提升语法有效性，提示我们在处理电商领域结构化数据（如商品参数模板、广告文案规则）时，可以尝试显式建模格式变化而非依赖模型隐式记忆。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：标准子词分词将 hello、Hello、HELLO、Héllo 视为独立 token，导致词汇膨胀、嵌入空间碎片化；而有损归一化（如小写化、去重音）则永久丢失信息。为此需要一种既能压缩词汇又不丢失表面变化的方案。

**方法关键点**：Functionalizer 是一个无损预分词框架，在标准分词之前将每个词分解为一个规范基础 token（operand）加上一系列参数化变换操作符（opcode）前缀，操作符编码在 Unicode Private Use Area。操作符包括 CAPITALIZE（大小写）、13 个变音符号专用操作符、REPEAT 和 MULTIREPEAT（字符重复），全部可逆。这样词汇表只需存储 canonical base，表面变化由操作符组合表达，实现词汇高效且信息无损。

**关键结果数字**：在自然语言和代码语料上，Functionalizer 在完整覆盖语料的同时显著减小词汇量，实际词汇槽需求降低最高达 19.7%。在 ~98M 参数 GPT-2 模型下游评估中，Python 代码语法有效性从 7.70% 提升至 9.12%，自然语言文本的重复 n-gram 生成减少。结果表明函数分解能有效提升词汇效率和结构感知的语言建模能力。
