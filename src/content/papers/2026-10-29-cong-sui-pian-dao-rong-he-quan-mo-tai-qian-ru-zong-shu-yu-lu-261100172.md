---
title: 'From Fragmentation to Fusion: A Survey and Roadmap for Omnimodal Embeddings'
title_zh: 从碎片到融合：全模态嵌入综述与路线图
authors:
- Ziyin Zhang
- Yuyu Guo
- Ying Zhang
- Siqiao Xue
- Zihan Liao
- Jin Qin
- Wenjie Yang
- Siyuan Yang
- Shijie Li
- Cheng Chen
affiliations:
- Ant Group
- Shanghai Jiao Tong University
- Australian National University
- Tongji University
- National University of Singapore
arxiv_id: '2611.00172'
url: https://arxiv.org/abs/2611.00172
pdf_url: https://arxiv.org/pdf/2611.00172
published: '2026-10-29'
collected: '2026-11-03'
category: Multimodal
direction: 多模态嵌入统一框架与路线图
tags:
- Omnimodal Embeddings
- Multimodal Learning
- Contrastive Learning
- Joint Embedding
- Survey
- Embedding Unification
one_liner: 提出覆盖、可比、组合三能力框架与三条统一路径，系统梳理多模态嵌入研究
practical_value: '- 在推荐/搜索中构建多模态商品或内容 embedding 时，先诊断系统在 3C 上的短板：是否覆盖了用户 query、商品图、描述、视频等所有输入？不同模态
  embedding 是否真的可比（同空间）？若需组合属性（如“红色连衣裙”），仅靠对齐可能不足，应评估联合嵌入。

  - 工程实现上可阶段式升级：若资源有限，先用 transformation 将表格、图等序列化为文本，复用现有 text encoder 快速上线；但要注意转换损失，适合冷启动和
  MVP。

  - 对比学习对齐双塔（如图文）存在 modality gap，导致跨模态检索的相似度分数不可直接比较；可在损失中加 gap 校准项，或后处理投影到同一子空间，提升图文一致性。

  - 对 Agent 场景：当 LLM 需要理解混合输入（商品列表、图片、用户行为）时，优先使用联合嵌入模型而非分别编码再拼接，以保留组合语义，便于后续推理。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：嵌入模型是搜索、推荐等系统的底层基础，但各模态社区独立发展，缺乏统一视角。论文认为对比学习、Transformer 架构和粒度变化正在推动各模态嵌入研究走向收敛，因此需要一个跨模态的统一框架，厘清共性与差异。

**方法关键点**：提出三个递进能力——覆盖（coverage）：系统实际能编码哪些输入类型；可比性（comparability）：不同输入能否在同一空间直接比较；组合性（compositionality）：能否组合不同粒度或模态的语义。对应三条统一路径：转换（transformation）将其他模态渲染成图像或序列化为文本，如 PIXEL、TableRAG；对齐（alignment）用双塔对比学习（CLIP、CLAP），但存在 modality gap；联合嵌入（joint embedding）用单编码器深度跨模态交互（如 MM-Embed、VLM2Vec），被视为最终目标。论文还提出 3C 评估门，用于检查模型的覆盖、可比和组合能力。

**关键结果**：作为首个针对全模态嵌入的跨领域综述，系统梳理了可复用的解剖结构（五个正交组件）和各模态收敛轴，指出从碎片化到融合的演进路线。
