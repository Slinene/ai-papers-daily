---
title: Layer-wise Token Compression for Efficient Document Reranking
title_zh: 逐层令牌压缩以提升文档重排效率
authors:
- Shengyao Zhuang
- Zhichao Xu
- Ivano Lauriola
affiliations:
- Amazon AGI
- Amazon AWS
arxiv_id: '2605.20683'
url: https://arxiv.org/abs/2605.20683
pdf_url: https://arxiv.org/pdf/2605.20683
published: '2026-05-20'
collected: '2026-05-22'
category: RecSys
direction: 文档重排序效率优化 · Token 压缩
tags:
- Token Compression
- Cross-Encoder
- Listwise Reranking
- Efficiency
- Document Ranking
one_liner: 在中层Transformer层进行自适应令牌池化，保留早期交互并加速计算，吞吐量最高提升116%
practical_value: '- 电商搜索/推荐的重排序阶段常使用 cross-encoder，文档/商品描述较长导致推理延迟高；可借鉴 LTC 在中间层做
  token 池化，根据吞吐需求调节压缩率与层位置，平衡效果与速度。

  - 训练时必须加入压缩，让模型学习鲁棒的压缩表示；推理时直接对未压缩模型应用压缩会导致效果崩塌（尤其低层高压缩率）。微调成本低，but 效益显著。

  - 在 listwise LLM 重排（如商品列表排序）中，通过文档掩码仅压缩物品 token 而保留 query/instruction，可大幅提升吞吐（+73%），同时效果不降甚至提升，可复用到多物品评分场景。

  - 轻量压缩（如保留 80% tokens）可能产生正则化作用，使得模型在未见过的长文本上泛化更好，可用来处理商品描述长度差异大的情况，无需额外训练。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：基于 Transformer 的 cross-encoder 重排器是信息检索的核心，但 query-document 联合编码导致序列长、计算开销大。现有 token 压缩方法（如 Jasper）在嵌入层直接池化，对 bi-encoder 有效，但会破坏 cross-encoder 早期的细粒度交互，损害排序质量。需要一种保留交互的压缩策略。

**方法关键点**：
- 提出 **Layer-wise Token Compression (LTC)**：在 Transformer 的中间层（非嵌入层）使用 1D 自适应平均池化，减少序列长度。
- 超参数：压缩率 \(r\)（保留 token 比例）和目标层 \(l^*\)，低层保留完整交互，高层加速。
- 对 listwise LLM 重排，通过文档掩码仅压缩文档 token，保留 query/instruction，避免跨文档压缩。
- 训练时即加入压缩，使模型适应压缩表征。

**关键实验**：
- 数据集：MS MARCO 训练，DL19/DL20 评估；pointwise 用 Qwen3-0.6B，listwise 用 Mistral-7B。
- Baseline: 无压缩模型、Jasper 嵌入层压缩。
- 结果：passage ranking 中层压缩（l=8, r=0.4）无显著性能下降，QPS 提升 25%；document ranking（512 tokens）压缩模型 nDCG@10 达 0.663，超过未压缩的 0.651；listwise 压缩带来 27-73% 吞吐提升，部分指标优于 baseline；Jasper 同等 QPS 下 nDCG 骤降至 0.583。
- 零样本推理应用 LTC 性能崩溃，说明调优关键。
- BEIR 零样本迁移中，压缩模型效果与 baseline 相当，轻微压缩更优，表明正则化作用。

**核心 insight**：**中间层 token 压缩是 cross-encoder 效率与效果的最优折中点，训练时加入压缩可强化长度不变性，比嵌入层压缩安全得多。**
