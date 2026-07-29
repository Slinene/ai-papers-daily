---
title: Structure-aware Relative Policy Optimization for Ranking
title_zh: 面向排序的结构感知相对策略优化
authors:
- Yiteng Tu
- Weihang Su
- Zitao Su
- Yiqun Liu
- Min Zhang
- Qingyao Ai
affiliations:
- Tsinghua University
- Renmin University of China
arxiv_id: '2607.25268'
url: https://arxiv.org/abs/2607.25268
pdf_url: https://arxiv.org/pdf/2607.25268
published: '2026-07-28'
collected: '2026-07-29'
category: RecSys
direction: 结构感知的排序强化学习
tags:
- RL4Rec
- ListwiseRanking
- PolicyOptimization
- StructureAware
- KendallTau
- CreditAssignment
one_liner: 用 top-weighted Kendall-tau 距离归一化奖励差，使 RL 排序的优势估计偏向高效局部调整
practical_value: '- **将排列距离引入优势估计**：在做搜索/推荐/广告的 RL 重排时，可借鉴使用 top-weighted Kendall-tau
  距离归一化奖励差。这样能鼓励模型通过顶部位置的局部交换提升效果，避免仅凭标量奖励导致过度关注全局重排而破坏已收敛的策略。

  - **Action-level 更新替代序列级更新**：SRPO 在每个位置独立计算概率比和 KL 惩罚，更细粒度。在生成式推荐或列表生成模型中，可将每个位置的输出视为一个动作，直接复用此细粒度更新方式，提升训练稳定性。

  - **低样本环境下的鲁棒学习**：SRPO 在 group size 仅为 2 或 4 时性能即超越 GRPO 等基线，适合在线搜索广告等高延迟、稀疏反馈场景。可用极少量采样列表构建可靠优势，降低采样成本。

  - **tanh 平滑与组内标准化**：将结构归一化偏好除以组内奖励标准差再经 tanh 压缩，能有效抑制离群样本的梯度。这一 trick 可迁移到任何基于组内相对比较的
  RL 优化中（如对话策略、重写策略），提高训练稳定性。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于强化学习的排序方法（如 GRPO）将每个采样到的排列视为原子动作，仅通过标量奖励比较排列优劣，忽视了排列间的结构关系。例如，两个 NDCG 值相同的列表，一个仅靠顶部局部交换获得，另一个通过大幅重排实现。不加区分地给予相同优化信号会导致信用分配失准，甚至引发激进更新，破坏策略稳定性，尤其在有限反馈或复杂 listwise 奖励下影响严重。

### 方法
提出 **SRPO (Structure-aware Relative Policy Optimization)**，核心是利用排列间结构差异重新定义优势函数：
- **结构距离度量**：采用 top-weighted Kendall-tau 距离，对顶部位置的错序给予更高惩罚，捕捉排列的结构差异。
- **结构归一化偏好**：定义 $S_{ij} = \frac{\mathcal{R}(L_i) - \mathcal{R}(L_j)}{d(L_i, L_j) + \epsilon}$，表示单位排列变化带来的奖励提升，从而放大高效局部调整的贡献。
- **对比相对优势**：将 $S_{ij}$ 除以组内奖励标准差后经 $\tanh$ 平滑，再对组内其他样本取均值，得到每个排列的最终优势 $A_i^{RD}$。此设计天然具备方差缩减和离群抑制能力。
- **Action-level 更新**：在 Plackett-Luce 策略下，对排列的每个位置独立计算概率比 $r_\theta(L_{i,t}|X, L_{i,<t})$ 并乘以该优势，同时施加 KL 惩罚，实现细粒度策略更新。

### 关键结果
- **LTR 任务**（Istella、Yahoo、MSLR）：在 NDCG@10 等指标上全面超越 GRPO、PGRank、PPG 等 RL 基线，并在 group size=8 时即超过有监督 LambdaRank。例如，在 Yahoo 数据集上 SRPO 的 NDCG@10 达到 0.7707（GRPO 0.7671）。
- **LLM 重排**（E2Rank）：仅在 SRPO 微调后，域外 BEIR 7 数据集平均 NDCG@10 提升至 0.5286，优于所有基线和原模型（0.5255），显示出更强泛化性。
- **公平性优化**：在优化 exposure fairness 时，SRPO 同时取得最高 fair@10 和 NDCG，实现帕累托改进。
- **消融与分析**：移除位置加权、tanh 或奖励标准差均导致性能显著下降；SRPO 在 group size=2 时已展现优势，对奖励噪声也最为鲁棒。
