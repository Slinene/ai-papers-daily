---
title: Hölder Policy Optimisation
title_zh: Hölder策略优化：动态调度token聚合的RL训练框架
authors:
- Yuxiang Chen
- Dingli Liang
- Yihang Chen
- Ziqin Gong
- Chenyang Le
- Zhaokai Wang
- Jiachen Zhu
- Lingyu Yang
- Jianghao Lin
- Weinan Zhang
affiliations:
- University College London
- Shanghai Jiao Tong University
- The Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2605.12058'
url: https://arxiv.org/abs/2605.12058
pdf_url: https://arxiv.org/pdf/2605.12058
published: '2026-05-11'
collected: '2026-05-19'
category: Training
direction: LLM强化学习训练 · token聚合优化
tags:
- GRPO
- token-level aggregation
- Hölder mean
- policy optimization
- LLM reasoning
- agentic tasks
one_liner: 通过Hölder均值参数p动态调度，在GRPO中平衡梯度浓度与方差，实现数学推理和智能体任务的SOTA性能
practical_value: '- 动态调度聚合参数p的思路可直接迁移到电商推荐的长序列决策中：早期用较大p放大稀疏但关键的交互信号（如购买、加购），后期降低p控制梯度方差，提升策略收敛稳定性。

  - Hölder均值提供统一的token/动作聚合算子，只需调整一个连续参数即可在“放大关键信号”与“抑制噪声”之间平滑切换，适合推荐系统中不同阶段（探索期vs.稳定期）的需求。

  - 智能体交互任务（如对话式购物助手）中，可借鉴本文的p-annealing策略：保守的线性衰减（如1→-1）可避免过拟合早期噪声，显著提高长程任务成功率。

  - 实现简单，完全在log-space计算，仅需替换GRPO中的聚合步骤为带参数p的Hölder均值，无需额外模型或数据，便于快速实验。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：GRPO通过一组轨迹的组内相对优势进行策略优化，但在将轨迹级优势映射为策略更新时，需将序列内token级概率比聚合成一个标量。现有方法使用固定聚合算子（算术平均p=1，几何平均p→0），这在长程推理任务中暴露出浓度-稳定性的根本性权衡：稠密监督的任务（如MATH）下，算术平均会过度放大微小错误，引发高方差梯度导致训练崩溃；稀疏监督的任务（如AIME）下，几何平均会过度平滑稀有但关键的高值token，抑制“aha时刻”的学习。实证表明，不同任务的最优p差异显著，没有一种静态聚合能普适。

**方法关键点**：
- **HölderPO框架**：用Hölder均值（幂平均）统一token级概率比聚合，ρ_i,p(θ) = (1/|y| Σ r_i,t^p)^{1/p}（p=0时为几何平均）。梯度权重W_i,t ∝ r_i,t^p，p控制权重分布的偏斜方向。
- **理论性质**：证明p ↑ 使权重向最大ratio的token集中，放大稀疏学习信号；p ↓ 紧化梯度方差界。给出方差单调性定理和梯度浓度定理，明确无单个p能同时获得两端优势。
- **动态p-annealing**：提出从初值p_high（如+2）线性衰减至终值p_low（如-2）的调度，早期利用正p放大关键信号，后期利用负p收缩方差，实现了早期激进放大与晚期稳定收敛的无缝衔接。算法在log-space实现，仅需一行代码修改。

**关键结果**：
- 在Qwen2.5-Math-7B上，静态最优p随任务显著偏移：AIME24上p=3达46.7%（超越先前SOTA 43.3%），MATH500上p=-1达85.0%。
- 动态调度（2→-2）在五个数学基准（AIME、AMC、MATH、Minerva、Olympiad）平均Pass@1达54.9%，相对GRPO提升7.2%，超过PMPO等同期聚合方法。
- 扩展到ALFWorld具身智能体任务，使用Qwen2.5-1.5B-Instruct，动态调度（1→-1）平均成功率93.8%，相对GRPO（72.8%）提升28.8%。
- 额外实验验证了调度形状的影响（线性优于幂律），以及对不同基础模型（Qwen3系列）的泛化能力。

**一句话总结**：用一个可动态调节的Hölder参数p，统一并超越了现有固定聚合的GRPO变体，无需增加计算开销即解决了长程推理中的浓度-稳定性悖论。
