---
title: 'Compote: Collapse-Resistant Multiple Hypothesis Learning For Sequential Recommendation'
title_zh: COMPOTE：抗坍缩多假设学习的序列推荐
authors:
- Louis Castres Saint Martin
- Clement Calauzenes
- Alain Rakotomamonjy
- Patrick Gallinari
affiliations:
- Criteo AI Lab, Paris, France
- Sorbonne Université, CNRS, ISIR, Paris, France
arxiv_id: '2610.37005'
url: https://arxiv.org/abs/2610.37005
pdf_url: https://arxiv.org/pdf/2610.37005
published: '2026-10-27'
collected: '2026-10-28'
category: RecSys
direction: 多假设序列推荐 · 抗坍缩训练
tags:
- multi-hypothesis learning
- sequential recommendation
- winner-takes-all
- multi-interest
- annealed MCL
- head collapse
one_liner: 用退火 winner-takes-all 训练多假设头防止坍缩，仅凭 item ID 超越生成式与多兴趣基线
practical_value: '- 可直接迁移的训练目标：共享 Transformer 编码器 + 多个独立 MLP 头，用 ℓτ = −τ log Σ_m p_{m,y}^{1/τ}
  训练；从高温均匀更新退火到低温 winner-takes-all，能稳定地让多头按商品类目/意图区域分化，替代依赖路由或多样性正则的多兴趣建模。

  - 推理侧用 max-similarity 聚合 cosine 分数即可，无需 catalogue-wide softmax 归一化；论文验证各头 logZ 方差很小，因此可直接接入向量数据库/ANN
  检索，适合电商大目录低延迟召回。

  - 诊断多头是否坍缩：记录测试集上各头输出方向的平均 pairwise cosine similarity；若接近 1.00，说明架构或路由没用，先换退火 WTA
  目标，而不是继续加容量或加 MoE。

  - 做消融时用等容量单头模型、等权 ensemble、routing/MoE 三个对照，可干净地归因多假设目标本身；电商场景中用户短会话天然多意图，多假设头比单头更能覆盖候选意图。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
下一项预测本质上是模糊的：同一交互历史往往对应多个分布在目录不同区域的合理后续物品。常规序列推荐用一个查询向量压缩这些可能意图，导致预测落在多个模态之间；现有多兴趣方法虽然引入 WTA 训练，但通常绑定路由架构，且没有刻画最优解与聚合方式，容易出现所有兴趣头坍缩到同一方向。

**方法关键点**
- 架构：共享 causal Transformer 编码 item-id 历史，最后一个位置的表示 z 同时输入 M 个假设头 h_m(z)∈R^d 和一个置信度头；每个头输出目录分布 f_{m,i}=softmax(cos(h_m,e_i)/β)。
- 训练目标：ℓτ(y,p)=−τ log Σ_m p_{m,y}^{1/τ}。τ 大时所有头均匀更新，τ→0 时收敛到 min_m −log p_{m,y}，即 winner-takes-all；等价于带熵正则和 stop-gradient 的 annealed MCL。
- 推理聚合：max-pooling ω(p)=max_m p_{m,i}；实际可直接对 cosine 分数做 max-similarity 排序，去掉每个头的 catalog softmax 归一化，使其兼容向量数据库与 ANN 检索。
- 理论结果：最优假设按最大熵原则划分条件 next-item 分布；pooled scores 除饱和平局外保持 Bayes 排序；泛化界随假设数 M 只按 O(√(log M/n)) 增长。

**关键实验**
在 Amazon Reviews 2023 三个子集（Musical Instruments、Industrial & Scientific、Video Games）上做 5-core 过滤和 leave-one-out 评估，全目录排序计算 H@K/N@K。COMPOTE 在 12 个指标中 11 个最优；对比最强的 TIGER，N@5 在 Scientific 和 Game 上分别提升 9.7% 和 9.6%，且 COMPOTE 只用 item ID，无需文本和 beam search。等容量消融显示：单头 Iso-parameter、ensemble CE、routing/MoE 均落后；这些退化变体在测试集上头部 cosine 相似度 S=1.00，而 COMPOTE 为 0.58–0.64。Oracle 选择正确头后，N@5 可提升 53%–94%，证明多头产生了互补排序而非简单集成。

**最值得记住的一句话**
多头的收益来自退火 winner-takes-all 训练目标，而不是模型容量、ensembling 或 MoE 路由；先解决 head collapse，再用 max-similarity 做无归一化检索。
