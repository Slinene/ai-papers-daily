---
title: 'xPRT: Cross-Passage Retrieval Pretraining'
title_zh: xPRT：跨段落检索预训练
authors:
- Danush Khanna
- Himanshu Singhal
- Pranjal A. Chitale
- Bishal Santra
affiliations:
- Microsoft Research
arxiv_id: '2610.40122'
url: https://arxiv.org/abs/2610.40122
pdf_url: https://arxiv.org/pdf/2610.40122
published: '2026-10-29'
collected: '2026-10-30'
category: RAG
direction: 无监督检索预训练 · 跨段落对比学习
tags:
- Dense Retrieval
- Unsupervised Pretraining
- Contrastive Learning
- RAG
- Cross-Passage
- MTEB
one_liner: 提出无监督跨段落检索预训练框架 xPRT，利用文档内跨段落信号，在 MTEB 上平均超越最强基线 3.2%
practical_value: '- 电商搜索/推荐中的稠密检索模型可用商品详情页、用户评论等长文档内部段落关系构造无监督对比对，无需标注 query-doc 数据，降低训练成本。

  - 在已有无监督 checkpoint 上继续预训练时，直接使用常规对比学习目标可能性能回退，xPRT 的跨段落信号能带来互补增益，对检索模型持续预训练有参考价值。

  - 工程实现上，可从同一文档内采样正负段落，利用标题、章节、评论段落等结构信息生成难负样本，增强语义区分能力。

  - 若业务中已有 RAG 或搜索系统，可将 xPRT 作为额外预训练任务叠加到现有流程，提升检索器在语义匹配任务上的泛化性。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：密集检索器是 RAG 和搜索系统的核心组件，但训练需要昂贵的标注 query-doc 对。现有无监督预训练方法多基于语言建模或短片段对比学习，未能充分利用单个文档中跨段落的丰富信号。

**方法关键点**：提出 xPRT（Cross-Passage Retrieval Pretraining），无监督地从整个文档中学习关键信息分布及段落间连接。通过在文档内构造跨段落对比学习信号，作为现有检索预训练目标的补充。

**关键结果**：在 MTEB English v2 上，从公共无监督 checkpoint 继续预训练，固定语料、调度和训练过程。与五个 SOTA 目标对比，xPRT 平均超越最强基线 3.2%。在持续预训练场景下，许多基线方法出现明显性能回退，而 xPRT 提供最大的互补增益。消融实验证实增益来自跨段落信号。
