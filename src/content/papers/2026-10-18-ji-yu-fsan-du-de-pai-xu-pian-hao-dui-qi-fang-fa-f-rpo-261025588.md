---
title: Divergence based Ranked Preference Alignment for LLMs
title_zh: 基于f散度的排序偏好对齐方法（f-RPO）
authors:
- Rajdeep Haldar
- Yue Xing
- Qifan Song
affiliations:
- Purdue University
- Michigan State University
arxiv_id: '2610.25588'
url: https://arxiv.org/abs/2610.25588
pdf_url: https://arxiv.org/pdf/2610.25588
published: '2026-10-18'
collected: '2026-10-20'
category: LLM
direction: LLM 排序偏好对齐 · f-divergence
tags:
- Ranked Preference
- f-divergence
- LLM Alignment
- DPO
- Preference Optimization
one_liner: 将f-divergence对齐框架扩展到排序偏好，提出f-RPO，在排名恢复和生成质量上优于排序baseline
practical_value: '- 可直接利用**用户点击/转化排序数据**训练LLM对齐策略：f-RPO的目标函数形式简单（TV/RKL变体）：L_TV =
  ½ E[Σ_i ρ_i(−σ(r_i) + Σ_{j>i} q(j|i) σ(r_j))]，用隐式奖励 r=β log(π_θ/π_ref)，无需显式reward
  model，可嵌入现有DPO流程。

  - 构造排序数据时，采用**异质生成器（不同温度/模型）**产生候选，再由reward model打分并过滤低置信度样本（最小相邻margin≥0.5），可显著提升排序监督质量，适合电商场景下用LLM-as-judge批量生成偏好数据。

  - 权重设计ρ_x(i)∝k−i, q_x(j|i)∝j−i 天然满足rank-favored条件，且理论保证排序一致性；这种**高排名更大权重的列表级损失**可直接迁移到学习排序任务。

  - 方法用LoRA微调0.5B-9B小模型即获得明显排序能力提升，适合在广告/推荐轻量级模型上部署，可作为生成式推荐（如Semantic ID排序）的对齐模块。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

## 动机
当前LLM对齐主要基于pairwise偏好数据（DPO等），但排序反馈在一个标注中包含多个响应之间的相对偏好，信息量更大。然而，直接分解排序为pairwise比较会丢失列表结构，且统计上效率低。同时，近期工作将pairwise对齐目标解释为aligned与unaligned分布之间的f-divergence估计（如KTO、BCO、KLDO），理论清晰，但尚未扩展到排序反馈。本文旨在统一这两个视角，提出基于f-divergence的排序偏好优化框架f-RPO。

## 方法关键点
- **分布构造**：对于每个prompt x，给定k个排序响应y^(1)≻...≻y^(k)，定义高排名响应分布D+（aligned）和低排名响应分布D−（unaligned）。具体地，D+按排名靠前响应采样，D−按排名靠后响应采样，权重由ρ_x(i)和q_x(j|i)控制。
- **目标函数**：使用变分f-divergence估计，得到目标 L_f-RPO(θ) = −E[Σ_{i=1}^{k-1} ρ_x(i)( g_f(r_θ,i) − Σ_{j=i+1}^k q_x(j|i) f*(g_f(r_θ,j)) )]，其中r_θ=β log(π_θ/π_ref)是隐式奖励，g_f是canonical link function。选择reverse KL和total variation作为主要变体（见表1）。
- **权重设计**：实验中取ρ_x(i)∝k−i, q_x(j|i)∝j−i，满足rank-favored条件，保证密度比R_x(y)随真实效用单调。
- **理论保证**：定理1证明最优策略为 π_{θ*}(y|x) ∝ π_ref(y|x) exp( g_f^{-1}(f'(R_x(y)))/β )；定理2证明在rank-favored权重及β足够小时，最优策略保持排序一致性。k=2时退化为pairwise divergence-based alignment（Haldar et al. 2025）。

## 关键实验
- **数据集**：从UltraFeedback采样4000个prompts，用5个异质生成器（Qwen/LLaMA不同版本与温度）产生候选，Skywork Reward打分排序，过滤低置信度（相邻reward margin≥0.5），最终2279个高质量排序样本（train 1675/val 235/test 369）。
- **模型与训练**：在Qwen2.5-0.5B/1.5B/7B、Gemma-2-2B、Llama-3.2-3B、Llama-3.1-8B、Gemma-2-9B上使用LoRA（rank 64）微调。
- **对比baseline**：PL-DPO（Plackett-Luce DPO）、Mallows-RCPO、pairwise DPO。
- **主要结果**：f-RPO-TV和f-RPO-RKL在多数模型上获得最大Spearman ρ提升（如在Qwen2.5-1.5B上从base -0.0431提升到0.1538，PL-DPO仅0.0471）；AlpacaEval 2.0 win rate上f-RPO-TV在Qwen1.5B达81.24%，显著优于Mallows-RCPO (58.80%)和PL-DPO (56.50%)；消融表明ranking depth k越大越好，TV和RKL发散度最优。

**最值得记住**：将排序偏好作为aligned/unaligned分布的f-divergence估计，实现了简单、可解释且性能优异的LLM排序对齐，尤其TV和RKL变体在排名恢复和生成质量上均领先。
