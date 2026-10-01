---
title: Scaling Laws for Looped Mixture of Experts
title_zh: 循环混合专家模型的联合缩放定律
authors:
- Yanbei Chen
- Anirudh Goyal
- Raghuraman Krishnamoorthi
affiliations:
- Meta AI
arxiv_id: '2609.40316'
url: https://arxiv.org/abs/2609.40316
pdf_url: https://arxiv.org/pdf/2609.40316
published: '2026-09-29'
collected: '2026-10-01'
category: Training
direction: 循环 MoE 联合缩放定律
tags:
- scaling laws
- MoE
- looped transformers
- compute-optimal
- test-time scaling
- LLM efficiency
one_liner: 提出首个联合建模循环深度与 MoE 稀疏度的缩放定律，用于资源约束下最优循环 MoE 设计
practical_value: '- 在推荐/广告场景部署 LLM ranker 或 copy 生成模型时，可借鉴循环 MoE：固定 active 参数下提高 R
  换取 reasoning 能力，稀疏度 E 换取总体知识覆盖；按 latency/显存预算联合调 R 和 E，而不是简单增大 dense 参数。

  - 若有训练 scaling law 拟合能力，可仿照论文用小规模 (Nact,D,E,R) sweep 拟合含稀疏度条件的 Neff(R,m)，预估不同 FLOPs/内存下配置的
  loss，指导模型 ladder 选型；低内存设备优先高 R 低 E，富内存场景优先高 E 低 R。

  - 循环模型天然支持 test-time scaling：同一 checkpoint 只改 R 即可从低算力到高算力平滑提升效果（案例中 R 1→5 提升 Overall
  +10.3），适合推荐系夜间批量生成与在线高 QPS 弹性推理。

  - 工程实现采用 middle-block looping：只循环中间层，前两层和后两层不共享，配合逐层监督可让同一模型在多个 R 下可评测；注意全反向传播计算与
  unroll 参数成正比，可用 early exit 减少无效深循环。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
传统 scaling law 只刻画模型参数 N 和数据 D；MoE 通过稀疏路由在固定 active compute 下扩大总容量，循环 transformer 通过复用权重在固定参数下增加计算深度。两者互补，但已有工作要么只建模 recurrence，要么只建模 MoE sparsity，缺少同时刻画二者交互的统一 law。这导致无法系统回答：每个循环 pass 增加多少有效参数？稀疏度如何提升并维持这种增益？也无法在训练算力、推理算力、权重内存约束下做架构选型。

## 方法关键点
- 提出 Loop Scaling Laws：将标准 Chinchilla loss 中的模型项替换为 recurrence 依赖的有效参数 Neff(R)，并进一步扩展为稀疏度条件形式 Neff(R,m)。
- 核心循环映射为有界形式：Neff(R)=N+κ1·Nloop·(1−e^{-(R-1)/κ2})，每 pass 增益递减、总增益趋于有限渐近值；MoE 版本让 κ1、κ2 变成稀疏度 m=Nact/Ntotal 的函数 κj(m)=κj·m^(-θ)，m 越小越提升且拉长循环增益。
- 最终 MoE loop scaling law：L(Nact,D,R,E,m)=A·(E_hat)^δ·Neff(R,m)^(α+γ·ln E_hat)+B·(E_hat)^ω·D^(β+ζ·ln E_hat)+c，在 R=1、E=1 等边界退化为标准 dense / MoE / looped dense law。
- 实验 sweep 覆盖 Nact∈{0.3,0.6,1.0}B、D∈100–500B、E∈{1,2,4,8,16}、R∈{1,2,3,4,6,8}，采用 middle-block looping。

## 关键实验
- 有界映射在 held-out R=16、E、N、D 上均取得最低 RMSE；例如 held-out R 的 RMSE 从 Linear 0.2847、Power 0.0480、无稀疏条件 bounded 0.0190 降到本文稀疏条件 bounded 0.0100。
- 14 个下游 benchmark 显示：sparsity 可提供约 3× active-parameter 效率，recurrence 在 reasoning 上提供约 2× total-parameter 效率，联合扩展进一步推进前沿。
- 1.5×10^22 FLOPs 匹配算力下，0.3B active/1.3B total 的循环 MoE（R=4–5）在 BBH/GSM8K 上匹敌 0.6B active/2.9B total 的非循环 MoE；同时同一 checkpoint 从 R=1 到 R=5 使 Overall 由 36.6 提升到 46.9（+10.3），实现按需 test-time scaling。

> 最值得记住：循环的有效参数增益是有界的，且这个上界由 MoE 稀疏度决定；联合设计 recurrence 和 sparsity 比单轴扩展更接近参数效率最前沿。
