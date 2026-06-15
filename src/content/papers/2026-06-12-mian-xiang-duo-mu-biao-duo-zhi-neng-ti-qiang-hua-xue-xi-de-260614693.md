---
title: Learning Coordinated Preference for Multi-Objective Multi-Agent Reinforcement
  Learning
title_zh: 面向多目标多智能体强化学习的协调偏好学习
authors:
- Pengxin Wang
- Lihao Guo
- Yi Xie
- Bo Liu
- Siyang Cao
- Jingdi Chen
affiliations:
- University of Arizona
arxiv_id: '2606.14693'
url: https://arxiv.org/abs/2606.14693
pdf_url: https://arxiv.org/pdf/2606.14693
published: '2026-06-12'
collected: '2026-06-15'
category: MultiAgent
direction: 多智能体多目标偏好协调学习
tags:
- Multi-Agent RL
- Multi-Objective RL
- Preference Coordination
- CTDE
- Pareto Front
one_liner: 通过让智能体学习协调的个性化偏好向量，实现团队角色分工和帕累托前沿覆盖，提升多目标多智能体协作性能
practical_value: '- 多智能体协作系统可借鉴“个性化偏好分工”思路：不让所有 Agent 共享相同的目标权重，而是为每个 Agent 学习专属的偏好向量，促进角色分化（如一个侧重效率，另一个侧重安全），从而在整体目标上获得协同增益。这在推荐系统的多召回通道、多目标排序模型的协同中值得尝试。

  - 偏好的学习可建模为隐变量协调：使用基于 Dirichlet 分布的随机偏好规划器根据局部观测采样偏好，再输入偏好条件策略执行动作；训练时通过团队优势信号和多样性正则项更新规划器，实现端到端的偏好协调。这一机制可迁移到多
  Agent 推荐或广告竞价场景，让不同 Agent 自适应地关注不同指标。

  - 偏好多样性正则项（最大化 Agent 间偏好分布的 pairwise 距离）可防止所有 Agent 偏好坍缩至相同方向，强制形成互补的分工；在工程上，这类似于在多个策略网络间引入差异化约束，提升整体系统的鲁棒性。

  - 理论分析表明偏好多样性能够为团队目标带来一阶增量改善，这意味着在设计多目标多智能体系统时，可以优先考虑在偏好空间中增加多样性作为廉价的性能提升手段。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**  
多目标多智能体强化学习 (MOMARL) 面临目标间冲突和智能体间冲突交织的难题。以往做法是让所有智能体共享相同的标量化偏好，这会导致智能体在相同维度上竞争，引发行为冲突（如两辆车都抢效率则碰撞，都过度保守则死锁）。本文提出通过协调智能体级的个性化偏好，使不同智能体在共享的帕累托前沿上占据不同区域，形成互补角色，从而改善团队整体收益。

**方法关键点**  
- 将合作 MOMARL 形式化为团队最优均衡问题：寻找一个偏好配置及其诱导的策略均衡，最大化团队标量目标。
- 提出 PCMA 算法，基于 CTDE 框架：每个智能体拥有一个随机偏好规划器（输出 Dirichlet 分布参数并采样偏好向量）和一个偏好条件策略。策略依据局部观测和采样偏好选择动作。
- 训练时，集中式团队 critic 提供稀疏团队优势估计，个体向量 critic 提供多目标引导优势；actor 的优化优势为团队优势与偏好加权个体优势之和。
- 偏好规划器通过最大化团队优势并加入偏好多样性正则项（鼓励智能体间偏好 pairwise 距离）进行更新，避免偏好坍缩。
- 理论推导了团队目标一阶提升可分解为梯度改善项、平均偏好对齐项和多样性增益项，并证明了在偏好缓慢变化时策略可以跟踪局部队列解，支持逐步偏好优化。

**关键结果**  
在 MPE（Spread, Predator-Prey）、SMAC（3m/2s3z/8m）、CrazyRL 无人机任务及 CARLA 交通口场景上，PCMA 在成功率和平均奖励上均优于 MADDPG、IPPO、MAPPO 等固定偏好基线。例如在 Cooperative Spread 中成功率达 1.00（基线最高 0.80），平均奖励 0.89 vs 0.69；在 8m 任务上成功率 0.87 vs 0.80（MAPPO）。消融实验证实了偏好多样性和学习型规划器的必要性。
