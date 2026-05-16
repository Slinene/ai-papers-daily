---
title: Granite Embedding Multilingual R2 Models
title_zh: Granite 嵌入多语言 R2 模型
authors:
- Parul Awasthy
- Aashka Trivedi
- Yushu Yang
- Ken Barker
- Yulong Li
- Bhavani Iyer
- Martin Franz
- Meet Doshi
- Riyaz Bhat
- Vignesh P
affiliations:
- IBM Research
arxiv_id: '2605.13521'
url: https://arxiv.org/abs/2605.13521
pdf_url: https://arxiv.org/pdf/2605.13521
published: '2026-05-13'
collected: '2026-05-16'
category: Other
tags:
- Embedding
- Multilingual
- Retrieval
- ModernBERT
- Distillation
- Matryoshka
one_liner: 基于 ModernBERT 的多语言嵌入模型族，支持 200+ 语言与 32K 上下文，在检索、代码和长文档任务上达到领先水平，并提供同类最优的
  97M 参数压缩模型。
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：多语言文本嵌入模型在企业检索、RAG 等场景中至关重要，但现有开源模型存在语种覆盖不足、上下文长度受限、训练数据许可不友好等问题。本文旨在构建一套覆盖 200+ 语言、拥有 32K token 上下文窗口、且全部基于企业友好数据训练的高质量嵌入模型，同时提供不同参数规模以满足不同部署需求。

**方法关键点**
- **编码器架构**：基于 ModernBERT 改进，采用交替注意力、RoPE 位置编码、去除偏置项等优化，并扩充了多语言分词器（基础版 262K 词表，压缩版 180K 词表），以增强多语言效率。
- **三阶段训练**：大规模预训练（2.5T tokens）→ 上下文扩展至 8192，RoPE theta 提升 → 学习率衰减阶段融合英语、多语言与连续变体，使模型覆盖超过 1800 种语言。
- **嵌入微调**：使用对比学习（改进的 InfoNCE 损失）、多教师知识蒸馏（分别训练英语和多语言大模型教师）、上下文进一步扩展至 4K、模型合并以及 Matryoshka 表示学习（支持维度截断）。压缩版通过剪枝和词表选择从大模型初始化，再经蒸馏微调。
- **训练数据**：全部使用企业友好数据，排除 MS-MARCO，包含无监督标题-正文对、公开多语言数据、IBM 产品文档、合成数据（覆盖 18 种语言的长/短文本、代码、推理等），并经过多轮 LLM 评判过滤。

**关键结果数字**
- 全尺寸模型 (311M) 在 MTEB-v2 多语言检索平均得分 **65.2**，较前代 R1 (278M) 提升 13 点，位居 500M 以下开源模型前三。
- 压缩版 (97M) 得分 **60.3**，是 100M 以下开源多语言嵌入模型中的最高分，领先第二名 9+ 分。
- 长上下文检索 (LongEmbed) 上，全尺寸达 **71.7** nDCG@10，压缩版达 65.5，均基于 32K 上下文窗口。
- 代码检索 (MTEB Code) 全尺寸 **63.9**，压缩版 60.4；推理检索 (RaR-b) 全尺寸 **28.0**，压缩版 24.9。
- 吞吐量：311M 模型在 H100 上编码速度为 1828 doc/s (512 token)，97M 模型达 2534 doc/s，实现质量与效率的良好平衡。

**一句话总结**：Granite Embedding Multilingual R2 通过现代编码器架构、多阶段对比蒸馏和高质量企业数据，在覆盖 200+ 语言的同时，以 32K 长上下文和领先检索精度定义了多语言嵌入的新标杆。
