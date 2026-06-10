---
title: 'Trust Functions: Near-Lossless Weak-to-Strong Generalization by Learning When
  to Trust the Weak Teacher'
title_zh: 通过学习何时信任弱教师实现近乎无损的弱到强泛化
authors:
- Arda Uzunoglu
- Alvin Zhang
- Daniel Khashabi
affiliations:
- Johns Hopkins University
arxiv_id: '2606.01000'
url: https://arxiv.org/abs/2606.01000
pdf_url: https://arxiv.org/pdf/2606.01000
published: '2026-05-30'
collected: '2026-06-10'
category: Training
direction: 弱到强泛化 · 数据选择
tags:
- weak-to-strong generalization
- trust functions
- data selection
- LLM supervision
- snowballing chain
one_liner: 提出神经信任函数，从教师内部表示预测弱标签正确性以过滤噪声，实现匹配甚至超越真值训练的弱监督泛化，并可通过迭代链滚雪球式提强。
practical_value: '- **弱标签质量过滤**：当业务中只有弱监督（如用户点击、规则伪标签）时，可训练一个小型神经网络，从强模型的隐层表示预测标签正确性，仅用高信任度样本训练主模型，大幅减少噪声。

  - **隐式课程学习**：信任函数倾向选择简单样本，形成从易到难的自然课程，有助于大模型稳定训练，可直接用于冷启动或样本不均衡场景。

  - **迭代自我提升**：将当前模型作为下一轮的“教师”，用信任函数筛选其输出作为新训练数据，逐步提升模型能力，类似自训练，但过滤机制能防止错误累积，适合在标注稀缺时扩增高质量训练集。

  - **风险控制的数据选择**：提供基于霍夫丁上界的阈值校准方法，只需少量标注数据即可自动确定高纯度子集，避免人工调参，适合自动化数据生产 pipeline。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：当强模型超越人类标注质量时，传统监督假设失效。弱到强泛化旨在用弱教师监督强学生，但弱标签噪声往往导致学生无法逼近真值训练的效果。本文从数据选择角度切入，核心挑战是如何识别出真正可靠的弱标签作为训练信号。

**方法关键点**：
- 提出**信任函数**（trust functions），将弱标签可靠性量化为标量信任分，用于过滤弱监督数据。
- 实现为**神经信任函数（NTF）**：一个轻量残差MLP，输入弱教师最后一层隐状态（对应生成 token 的表示），预测该标签是否正确。训练时仅需有标签的源域数据，部署时在目标域零样本使用，适应分布内偏移。
- 训练流程：弱教师生成弱标签并提取隐状态 → 用标注源域训练NTF → 在未标注目标域用NTF打分并保留高信任样本 → 用该子集训练强学生。
- 迭代**弱到强链**：将训练出的学生作为下一轮教师，反复过滤和训练，实现复合提升。

**实验结果**：
- 在**世界知识**（MCQA，OLMo/Qwen系列）、**定量推理**（数学题，QWEN，AIME评测）、**策略游戏**（国际象棋谜题，Lichess）三个领域，NTF过滤的弱监督训练均达到与真值训练统计无差异甚至超越的性能（恢复率92%~110%+）。
- 信任链在策略游戏上滚动多代后，Qwen3-14B最终性能超过单步弱到强、真值训练和 naive 链基线。
- 机制分析表明：NTF保守地选择低难度样本（隐式课程）、在真值标签不完整时恢复更优走法、并产生更低秩、更一致的梯度更新方向。
