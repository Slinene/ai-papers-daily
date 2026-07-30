---
title: 'Embedding Items at Scale: Comparing GNN-Based and ID-Based Item Embeddings
  in the Yandex Ecosystem'
title_zh: 规模化物品嵌入：Yandex生态下GNN与ID嵌入对比
authors:
- Sergei Makeev
- Artem Matveev
- Vladimir Baikalov
- Kirill Khrylchenko
affiliations:
- Yandex
arxiv_id: '2607.26365'
url: https://arxiv.org/abs/2607.26365
pdf_url: https://arxiv.org/pdf/2607.26365
published: '2026-07-29'
collected: '2026-07-30'
category: RecSys
direction: 物品嵌入策略对比 · 工业级序列推荐
tags:
- sequential recommendation
- item embeddings
- GNN
- ID-based embedding
- industrial scale
- cost-quality trade-off
one_liner: 大规模工业系统对比表明，GNN预训练嵌入仅在数据有限时有益，数据充足时端到端ID嵌入无差异
practical_value: '- 大规模推荐系统（如电商首页Feed）训练数据充足时，直接使用哈希ID嵌入端到端训练即可，无需额外GNN预训练，节省特征工程和模型维护成本。

  - 新业务或冷启动阶段（如垂直品类推荐）数据稀疏，可引入GNN预训练物品嵌入提升模型效果，但需评估额外的图构建和更新开销。

  - 物品ID嵌入采用哈希技巧处理动态目录，降低嵌入表内存占用，适合频繁上新的电商场景，工程实现简单且有效。

  - 该结论为排序/召回模型中的物品表征架构选型提供了清晰决策依据：先评估数据规模再决定是否加入预训练模块。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：Transformer序列推荐模型中，物品嵌入策略直接影响效果和成本。工业界普遍使用GNN预训练嵌入或哈希ID嵌入端到端学习，但缺乏大规模场景下二者效果与成本的系统对比。

**方法**：在Yandex Market、Yandex Music两个成熟推荐系统及一个公开小数据集（Yandex Lavka）上，比较了基于GNN的预训练物品嵌入（如PinSage变体）与基于哈希技巧的ID嵌入（随机初始化，与Transformer联合训练）的效果。GNN嵌入利用物品属性、协同交互等图信息预训练；ID嵌入则直接映射到固定大小嵌入表，通过哈希解决海量物品ID问题。

**关键结果**：当训练数据充足（数亿交互）时，端到端ID嵌入与GNN预训练嵌入的下游推荐准确率（HR/MRR）无显著差异，预训练未带来增益；但在小数据场景（百万级交互）下，GNN预训练嵌入显著优于随机初始化的ID嵌入。成本方面，GNN预训练需额外维护图数据和训练管线，而ID嵌入免去此环节，工程更简洁。
