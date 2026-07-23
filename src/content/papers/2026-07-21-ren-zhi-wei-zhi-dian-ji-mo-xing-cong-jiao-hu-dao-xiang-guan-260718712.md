---
title: 'An Epistemic Position-Based Click Model: From Interactions to Epistemic Distributions
  of Relevance and Bias'
title_zh: 认知位置点击模型：从交互到相关性与偏差的不确定性分布
authors:
- Oscar Rolando Ramirez Milian
- Harrie Oosterhuis
affiliations:
- University of Amsterdam
- Radboud University Nijmegen
arxiv_id: '2607.18712'
url: https://arxiv.org/abs/2607.18712
pdf_url: https://arxiv.org/pdf/2607.18712
published: '2026-07-21'
collected: '2026-07-23'
category: RecSys
direction: 点击模型的不确定性量化
tags:
- click model
- epistemic uncertainty
- position bias
- evidence deep learning
- beta distribution
one_liner: 提出首个证据深度学习点击模型，输出相关性与位置偏差的 Beta 分布以量化认知不确定性
practical_value: '- 在推荐/搜索系统的点击建模中引入认知不确定性，可获得预测置信度，用于在线决策的谨慎探索或保守策略，例如在新物品冷启动时避免过度依赖不可靠的预估。

  - Beta 分布输出可直接用于后续的 bandit 或强化学习算法，天然适配 Thompson Sampling，提升探索效率。

  - 位置偏差校正的不确定性估计可帮助离线评估更稳健，识别不可信的位置效应，避免错误归因。

  - 方法采用证据深度学习，工程上只需在原有点击模型基础上增加输出层并改损失函数，额外计算成本低，易于部署到现有点击率预估模型。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有位置点击模型（PBM）仅给出相关性与偏差的点估计，无法衡量预测的认知不确定性（epistemic uncertainty），导致推荐与搜索系统缺乏对自身预测的置信度判断。

**方法**：首次将证据深度学习（evidential deep learning）引入点击模型，提出 Evidential PBM。模型以物品特征和位置特征为输入，为每个物品-位置对输出相关性与偏差的 Beta 分布参数（α, β），从而刻画点击概率的认知不确定性。为稳定优化，设计了近似与条件化技巧：用二项似然的连续近似缓解数值不稳定，通过条件化数据采样减少梯度方差。

**结果**：在合成与半合成数据上，Evidential PBM 能有效捕获对未见过数据的认知不确定性，其预测分布随数据增多而收缩；标准策略梯度方法则无法学到有意义的分布。该方法为点击建模提供了可解释的不确定性度量，迈出贝叶斯点击模型的关键一步。
