---
title: Exposure-Based Reinforcement Learning to Rank
title_zh: 基于曝光的强化学习排序方法
authors:
- Harrie Oosterhuis
- Rolf Jagerman
- Zhen Qin
- Xuanhui Wang
affiliations:
- University of Amsterdam
- Google DeepMind
arxiv_id: '2607.18689'
url: https://arxiv.org/abs/2607.18689
pdf_url: https://arxiv.org/pdf/2607.18689
published: '2026-07-21'
collected: '2026-07-23'
category: RecSys
direction: 强化学习排序 · 曝光分布估计
tags:
- Reinforcement Learning
- Learning to Rank
- Exposure
- Baseline Corrections
- Marginalization
- Auto-Differentiation
one_liner: 通过曝光分布抽象与基线校正，实现能自动微分的RL排序，显著提升收敛速度与稳定性
practical_value: '- 曝光分布抽象：可将任意曝光驱动的损失（DCG、公平性、蒸馏）统一写成关于曝光向量的可微函数，然后利用曝光估计器自动获得梯度，适合电商推荐中多目标优化。

  - 实现即插即用：曝光估计器已集成进JAX/RAX，只需实现`exposure()`函数，后续损失函数不超过三行代码，大幅降低RL排序的工程门槛。

  - 基线校正选择：曝光估计器的基线是文档期望曝光，实验证明它比基于效用或位置轨迹的基线更有效，在少量采样（N≥5）时已显著优于其他方法，适合实时在线学习场景。

  - 边际化降低方差：对每个位置枚举所有文档的放置概率，利用GPU矩阵运算高效实现，比纯采样估计收敛更快且更稳定，可借鉴到其他大规模动作空间的RL任务。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
现有的强化学习排序方法（如PL-Rank）需实现复杂的自定义梯度，难以集成自动微分，且数值不稳定，在32位浮点下出现严重收敛问题，限制了在工业排序系统中的推广。重新设计RL for LTR，目标是利用GPU并行和方差缩减技术，在保持计算效率的同时提升稳定性与易用性。

**方法关键点**  
- **基线校正**：针对不同的梯度估计器，设计了对应的基线函数以降低方差。特别是曝光估计器以文档的期望曝光作为基线，实验表明这一选择最有效。
- **部分边际化**：不再将整个排列视为动作，而是对每个排名位置枚举所有未放置文档的放置概率，利用PL模型的条件softmax直接计算期望奖励。这一过程完全通过矩阵运算在GPU上实现，避免了采样带来的高方差。
- **曝光分布抽象**：提出先行估计文档曝光的分布，再将梯度计算交由下游损失函数通过链式法则完成。这样任何曝光驱动的损失（DCG、公平性指标、蒸馏损失）只需实现为一个关于曝光向量的可微函数，即可自动获得策略梯度，实现了即插即用。
- **自动微分集成**：实现中将曝光估计器封装为一个JAX函数，返回估计曝光的同时利用stop_gradient技巧内置梯度估计逻辑，完全对上层损失透明。

**关键实验**  
在MSLR-Web30k和Istella-S两个LTR基准上，优化NDCG@10，与PL-Rank、标准策略梯度、位置轨迹、边际化-全部等方法全面对比。
- PL-Rank在32位精度下极不稳定，250轮后性能急剧下降，而曝光估计器始终保持稳定。
- 曝光估计器收敛速度最快，所需轮数仅为其他方法的约1/3；在MSLR上N≥25时NDCG@10可达0.4812，显著高于所有基线（p<0.01）。
- 计算时间上，N≤100时曝光估计器与标准RL相当，在GPU上没有额外成本。
- 在优化公平性损失和蒸馏损失时，曝光估计器同样有效且实现更简单。

**最值得记住的一句话**  
将曝光分布作为强化学习与损失函数之间的统一抽象层，可以让排序策略优化像普通深度学习一样简洁可微。
