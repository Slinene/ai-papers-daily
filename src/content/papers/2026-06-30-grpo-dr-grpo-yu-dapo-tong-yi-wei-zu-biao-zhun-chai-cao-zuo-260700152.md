---
title: 'GRPO, Dr. GRPO, and DAPO Are Three Operations on One Number: The Group-Standard-Deviation
  Identity'
title_zh: GRPO、Dr. GRPO 与 DAPO 统一为组标准差操作
authors:
- Yong Yi Bay
- Kathleen A. Yearick
affiliations:
- University of Illinois at Urbana-Champaign
arxiv_id: '2607.00152'
url: https://arxiv.org/abs/2607.00152
pdf_url: https://arxiv.org/pdf/2607.00152
published: '2026-06-30'
collected: '2026-07-02'
category: Training
direction: GRPO/Dr.GRPO/DAPO 统一于组标准差操作
tags:
- GRPO
- Dr. GRPO
- DAPO
- RLVR
- Reward Standard Deviation
- Group-Size Law
one_liner: 三种 RLVR 训练技巧本质上是对同一量（组奖励标准差）的乘、除、过滤操作，且更新量正好等于该标准差
practical_value: '- 在推荐系统的 RLVR 训练中，若奖励为二元（如点击/未点击），优势归一化（除以组标准差）会改变隐式优化目标：除以标准差趋向
  arcsine 变换，抬高极端难度样本的权重；去掉则回到原始成功率目标。可根据业务目标选择是否保留该操作。

  - 无声组（组内奖励全 0 或全 1）产生零梯度，可借鉴 DAPO 的动态采样：在组 batch 中丢弃 σ=0 的组，避免浪费计算。在广告/搜索的曝光日志中，可预先识别全正或全负的
  batch 并跳过更新。

  - 组大小法则 G ≳ 1/(8ε p(1-p)) 给出给定难度 p 下达到目标梯度保真度所需的样本数。在物品或广告推荐中，不同物品（如冷门物品）的点击率 p
  差异大，可据此动态分配每个 prompt 的采样预算，代替固定 G。

  - 可以直接用组标准差作为每步训练的诊断指标：实时监测 σ 的分布和无声组比例，识别模型在哪些难度区间无有效对比信号，从而调整采样策略或奖励设计。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

## 动机
当前 LLM 推理训练（如 R1 风格）依赖 GRPO，其核心操作是将组内奖励减去均值后再除以组标准差。这一除法常被视为无害的归一化细节，但近期 Dr. GRPO 指出它引入「问题级难度偏差」，并直接去掉除法；DAPO 则过滤掉标准差为零的组。三种方法表面上像是不同的补丁，但缺少一个统一的数学理解，导致训练细节被当作独立技巧流传。

## 方法关键点
- **核心恒等式**：对于二元奖励（正确=1，错误=0），一个 prompt 的 GRPO 参数更新可用确切的有限组形式表达为  
`g = σ (¯s₊ − ¯s₋)`，  
其中 σ = √(k(G−k))/G 是组奖励的标准差，¯s₊ 和 ¯s₋ 分别是正确与错误回复的得分向量均值。更新大小就是组标准差，方向是正确与错误回复的对比。
- **三种方法即三种操作**：GRPO 将优势除以 σ（上升至 arcsine 目标），Dr. GRPO 去掉该除法（保持原始成功率目标），DAPO 丢弃 σ = 0 的组。它们都只作用于同一个标量 σ。
- **组大小法则**：要达到大组梯度的 1−ε 保真度，所需组大小 G ≳ 1/(8ε p(1-p))。难度越极端（p 接近 0 或 1），需要的组越大；p=0.5 时 G=11 即可达 95% 保真度，而 p=0.05 需 G≈69。
- **无声组率**：组内全对或全错的概率为 p^G + (1-p)^G，直接给出了 DAPO 丢弃掉的组比例。

## 关键实验
- **Big‑Math 真实难度分析**：在 215,608 道题目上，GRPO 的标准化操作使极端难度 prompt（解答率 <0.1 或 >0.9）分得的梯度预算从 Dr. GRPO 的 13.9% 升至 24.7%（几乎翻倍）。在常用 G=8 下，无声组比例达 44%，与直接重采样统计仅差两个百分点。
- **受控训练验证**：在 6000 个 Bernoulli‑logit 类 prompt 上运行 150 步，无声组率的预测值与实测值吻合度 R² = 0.999；按难度 bin 的梯度质量与有限 G 闭合形式完全匹配；GRPO 对最困难四分之一 prompt 的最终解答率提升至 0.99，而 Dr. GRPO 仅为 0.88，可视化难度偏差对学习轨迹的影响。

## 核心结论
“组标准差不是归一化分母，而是该 prompt 的学习信号大小。”所有相关的设计选择（除法、丢弃、组大小）都可以从这一量出发统一理解。
