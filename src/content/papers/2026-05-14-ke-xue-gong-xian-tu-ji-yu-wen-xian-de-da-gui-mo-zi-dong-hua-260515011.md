---
title: 'The Scientific Contribution Graph: Automated Literature-based Technological
  Roadmapping at Scale'
title_zh: 科学贡献图：基于文献的大规模自动化技术路线图
authors:
- Peter A. Jansen
affiliations:
- University of Arizona
- Allen Institute for Artificial Intelligence
arxiv_id: '2605.15011'
url: https://arxiv.org/abs/2605.15011
pdf_url: https://arxiv.org/pdf/2605.15011
published: '2026-05-14'
collected: '2026-05-17'
category: Other
direction: 科学发现自动化·前提预测
tags:
- Scientific Contribution Graph
- Technological Roadmapping
- Prerequisite Prediction
- Knowledge Graph
- AI-NLP
- Automated Discovery
one_liner: 构建200万条科学贡献和1250万条先决边的大规模图谱，并提出科学前提预测任务
practical_value: '- **关系抽取与图谱构建自动化**：论文自动从文献抽取贡献并连接先决关系，可迁移到电商商品功能依赖图或产品迭代图谱构建，例如自动识别“某技术A的改进直接依赖于技术B”。

  - **前提预测任务设计**：预测哪些现有能力能促成未来发现，可类比到电商中预测哪些现有商品属性或技术会驱动下一代爆款，辅助选品和研发决策。

  - **时序过滤回测评估**：采用时间分割避免未来信息泄露，严格评估预测性能。在推荐系统中评估模型时，可借鉴这种严格的时间感知验证方法，防止数据穿越。

  - **大规模自动化常识图构建思路**：通过实体链接和句子级关系抽取构建领域知识图谱，可直接复用到电商知识图谱建设（如成分、卖点、适用场景的先决关系）。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：科学贡献很少孤立发展，理解其先决关系对研究进展评估和自动化科学发现至关重要。现有方法仅提供论文级引用或句子级三元组，无法细粒度解析贡献间的依赖。

**方法**：构建了 Scientific Contribution Graph，从23万篇AI/NLP开放论文中自动抽取200万条详细科学贡献，并通过实体链接和关系抽取生成1250万条先决边，形成技术路线图网络。进一步提出科学前提预测任务：给定未来新发现，预测哪些现有技术可能促成它。使用时间过滤回测（严格按时间分割训练/测试）评估，模型表现随技术迭代快速提升，最佳达到 **0.48 MAP**。

**结果**：该资源首次在大规模上实现细粒度技术路线图自动化构建，并验证了前提预测可行性，为科学影响评估和自动化发现系统提供了基础。
