---
title: Scaling Laws For Data-Constrained Dense Retrieval
title_zh: 数据受限稠密检索的缩放律与算力分配
authors:
- Bowen Fu
- Jingtao Zhan
affiliations:
- Tsinghua Shenzhen International Graduate School
- Xi'an Jiaotong University
arxiv_id: '2611.04979'
url: https://arxiv.org/abs/2611.04979
pdf_url: https://arxiv.org/pdf/2611.04979
published: '2026-11-03'
collected: '2026-11-04'
category: Training
direction: 数据受限 Dense Retrieval 的 scaling law
tags:
- scaling laws
- dense retrieval
- data-constrained training
- compute efficiency
- fine-tuning
one_liner: 提出 MAEL 作为数据受限微调的稳定目标，拟合乘法 scaling law 并量化模型规模相对数据规模的计算效率优势
practical_value: '- 在标注/点击数据受限且重复多 epoch 的检索召回微调中，用 MAEL（训练期间最低 eval loss）替代固定 step
  的 eval loss 做模型选择与资源分配；它对学习率不敏感，且与 MRR@10、Recall@100 等线上指标高度相关（Pearson ≤ -0.985），适合小规模网格外推。

  - 学习率主要改变到达 MAEL 的步数而非最终最低 loss：scaled step = step × lr / (2e-5) 可对齐曲线。工程上可以先小网络扫学习率确定收敛速度，不必为每个配置重跑大搜索。

  - 资源分配：在 5K-320K 唯一样本、BERT-Tiny→Base 的数据受限 regime 下，增加预训练模型大小比增加唯一 in-domain 标注数据约
  1.46 倍更 fine-tuning compute 高效；若模型容量受线上延迟/部署限制，再补唯一数据。

  - Weight decay 调参：不要固定 λ，改用 EMA timescale τ_epoch = B / (η λ U) 作为不变尺度；数据减半时 weight
  decay 翻倍，常能降低 MAEL 并提升 in-domain 与 BEIR OOD 检索指标。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

动机：dense retrieval 通常用有限监督数据微调预训练 LM，标注/点击数据稀缺且跨 epoch 重复使用；传统 scaling law 假设唯一数据充裕，无法指导该数据受限场景下模型规模 vs 数据预算的算力分配。

方法关键点：定义 MAEL 为训练中最低 eval loss；在 BERT-Tiny 至 BERT-Base、5K-320K 唯一 MS MARCO 样本上 fine-tune 35 个配置，使用 infoNCE+256 随机负样本；发现学习率影响轨迹但 MAEL 和表征几乎不变，用 scaled step 归一化后曲线塌缩；拟合乘法 MAEL(N,U)=A N^α U^β+δ，对比 Kaplan/Chinchilla 加法形式；推导最优 step scaling，并给出 weight decay 的 EMA timescale 不变式；最后由 loss+step scaling 得 compute 效率比。

关键实验：乘法律 R²=0.99、RMSE 0.035，明显优于 Chinchilla R²=0.96；留出模型规模/数据预算预测平均相对误差 2.77%-3.28%，外推误差 3.14%-4.45%；MAEL 与 MRR@10、Recall@100、nDCG@10、MAP@10 的 Pearson r 约 -0.985 到 -0.995；最优步数 scaling R²=0.95；最优 weight decay 在 EMA timescale 下近似固定；增加模型规模相对增加唯一数据对降低 MAEL 的 compute 效率比约 1.46 倍；固定算力下，BERT-Base 配 21.7K 数据 vs BERT-Medium 配 41.2K 数据，前者 MAEL 更低（0.690 vs 0.720）且算力仅多 8%。

最值得记住的一句话：数据受限 dense retrieval 微调中，MAEL 是对学习率不敏感、与线上指标高度相关的稳定优化目标；在 5K-320K 范围内，优先扩大预训练模型规模比追加唯一标注数据更算力高效。
