---
title: 'QuasiMoTTo: Quasi-Monte Carlo Test-Time Scaling'
title_zh: QuasiMoTTo：准蒙特卡洛测试时扩展
authors:
- Michael Y. Li
- Anthony Zhan
- Kanishk Gandhi
- Noah D. Goodman
- Emily B. Fox
affiliations:
- Stanford University
arxiv_id: '2607.01179'
url: https://arxiv.org/abs/2607.01179
pdf_url: https://arxiv.org/pdf/2607.01179
published: '2026-07-01'
collected: '2026-07-02'
category: LLM
direction: QMC 相关采样 · 推理与RL 样本效率
tags:
- Quasi-Monte Carlo
- test-time scaling
- sample efficiency
- GRPO
- pass@k
- arithmetic coding
one_liner: 用准蒙特卡洛相关采样替代独立采样，推理与RL训练中样本效率提升25-50%
practical_value: '- 在推荐排序/agent 推理的 beam search 或并行采样中，可用 lattice QMC 生成更均匀覆盖的候选集，减少冗余生成，维持每条候选的边缘分布不变（即仍是原策略的准确样本），从而在相同成本下提升
  recall 或 pass@k。

  - 在策略梯度训练（如 GRPO）中，通过 QMC 采样提高组内样本多样性，可以降低零方差组的比例，增大有效梯度样本数，加速收敛；可尝试在广告竞价策略或推荐对话策略训练中引入。

  - 算术编码的逆 CDF 采样方法本身实现了低 overhead 的并行生成，可复用到任何需要高效并行生成的场景（如搜索召回时的多条 query 改写）。

  - 对于已有独立采样的系统，QMC 采样是几乎零成本的 drop-in 替换，仅需在 batch 生成前生成均匀随机数并传递给解码器，不改变模型推理逻辑。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
并行独立采样（i.i.d.）常用于 LLM 的测试时扩展和 RL 训练，但独立样本会反复访问相同的高概率区域，造成大量冗余，降低了样本效率。理想情况是让每个样本探索不同解空间，但独立采样难以做到。本文观察到，只要保证每个样本的边缘分布是原语言模型分布，其联合分布可以设计成相关样本，从而在保持准确性的同时提升整体覆盖度。

**方法关键点**
- 提出 QuasiMoTTo，利用 randomized Quasi‑Monte Carlo（QMC）生成在 [0,1] 上均匀但更分散的相关点，再通过算术编码将点映射为语言模型的精确样本。
- 提供三种 QMC 方案：lattice（均匀偏移的网格点）、stratified（分层采样）和 token‑level Sobol 序列，覆盖不同的覆盖度‑自由度权衡。
- 算术编码将序列映射为前缀区间，逆 CDF 采样只需维护一个 0‑1 之间的相对坐标，因此 k 条序列可完全并行解码，无通信开销。
- 针对依赖独立性的 pass@k 估计器，设计了 dyadic bootstrap 估计器，通过子采样恢复无偏估计。

**关键结果**
- 在四个符号推理基准（Countdown, Maze, Sudoku, 1D‑ARC）上，QuasiMoTTo（lattice）比 i.i.d. 采样减少 25–47% 的样本量即可达到相同 pass@k。
- QuasiMoTTo 的 pass@k 几乎触及理论上的 union‑bound 上限，几乎没有给任何保持边缘分布的方法留下改进空间。
- 在 GRPO 强化学习训练中，使用 QMC 采样替代 i.i.d. 采样，可减少约 50% 的训练步数达到相同 pass@1，主要因为 QMC 降低了零方差组的比例，增大了有效学习信号。
- 采样带来的额外开销可忽略不计（仅需一次批量的均匀随机数生成和轻微的逆 CDF 簿记）。

**一句话核心**：用相关样本替代独立样本是零成本提升样本效率的方法。
