---
title: Variance Reduction for Expectations with Diffusion Teachers
title_zh: 扩散教师模型期望的方差减少
authors:
- Jesse Bettencourt
- Xindi Wu
- Matan Atzmon
- James Lucas
- Jonathan Lorraine
affiliations:
- NVIDIA
- University of Toronto
- Princeton University
arxiv_id: '2605.21489'
url: https://arxiv.org/abs/2605.21489
pdf_url: https://arxiv.org/pdf/2605.21489
published: '2026-05-20'
collected: '2026-05-24'
category: Training
direction: 扩散模型下游任务梯度方差优化
tags:
- Diffusion Models
- Variance Reduction
- Monte Carlo
- Importance Sampling
- Score Distillation
- Text-to-3D
one_liner: CARV通过分层蒙特卡洛估计摊销昂贵前向计算，以2-3倍有效计算倍乘降低下游梯度方差
practical_value: '- 在推荐系统使用扩散模型做内容生成或特征提取时，可采用**廉价噪声重采样摊销昂贵前向计算**的模式：将多次去噪步的共享计算提前完成，仅在最终步或采样时重新采样噪声，大幅降低推理/训练成本。

  - 当目标函数涉及对时间步的期望时，可**借鉴重要性采样+分层逆CDF**，根据梯度方差分布动态调整时间步采样概率，在电商多模态模型（如视频生成）中减少约25%的噪声估计方差。

  - 构建**计算感知的方差核算框架**，显式衡量不同随机源的方差贡献与计算开销，辅助决策哪些组件值得投入更多采样预算——这不限于扩散模型，Agent多步推理中的蒙特卡洛估计同样可应用。

  - 在单步蒸馏等场景，若**梯度方差已非瓶颈**，大幅降低方差未必提升下游指标（如FID），提示业务中应优先诊断瓶颈后再投入方差优化资源。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：预训练扩散模型被广泛用作冻结教师，为文本到3D、单步蒸馏、数据归因等下游管道提供梯度。这些梯度是对噪声水平和噪声样本的蒙特卡洛期望，每次抽样需运行昂贵上游操作（渲染、模拟、编码），因此估计量方差主导了计算成本。现有方差减少方法多针对教师训练本身，下游应用缺乏原则性设计。

**方法**：提出CARV（Compute-Aware Variance Reduction），建立计算感知的方差核算框架，揭示方差主要来源于昂贵上游操作。据此设计**分层蒙特卡洛估计器**：先将昂贵前向计算的结果缓存，然后在其上廉价地重采样扩散噪声，从而摊销计算成本；进一步加入**时间步重要性采样**（根据梯度范数调整分布）和**分层逆CDF构造**（保证均衡覆盖），在不引入偏倚的前提下进一步压减方差。

**结果**：在文本到3D蒸馏和归因任务上，CARV实现**2-3倍有效计算倍乘**（大部分来自摊销重用，约25%来自重要性采样+分层），直接降低等效训练成本。在单步蒸馏中，相同技术将梯度方差降低一个数量级，但下游FID未改善，表明该场景下MC方差已非瓶颈。
