---
title: 'From Approximation to Emergence: A Theory of Deep Learning'
title_zh: 从近似到涌现：深度学习理论统一框架
authors:
- Zhilin Zhao
affiliations:
- Sun Yat-sen University
arxiv_id: '2607.01311'
url: https://arxiv.org/abs/2607.01311
pdf_url: https://arxiv.org/pdf/2607.01311
published: '2026-07-01'
collected: '2026-07-04'
category: Training
direction: 深度学习理论统一框架
tags:
- deep learning theory
- approximation
- optimization
- generalization
- emergence
- scaling laws
one_liner: 系统梳理深度学习理论，从经典近似、优化、泛化到现代涌现现象，构建统一研究叙事
practical_value: '- 本书为纯理论综述，业务可借鉴点有限。

  - 关于 scaling laws 和 emergence 的理论分析可辅助理解大模型在推荐系统中的行为：随着模型规模和数据量增长，性能可能出现跃升，指导资源投入策略。

  - 泛化与鲁棒性理论可应用于推荐模型的离线评估与线上风险控制，尤其面对分布偏移时。

  - 机制可解释性理论为推荐模型的特征重要性归因、内部行为诊断提供思想框架，有助于提升模型可信度。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**：深度学习已无法用单一数学理论解释，从经典的近似、优化、泛化三要素，到过参数化、生成建模、扩展律、涌现等新现象，亟需一个统一的、证明导向的理论地图。

**方法**：本书不提出新定理，而是以研究叙事的方式整合海量文献。将深度学习理论视为一组部分重叠的解释体系：近似理论研究函数表示效率，优化理论解释非凸训练为何收敛到有效解，泛化理论阐明高容量模型为何不严重过拟合。进而将范畴拓展到鲁棒性、分布偏移、生成模型、Transformer、上下文学习、扩展律、可解释性、对齐和涌现。每个理论都从三个维度审视：它控制什么对象？依赖哪些前提假设？留下哪些未解释的现象？全书通过对比假设与结论，凸显不同理论路径的优势与局限。

**关键结论**：呈现了一份严谨但不完备的深度学习理论现状图谱，强调各理论在揭示真实机制的同时也引入了独特的建模假设，指出当前理论的核心问题正从单一损失面分析转向理解从规模、数据、架构和训练中如何自发生成学习机制。本书无具体实验数字，主要提供结构化理论视角。
