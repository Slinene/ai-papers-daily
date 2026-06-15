---
title: 'Free Heavy-Tailed Lunch for Muon: A Theoretical Justification of Empirical
  Success'
title_zh: Muon优化器的重尾噪声理论：为何非欧几里得方法在训练Transformer时更优
authors:
- Florian Hübler
- Thomas Pethick
- Suvrit Sra
affiliations:
- ETH Zurich
- Technical University of Munich
- Munich Center for Machine Learning
arxiv_id: '2606.14560'
url: https://arxiv.org/abs/2606.14560
pdf_url: https://arxiv.org/pdf/2606.14560
published: '2026-06-12'
collected: '2026-06-15'
category: Training
direction: 优化算法理论 · 非欧几里得优化
tags:
- Muon
- heavy-tailed noise
- non-Euclidean optimization
- sample complexity
- Transformer training
one_liner: 证明Muon在重尾噪声下能以最优样本复杂度达到核范数平稳点，且无需额外维度依赖
practical_value: '- 训练深度推荐模型（如Transformer-based CTR预估）时，可尝试用Muon替换AdamW，尤其适用于大矩阵参数（如Embedding层、注意力投影层）；其更新基于谱范数，可避免维度依赖的样本复杂度膨胀。

  - 在重尾噪声环境下（如点击、转化数据的长尾分布梯度），Muon理论上能稳定收敛，工程上可优先考虑非欧几里得优化器。

  - 文章指出除谱范数外的其他Schatten范数也具竞争力，可启发尝试新正则化或约束（如核范数、Frobenius范数组合）来提升模型训练稳健性。

  - 理论结果提示：优化器的选择需与平稳性度量相匹配；若业务中更关注核范数意义上的收敛，Muon类方法有理论保障，可指导自定义优化器的设计。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：Muon和Scion等基于矩阵范数的非欧几里得优化器在训练Transformer时实验表现强劲，但其理论优势，特别是在重尾随机梯度噪声下的收敛性，一直缺乏清晰解释。

**方法**：作者在非凸重尾设定下（梯度只有bounded p-th矩，p∈(1,2]），分析了归一化最速下降法。核心比较欧几里得方法（如SGD）与基于谱范数的Muon更新。关键洞察：当以核范数衡量平稳性时，Muon的样本复杂度为 O(min{m,n}·ΔL/ε²·(σ/ε)^{p/(p-1)})，不含额外矩阵维度乘积因子；而欧几里得方法会引入√(max(m,n))或更糟的维度依赖。作者进一步证明，该复杂度及其维度依赖性在同类一阶方法中是最优的。

**结果**：理论显示，Muon能有效吸收重尾噪声，避免维度灾难，而欧几里得方法在相同平稳性度量下更差。LLM实验支持理论发现，并意外表明其他Schatten范数（如核范数）几何在某些场景也能取得有竞争力的表现。
