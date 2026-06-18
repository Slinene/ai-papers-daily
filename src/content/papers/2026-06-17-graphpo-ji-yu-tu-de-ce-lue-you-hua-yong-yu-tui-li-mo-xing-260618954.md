---
title: 'GraphPO: Graph-based Policy Optimization for Reasoning Models'
title_zh: GraphPO：基于图的策略优化用于推理模型
authors:
- Yuliang Zhan
- Xinyu Tang
- Jian Li
- Dandan Zheng
- Weilong Chai
- Jingdong Chen
- Jun Zhou
- Ge Wu
- Wenyue Tang
- Hao Sun
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
- Ant Group
arxiv_id: '2606.18954'
url: https://arxiv.org/abs/2606.18954
pdf_url: https://arxiv.org/pdf/2606.18954
published: '2026-06-17'
collected: '2026-06-18'
category: Training
direction: 图结构策略优化 · 推理效率提升
tags:
- GraphPO
- RLVR
- reasoning
- policy optimization
- semantic equivalence
- advantage estimation
one_liner: 将推理路径建模为有向无环图，合并语义等价状态共享后缀，减少冗余探索并提升 RLVR 效率
practical_value: '- **多步推理任务中的冗余剪枝**：在对话式搜索、商品推荐 query 改写等链式推理场景，可将推理步骤表示为有向无环图，当不同中间状态语义等价时（如“想买运动鞋”和“需要跑步装备”），合并为同一节点共享后续路径，减少重复计算和
  token 消耗。

  - **Agent 搜索/交互的策略优化**：在基于 RL 的 Agent 决策（如多轮商品搜索、广告竞价策略）中，用图结构代替树结构，对相似交互路径进行等价类合并，使探索预算聚焦到多样性分支，加速策略收敛。

  - **过程奖励信号的精细化**：借鉴 GraphPO 对节点入边赋效率优势、出边赋正确性优势的设计，可以为中间步骤提供更稳定的局部奖励，替代传统稀疏结果奖励，适用于需要过程监督的生成式推荐模型训练。

  - **降低优势估计方差**：理论及实验表明跨分支合并能降低优势估计方差，在推荐强化学习中同样可对相似用户状态聚类，提升训练稳定性。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有 RLVR 范式独立采样响应，常包含相似中间步骤，导致冗余探索、计算浪费，且稀疏的最终答案奖励难以定位有效步骤。树结构方法虽通过共享前缀和分支比较提供细粒度信号，但分支仍然独立扩展，不同分支到达相似推理状态时无法共享信息，仅做局部比较导致优势估计方差偏高。

**方法**：提出 GraphPO，将 rollout 表示为有向无环图，推理步骤作为边，由推理路径总结出的语义状态作为节点。通过语义等价合并将等价推理路径归入等价类，共享后缀并重分配预算，减少冗余扩展。进一步为入边分配效率优势、为出边分配正确性优势，在得出最终结果的同时提供过程监督信号，提升推理效率。理论分析表明该方法能降低优势估计方差、提高推理效率。

**结果**：在三个不同规模 LLM 上，分别使用推理基准和 Agent 搜索基准测试，GraphPO 在相同 token 预算或响应预算下，一致优于链式 RL 和树搜索基线。
