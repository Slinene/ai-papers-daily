---
title: 'DynMuon: A Dynamic Spectral Shaping View of Muon'
title_zh: DynMuon：动态频谱塑形优化器
authors:
- Fangzhou Wu
- Rikhav Shah
- Sandeep Silwal
- Qiuyi Zhang
affiliations:
- University of Wisconsin–Madison
- MIT
- Elorian AI
arxiv_id: '2605.17109'
url: https://arxiv.org/abs/2605.17109
pdf_url: https://arxiv.org/pdf/2605.17109
published: '2026-05-15'
collected: '2026-05-22'
category: Training
direction: 动态频谱塑形优化 · Muon改进
tags:
- Muon
- Spectral Shaping
- Dynamic Schedule
- LLM Training
- Optimizer
- Newton-Schulz
one_liner: 动态调度Muon类矩阵更新的频谱指数p从正到负，早期聚焦高曲率方向，后期转向平坦方向，实现更优收敛
practical_value: '- **动态频谱调度可迁移**：在训练推荐模型（如CTR预估、Embedding矩阵）的矩阵参数时，可引入类似DynMuon的阶段式频谱调整，前期用高曲率方向加速信号衰减，后期转向平坦方向捕捉剩余信号，避免固定谱变换的次优性。

  - **高效近似实现**：利用Newton–Schulz迭代+二阶泰勒展开近似任意p的UΣ^pV^T更新，额外计算成本仅比Muon增加0.3%~2.5%，可即插即用地嵌入现有AdamW/Muon框架，适合大规模电商模型训练。

  - **噪声感知的调度设计思路**：通过曲率方向上的信号-噪声分解（如本文的mode-wise分析），可诊断训练中各子空间的优化状态，指导自适应调度，例如在Agent多智体协作训练中动态分配参数更新强度。

  - **简单的logistic调度策略**：p从1平滑降至-0.25，仅需两个超参数（τ, w），鲁棒性强，无需在线估计曲率，可直接作为默认配置，为其他动态优化器设计提供参考。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：Muon优化器通过将动量更新矩阵的奇异值替换为1（即polar factor U V^T）在LLM训练中取得显著效果，但这种固定频谱变换是否适用于所有训练阶段？近期工作开始探索更一般的频谱塑形族UΣ^pV^T，但缺乏动态视角。本文研究如何根据训练进展动态调整频谱指数p，以进一步提升优化效果。

**方法关键点**：
1. 将Muon推广到幂律频谱塑形族UΣ^pV^T，提出噪声感知的局部动态模型，将曲率方向上的残差信号与随机梯度噪声分解，揭示p控制信号收缩与噪声放大的模态间权衡。
2. 理论分析指出：早期残差集中于高曲率方向，正p加速其衰减；后期残差转向平坦方向，而平坦方向噪声相对较小，允许使用稍负的p（-0.25左右）加强更新，且不会因负得太猛而放大噪声。
3. 提出DynMuon，用logistic调度p从1平滑降至-0.25；高效实现利用Newton‑Schulz近似Muon更新（A^{-1/2}X_n），再对A^{p/2}做二阶泰勒展开，避免完全SVD，保持与Muon相同的计算复杂度。

**关键实验**：在GPT风格（127M~1.11B）和Qwen风格（171M）模型上，使用FineWeb/FineWeb-Edu数据训练10B或20B tokens，对比Muon、AdamW等。DynMuon在所有规模下验证损失更低，且达到Muon 80%训练步数时的目标损失可提前10.6%~26.5%步数，每步时间仅额外1.003~1.025倍；在多种学习率、数据集上鲁棒，-0.25的p_min表现最优。

**核心结论**：固定p=0并非全局最优；通过简单的正到负p调度，即可在几乎无额外计算开销下显著改善大模型训练，为未来在线自适应频谱调度打开了方向。
