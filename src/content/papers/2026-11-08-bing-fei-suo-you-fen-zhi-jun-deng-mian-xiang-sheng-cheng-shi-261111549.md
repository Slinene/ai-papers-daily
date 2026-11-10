---
title: 'Not All Branches Are Equal: Adaptive Semantic ID Construction for Generative
  Recommendation'
title_zh: 并非所有分支均等：面向生成式推荐的自适应语义ID构建
authors:
- Guy Hadad
- Haggai Roitman
- Bracha Shapira
affiliations:
- Ben-Gurion University of the Negev
arxiv_id: '2611.11549'
url: https://arxiv.org/abs/2611.11549
pdf_url: https://arxiv.org/pdf/2611.11549
published: '2026-11-08'
collected: '2026-11-10'
category: GenRec
direction: 生成式推荐 · 自适应树形Semantic ID
tags:
- Semantic ID
- Generative Recommendation
- Hierarchical Clustering
- Adaptive Branching
- Long-tail
- RQ-VAE
one_liner: 提出AST，将语义ID构造为自适应分支树并引入概率质量约束，在五个Amazon数据集上平均提升13%以上
practical_value: '- 语义ID构建应视为树路径而非独立token：用top-down divisive clustering替代RQ-VAE残差量化，共享前缀直接代表几何邻近，可避免codebook
  collapse和大量无效ID路径，减少beam search浪费，适合电商大规模生成式召回。

  - 在稠密/稀疏区域自适应分支：每节点用silhouette coefficient动态选择K，不再固定codebook size；线上可按局部商品密度分配建模容量，提升长尾品类结构合理性。

  - 加入概率质量约束处理长尾：AST-V1用MILP在KMeans中心固定下重分配，AST-V2用质量加权silhouette和交替优化；电商/广告中可按item交互频率约束分支最小质量ρ，避免稀有前缀训练信号不足。

  - 冷启动接入成本低：新商品沿树greedy nearest-centroid traverse，O(BdL)与catalog规模无关，可快速为新品生成语义ID；但需注意下游模型仍可能未见过该token序列。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
现有生成式推荐把商品表示为语义ID序列，但主流方法（如TIGER使用的RQ-VAE）来自残差量化，假设各层token具有独立语义。作者在Amazon Beauty数据集上的分析显示：共享前缀的item相似度显著更高（1000:0.758, 1100:0.874, 1110:0.920，全局0.554），而仅共享后缀几乎不增加相似度（0111:0.582 vs 1000:0.740）。这说明语义ID本质是树路径，每个token的含义由前缀决定，而非独立属性。固定码本RQ-VAE还会产生codebook collapse和大量无效ID序列（可能超过99.9%），浪费beam search容量。

**方法关键点**
- **Adaptive Silhouette Tree (AST)**：自顶向下分裂聚类生成语义ID。每节点用KMeans划分，分支数K通过在候选区间内最大化silhouette coefficient动态选择，而非固定分支因子；前L=m-1个token为树路径，最后token按item ID在叶子桶内唯一化。
- **结构保证**：前缀集合构成laminar family，共享前缀直接蕴含几何邻近；所有code都被真实item占用，无hallucinated ID序列。
- **约束变体**：AST-V1对KMeans固定中心用MILP重分配，满足每个child至少ρ的最小概率质量；AST-V2将质量信息融入silhouette打分和centroid更新，交替执行MILP分配与mass-weighted mean更新，具备收敛保证。
- **冷启动**：新item沿树greedy nearest-centroid traverse，复杂度O(BdL)，与catalog大小无关。

**关键实验**
在五个Amazon Review数据集（Beauty、Toys、Sports、Health、Home）上，统一使用Qwen3-Embedding-0.6B编码item文本，T5 encoder-decoder作为下游生成式推荐器。对比RQ-VAE、RQ-VAE-L、CRVQAE、Qinco2、RVQ、CoST、RQ-Means、RQ-Means-B、RRS、SEATER等baseline。AST-V2取得平均R@5 4.00、R@10 5.95、N@5 2.67、N@10 3.29，相对最强非AST baseline平均提升12.68%、13.55%、12.66%、13.45%，总体13.08%。AST在head/tail item上均位于Pareto frontier，表现均衡；消融显示去掉mass约束或固定分支会下降，小数据集上更明显；最优语义ID长度为4-5；对embedding backbone更稳健。

**最值得记住的一句话**：语义ID应当被构造成树路径而非独立token，自适应分支+概率质量约束能显著提升生成式推荐性能，并消除无效码本路径带来的解码浪费。
