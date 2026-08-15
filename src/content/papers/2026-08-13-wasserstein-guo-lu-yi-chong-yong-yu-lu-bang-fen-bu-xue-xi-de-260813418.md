---
title: 'Wasserstein Filtering: A Sample Selection Method for Robust Distribution Learning'
title_zh: Wasserstein 过滤：一种用于鲁棒分布学习的样本选择方法
authors:
- Yikai Xu
- Zhao Chen
- Jian Huang
affiliations:
- The Hong Kong Polytechnic University
- Fudan University
arxiv_id: '2608.13418'
url: https://arxiv.org/abs/2608.13418
pdf_url: https://arxiv.org/pdf/2608.13418
published: '2026-08-13'
collected: '2026-08-15'
category: Other
direction: 鲁棒分布学习与异常检测
tags:
- Wasserstein distance
- sample selection
- outlier detection
- optimal transport
- robust learning
- diffusion models
one_liner: 提出 Wasserstein Filtering，通过最大化子集与污染数据集的 Wasserstein 距离来剔除异常样本，并给出可扩展算法
practical_value: '- 可作为训练数据清洗的通用预处理工具：在用户行为日志、点击数据中常混有 bot 流量或噪声样本，WF 用分布距离直接筛选干净子集，不依赖具体模型，适合在特征工程阶段引入。

  - 边际筛选算法 SinkMarg 计算快，适合大规模推荐/广告日志的初筛；需要更高精度时再用 SinkWF 或 SlicedWF 做联合优化，工程上可以分两级漏斗。

  - 对生成式推荐或创意生成模型：若训练数据含大量低质/异常样本，WF 能先筛出干净数据，再训练 diffusion 等生成模型，缓解模式坍塌或生成质量下降。

  - 异常检测场景中，WF 的“最大化 Wasserstein 距离”思路可迁移到流量反作弊、异常用户识别，作为无监督异常分数的一种新视角。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：现实数据集常被对抗性污染，目标是从含异常样本的数据中恢复干净分布。传统鲁棒估计依赖特定模型假设，本文提出样本选择框架 Wasserstein Filtering (WF)，丢弃可疑样本后用剩余数据的经验测度估计目标分布。

**方法关键点**：核心洞察是选择子集，使其经验分布与完全污染数据经验分布的 Wasserstein 距离最大化，从而优先隔离几何上有影响力的离群点。为降低计算复杂度，作者提出三种算法：边际筛选方案 SinkMarg、基于熵最优传输的联合优化算法 SinkWF、以及基于 sliced Wasserstein 近似的 SlicedWF。理论方面引入 Far Exclusion and Local Projection (FELP) 污染模型，刻画包含远分离离群点和局部不可区分扰动的污染。在该模型下，WF 估计器在协方差有界的分布族上达到 minimax 最优。

**关键结果**：在合成数据、基准异常检测套件以及扩散模型鲁棒生成学习上，WF 作为模型无关的预处理工具，异常检测性能具有竞争力，且在重度污染下为生成建模带来显著下游收益。
