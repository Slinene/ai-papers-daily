---
title: Self-evolving LLM agents with in-distribution Optimization
title_zh: 自进化 LLM 智能体与分布内优化
authors:
- Yudi Zhang
- Meng Fang
- Zhenfang Chen
- Mykola Pechenizkiy
affiliations:
- Eindhoven University of Technology
- University of Liverpool
- MIT-IBM Watson AI Lab
arxiv_id: '2606.07367'
url: https://arxiv.org/abs/2606.07367
pdf_url: https://arxiv.org/pdf/2606.07367
published: '2026-06-05'
collected: '2026-06-08'
category: Agent
direction: LLM Agent 自进化训练 · 离线强化学习
tags:
- self-evolving agents
- process reward
- distribution shift
- offline RL
- IQL
- LLM agents
one_liner: 提出 Q-Evolve，通过混合离线数据的加权 IQL 与 GAE 自动生成过程奖励，结合行为近端策略优化实现 LLM 智能体的稳定自进化
practical_value: '- 在电商客服 / 导购等长程对话 Agent 中，可采用混合离线数据（专家对话 + 自身探索记录）训练价值函数，通过 GAE
  从稀疏成功信号自动生成步骤级奖励，省去人工标注过程标签。

  - 借鉴加权 IQL 技巧：对成功轨迹、更靠近终端步的样本赋予更高权重，能有效稳定稀疏奖励下的价值学习，可迁移至点击率预估延迟转化等类似信用分配问题。

  - 使用行为近端策略优化（BPPO）结合非对称裁剪（对负优势动作允许更大抑制），可在离线数据上安全地优化策略，防止灾难性遗忘和分布偏移，适用于线上策略迭代。

  - 自进化循环模式（收集新经验 → 与专家数据混合 → 重新训练价值网络 → 重新计算奖励 → 更新策略）可应用于推荐系统的用户建模迭代，让模型在有限探索成本下持续提升。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：LLM 智能体在长程交互任务中面临稀疏、延迟的终局奖励，信用分配困难。现有过程奖励模型依赖在线搜索或人工标注，且普遍忽视分布偏移——当策略更新后，过程奖励模型对未见状态 - 动作对的评价可靠性下降，导致训练不稳定甚至退化。因此，亟需一种能在同一分布内自动生成可靠步骤级监督并稳定更新策略的方法。

**方法关键点**：
- **混合离线数据构造**：合并专家演示与智能体自生成轨迹，并利用环境自然语言反馈进行回顾性辅助奖励标注（格式错误、无效动作等），为后续学习提供初始信号。
- **加权隐式 Q 学习（Weighted IQL）** ：在混合数据集上学习分布内价值函数 V 和 Q，通过对成功轨迹、靠近终止步的样本施加更高权重，稳定稀疏奖励下的 Bellman 备份，避免直接最大化分布外动作。
- **过程奖励生成**：利用 GAE 从 V 和原始任务奖励计算标准化优势，作为步骤级过程奖励，无需环境回溯或人工标注，且保持与任务目标一致。
- **分布内策略优化**：采用行为近端策略优化（BPPO），对正优势动作进行受限裁剪以鼓励，对负优势动作采用宽松的下界裁剪（ϵ_low > ϵ_high）以显式抑制有害行为，同时加入 KL 正则化防止策略偏离。
- **自进化闭环**：新策略收集更多交互数据，与专家数据重新混合，再次训练 critic 并重标记奖励，再优化策略，形成政策、价值、数据三者协同进化的迭代过程。

**关键结果**：在 ALFWorld、WebShop、ScienceWorld 三个长程决策环境上，用 Llama-2-7B-Chat 基座，Q-Evolve 平均得分 79.4，超出最强基线 QLASS（74.5，需 600K 环境步数）和 ETO（69.4）。ALFWorld 上仅需 20K 环境步数即大幅领先。在 Qwen2.5-7B-Instruct 上仅 13K 步即超越所有在线 RL 基线（320K 步）。消融实验证实回顾性标注、加权 IQL、GAE、BPPO 均不可或缺。
