---
title: 'From Spectra to Joint Schedules in LLM Pre-training: 3+3(+2) Scaling-Law Regimes'
title_zh: 从谱到联合调度：LLM 预训练中的 3+3(+2) 缩放律机制
authors:
- Yichen Wang
- Fanghui Liu
- Yudong Chen
affiliations:
- University of Wisconsin–Madison
- Shanghai Jiao Tong University
arxiv_id: '2609.40148'
url: https://arxiv.org/abs/2609.40148
pdf_url: https://arxiv.org/pdf/2609.40148
published: '2026-09-30'
collected: '2026-10-01'
category: Training
direction: LLM 预训练缩放律与调度理论
tags:
- Scaling Laws
- Learning Rate Schedule
- Batch Size Schedule
- Random Features
- Intrinsic Time
- LLM Pre-training
one_liner: 用线性随机特征证明功率律由累积谱质量决定，并给出 LR/batch 联合调度下保持、改变或破坏损失缩放律的条件与可迁移代理模型
practical_value: '- 训练大规模推荐/广告/搜索模型时，可把 schedule 坐标改成 intrinsic time T=∑η 与 ratio
  r=B/η，复用 7 参数 surrogate 预测不同 LR/batch schedule 组合的 loss；拟合一条 8-1-1 轨迹后，可 zero-refit
  预测 WSD 等 held-out schedule，适合做训练预算分配与 early stopping。

  - 若记忆核指数 qK≈1（论文在 OpenWebText/FineWeb/peS2o 上均拟合约 1，许多 LLM/大模型可能接近），存在 memory ceiling：后期继续降噪（如增大
  batch 或降低 LR）无法改善最终损失衰减率，应把算力留给前期/中期信号学习，而不是末期降噪。

  - 最优 batch size path 可近似为 r*(u)∝ sqrt((1+T-u)^{-qK}[F(u)+σ^2])，即噪声大且会存留到评估时刻的区间应分配更大
  batch；这给出了 WSD / warmup-stable-decay 在数据或算力预算下的一种可操作调参依据。

  - 若换用 Muon 等非 SGD optimizer，注意等价坐标可能变成 B/η^2 而非 B/η；在不同优化器之间迁移 schedule 时不能用同一套
  intrinsic-time 不变性假设。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：Scaling law 的幂律学习曲线常被当作模型-数据固定属性，但 LR 和 batch size schedule 会改变观察损失。作者把问题拆成两个：底层动力学何时产生功率律响应分量，以及 joint schedule 何时保持、改变或破坏这种功率律。

**方法关键点**：
- 在线性 random features + noisy online SGD 代理模型中，条件于 representation 得到精确 Volterra 方程：forcing term 传播未解决目标误差，memory kernel 传播随机误差注入。
- 核心判据：cumulative weighted spectral mass 的低谱缩放决定 forcing/memory 是否幂律，而不是逐特征值或逐目标系数的坐标幂律；不规则谱或目标也能产生 canonical exponent。
- 在 PLRF λ_j=j^{-2α}, θ_j=j^{-β} 下定义响应坐标 qF=(2α+2β-1)/(2α), qK=2-1/(2α)，得到 3 LM + 3 IM + 2 FB 传播相图；joint schedule 由 intrinsic time T=∑η 和 ratio r=B/η 控制，推导 preserve/change/destroy 边界与 memory ceiling。
- 提出 7 参数 forcing-memory surrogate：L(T)=L∞+A_F(1+T)^{-qF}+∫ [A0+A1(1+u)^{-qF}]/r(u)*(1+cK(T-u))^{-qK}du，可跨 schedule 迁移。

**关键结果**：
- 300M nanoGPT 上，固定 B/η 路径下不同 LR/batch factor 在 intrinsic time 下几乎重合；拟合 8-1-1 后 zero-refit 预测 WSD 轨迹，误差小。
- 三个数据集拟合 qK≈1：OpenWebText 1.017、FineWeb 0.952、peS2o V2 0.995，qF<1，处在 LM/IM 边界；对应 α≈1/2，与 Chinchilla 近 sqrt width 最优一致。
- Muon 轨迹在 B/η^2 下坍塌，说明优化器坐标系不同；资源最优 rate 按相区分，多数 LM/IM 数据最优为 D^{-p/(1+p)}。

最值得记住的一句话：幂律不是模型-数据固有属性，而是由累积低谱质量与 B_t/η_t 路径共同塑造的动态响应。
