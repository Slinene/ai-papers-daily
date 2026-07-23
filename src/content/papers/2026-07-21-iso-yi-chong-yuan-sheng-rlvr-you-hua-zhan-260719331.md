---
title: 'ISO: An RLVR-Native Optimization Stack'
title_zh: ISO：一种原生 RLVR 优化栈
authors:
- Hanqing Zhu
- Wenyan Cong
- Zhizhou Sha
- Sagnik Mukherjee
- Xinyuan Song
- David González-Martínez
- Xiaoxia Wu
- Yuandong Tian
- Shiwei Liu
- David Z. Pan
affiliations:
- The University of Texas at Austin
- UIUC
- Emory University
- Together AI
- Recursive Superintelligence Inc
- ELLIS Institute Tübingen
arxiv_id: '2607.19331'
url: https://arxiv.org/abs/2607.19331
pdf_url: https://arxiv.org/pdf/2607.19331
published: '2026-07-21'
collected: '2026-07-23'
category: Training
direction: RLVR 训练优化 · 等谱优化
tags:
- RLVR
- Isospectral Optimization
- Spectral Inheritance
- Model Merging
- AdamW
- Post-training
one_liner: 发现 RLVR 中的谱继承现象，提出等谱优化框架，固定奇异值只优化奇异框架，加速训练与模型合并。
practical_value: '- **加速 Agent 或推理模型微调**：借鉴 ISO-Optimizer 将权重矩阵 SVD 后固定奇异值谱，仅优化输入/输出奇异框架，可在电商搜索
  Agent 或生成式推荐模型的 RL fine‑tuning 中大幅减少训练步数，快速验证 reward 设计。

  - **无数据模型合并**：ISO-Merger 能将多个共享基模型的专项模型（如分别擅长意图识别、参数抽取的 Agent 模型）合并为一个固定谱模型，无需任何额外数据或梯度更新，直接产出可部署的聚合模型，降低线上迭代成本。

  - **从预训练到 RL 后训练的优化器迁移**：可保留基模型的谱结构，仅将标准优化器（如 AdamW）应用于奇异框架，在推荐系统召回或排序模型的后训练场景中，可能获得更稳定、更快的收敛。

  - **模型压缩或部署**：固定谱意味着模型大部分参数保持静态，可结合低秩更新或量化，适合边缘侧 Agent 或推荐模型的轻量化部署。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：RLVR 虽显著提升语言模型推理能力，但其将奖励反馈转化为权重更新的优化层仍缺乏系统性研究。作者基于先前对模型权重奇异结构的分析，揭示 RLVR 中存在**谱继承**现象：后训练可重用基模型的权重谱，仅通过改变输入/输出奇异框架来习得新行为，且框架的完整适应性对重构学习目标至关重要。

**方法**：将该现象形式化为**等谱优化**框架，固定预训练权重的奇异值谱，仅优化正交框架变量。包含两种互补形式：
- **离线 ISO-Merger**：将多个共享基模型的专项模型（specialists）的框架变化合并为一个固定谱模型，无需任何后合并数据、rollout、梯度更新或蒸馏，即可恢复各专项能力并实现聚合最优。
- **在线 ISO-Optimizer**：将任意标准优化器（如 AdamW、Muon）直接作用于框架变量，保持基谱固定，在推理与代码任务上训练 1.5B–8B 参数模型。

**关键结果**：在 Qwen3-8B-Base 上，标准 AdamW 训练 270 步达到综合准确率 0.495，ISO-AdamW 仅需 100 步即达到相同准确率，210 步时进一步提升至 0.509。贯穿多种规模和任务，ISO-Optimizer 均以更少训练步数匹配或超越常规优化器效果。
