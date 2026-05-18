---
title: 'Res$^2$CLIP: Few-Shot Generalist Anomaly Detection with Residual-to-Residual
  Alignment'
title_zh: Res²CLIP：基于残差到残差对齐的少样本通用异常检测
authors:
- Xinyue Liu
- Jianyuan Wang
- Biao Leng
- Shuo Zhang
affiliations:
- Beihang University
- University of Science and Technology Beijing
- Beijing Jiaotong University
arxiv_id: '2605.16171'
url: https://arxiv.org/abs/2605.16171
pdf_url: https://arxiv.org/pdf/2605.16171
published: '2026-05-15'
collected: '2026-05-18'
category: Multimodal
direction: 多模态异常检测 · 残差对齐
tags:
- few-shot anomaly detection
- CLIP
- residual alignment
- vision-language
- cross-category generalization
- multimodal
one_liner: 将多模态对齐完全移入统一残差空间，同时解决跨粒度不匹配与跨类别泛化退化问题
practical_value: '- 对于电商商品的少样本缺陷检测，可直接沿用残差对齐思路：冻结 CLIP 主干，仅在残差空间中学习可训练的文本/视觉提示，避免辅助数据集导致类别偏差，实现对新品类的快速适应。

  - 在跨模态推荐（如文本-图像搜索）中，可借鉴残差空间对齐的设计：让模型关注相对差异而非绝对特征，提升未见品类的泛化能力；可设计对称的残差桥接损失，强化图文匹配的判别性。

  - 微调 CLIP 做下游任务时，将优化约束在残差域可减少灾难性遗忘，保护开集泛化能力；此 trick 可用于商品描述生成、多模态知识图谱构建等需要保持开放世界能力的场景。

  - 方法中的“残差预归一化”和“残差对齐损失”可拆解复用：前端用预归一化抑制正常样本的细粒度差异，后端用均方误对齐让模型聚焦异常偏差，两者结合可提升少样本下的异常区分度。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：现有 CLIP 用于少样本通用异常检测存在两个核心矛盾：1）粗粒度统一文本提示难以匹配细粒度前后景区分，导致跨粒度错配；2）在辅助数据集上微调会破坏 CLIP 的开集泛化能力，引起跨类别退化。

**方法**：提出将多模态对齐完全移入**统一残差空间**，残差表示天然消除正常特征差异与类别偏差，同时解决上述两问题。设计**Res²CLIP**，首个对称连接视觉与文本 CLIP 残差空间的框架，包含三个分支：文本提示分支、视觉提示分支，以及新颖的残差到残差对齐分支。所有可学习优化均约束在残差域内，并通过残差对齐目标迫使模型聚焦相对异常偏差而非类别特定特征。

**关键结果**：在多个异常检测数据集上验证了有效性，方法无需在新类别上重训练即具备强泛化能力。
