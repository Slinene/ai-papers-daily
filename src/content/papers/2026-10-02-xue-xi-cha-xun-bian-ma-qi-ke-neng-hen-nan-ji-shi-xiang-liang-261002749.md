---
title: Learning Query Encoders Can Be Hard Even When Vector Retrieval Is Geometrically
  Easy
title_zh: 学习查询编码器可能很难，即使向量检索几何上容易
authors:
- Anders Wikum
- Nina Mishra
- Amin Saberi
- Tal Wagner
affiliations:
- Stanford University
- Amazon AWS
- Tel Aviv University
arxiv_id: '2610.02749'
url: https://arxiv.org/abs/2610.02749
pdf_url: https://arxiv.org/pdf/2610.02749
published: '2026-10-02'
collected: '2026-10-05'
category: RecSys
direction: 向量检索 · 查询编码器可学性
tags:
- vector retrieval
- query encoder
- bi-encoder
- statistical query
- recall
- learnability
one_liner: 证明冻结文档索引几何容量充足时，查询编码器学习仍存在统计查询下指数级困难
practical_value: '- 双塔召回（电商/search/推荐）中，上线新 query encoder 前先算冻结 doc index 的 oracle
  recall：用 ground-truth query embedding 或暴力 kNN 可达召回作为上界，定位瓶颈在文档几何还是 query 编码器；若 gap
  很大，优先改进 query 侧训练信号而非替换向量库。

  - 论文证明仅靠聚合统计的 query encoder 学习可能指数级困难，提示实践不能只堆数据/加负样本量；可尝试更细粒度的监督（hard negatives、teacher
  distillation、pairwise/listwise）或引入交互式打分头来辅助单向量召回。

  - 若召回明显低于索引几何容量，可对 query 侧做诊断：线性 probe / 小网络能否逼近最好召回；如果简单模型也差，说明训练目标或分布不匹配，考虑生成合成
  query-doc 对、用 LLM 扩展查询意图。

  - RAG 场景同样适用：先测 frozen corpus 的检索上界，避免把 query encoder 问题误判为文档切分或 embedding 模型问题。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：双塔向量检索中，文档索引和 query encoder 分开训练/使用；过去研究关注 embedding 维度能否表达所有 top-k 答案，但较少考察冻结索引下 query encoder 能否学到接近几何上限的召回。

方法：该工作用冻结文档索引能实现的最大 recall 作为几何容量指标，在多个真实检索 benchmark 上对比单向量 query encoder 的实际召回；并构造一个检索任务，其 query encoder 可由极小的单隐层 ReLU 网络完美表示，但在统计查询（Statistical Query）学习框架下，任何 learner 都需指数多个统计查询才能获得超过随机基线 k/n 的召回优势。

结果：实验显示单向量 query encoder 的检索质量远低于文档索引支持的上限；理论构造给出 query encoder 可学性的计算障碍，说明几何上容易并不等于 query encoder 可学。
