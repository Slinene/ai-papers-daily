---
title: 'HodgeCover: Higher-Order Topological Coverage Drives Compression of Sparse
  Mixture-of-Experts'
title_zh: HodgeCover：高阶拓扑覆盖驱动稀疏MoE压缩
authors:
- Tao Zhong
- Dongzhe Zheng
- Christine Allen-Blanchette
affiliations:
- Princeton University
arxiv_id: '2605.13997'
url: https://arxiv.org/abs/2605.13997
pdf_url: https://arxiv.org/pdf/2605.13997
published: '2026-05-12'
collected: '2026-05-18'
category: LLM
direction: 稀疏MoE压缩 · 高阶拓扑
tags:
- Mixture-of-Experts
- Model Compression
- Hodge Decomposition
- Simplicial Complex
- Topological Data Analysis
one_liner: 利用Hodge分解暴露MoE专家三元合并障碍，通过覆盖谐和核与临界三角形实现无学习压缩
practical_value: '- 若业务模型包含MoE层（如多任务推荐、多域适配），可直接使用基于KL散度的专家合并障碍构建方法，并通过Hodge分解识别被成对信号掩盖的三元合并风险，避免压缩后精度异常下降。

  - 方法无重训练，适合在线服务模型快速压缩；混合变体（HodgeCover + 权重剪枝）可灵活平衡保留质量与压缩率，提供现实可行的压缩前沿。

  - 拓扑视角可迁移至其他多组件联合决策问题，如推荐中多兴趣路由模块、多Agent协作选择等，考虑高阶交互避免局部最优。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有无学习稀疏MoE压缩基于成对专家兼容性评分（如路由KL散度），但无法检测到三个专家两两兼容却整体不可合并的障碍（见图1三角环）。这导致盲目合并造成的性能下降。

**方法**：将MoE层建模为以专家为顶点的2-复形：边权为成对KL合并障碍，面权为三元联合障碍。对该复形上的边障碍信号进行Hodge分解，提取出独立于成对信号的谐和核分量——这正是成对方法遗漏的障碍。基于此提出HodgeCover：贪婪地选择覆盖谐和核中临界边和三元临界三角形，即优先合并那些成对兼容但三元有潜在障碍的专家组；同时提供混合变体，对幸存专家施加权重剪枝实现更高压缩率。

**结果**：在三个开源稀疏MoE backbone（如Switch Transformer）上，极端专家减量（如保留25%路由质量）时，HodgeCover在纯专家合并轴上达到现有最优水平；在混合压缩轴上，尤其在激进压缩区域，性能领先，并独特地平衡了Hodge四个分量的质量保留。这表明显式建模高阶拓扑障碍改变了哪个压缩器在关键区域取胜。
