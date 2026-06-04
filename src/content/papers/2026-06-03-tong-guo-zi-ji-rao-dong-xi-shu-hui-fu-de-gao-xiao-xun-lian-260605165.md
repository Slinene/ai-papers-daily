---
title: 'STRIDE: Training Data Attribution via Sparse Recovery from Subset Perturbations'
title_zh: 通过子集扰动稀疏恢复的高效训练数据归因
authors:
- Rishit Dagli
- Abir Harrasse
- Luke Zhang
- Florent Draye
- Amirali Abdullah
- Bernhard Schölkopf
- Zhijing Jin
affiliations:
- University of Toronto
- Vector Institute
- Max Planck Institute for Intelligent Systems
- ELLIS Institute
- Thoughtworks
arxiv_id: '2606.05165'
url: https://arxiv.org/abs/2606.05165
pdf_url: https://arxiv.org/pdf/2606.05165
published: '2026-06-03'
collected: '2026-06-04'
category: Training
direction: 训练数据归因 · 稀疏恢复
tags:
- TDA
- sparse recovery
- activation steering
- LLM pretraining
- data attribution
one_liner: 将训练数据归因建模为激活空间的稀疏恢复问题，让轻量 steering operator 模拟数据影响，速度快 13 倍且 SOTA
practical_value: '可作为电商推荐/Agent 系统中追溯预测来源、诊断数据问题的高效工具：

  - 将训练数据影响分析从梯度空间迁移到激活空间，避免反复重训练或全梯度计算，适合在线即时归因需求

  - 利用稀疏恢复选择关键训练样本，可快速定位导致推荐错误或 Agent 决策异常的训练案例，辅助数据清洗与调试

  - 通过预训练 steering operators 实现 “即插即用” 的归因能力，可集成进数据反馈闭环，用于增量数据质量评估与数据选择

  - 方法对模型架构无侵入，仅需提取激活值，可适配各类基于 Transformer 的推荐模型与生成式推荐管道'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：训练数据归因（TDA）能追溯模型预测到具体训练样本，但因果干预需反复重训练，代价巨大；主流的梯度近似方法在处理亿级参数模型时依然昂贵且依赖局部线性假设。

**方法**：STRIDE 转向激活空间，学习一组轻量级 “steering operator”，每个 operator 对应一个训练子集的平均行为偏移。给定测试样本，将 steering operator 施加到模型中间激活上，测量其引起的预测变化，然后将该变化向量建模为所有训练子集影响的稀疏线性组合，通过 LASSO 恢复每个子集的贡献，再向下分解到单个样本。整个过程类似压缩感知，只需训练算子时的数据集划分成本和测试时的一次前向扰动，无需访问梯度或多次重训练。

**结果**：在 LLM 预训练数据归因任务上，STRIDE 的线性数据建模分数（LDS）超过所有强基线，同时速度是此前最优方法的 13 倍以上。作者还展示了 STRIDE 在数据选择、数据污染检测和定性分析中的有效性，能够精准找出对特定生成内容影响最大的训练样本。
