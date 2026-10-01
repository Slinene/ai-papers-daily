---
title: Learning Multiresolution Relevance for Hierarchical Generative Retrieval
title_zh: 学习层级生成式检索的多分辨率相关监督
authors:
- Weihao Shen
- Wei Chen
- Fuwei Zhang
- Guojun Liu
- Qingsong Hua
- Wei Lin
- Fuzhen Zhuang
affiliations:
- Beihang University
- Meituan
arxiv_id: '2609.39312'
url: https://arxiv.org/abs/2609.39312
pdf_url: https://arxiv.org/pdf/2609.39312
published: '2026-09-30'
collected: '2026-10-01'
category: GenRec
direction: 生成式检索 · Semantic ID 多分辨率监督
tags:
- Generative Retrieval
- Semantic ID
- Hierarchical Supervision
- Multi-Resolution Relevance
- E-commerce Search
one_liner: 将文档相关度投影为 SID 层级各层的条件分支分布，训练共享 query 表示并保留标准自回归推理
practical_value: '- 对于生成式召回中一个 query 对应多个相关 item 且共享粗粒度 ID 的情况，将 item 相关性按 SID/品类树投影到各层前缀，构造条件分支分布作为辅助监督，训练后丢弃辅助头，不增加推理延迟，可直接叠加到现有
  full-SID/生成式召回训练。

  - 用 parent relevance mass 加权局部 KL，并在候选集包含所有相关 children 和若干高打分 legal sibling negatives，显式建模同父节点分支竞争，比每条正样本独立
  one-hot 监督更稳，可迁移到层级品类树下的 item ID 生成。

  - 推理时可在 beam search 中加入前缀级 query-catalog 兼容性打分（如品类、属性、词法匹配），权重在验证集选，提升最终排序中相关分支覆盖率；中间层作用更大，别只靠
  leaf 分数。

  - 可借鉴 refinement entropy / ambiguity 指标量化 query 在每层 ID 的分支不确定性，用于评估 ID 结构是否合理、标注是否稀疏；不完整标注会掩盖粗粒度分支。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

动机：
生成式检索中 SID 逐层解码，但同一 query 的多个相关文档可能在浅层共享前缀、深层分叉。标准 full-SID 监督把每个相关文档当作独立路径，没有显式学习同一父前缀下多个子分支的相关度分配，导致中间层检索决策监督不充分、目标采样方差大。

方法关键点：
- 将 query 到文档的相关度（二元或分档 3/2/1）归一化后投影到 SID 前缀树，得到每层前缀质量和条件分支分布。
- RARS 在共享 query 表示基础上用 prefix-conditioned 头打分，局部 softmax 归一化；损失为 parent mass 加权的 KL 散度，联合 full-SID 损失训练；辅助头推理时丢弃，保留标准 trie-constrained beam search。
- 每个相关父节点的候选集包含所有相关 children 和至多 32 个高打分合法 siblings，显式做同父竞争。
- 定义 refinement entropy 刻画每层分支不确定性；推理可选加入前缀级 query-catalog 兼容性打分。

关键实验：
- 在 ESCI 的美/西/日三个多语言产品搜索数据上，与匹配的 CaLIR base 及 grouped soft-target、decoder soft-target、sampled-tree 对比。
- AR-only 推理下 RARS 提升 Recall@100：US +1.58、ES +0.71、JP +0.70；NDCG@10 提升 +1.24/+1.22/+0.57。
- 加入 all-level 兼容性打分后，US R@100 39.62 vs base 38.24，NDCG@10 13.00 vs 12.00。
- 增益在 4x256 RQ-VAE、层次 k-means、5x256 等不同 ID 结构，以及 Exact-only 正例定义下均保持。

值得记住的一句话：
把文档相关度投影为 SID 每层前缀上的条件分布，用 parent-mass 加权的 KL 监督共享 query 表示，辅助头训完即弃，只留下更强的 query encoder 和标准自回归检索。
