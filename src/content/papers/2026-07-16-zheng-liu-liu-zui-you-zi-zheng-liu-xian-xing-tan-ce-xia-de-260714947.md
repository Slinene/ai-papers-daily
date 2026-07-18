---
title: Optimal Self-Distillation for Rectified Flow via Linear Probing
title_zh: 整流流最优自蒸馏：线性探测下的闭式解与自动正则化校正
authors:
- Saptarshi Roy
- Debepsita Mukherjee
- Pratik Patil
affiliations:
- University of Texas, Austin
arxiv_id: '2607.14947'
url: https://arxiv.org/abs/2607.14947
pdf_url: https://arxiv.org/pdf/2607.14947
published: '2026-07-16'
collected: '2026-07-18'
category: Training
direction: 生成模型自蒸馏优化
tags:
- Self-Distillation
- Rectified Flow
- Linear Probing
- Ridge Regularization
- Generative Models
- Generalized Cross-Validation
one_liner: 提出整流流中通过混合真实与教师速度的自蒸馏可严格改进教师，并给出最优混合系数的闭式解
practical_value: '- 若在生成式推荐（如扩散模型生成 item embedding）中遇到自蒸馏场景，可直接引用闭式最优混合系数，避免网格搜索，降低调参成本。

  - 符号规则（正混合修正欠正则化，负混合修正过正则化）可作为诊断工具：根据教师模型的正则化状态决定合成数据与真实数据的混合方向。

  - 一阶段 GCV 或验证调优方法可集成到训练流程中，自动决定合成/真实数据配比，提升生成样本质量。

  - 理论保证的生成误差下降，对需要严格质量控制的下游业务（如广告创意生成）具有可靠性的参考价值。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：生成模型越来越多依赖自生成信号训练，但可能崩溃或漂移。为探索有保障的自改进，本文研究整流流（RF）中的最优自蒸馏（SD）：给定一个次优教师速度场，学生通过混合真实 RF 速度和教师速度训练，能否稳定提升教师？

方法：考虑线性整流流框架，配合岭正则化与固定插值对，证明了一个精确的仿射路径恒等式，并据此推导出最优混合系数的闭式解。该系数由教师风险沿正则化路径的非平稳性决定，且满足符号规则：当教师欠正则化时混合系数为正，过正则化时为负。同时提出基于广义交叉验证（GCV）或验证集的一次性调优方法，无需对混合权重做网格搜索。

结果：结合 RF 的 Wasserstein 收敛界，从理论上证明了最优 SD 可降低连续时间与有限步下的生成误差中的速度估计项。实验涵盖高斯模型、高斯混合及图像数据，均显示最优 SD 在速度风险、模式恢复和有限步生成质量上优于原始教师和纯蒸馏基线。
