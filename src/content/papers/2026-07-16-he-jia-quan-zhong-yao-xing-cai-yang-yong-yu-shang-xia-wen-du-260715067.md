---
title: Kernel weighted importance sampling for off-policy evaluation in contextual
  bandits
title_zh: 核加权重要性采样用于上下文赌博机的离线策略评估
authors:
- Joshua Spear
- Matthieu Komorowski
- Rebecca Pope
- Neil J Sebire
- Erica E. M. Moodie
affiliations:
- University College London
- Strive Health Ltd.
- National Institute for Health Research
- Great Ormond Street Hospital
- McGill University
arxiv_id: '2607.15067'
url: https://arxiv.org/abs/2607.15067
pdf_url: https://arxiv.org/pdf/2607.15067
published: '2026-07-16'
collected: '2026-07-17'
category: RecSys
direction: 离线策略评估 · 重要性采样
tags:
- Off-policy evaluation
- importance sampling
- kernel methods
- contextual bandits
- bias-variance trade-off
one_liner: 将核平滑引入加权重要性采样，在行为策略误设时显著提升离线评估的准确性与稳健性
practical_value: '- 当 logging policy 模型因策略更新而失准时，Kernel-WIS 提供更稳健的离线评估，适合推荐/广告系统的频繁策略迭代

  - 核平滑思想可直接嵌入现有重要性采样评估流程：利用用户/物品的特征向量计算局部密度，对重要性权重做归一化，无需额外模型

  - 带宽选择通过交叉验证自动完成，可部署为离线评估流程中的一个超参数调优模块，降低人工成本

  - 连续奖励场景（如点击率预估）需谨慎使用，实验显示 Kernel-WIS 可能劣于 WIS，可考虑使用混合策略或对奖励离散化'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：上下文赌博机离线评估中，普通重要性采样（VIS）方差大而不实用，加权重要性采样（WIS）通过分母归一化控制方差，但依赖全局归一化且行为策略模型易错误指定。需要一种能结合 VIS 的线性（无偏性）与 WIS 的有界性（低方差）的估计器。Kernel-WIS 通过引入状态空间的局部平滑，在行为策略误设时提升评估鲁棒性。

**方法关键点**：
- 先定义 State-WIS：对每个状态单独计算 WIS，实现理想的有界性与状态条件独立，但欠平滑；以 State-WIS 为极限形式（带宽 h→0）
- Kernel-WIS 估计器：`ˆJ = 1/n Σ r_i w_i ( Σ_j k_h(s_i,s_j) w_j / Σ_j k_h(s_i,s_j) )^{-1}`，分母为 E[W|S] 的核回归估计（Nadaraya-Watson），采用 RBF 核
- 渐近一致性证明：在 h→0 且满足 9 条假设下几乎必然收敛至真实期望回报
- 带宽选择：将分母视为对 E[W|S] 的回归问题，用 K 折交叉验证最小化 MSE，利用导数的解析形式（RBF核）做 L-BFGS-B 优化，多初始化避免局部最优

**关键实验**：
- 数据集：10 个多分类公开数据集（optdigits、letter、kropt 等），构造成单动作奖励的 contextual bandit
- 策略：logging 策略用 Gibbs 测度（温度 + 故障动作集控制），evaluation 策略用学习出的 softmax 策略
- 对比基线：VIS、WIS、State-WIS、CLPD VIS
- 行为策略正确时：Kernel-WIS 与 WIS 性能无统计差异，均方误差接近
- 行为策略错误指定时：Kernel-WIS 显著优于 WIS（p<0.05），中位误差降低 20% 以上，尤其在较大数据集（n>1500）效果明显
- 尾部行为：Kernel-WIS 的 75 分位和 100 分位预测更稳定，峰值远低于 VIS 和 CLPD VIS
- 连续奖励敏感性：在 optdigits 的连续奖励版本中，Kernel-WIS 劣于 WIS，说明其对奖励结构敏感

**核心结论**：Kernel-WIS 通过局部核平滑实现了 WIS 的有界性和 VIS 的独立性之间的平衡，在模型误设下显著提升 OPE 的准确性，是一种轻量且有效的稳健评估方法
