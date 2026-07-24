---
title: Probabilistic Residual Learning for Online Recommendations
title_zh: 即插即用的概率残差学习提升跨域推荐
authors:
- Wenyuan Wang
- Yusong Zhao
- Zihao Xu
- Hengyi Wang
- Qi Xu
- Zhigang Hua
- Yan Xie
- Yi Wang
- Zihao Zhao
- Bo Long
affiliations:
- Rutgers University
- Meta
- University of Copenhagen
- UIUC
arxiv_id: '2607.20863'
url: https://arxiv.org/abs/2607.20863
pdf_url: https://arxiv.org/pdf/2607.20863
published: '2026-07-23'
collected: '2026-07-24'
category: RecSys
direction: 跨域推荐 · 因果去偏 · 用户聚类
tags:
- Probabilistic Residual Learning
- Plug-and-play
- Causal Debiasing
- Cross-domain Recommendation
- Bayesian Deep Learning
- Cold-start
one_liner: 提出即插即用的因果贝叶斯框架PRL，通过概率用户聚类与do-calculus去偏，显著提升基础推荐模型的跨域冷启动性能。
practical_value: '- **即插即用增强现有模型**：PRL 可作为任意深度推荐模型的附加模块，仅学习残差，无需调整原模型，适合在线上系统迭代升级。

  - **残差建模策略**：对基础推荐器的输出残差进行建模与纠正，尤其适用于跨市场扩张、新用户群冷启动等场景，可快速训练轻量纠正子模型。

  - **概率用户聚类与簇特定子模型**：自动发现用户偏好群组，每个簇用独立子模型预测残差，能提升个性化精度，类似将 MoE 思想应用于跨域迁移。

  - **因果去偏缓解曝光/流行度偏差**：通过 do-calculus 边缘化域级混淆因子，降低市场特有偏见，增强跨域泛化；在广告或电商推荐中可用于消除国家或渠道带来的偏差。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
深度推荐系统难以适应无重叠用户/物品的跨域冷启动场景，且常受域特有混淆因子（如曝光、流行度）影响。现有跨域方法多依赖共享用户或物品，无法处理完全分割的市场。PRL 旨在提供一种即插即用的通用提升框架，通过建模基础推荐残差实现跨域适应。

**方法关键点**
- **残差建模**：PRL 固定基础推荐模型，仅学习其预测与真实评分之间的残差 $\tilde{R}_{ij}$。
- **层次贝叶斯生成模型**：假设用户属于 $K$ 个潜在簇，每个簇具有高斯先验；物品表示由内容编码与域混淆因子共同生成；残差评分由用户、物品隐变量和域混淆因子决定。
- **概率聚类**：通过变分推断得到每个用户的簇后验概率，并按最大后验分配簇 ID，对应子模型只使用该簇用户数据训练。
- **因果去偏**：引入域级混淆因子 $\mathbf{s}_m$，在推断时用 do-calculus 对 $\mathbf{s}_m$ 进行边缘化，预测去偏残差。
- **高效更新**：用户和物品隐变量具有封闭形式更新规则，复杂度仅依赖用户有交互的物品数，而非全局物品量。

**关键实验**
在 XMRec（18 国市场跨域冷启动）和 MovieLens（年龄组域）上，PRL 作为 CDL、DLRM、PerK、NCF、LightGCN 的插件进行测试。
- XMRec 上效果显著：以 CDL 为基础，Recall@20 从 0.0143 提升至 0.1091；PerK 从 0.1098 至 0.1635。
- 消融实验证实因果组件关键：去除因果的 PRL 性能均有下降；用户聚类亦带来增益。
- 案例分析显示，PRL 将相机类目推荐的国家偏差比值从 1.75× 降至 1.14×，缓解了市场特有偏好偏差。

**核心要点**
PRL 以残差学习、概率聚类与因果去偏三合一的设计，为跨域推荐提供了无需改动基础模型的稳定增益方案。
