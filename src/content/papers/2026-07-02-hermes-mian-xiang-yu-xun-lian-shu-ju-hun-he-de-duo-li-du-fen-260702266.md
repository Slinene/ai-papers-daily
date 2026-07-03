---
title: 'HERMES: A Multi-Granularity Labeling Substrate for Pre-training Data Mixtures'
title_zh: HERMES：面向预训练数据混合的多粒度分层标注基板
authors:
- Ziyun Qiao
- Yue Min
- Ruining Chen
- Yujun Li
affiliations:
- Wizard Quant
- Peking University
- University of Science and Technology of China
arxiv_id: '2607.02266'
url: https://arxiv.org/abs/2607.02266
pdf_url: https://arxiv.org/pdf/2607.02266
published: '2026-07-02'
collected: '2026-07-03'
category: Training
direction: 预训练数据混合 · 多粒度标签
tags:
- Data Mixing
- Pre-training
- Hierarchical Clustering
- Vector Quantization
- Label System
- Granularity Control
one_liner: 提出一种基于残差矢量量化的多粒度数据标注框架，使预训练数据混合从固定标签转变为可重用粒度层次导航。
practical_value: '- 在电商推荐模型训练中，可借鉴 HERMES 的语义嵌入 + 残差矢量量化构建商品或用户行为的多粒度类别体系，替代固定的 taxonomy，实现
  training data mixture 的动态粒度调节。

  - 实验中发现的“粗粒度下等比例覆盖 + 质量前 30% 混合规则有效，细粒度下因候选池收缩而失效”现象，提示在推荐数据采样时需根据当前粒度调整采样策略，避免直接在极细粒度下套用同一种比例规则。

  - 该层次标签基板可复用于推荐模型的预训练、微调或持续训练阶段，作为 data loader 的输入，按不同前缀长度控制样本分布，探索多任务能力 Lift。

  - 工程实现上，3 阶段 RVQ 编码开销可控，可离线一次性为全量数据集标注，后续只需通过前缀截断切换粒度，适合工业级海量数据场景。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：现有预训练数据混合方法将语料划分为固定组别（来源、主题、扁平聚类），这些标签系统仅支持单一语义轴和单一粒度，改变分辨率需重建标签，限制了混合策略的表达能力。
方法：HERMES 提出一种数据衍生的层次化标注基板：先用 Learned Semantic Transform 获得文档嵌入，再通过 3 阶段残差矢量量化（RVQ）编码为从粗到细的离散代码，前缀长度控制粒度，最高可达约 13 万个单元。该基板在粗粒度上与 KMeans 方法性能持平，但其核心价值在于可重用的多粒度层次结构。
结果：在 1B 参数、25B token 预训练实验中，HERMES 展示了固定粒度流程无法观察到的交互：在某一前缀长度下，等比例覆盖与质量前 30% 的混合规则使 16 项任务能力宏观平均提升 +0.0253；当粒度进一步变细、候选池收缩约 5 倍后，同一规则的优势消失。该工作将数据混合设计从选择固定标签集转变为在可复用、数据衍生的粒度层次中导航。
