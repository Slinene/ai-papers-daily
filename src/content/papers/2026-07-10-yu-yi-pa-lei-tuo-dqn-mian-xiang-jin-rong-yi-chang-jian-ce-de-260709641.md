---
title: 'Semantic Pareto-DQN: A Multi-Objective Reinforcement Learning Framework for
  Financial Anomaly Detection'
title_zh: 语义帕累托-DQN：面向金融异常检测的多目标强化学习框架
authors:
- Cláudio Lúcio do Val Lopes
- Lucca Machado da Silva
affiliations:
- A3Data
arxiv_id: '2607.09641'
url: https://arxiv.org/abs/2607.09641
pdf_url: https://arxiv.org/pdf/2607.09641
published: '2026-07-10'
collected: '2026-07-13'
category: Agent
direction: 多目标强化学习 · LLM 语义表示
tags:
- Multi-Objective RL
- LLM
- Pareto Frontier
- Fraud Detection
- Semantic State
- DQN
one_liner: 用 LLM 编码交易描述作状态，多目标解耦效益与摩擦，打破零召回成规
practical_value: '- **将异构特征转化为自然语言叙述并用 LLM 编码**：在电商/推荐系统中，可将用户行为序列、商品属性、上下文信息拼接为简洁的自然语言
  Prompt，通过 LLM 获得鲁棒的通用语义 state embedding，替代手工特征工程，提升多模态信号融合稳定性。

  - **多目标奖励解耦设计**：在推荐场景中（如平衡 CTR、GMV、用户停留时长），采用向量化奖励取代加权求和，每个维度独立反馈，agent 可直接学习不同目标间的权衡，避免标量化带来的目标淹没。实现上可仿照本文
  Pareto-DQN，输出多维 Q 值并通过帕累托前沿动态选择动作。

  - **利用 RL 处理极端类别不平衡**：对于点击、转化等低概率事件，传统分类器容易坍缩到多数类。可借鉴本文的自适应决策理念，用 RL agent 在线决策是否推送/出价，通过奖励信号中显式纳入对少数类的补偿，突破静态模型的
  recall 陷阱。

  - **帕累托前沿导航实现策略热切换**：在线上服务中，根据业务需要（如大促期间更重视 GMV，平时更重视体验）可以实时在帕累托前沿上移动选择不同的策略点，无需重新训练，适合多变的电商运营需求。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：金融异常检测面临极端类别不平衡，传统单目标算法易发生“欺诈坍塌”，仅预测多数类，无法有效平衡拦截异常与控制客户摩擦。现有方法依赖数据重采样，容易失真。

**方法关键点**：
1. **语义状态构造**：将异构交易特征合成为自然语言叙述，利用 LLM 编码，获得尺度不变的鲁棒状态表示，避免手工特征工程。
2. **向量化多目标奖励**：解耦金融效益、运营摩擦、语义发现三个奖励维度，agent 直接优化多维 Q 值函数。
3. **连续帕累托导航**：通过学习连续帕累托前沿，动态调整不同目标之间的权衡，应对误报与漏报的非对称成本。
4. **训练框架**：基于 DQN 扩展，用多目标摩尔帕累托选择动作，无需事先指定标量偏好。

**关键结果**：在 E-Commerce 欺诈和 UCI Credit 数据集上，Semantic Pareto-DQN 成功打破零召回陷阱，相比标量化的基线取得显著更高的少数类召回率，同时在可控的运营摩擦内实现了有效的异常发现。
