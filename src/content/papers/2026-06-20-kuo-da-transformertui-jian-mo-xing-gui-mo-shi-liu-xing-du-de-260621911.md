---
title: 'The Pitfall of Scaling Up: Uncovering and Mitigating Popularity Bias Amplification
  in Scaling Transformer-based Recommenders'
title_zh: 扩大Transformer推荐模型规模时流行度偏差的放大陷阱及其缓解
authors:
- Weiqin Yang
- Yue Pan
- Chongming Gao
- Sheng Zhou
- Xiang Wang
- Can Wang
- Jiawei Chen
affiliations:
- Zhejiang University
- University of Science and Technology of China
arxiv_id: '2606.21911'
url: https://arxiv.org/abs/2606.21911
pdf_url: https://arxiv.org/pdf/2606.21911
published: '2026-06-20'
collected: '2026-06-23'
category: RecSys
direction: 序列推荐 · 流行度偏差与谱正则化
tags:
- Popularity Bias
- Spectral Collapse
- Transformer
- Sequential Recommendation
- Scaling Laws
- Spectral Regularization
one_liner: 揭示Transformer序列推荐深度缩放导致谱坍缩放大流行度偏差，提出层级谱正则化方法SPRINT实现准确性与公平的双赢。
practical_value: '- 在电商/广告推荐中扩大Transformer深度时，需警惕流行度偏差同步放大，导致长尾物品曝光下降；SPRINT 的注意力和前馈正则化可直接嵌入现有架构，以极小计算成本（~3%训练时间）控制谱范数。

  - 具体实现：对自注意力矩阵的列和施加logsumexp平滑上界，防止少数热门物品垄断注意力权重；对前馈权重用幂迭代估计谱范数并正则化，抑制深度网络中的低秩坍缩。

  - 两个正则项联合可使模型在扩大规模时保持准确率和公平性的帕累托前沿，例如在SASRec++上NDCG@5提升15.7%，Fair-0.8提升7.12%，适合大规模排序系统。

  - 方法对Transformer模块通用，已验证可迁移至生成式推荐（TIGER、LETTER），实现长尾曝光提升，为工业级模型扩展提供了偏差控制方案。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
以缩放定律驱动的大模型时代，推荐系统也开始追求更大的参数量与更深的Transformer架构。然而，本研究发现一个关键陷阱：在序列推荐中，扩大模型深度会同步放大流行度偏差——模型过度推荐热门物品，长尾物品曝光严重受损，甚至削弱整体生态。理解并解决这一偏差放大对于可持续的模型扩展至关重要。

**方法关键点**  
- 根因分析：注意力机制天然赋予热门物品更高的聚合权重，堆叠多层后使预测矩阵的谱范数呈指数增长；前馈投影在梯度下降中更关注主奇异方向，导致谱坍缩（最大奇异值极度主导），而该主成分与物品流行度高度相关，由此放大偏差。
- 提出SPRINT（Scalable Popularity Regularization IN Transformers）：
  - 注意力正则化：约束每层注意力矩阵的最大列和（用logsumexp平滑上界），抑制少数热门物品对注意力聚合的垄断。
  - 前馈正则化：约束每层前馈权重的谱范数（幂迭代高效估计），防止深度堆叠引发的谱爆炸。
- 整体目标：推荐损失 + λ₁·Σ log(注意力列和上界) + λ₂·Σ log(权重谱范数)。可理论证明SPRINT能上界预测矩阵的谱范数，从原理上缓解流行度偏差。

**关键结果**  
- 在ML-1M、Beauty、Toy等6个数据集，基于SASRec++和HSTU双骨干，SPRINT相较最好基线平均提升NDCG/HR@5约15.7%，Fair-0.8（长尾曝光）提升7.12%，并建立了更优的准确-公平帕累托前沿。
- 大规模缩放实验（参数量从0.05M到0.34B，6912倍）证明SPRINT在保持准确率增长的同时，显著改善长尾分布。
- 消融实验与层缩放（2→8层）表明，无正则化时深度增加导致性能饱和或退化，而SPRINT持续提升，且额外训练开销仅约3%。
- 方法可泛化至生成式推荐（TIGER、LETTER），同样取得公平性增益。

**一句话结论**：Transformer推荐系统的深度缩放会因谱坍缩加剧流行度偏差，但通过对注意力和前馈层的针对性谱正则化，可以解锁准确与公平兼得的可持续扩展。
