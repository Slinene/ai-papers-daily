---
title: Do Neural Retrievers Prefer Certain Documents? Evidence of Learned Relevance
  Priors
title_zh: 神经检索的隐性偏好：模型从标注中学会了偏爱某些文档
authors:
- Francisco Valentini
- Edgar Altszyler
- Martin Fajcik
affiliations:
- CONICET-Universidad de Buenos Aires
- Quantit, Buenos Aires, Argentina
- Brno University of Technology, Brno, Czech Republic
arxiv_id: '2606.02814'
url: https://arxiv.org/abs/2606.02814
pdf_url: https://arxiv.org/pdf/2606.02814
published: '2026-06-01'
collected: '2026-06-03'
category: RecSys
direction: 监督式稠密检索中的隐性文档先验
tags:
- relevance prior
- document findability
- neural retrievers
- annotation bias
- bi-encoder
one_liner: 发现监督式双编码器在检索时会学到文档级相关性先验，导致低先验但真正相关的文档更难被找到
practical_value: '- 用逻辑回归在冻结文档嵌入上训练相关性先验分类器，可快速诊断检索模型是否对特定文档类型存在系统性偏好，适合在电商搜索或推荐召回上线前做偏置审计。

  - 标注数据中的“主流、全面、自包含”文档更易被选为正例，实际业务中应警惕训练数据构建带来的隐性偏好，可考虑对冷门、碎片化或技术性强的内容做主动过采样或数据增强。

  - 先验得分与文档可寻性高度相关，可将其作为离线评估指标之一，识别出模型可能“歧视”的文档集合，针对性改进索引或重排序策略。

  - LLM 生成式解释框架可迁移至推荐系统的特征归因或数据分布分析，用自然语言描述两个文档集合的差异，便于团队理解模型偏置来源。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
神经检索模型（双编码器）在日常训练中依赖人工标注的 query-document 对，但标注过程只会挑选部分文档进行标注，这种选择往往偏向某些文档类型（如全面、自包含的百科式文本）。模型是否会因此学会一种与 query 无关的文档级“相关性先验”，从而在检索时系统性歧视那些真正相关但不符合主流偏好的文档？论文通过实验证明这种隐式先验确实存在，并量化了它造成的“可寻性差距”。

**方法关键点**
- 提出文档可寻性（findability）指标：文档在所有相关 query 下的平均倒数排名。
- 用线性探针（逻辑回归）从冻结的文档嵌入中估计隐式相关性先验 P(R|d)，该先验不依赖 query。
- 玩具实验注入虚假 token [X] 作为伪先验，验证监督双编码器会吸收这种信号并形成可寻性差距。
- 主实验使用三个开源强双编码器（BGE-en-icl、NV-Embed-v2、gte-Qwen2-7B-instruct），在 MTEB 的多个非对称检索数据集上评估。
- 先用 BGE 的训练集训练先验模型，再在未见过的文档集上测试 AUC，并分析先验分数与可寻性的关系。
- 用匹配文档对（控制长度、相关文档数等混杂因素）加 LLM 合成 query，隔离先验效应。
- 用 LLM 生成自然语言解释，对比 judged-relevant vs. unjudged 以及 high-prior vs. low-prior 文档的文本差异。

**关键结果**
- 先验模型在多数数据集上 AUC 显著高于 0.5，如 FEVER 达 0.93，Climate-FEVER 0.90，表明先验信号泛化到新文档。
- 稠密检索器的可寻性随先验分数单调上升（例如 DBPedia 中可寻性从 0.1 升至 0.4），而 BM25 无一致趋势。
- 匹配对照实验中，稠密模型高、低先验文档的可寻性平均差约 0.05~0.10，BM25 差距极小。
- LLM 解释：被标注相关的文档多为“全面的主流主题介绍，自包含”，未标注文档常为“碎片化、缺少上下文、小众技术细节”；高先验文档类似百科全书，低先验文档偏向实用指南或原始数据。

**最值得记住的一句话**
监督式检索模型不只是学会了相关性，更内化了训练标注中的文档类型偏好，使得大量真正相关但不符合主流样式的文档被系统性压制在检索结果底部。
