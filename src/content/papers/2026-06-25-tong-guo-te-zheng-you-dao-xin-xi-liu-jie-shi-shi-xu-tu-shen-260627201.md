---
title: Explaining Temporal Graph Neural Networks via Feature-induced Information Flow
title_zh: 通过特征诱导信息流解释时序图神经网络
authors:
- Ping Xiong
- Thomas Schnake
- Klaus-Robert Müller
- Shinichi Nakajima
affiliations:
- Berlin Institute for the Foundations of Learning and Data
- Technical University of Berlin
- RIKEN AIP
- Korea University
- Max Planck Institute for Informatics
arxiv_id: '2606.27201'
url: https://arxiv.org/abs/2606.27201
pdf_url: https://arxiv.org/pdf/2606.27201
published: '2026-06-25'
collected: '2026-06-27'
category: Other
direction: 图神经网络解释 · 时序事件图
tags:
- Temporal Graph Neural Networks
- Explainability
- Normalized Relevance Measure
- Information Flow
- Attribution
- Event-based Graphs
one_liner: 基于归一化相关性度量（NRM）的模块化分解方法，捕获事件驱动变量的全信息流以解释时序图神经网络
practical_value: '- 在电商行为序列建模中，若采用事件驱动图神经网络（如用户点击、购买事件），可借鉴 NRM 框架量化每个历史事件对当前推荐结果的贡献，生成可解释的归因报告。

  - 模块化分解方法使复杂图神经网络的解释可系统构建，适用于多组件协同的推荐模型（如多兴趣提取模块叠加图卷积），可降低工程实现复杂度。

  - 高阶交互分析能力能揭示多个事件（例如浏览、加购、收藏）的联动影响，帮助运营理解用户决策链条，优化推荐策略。

  - 方法强调的归一化机制保证了跨层比较的公平性，可迁移到需要对比不同特征重要度的其他深度学习模型中。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：事件驱动的时序图神经网络（ETGNNs）在社交网络、流行病追踪、推荐等领域效果显著，但可解释性不足。现有方法仅关注从事件嵌入到输出的部分信息流，忽略了通过“事件诱导变量”（如节点状态更新）传递的重要路径，这些变量对捕获长程时间依赖至关重要。亟需一种能分析全部信息流的归因方法。

**方法**：基于归一化相关性度量（NRM）框架，提出一种全信息流归因方法。它显式量化两类信息流：源自事件嵌入的初始流，以及流经事件诱导变量的间接流。通过引入模块化分解，系统构建复杂 ETGNN 架构的相关性结构，支持跨层变量的可比性，并能分析事件间的高阶交互。该方法以更透明的方式分配各组件对预测的贡献。

**结果**：在两个合成数据集（流行病追踪、社会动力学）和一个真实政治事件网络数据集上，定性和定量实验均表明，本方法在解释保真度和人类可理解性上持续优于现有解释方法。尤其在长程依赖场景，它能更准确地捕捉关键事件和间接影响。
