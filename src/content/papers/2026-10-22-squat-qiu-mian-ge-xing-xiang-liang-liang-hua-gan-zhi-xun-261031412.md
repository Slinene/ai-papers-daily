---
title: 'SQuAT: Spherical Lattice Vector Quantization-Aware Training'
title_zh: SQuAT：球面格型向量量化感知训练
authors:
- Sebastian Loeschcke
- Ivan Koryakovskiy
- Tycho F. A. van der Ouderaa
- Riccardo Del Chiaro
- Mart van Baalen
- Paul N. Whatmough
- Markus Nagel
affiliations:
- University of Copenhagen
- Qualcomm AI Research
arxiv_id: '2610.31412'
url: https://arxiv.org/abs/2610.31412
pdf_url: https://arxiv.org/pdf/2610.31412
published: '2026-10-22'
collected: '2026-10-24'
category: Training
direction: LLM量化训练 · 球面格型VQ
tags:
- Quantization
- QAT
- Vector Quantization
- Shape-Gain
- Spherical Optimization
- LLM Compression
one_liner: 提出分离STE的shape-gain向量量化训练，诱导球面优化，实现LLM低比特压缩SOTA
practical_value: '- 在推荐/广告模型的 embedding 表或大权重矩阵压缩中，可借鉴 shape-gain 分解：将权重块拆为方向向量和标量增益，方向用球面码本量化，增益用少量比特（如
  chi 分位标量量化），能在低比特下保留更多角度信息。

  - 分离 STE 设计：在量化训练时对 shape 和 gain 分别使用 STE，而非对整个量化器用联合 STE，可诱导切空间更新，改善低比特收敛，该技巧可迁移至其他
  VQ 或低秩训练场景。

  - 若需对大规模模型做 VQ-QAT，采用分块分配、索引缓存、Triton 融合最近邻搜索，可将训练速度提升一个数量级（12.8×），适合电商场景下亿级参数的在线部署。

  - E8S 球面码本支持分数比特率（如 1.75 bpw），有助于在存储与精度之间找到更细粒度的 Pareto 最优，对资源受限的端侧推荐模型尤其有用。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
低比特 LLM 量化中，向量量化（VQ）尤其格型方法在率失真上优于标量量化，但 VQ-QAT 在大规模模型和长训练上研究不足，且传统 STE 直接作用于整个量化器，忽略了 shape-gain 分解的几何结构。何设计与球面几何对齐的 QAT 规则成为关键。

## 方法关键点
- **Shape-gain 分解**：每个权重块表示为 `w = γ s`，方向 `s` 用 E8 派生的球面码本（E8P12 或提出的 E8S）量化，增益 `γ` 用卡方分位标量量化。
- **分离 STE**：对 shape 和 gain 分别施加 STE（`∂ŝ/∂s ≈ I`, `∂γ̂/∂γ ≈ 1`），而非对整体 `Q(w)` 用联合 STE。这诱导方向参数的切空间更新，结合归一化作为 retraction，形成球面黎曼优化。
- **E8S 码本**：从 E8 格低范数壳枚举、可选子采样匹配分数比特率，支持 1.75/2.0/2.25 等非整数 bpw，解锁标量方法无法达到的 Pareto 最优点。
- **工程优化**：分布式精确最近邻分配，每个 worker 量化不重叠权重块，仅通信离散索引；Triton 融合核、索引缓存，训练时间从 62.5 s/it 降至 4.9 s/it（12.8× 加速）。

## 关键实验
- 数据集与设置：DCLM-Edu，JSD 蒸馏，训练 0.25B–10B tokens；模型包括 LLaMA-3.2-1B/3B、Qwen3-4B、Qwen3-1.7B。
- 对比基线：标准 VQ-QAT（联合 STE）、INT-QAT（SEQ）、QTIP、PV-Tuning 等。
- 主要结果：
  - 2.25 bpw 下，SQUAT 在 WikiText2 困惑度优于 INT-QAT（如 10B tokens 时 LLaMA-3.2-1B 13.74 vs 14.33），MMLU 在 1B tokens 时最高提升 7.9%。
  - 相同量化器和初始化下，SQUAT 相比标准 VQ-QAT GSM8K 最大提升 4.9%。
  - 使用 E8S 码本比 E8P12 在同等比特下更好，验证了球面码本与分离 STE 的协同。

## 核心结论
分离 shape-gain STE 可诱导球面优化，显著改善低比特 VQ-QAT，同时支持分数比特率，为大规模 LLM 压缩提供新方向。
