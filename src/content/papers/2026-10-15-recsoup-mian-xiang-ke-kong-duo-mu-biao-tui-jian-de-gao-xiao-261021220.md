---
title: 'RecSoup: Efficient Model Merging Approach for Controllable Multi-Objective
  Recommendation'
title_zh: RecSoup：面向可控多目标推荐的高效模型合并方法
authors:
- Zidong Jia
- Guofu Xie
- Xiao Zhang
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
arxiv_id: '2610.21220'
url: https://arxiv.org/abs/2610.21220
pdf_url: https://arxiv.org/pdf/2610.21220
published: '2026-10-15'
collected: '2026-10-16'
category: RecSys
direction: 多目标推荐 · 模型合并
tags:
- Model Merging
- Controllable Multi-Objective Recommendation
- Pareto Front
- Pruning
- Inference Efficiency
one_liner: RecSoup 通过剪枝消解跨目标干扰并学习偏好到合并系数的映射，实现推理时可控多目标推荐，较参数生成提速 165–228 倍
practical_value: '- 模型合并复用已有目标 specialists：工业推荐系统常有多目标模型（如点击、转化、时长、多样性），可离线训练多个单目标专家后，用剪枝+轻量
  gating 网络做推理时融合，无需重训全量模型，部署成本低；相比 hypernetwork 生成参数，推理延迟降低 165–228×，适合高 QPS 在线服务。

  - 剪枝标准可迁移：将 objective-specific importance 与 cross-objective relevance 结合，用 |τ_i,j
  * mean_{k≠i} τ_k,j| 保留方向冲突但耦合强的参数，避免因符号不同误删关键权重；该思路可复用于多任务模型合并、LoRA 专家合并、多场景参数融合中的冲突消解。

  - 偏好到合并系数用可学习 MLP 而非直接使用偏好向量：业务中多个目标不同尺度/非线性交互时，直接加权效果差；可固定专家参数只更新 gating 网络，用少量样本即可训练，便于在线通过调整
  preference weights 切换业务目标（如大促期间提高转化、日常提高多样性）。

  - 剪枝保留比例 ρ 在 0.9–0.95 时实际保留 40–70% 参数即可，剪枝不一定总是有益：当任务向量干扰弱时可不剪枝；可将其作为超参或根据专家间重叠度决定是否启用，避免过度稀疏化损失目标信号。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：推荐系统需同时优化准确率、多样性、公平性等多个冲突目标，实际场景中目标权重常随用户/系统需求动态变化。可控多目标推荐（CMOR）要求推理时无需重训即可调整权衡，但现有后处理重排受限于候选集，参数生成方法（如 hypernetwork、diffusion）训练推理开销大且优化不稳定。模型合并提供轻量复用的可能，但直接应用面临两大障碍：任务向量不在线性子空间（PCA 显示 PC1 仅解释约 25% 方差），以及跨目标参数干扰。

**方法关键点**：RecSoup 采用两阶段解耦设计。第一阶段剪枝消解干扰：对每个目标的任务向量，计算联合重要性分数 S_ij = β·T_self + (1−β)·T_align，其中 T_self 是参数平方占该任务向量 ℓ2 范数的比例，T_align 是当前参数与其余目标同位置平均更新幅度的绝对值乘积；按分数排序后用动态 norm retention 保留能覆盖 ρ=0.9–0.95 信息量的 top-k 参数（实际保留约 40–70%），得到稀疏任务向量。第二阶段自适应合并：用轻量 gating network f_φ(μ) 将用户偏好向量 μ 映射到 merging coefficients λ，合并参数 θ_merged = θ_base + Σ λ_i τ_i^pruned；仅训练 gating，base 模型和任务向量冻结，用小批量数据近似偏好加权损失。理论证明模型合并不受参数生成映射 Lipschitz 光滑性约束，可完整覆盖 Pareto front；推理时合并复杂度为 O(N·P)，远低于生成式方法的 O(P·H) 或 O(T·P·d)。

**关键结果**：在 MovieLens-1M、Amazon Grocery 和 Toys 三个数据集，SASRec/GRU4Rec/TiSASRec 三种 backbone 上，RecSoup 的 Hypervolume 普遍优于 Soup/TATR 等合并基线，其中 ML-1M SASRec 提升 8.5%、TiSASRec 提升 7.3%；Amazon 上比参数生成方法 HV 高 20–50%，且 controllability 保持 0.89 以上。推理时参数构建延迟：RecSoup 约 0.04ms，hypernetwork 约 7.5–9.4ms，加速 165–228×；diffusion 约 87.79s。扩展到 Accuracy-Fairness 和三目标场景仍保持最优 HV。
