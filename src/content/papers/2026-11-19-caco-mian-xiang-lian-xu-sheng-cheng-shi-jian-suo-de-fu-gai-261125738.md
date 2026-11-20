---
title: 'CACO: Coverage-Aware Coordinated Optimization for Continuous Generative Retrieval'
title_zh: CACO：面向连续生成式检索的覆盖感知协同优化
authors:
- Pan Zhang
- Nan Zhuang
- Yongkang Zhang
- Kun Xú
- Zhongtao Jiang
- Zhiwei Wang
- Kun Xǔ
- Youhuan Li
affiliations:
- Hunan University
- Peking University
- Huazhong Agricultural University
arxiv_id: '2611.25738'
url: https://arxiv.org/abs/2611.25738
pdf_url: https://arxiv.org/pdf/2611.25738
published: '2026-11-19'
collected: '2026-11-20'
category: GenRec
direction: 生成式检索 · 多查询覆盖优化
tags:
- continuous generative retrieval
- flow matching
- multi-query retrieval
- coverage optimization
- self-supervised post-training
- recommender systems
one_liner: 在固定召回预算下协同调整多查询，以频率加权覆盖目标提升互补召回并大幅降低重复率
practical_value: '- 如果业务里已有多向量/多 query 召回，可以直接在冻结的 flow matching 或 diffusion 生成器后挂一个轻量
  adjustment network（cross-attn + query 间双向 attention + 相对方向 gate），不增大 L×K，推理延迟只加
  0.5%–3%，但重复率可下降 53%–65%。

  - 没有完整 relevance 标注时，可用「reference query pool 的 ANN 检索频率」作为 label-free 相关性代理：item
  权重 w_h(v)=c_h(v)^α，目标函数对每个唯一 item 只计一次；α 选择看 backbone 重叠程度，高重叠用小 α（0–0.5），低重叠用 α=1。

  - 面对不可微 ANN top-K 检索，可以用 tangential antithetic perturbation + 单 query 反事实替换构造边际覆盖增益，得到
  Gaussian-smoothed coverage 的无偏梯度；训练时只需 2L 次检索，适合作为黑盒召回指标的轻量优化手段。

  - 如果要先验证目标函数是否合理，可以先离线对 reference queries 做 greedy marginal gain 选择；论文显示该贪心选择在 30
  个 backbone–dataset 设置上都能提升 recall，可作为上线前便宜验证。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
连续生成式检索会为同一用户采样 L 个 query 做 ANN，预算固定为 L×K。现有方法要么独立采样、要么只做兴趣/分布多样性，忽略集合级覆盖：多个 query 可能反复命中同一批 item，浪费召回位。更麻烦的是直接观察到的正样本只能提供部分监督，盲目扩覆盖会引入无关 item；同时 ANN 离散检索不可微，无法直接端到端优化覆盖指标。

**方法关键点**
- **频率加权覆盖目标**：从冻结 backbone 采样 M 个 reference queries，统计每个 item 被检索到的次数 c_h(v)，权重 w_h(v)=c_h(v)^α，目标 F_h(Q)=Σ_{v∈U_K(Q)} w_h(v)，即每个唯一 item 只计一次。Offline greedy 选择验证该目标在所有 30 个 backbone–dataset 设置上都能提升 recall。
- **协同 query 调整网络**：冻结生成器输出初始 queries 和 history hidden states；N 层 cross-attn 接入用户历史，query 间双向 self-attn 建模协调，再用相对方向 gate 输出 r_i = W_r X_i + Σ_j β_ij(q_j−q_i)，β_ij 由最后一层 attention 权重和可学习 head 向量得到，可正可负。更新通过 tangent-space projection 和有界 spherical retraction，零初始化保证初始为 identity。
- **边际覆盖训练**：对每个 query 做切空间 antithetic 扰动 q_i^±，保持其他 query 不变做单 query 反事实替换，计算归一化覆盖差 Δ_i；loss 为 −Σ Δ_i⟨μ_i, ε_i⟩/(2σ)，是 Gaussian-smoothed coverage 的无偏梯度估计，训练只需 2L 次检索。Reference pool 在 epoch 2 用调整后的 queries 刷新，提供更强监督。

**关键结果**
8 个公开 benchmark + 一个 24 partition streaming industrial 数据，覆盖 6 个 frozen 生成 backbone。CACO 相对最强 baseline Recall@100 最高 +23.7%、Recall@400 最高 +23.9%；相对同 backbone Base，R@100 提升 1.01–3.99pp，R@400 提升 2.55–7.36pp；inter-query MPJ 下降 53.3%–64.9%，端到端推理延迟仅增加 0.5%–3.0%。跨 backbone 的 18 个设置全部提升 0.89–8.72pp；ablation 显示 query interaction 和 relative directions gate 都必要，greedy distillation 明显弱于边际覆盖学习。

**最值得记住的一句话**
多 query 召回的价值不是每个 query 单独召回多少，而是它能在其他 query 未覆盖的高相关 item 上贡献多少；用 reference queries 的检索频率做 label-free 相关性代理，就能以极低推理开销训练出这种边际覆盖能力。
