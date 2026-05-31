---
title: 'Latent Terms: Dense Retrievers Contain Trivially Extractable BM25-ready Zipfian
  Vocabularies'
title_zh: 潜在词项：密集检索器含有可轻易提取的BM25就绪齐普夫词汇
authors:
- Benjamin Clavié
- Sean Lee
- Aamir Shakir
- Makoto P. Kato
affiliations:
- Mixedbread AI
- National Institute of Informatics
- University of Tsukuba
arxiv_id: '2605.29384'
url: https://arxiv.org/abs/2605.29384
pdf_url: https://arxiv.org/pdf/2605.29384
published: '2026-05-28'
collected: '2026-05-31'
category: RecSys
direction: 密集检索器稀疏词汇抽取与混合检索
tags:
- sparse autoencoders
- BM25
- dense retrievers
- latent vocabulary
- neural IR
one_liner: 提出Latent Terms，用稀疏自编码器从冻结密集检索器中提取稀疏词汇，直接用于BM25检索，效果匹配或超越原密集模型及SPLADE
practical_value: '- 已有密集检索系统的电商搜索可直接复用：在冻结的双编码器上训练稀疏自编码器，得到BM25兼容的稀疏特征，无需重新训练即可搭建混合检索，提升召回率。

  - 该方法无需任何稀疏检索监督或查询扩展目标，适用于商品描述等长文本场景，可利用现有密集模型快速构建倒排索引，降低工程成本。

  - 提取出的稀疏词汇呈现齐普夫分布，可解释性强，便于分析模型学到了哪些重要词项，辅助构建更好的 query 理解和同义词表。

  - 在 LIMIT 这类单向量检索易失败的任务上，Latent Terms 大幅优于原密集模型，说明其可弥补向量检索的精确匹配短板，适合高精度召回场景。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：神经密集检索器（单/多向量）通常仅通过向量相似度评分，缺乏可解释的稀疏词汇表示，难以结合经典 BM25 的高效索引与精确词汇匹配能力。现有方法需专门训练稀疏检索模型，成本高且与密集模型解耦。

**方法**：提出 Latent Terms，在冻结的密集检索模型上训练稀疏自编码器（SAE），自编码器将模型隐层激活映射到高维稀疏编码并重建，这一过程自动涌现出一个潜在词汇表，其词项频率近似齐普夫分布。该稀疏编码可直接用于 BM25 评分，无需任何检索相关微调或查询扩展监督。

**结果**：在 MS MARCO 等基准上，Latent Terms 的单向量评分性能匹配或超越原密集模型和 SPLADE 变体；在专门检验单向量检索短板的 LIMIT 任务上，显著优于原模型。这表明密集检索器内部蕴含比默认评分函数更丰富的可索引结构。
