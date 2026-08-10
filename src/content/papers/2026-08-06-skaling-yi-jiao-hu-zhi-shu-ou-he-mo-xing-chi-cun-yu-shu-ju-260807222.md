---
title: 'Skaling: Chinchilla''s Exponents Meet Kaplan''s Coupling'
title_zh: Skaling：以交互指数耦合模型尺寸与数据的缩放法则
authors:
- Mathurin Videau
- Badr Youbi-Idrissi
- David Lopez-Paz
- Kartik Ahuja
affiliations:
- FAIR at Meta
arxiv_id: '2608.07222'
url: https://arxiv.org/abs/2608.07222
pdf_url: https://arxiv.org/pdf/2608.07222
published: '2026-08-06'
collected: '2026-08-10'
category: Training
direction: 缩放法则改进 · 计算最优预测
tags:
- scaling laws
- compute-optimal training
- LLM
- interaction exponent
- sparse grid
one_liner: 引入交互指数耦合模型容量与数据，解决标准缩放法则在极端区间的预测偏差，MAPE 降低 1.5–3 倍
practical_value: "- **小规模代理实验精准指导大规模训练**：直接采用 Skaling 法则对搜索/推荐模型（如召回双塔、精排大模型）进行缩放预测，捕捉模型尺寸与数据量的交互效应，避免因独立假设导致在数据稀疏或过训练时的计算资源错配。\
  \  \n- **低成本外推最优配置**：结合文中稀疏网格策略，用少量低计算量实验（约全网格的 1/10 计算量）即可准确外推更大规模下的 Loss 与最优参数比，适合业务中需快速评估多个模型尺度时的预算分配。\
  \  \n- **Agent 微调与 RLHF 的 scaling 决策**：在为下游任务微调 LLM Agent 时，可利用该法则预测不同基座大小与微调数据量组合的性能，帮助在预算内选取性价比最高的配置。\
  \  \n- **交互项设计思路可迁移**：当推荐模型存在组件间的强耦合（如特征域数量与 embedding 维度的联合缩放），可在损失预测函数中显式引入耦合项，提升拟合效果，该方法具有通用性。"
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：标准神经缩放法则（如 Chinchilla）假设模型容量与训练数据对损失的影响相互独立，这导致在数据稀缺或过度训练等极端区域预测偏差大，表现为系统性高估或低估。为更稳健地指导大模型训练的计算预算分配，需要一种能捕捉两者耦合效应的缩放函数。

**方法关键点**：提出 Skaling 法则，在其标准幂律形式中引入一个交互指数，将模型尺寸 N 与数据量 D 的耦合效应显式建模为 L(N,D) = ... + a·N^α·D^β 中的交互项，允许两者非独立叠加。同时设计了一种稀疏网格实验策略，仅在低计算量区域（即小模型、少数据）采样，利用 Skaling 外推全网格表现，大幅降低实验成本。

**关键结果**：相比 Chinchilla，Skaling 在插值和 4× 外推任务上的 MAPE 降低 1.5–3 倍；在 76% 的训练配置上预测更准，中位优势 2.2 倍，1/3 配置优势 ≥4 倍。结合稀疏网格，仅需均匀扫描约 1/10 的计算量即可准确预测全网格损失，成功复现了 Chinchilla 计算最优配置。
