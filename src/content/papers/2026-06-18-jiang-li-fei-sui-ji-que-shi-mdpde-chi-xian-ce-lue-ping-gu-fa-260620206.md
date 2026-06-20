---
title: Off-Policy Evaluation for Missingness-Aware Policies in MDPs with Rewards Missing
  Not at Random
title_zh: 奖励非随机缺失MDP的离线策略评估方法
authors:
- Ziheng Wei
- Annie Qu
- Rui Miao
affiliations:
- Department of Statistics, University of Michigan at Ann Arbor
- Department of Statistics and Applied Probability, University of California at Santa
  Barbara
- Department of Mathematical Sciences, University of Texas at Dallas
arxiv_id: '2606.20206'
url: https://arxiv.org/abs/2606.20206
pdf_url: https://arxiv.org/pdf/2606.20206
published: '2026-06-18'
collected: '2026-06-20'
category: Eval
direction: 离线策略评估 · 缺失非随机奖励
tags:
- Off-Policy Evaluation
- Missing Not At Random
- Fitted Q-Evaluation
- Bridge Function
- MDP
one_liner: 利用未来状态与桥函数识别MNAR奖励，构建缺失感知的FQE式OPE估计量
practical_value: '- 离线评估奖励缺失场景：当用户反馈（点击/转化）稀疏且非随机缺失时，传统OPE有偏，可采用影子变量（未来状态）和桥函数方法纠正选择偏误，提升评估准确性。

  - 利用用户后续行为作为工具变量：在用户路径数据中，后续浏览、停留时长等可作为影子变量，帮助推断缺失的转化奖励，无需依赖不可验证的缺失机制假设。

  - FQE式实现：工程上可基于Fitted Q-Evaluation框架，用神经网络学习Q函数，并集成桥函数通过min-max优化估计，避免显式建模缺失模型和双重采样，适合大规模推荐系统。

  - 支持缺失感知策略评估：新策略可根据历史缺失模式调整动作（例如对不活跃用户增加激励），本方法允许评估此类策略，更贴合实际业务需求。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**：离线强化学习依赖批次数据，但奖励常因记录稀疏或截断而缺失，且缺失机制非随机（MNAR），导致现有基于随机缺失假设的OPE方法产生选择偏误，影响策略评估可靠性。

**方法关键点**：
- 将缺失过程形式化为奖励依赖的倾向模型，利用未来状态作为影子变量，在未建模MNAR机制的前提下识别完整数据的条件期望奖励。
- 引入**桥函数**，建立观测奖励与完整奖励条件期望的映射关系，通过min-max优化估计桥函数，避免显式建模缺失机制和双重采样。
- 基于识别的奖励，提出**Fitted-Q-Evaluation (FQE) 风格估计量**，迭代传播恢复的奖励，并允许目标策略依赖历史缺失指示器，实现缺失感知的策略评估。

**关键结果**：
- 理论上证明了估计量的**一致性**，并给出**有限样本误差界**。
- 在模拟数据和MIMIC-III脓毒症真实数据上，方法在MSE等指标上**显著优于**现有忽略MNAR的基线方法。
