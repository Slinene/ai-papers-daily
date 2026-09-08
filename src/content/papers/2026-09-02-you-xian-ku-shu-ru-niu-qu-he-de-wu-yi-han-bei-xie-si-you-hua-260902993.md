---
title: No-Regret Bayesian Optimization with Finite-Library Input-Warped Kernels
title_zh: 有限库输入扭曲核的无遗憾贝叶斯优化
authors:
- Edvin Ketabati Augustinsson
- Robert A. Bridges
affiliations:
- AI Sweden
arxiv_id: '2609.02993'
url: https://arxiv.org/abs/2609.02993
pdf_url: https://arxiv.org/pdf/2609.02993
published: '2026-09-02'
collected: '2026-09-08'
category: Other
direction: 贝叶斯优化 · 输入扭曲核
tags:
- Bayesian Optimization
- Input Warping
- GP-UCB
- Kernel
- Hyperparameter Optimization
- Multi-Agent System
one_liner: 用有限库光滑输入扭曲自适应 GP-UCB 的核几何，在不牺牲收敛保证下提升黑盒优化样本效率
practical_value: '- 在电商/广告模型的超参调优（如 learning rate、embedding size、正则系数）中，很多参数本质是对数或幂律敏感，手动
  log 缩放经验性强且不完整；可构造包含 identity、log、logit、power transform 的有限扭曲库，让 BO 根据历史观测自动选择扭曲，代替人工缩放。

  - 对搜索/推荐系统的在线实验或仿真实验设计，若目标函数存在局部峰值或置信陷阱，直接使用 GP-UCB 可能过早收敛；FLIWBO-UCB 的输入扭曲库可让其逃逸陷阱，且保留
  no-regret 保证，适合预算极低的黑箱评估场景。

  - 在多智能体系统（如智能客服、广告竞价 Agent 协作）需调节多个维度设计参数且每次评估昂贵时，该方法在 20 维噪声评估下可行，可作为 Agent 系统超参调优的实用
  BO 组件。

  - 工程实现上，扭曲库的选择规则可以是任何历史相关规则（如 UCB 或 EI），这给线上系统留出灵活空间；注意库大小带来的 regret 代价为 √Nε，库不宜过大，可在调优前根据参数先验缩小候选扭曲。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**：GP-BO 在昂贵黑盒优化中依赖核函数编码输入邻近性与目标相似度的几何关系。当原始坐标与该几何不匹配（如对数缩放超参数、局部峰值）时，样本效率大幅下降，但现有 GP-UCB 收敛保证要求固定核。

**方法关键点**：提出 FLIWBO，从有限光滑输入映射库中按任意历史相关规则选择扭曲，实时调整输入几何，同时保留高概率收敛保证。关键假设温和，且显式给出库大小带来的 √Nε 代价。

**结果**：受控诊断显示有限库扭曲能修复人为植入的几何错配；在四个重复基准（扭曲合成目标、置信栅栏陷阱、Fashion-MNIST HPO）中，FLIWBO-UCB 在几何错配下击败原始坐标 GP-UCB，逃过甚至 oracle-warp EI 失败的陷阱，恢复手动 log 缩放大部收益，并在具备匹配 regret 保证的方法中领先；20 维 MAS 设计研究验证了在昂贵噪声评估下的可行性。
