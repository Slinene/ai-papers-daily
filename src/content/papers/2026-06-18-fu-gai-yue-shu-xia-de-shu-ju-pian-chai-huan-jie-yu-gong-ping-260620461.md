---
title: Data Bias Mitigation under Coverage Constraints & The Price of Fairness
title_zh: 覆盖约束下的数据偏差缓解与公平代价
authors:
- Bruno Scarone
- Alfredo Viola
- Renée J. Miller
affiliations:
- Khoury College of Computer Sciences, Northeastern University, USA
- Casa de Investigadores Científicos La Comarca, Uruguay
- Cheriton School of Computer Science, University of Waterloo, Canada
arxiv_id: '2606.20461'
url: https://arxiv.org/abs/2606.20461
pdf_url: https://arxiv.org/pdf/2606.20461
published: '2026-06-18'
collected: '2026-06-20'
category: Other
direction: 数据公平性 · 覆盖约束与整数规划
tags:
- data bias
- fairness
- coverage constraints
- integer linear programming
- data efficiency
- intersectionality
one_liner: 在覆盖约束下用整数线性规划优化数据偏差缓解，显式量化公平代价与数据效率的权衡
practical_value: '- 在构建推荐系统的训练数据时，借鉴覆盖约束的思想，强制要求每个用户子群体（如按性别×年龄×消费层级）达到最低样本量，避免长尾群体被模型忽略，提升公平性与整体性能。

  - 使用整数线性规划对数据采样/增补策略进行全局优化，而非启发式重采样，可在数据购买成本或标注预算有限时，获得最优的数据修改方案，支持数据治理决策。

  - 引入“公平代价”的量化概念，在业务中设定可接受的公平性容忍阈值（例如法律合规要求的特定偏差上限），据此计算最小数据修改成本，帮助在成本与公平间制定可解释的权衡。

  - 该方法不依赖特定模型，可与现有分类器或推荐模型解耦，适合作为数据预处理管线的一部分，在电商/广告推荐中先行修正训练数据分布，再训练下游模型。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：机器学习模型对交叉敏感属性（如种族×性别）群体常表现出歧视或性能下降，根源在于缺乏可量化的偏差指标和训练数据中交叉子群体不足。现有缓解方法未显式处理覆盖约束，导致零偏差要求与数据效率冲突。  
**方法**：扩展一个偏差缓解框架，加入覆盖约束，强制各个（交叉）群体在数据中达到最低代表量；为提升数据效率，允许小幅偏差近似误差。核心是将偏差缓解建模为整数线性规划（ILP），在所有可行数据修改策略中寻找最优解，并定义“公平代价”作为公平容忍度的函数，即达到指定偏差水平所需的最小数据修改成本（如数据购买或重标注成本）。  
**结果**：在多个公开数据集上验证，该框架能保持多种分类器的预测精度；覆盖约束不仅改善统计代表性，更是保证下游ML性能的关键。ILP在小规模数据集上可精确求解，并直观展示不同公平容忍度下的成本变化。
