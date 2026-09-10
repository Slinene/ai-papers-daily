---
title: 'REDSI: Addressing the Reproducibility and Evaluation Consistency of Differentiable
  Search Indexing for Document Retrieval'
title_zh: REDSI：解决可微搜索索引文档检索的可复现性与评估一致性问题
authors:
- Vivien Nicolas
- Hicham Randrianarivo
- Pascale Sébillot
- Caio Corro
affiliations:
- Artefact Research Center
- INSA Rennes, IRISA, CNRS, Université de Rennes
- MICS, CentraleSupélec, Université Paris-Saclay
arxiv_id: '2609.08860'
url: https://arxiv.org/abs/2609.08860
pdf_url: https://arxiv.org/pdf/2609.08860
published: '2026-09-08'
collected: '2026-09-10'
category: GenRec
direction: 生成式检索 · DSI 可复现性
tags:
- Differentiable Search Index
- Generative Retrieval
- Reproducibility
- NQ320K
- Atomic Identifiers
- Document Retrieval
one_liner: 首个支持 DSI 三种标识符的开源实现及参数化 NQ320K 构建管道，系统分析模型缩放
practical_value: '- 商品/文档标识符设计：如果商品库规模在几十万以内，直接使用 atomic ID（每个商品一个输出 token）可能比 semantic
  ID 更好，训练快、推理只需一步解码，且对模型容量下降更鲁棒；注意大规模库的输出词表扩展性。

  - 数据集构建：复用公开数据集或自建检索/推荐数据集时，明确去重键（稳定 ID 如 SKU/商品ID，而非 title 或 URL），清洗文本序列化（去除 infobox、导航、特殊字符）以减少
  unk token，对固定输入长度前缀影响显著。

  - 训练采样比例：不要盲从原论文的 indexing:retrieval ratio，应调参。本文发现自然比例（约 1:2.8）远好于 DSI 原文的 32:1，这个超参常被忽略但影响显著。

  - 解码简化：生成式检索/推荐中，在 beam search 后接 valid ID 过滤即可，无需实现复杂的 trie 约束解码；模型缩小时同样有效，可降低工程复杂度。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：DSI 是生成式检索的 de facto 基线，但难以复现：无公开实现覆盖全部三种文档标识符，NQ320K 数据集构建方式多样且缺乏说明，导致各论文结果不可比。现有工作偏好多 token 标识符（semantic/naive）和模型放大，忽略 atomic 标识符及小模型鲁棒性。

**方法关键点**：
- 发布 REDSI，统一训练/评估管道，支持 atomic、naive、semantic 三种标识符。
- 构建参数化 NQ320K 管道，分离去重和序列化：去重规则包括 TEXT4K、TITLE、URL、PAGEID；序列化包括 NCINORM（沿用 NCI 预处理）和 HTMLNORM（从原始 HTML 重建，减少 unk token，清洗 infobox/nav/IPA）。
- 发现 indexing-to-retrieval ratio 是关键超参：自然比例（约 1:2.8）优于原 DSI 的 32:1。
- 解码：unconstrained beam search + post-filtering 即可，trie 约束解码无一致提升。

**关键实验与结果**：
- 在 NQ320K 四个变体（TITLE/PAGEID × NCINORM/HTMLNORM）上训练 T5-Efficient-Tiny/Small/Base。
- Atomic 标识符在所有模型尺度上 MRR@10 最高：T5-Base 上 atomic 68.8–70.0，naive 60.1–62.0，semantic 59.7–61.1。
- 44M 参数 atomic 模型（MRR@10 62.2）超过 220M 参数 naive（60.1）或 semantic（59.7）模型。
- Atomic 训练到峰值仅需 6.8 小时，naive/semantic 需 74.5 小时以上。
- 使用 PAGEID 去重比 TITLE 一致提升；HTMLNORM 比 NCINORM 略好。
- 语义标识符在小模型下无效生成率更低，但 MRR 仍低于 atomic。

**最值得记住的一句话**：在中小规模生成式检索中，atomic identifiers 是最强且最鲁棒的选择，而数据集构建和 indexing/retrieval 采样比例对结果的影响被显著低估。
