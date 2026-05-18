---
title: $φ$-Balancing for Mixture-of-Experts Training
title_zh: ϕ-均衡：面向混合专家训练的凸对偶负载均衡框架
authors:
- Lizhang Chen
- Jonathan Li
- Qi Wang
- Runlong Liao
- Shuozhe Li
- Chen Liang
- Ni Lao
- Qiang Liu
affiliations:
- University of Texas at Austin
- Northwestern University
arxiv_id: '2605.15403'
url: https://arxiv.org/abs/2605.15403
pdf_url: https://arxiv.org/pdf/2605.15403
published: '2026-05-14'
collected: '2026-05-18'
category: Training
direction: MoE 训练 · 负载均衡
tags:
- MoE
- Load Balancing
- Mirror Descent
- Convex Duality
- EMA
- Negative Entropy
one_liner: 利用严格凸势函数与镜面下降，将 MoE 负载均衡从启发式 batch 统计提升为人口级凸优化，仅需 EMA 跟踪路由概率即实现更稳定均衡与专家专业化
practical_value: '- **用 EMA 替代 batch 统计，消除负载均衡偏差**：在电商推荐或 Agent 系统的 MoE 层中，可直接将 ST-MoE
  损失中的 batch 频率 `f_e` 替换为 EMA 路由概率经镜面映射 `∇ϕ(m)` 的加权，实现全局均衡，避免因小批次造成的不均匀分配，对长尾流量和冷启动专家更友好。

  - **负熵势函数是简单有效的默认选择**：实验证明负熵作为 ϕ 在各种规模与粒度下均最优，实现简单（`L_aux = Σ p_e * (log m_e + 1)`），且对
  EMA 衰减率鲁棒（推荐 0.6–0.7），可直接替换现有负载均衡损失而无需额外调参。

  - **促进专家专业化，适配多域推荐**：ϕ-均衡允许路由根据全局分布动态分配专家，使不同专家自然专注于不同商品类目或行为模式，适合电商多场景联合建模（如搜索、推荐、广告），可尝试冻结部分专家实现领域隔离。

  - **工程开销极小，易于集成**：仅需在每个 MoE 层维护一份 EMA 向量并增加一步 `stop_gradient` 的 `∇ϕ` 计算，额外算力可忽略，适合大规模分布式训练，能够无缝融入现有
  DeepSpeed-MoE 等框架。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

**动机**  
现有 MoE 负载均衡方法（如 ST-MoE 的辅助损失 `Σ f_e·p_e`）依赖每批次的离散派遣频率，是启发式且在小批量下存在偏倚，无法真正优化全局（数据集级）均匀分配，容易抑制专家专业化。本文旨在建立一个原则性优化框架，直接最小化路由概率的全局期望分布的凸势函数，实现人口级均衡。

**方法关键点**  
- 定义全局目标：`min_θ ϕ(¯p(θ))`，其中 `¯p = E_x[p(x;θ)]` 为路由概率的总体均值，`ϕ` 严格凸、对称、可微。  
- 利用凸对偶：`ϕ(p) = sup_q ⟨p,q⟩ - ϕ*(q)`，将原问题转化为 min-max 问题 `min_θ max_q E_x[⟨p(x;θ),q⟩] - ϕ*(q)`。  
- 镜面下降求解内层最大化：维护 `p` 的指数移动平均 `m ← (1-η)m + η p_batch`，令对偶变量 `q = ∇ϕ(m)`，最终辅助损失为 `L_aux = ⟨p_batch, q⟩`（对 `q` 使用 stop_gradient）。  
- 此形式直接用软路由概率替代硬频率，避免了离散噪声，且通过 EMA 逼近全局分布，消除了小批量偏差。  
- 多种 `ϕ` 可选（ℓp 范数、负熵等），发现负熵 (`ϕ(m)=Σ m log m`) 实际效果最佳。

**关键实验与结果**  
- 预训练：在 Gemma-MoE 上系统扩展参数量（111M–986M）、专家数（8–128）、粒度（G=2–32），ϕ-均衡始终较 ST-MoE 和 loss-free 基线取得更低验证损失和更小的全局负载违反指标（MaxVioglobal）。  
- 微调：在 DeepSeek-MoE-16B-Chat、V2-Lite、Moonlight-16B-A3B 三个模型上，覆盖 7 个基准（数学、代码、多领域），ϕ-均衡在 80% 以上设置中 accuracy 最高，平均提升 1–3 个百分点，且路由展现出更强的领域专业化（图 6）。  
- 消融：负熵势函数在各任务上表现最优；EMA 跟踪概率与跟踪频率效果相当；EMA 衰减率 η∈[0.6,0.7] 时稳健。

**核心结论**  
以凸对偶与镜面下降为桥梁，可统一多数现有负载均衡方法，将启发式调整提升为人口级优化的通用框架，且实现成本极低，适合大规模 MoE 训练。
