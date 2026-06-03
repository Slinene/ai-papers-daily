---
title: 'Small RL Controller, Large Language Model: RL-Guided Adaptive Sampling for
  Test-Time Scaling'
title_zh: 小RL控制器驱动大语言模型：RL引导的自适应采样实现测试时扩展
authors:
- Runpeng Dai
- Tong Zheng
- Rui Liu
- Chengsong Huang
- Hongtu Zhu
affiliations:
- University of North Carolina at Chapel Hill
- University of Maryland, College Park
- Washington University in St. Louis
arxiv_id: '2606.03102'
url: https://arxiv.org/abs/2606.03102
pdf_url: https://arxiv.org/pdf/2606.03102
published: '2026-06-01'
collected: '2026-06-03'
category: Reasoning
direction: 测试时扩展 · 强化学习自适应采样
tags:
- Test-Time Scaling
- Adaptive Sampling
- Reinforcement Learning
- Self-Consistency
- MDP
one_liner: 将自适应采样建模为MDP，用4层MLP的RL控制器仅依赖答案统计联合优化正确率、延迟与计算量。
practical_value: '- **动态资源分配MDP化**：将推理预算分配形式化为MDP的思路可直接迁移到电商推荐系统的召回、排序阶段，用轻量RL控制器动态决定何时停止多路召回或特征计算，平衡延迟与效果。

  - **仅依赖轻量统计状态**：状态仅需top-K答案计数、总样本数和熵，无需模型内部logits或置信度，部署极简，适合在线服务场景。类似地，在推荐系统中可以仅用候选集统计特征（如多样性、得分分布）做决策。

  - **跨模型泛化能力**：控制器在不同LLM和数据集间可迁移，暗示训练一个通用预算分配器可行。在Agent或多智体场景中，可先基于低成本模型训练协调器，再无损迁移到昂贵模型上使用。

  - **Lagrangian视角提供约束优化理论支撑**：将延迟/计算约束通过拉格朗日对偶显式引入奖励函数，便于在业务中直接设定成本上限并寻优，可启发多目标推荐系统的在线预算控制。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
测试时扩展（如Self-Consistency）可显著提升LLM推理性能，但带来高昂的计算与延迟成本。现有自适应采样方法（如ASC、ESC）要么依赖启发式阈值或分布假设，要么需要模型内部信号（置信度、隐藏状态），且常破坏原有推理流程。亟需一种轻量、无侵入且能显式优化准确率–成本–延迟三元权衡的方法。

**方法关键点**  
- **MDP建模**：将自适应采样定义为有限时域MDP。状态为当前采样池中答案的top-K频率、总数及熵，动作空间{0,1,2,4}，0表示停止并对池内答案进行多数投票，其余表示并行追加指定数量样本。
- **奖励设计**：步级奖励为$–\lambda_{lat} – \lambda_{comp} * a_t$，惩罚额外轮次与样本；终端奖励基于当前多数答案是否与继续采样到最大预算N=32时的多数答案一致（一致+1，否则-1），避免依赖真实标签。
- **控制器**：4层MLP，用PPO训练，离线采样128条回答构造轨迹，仅需CPU训练与部署，完全无侵入。
- **Lagrangian视角**：优化目标等价于在约束期望轮次与样本数下最大化准确率的拉格朗日松弛，为调参提供理论依据。

**关键结果**  
在AIME24、AIME25、HMMT25三个数学推理基准上，使用Qwen3-0.6B/1.7B/4B及GPT-4.1-nano作为采样器。RL-Guided Sampling相比ASC：平均采样轮次减少近3–4倍，总样本数减少约30%，准确率持平；相比ESC：轮次减少约10%，总样本减少约35%，且准确率略高。控制器跨数据集和模型（如从Qwen3-0.6B训练的控制器直接用于GPT-4.1-nano）仍保持显著效率优势。消融实验表明，使用“运行多数票”作为奖励信号优于全量多数或真实标签，后者反而引入噪声导致效果下降。

**一句话核心**  
仅用答案统计的轻量RL控制器即可实现超越启发式方法的自适应采样，无需模型内部信号，且跨模型泛化。
