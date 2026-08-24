---
title: 'SPARCL: Spectral Partitioned Analytic Continual Learning'
title_zh: SPARCL：谱分区解析持续学习
authors:
- James Hartley
- Zeropy Surio
- Daniel Whitmore
- Hannah Clarke
- Thomas Reed
affiliations:
- University of Sheffield
arxiv_id: '2608.21307'
url: https://arxiv.org/abs/2608.21307
pdf_url: https://arxiv.org/pdf/2608.21307
published: '2026-08-21'
collected: '2026-08-24'
category: Training
direction: 持续学习 · 谱分解冻结核心子空间
tags:
- Continual Learning
- Analytic Learning
- Spectral Partitioning
- Exemplar-Free
- Class-Incremental Learning
one_liner: 识别解析持续学习中的谱干扰问题，通过冻结高能核心子空间并在残差块上递归最小二乘更新，实现闭环解与旧类 logits 核心贡献不变性
practical_value: '- 在推荐/广告模型的增量更新中，可对特征自相关矩阵做谱分解，冻结高能量方向（对应用户主流兴趣、物品核心属性），仅在残差子空间用递归最小二乘（RLS）更新，减少对旧知识干扰。

  - 用 RLS 闭式解替代梯度下降做在线更新，计算快且无需存储旧样本，适合高吞吐实时场景（如新物品冷启动、新活动不断上线）。

  - 残差随机投影扩展为每个新任务/新产品增加轻量子空间，不干扰核心部分，可作为类似 LoRA 的模块化扩展策略。

  - 注意：本文针对分类任务，推荐系统直接迁移需改造，但“谱分区+冻结核心+残差更新”的架构思想值得借鉴。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：解析持续学习（Analytic Continual Learning）用闭环岭回归替代梯度更新，但仍存在旧类漂移。现有遗忘解释聚焦于梯度覆盖，不适用于精确递归求解。作者指出真正原因是**谱干扰**：所有任务共享逆自相关算子 $(R+\lambda I)^{-1}$，新任务样本加载到旧类主导特征方向时稀释谱，即使不重访旧标签也会扰动旧类 logits。

**方法关键点**：提出 SPARCL，将运行中的自相关矩阵分解为高能核心与残差补集；在核心子空间冻结旧类分类器分量，只在残差块上通过递归最小二乘更新，并可选残差随机投影扩展容量。得到简单闭式更新，并证明旧 logits 核心贡献的不变性保证。

**关键结果数字**：在 CIFAR-100、CUB-200、ImageNet-R、ImageNet-A 上使用冻结 ViT-B/16 协议，SPARCL 大幅缩小经典解析方法与强表示匹配方法（如代表匹配）的差距，并与 Fly-CL 等稀疏特征去相关方法互补。
