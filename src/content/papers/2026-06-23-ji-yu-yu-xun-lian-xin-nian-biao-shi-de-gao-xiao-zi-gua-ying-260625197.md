---
title: Efficient Adaptive Data Acquisition via Pretrained Belief Representations
title_zh: 基于预训练信念表示的高效自适应数据获取
authors:
- Daolang Huang
- Zhuoyue Huang
- Conor Hassan
- Luigi Acerbi
- Samuel Kaski
- Tom Rainforth
affiliations:
- ELLIS Institute Finland
- Department of Computer Science, Aalto University, Finland
- Department of Computer Science, University of Helsinki, Finland
- Department of Computer Science, University of Manchester, UK
- Department of Statistics, University of Oxford, UK
arxiv_id: '2606.25197'
url: https://arxiv.org/abs/2606.25197
pdf_url: https://arxiv.org/pdf/2606.25197
published: '2026-06-23'
collected: '2026-06-28'
category: Agent
direction: 预训练信念驱动的自适应数据获取策略
tags:
- belief representation
- amortized policy
- Bayesian experimental design
- Bayesian optimization
- active learning
- foundation model
one_liner: 提出POLAR，用预训练模型编码信念状态以解耦表示与策略学习，统一高效地解决贝叶斯实验设计、优化与主动学习
practical_value: '- 在在线推荐、广告搜索中，可将预训练的用户行为序列模型（如Transformers）作为信念状态编码器，仅微调轻量策略头用于bandit/RL决策，避免从零训练。

  - 自动化A/B测试或超参数调优时，可用POLAR实现样本高效的贝叶斯优化，大幅减少实验成本。

  - 主动学习选择标注样本：利用预训练的语境表示作为信念状态，训练策略头快速适应新任务，所需查询数显著减少。

  - 工程上，解耦表示与策略允许复用预训练表征，只需更新策略头，方便增量部署与策略迭代。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**：自适应数据获取（贝叶斯实验设计、贝叶斯优化、主动学习）的传统方法分两类：基于后验的依赖可能失配的代理模型与近似后验，直接策略学习则忽略已有的模型表示，两者都使学习困难。需一种能利用强表示、训练高效的统一框架。

**方法**：核心洞察是最优获取决策仅通过充分信念状态依赖于历史。POLAR框架用预训练的预测基础模型（如Transformer）直接将观察历史编码为信念表示，解耦表示学习与策略学习。在此固定表示之上，仅训练一个任务特定的策略头，不同任务仅需切换效用函数（如实验设计的信息增益、优化的期望提升、主动学习的不确定性），实现跨场景的摊销策略学习。

**结果**：在多个涵盖三种场景的任务上，POLAR不仅超越了当前最先进的摊销方法，所需训练样本量还大幅减少，验证了其高效性、通用性和可扩展性。
