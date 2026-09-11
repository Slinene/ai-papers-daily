---
title: 'Data Scarcity and Model Sparsity: Mixtures-of-Experts Overfit More to Repeated
  Data'
title_zh: 数据稀缺与模型稀疏：MoE 对重复数据更易过拟合
authors:
- Atindra Jha
- Margaret Li
- Jure Leskovec
- Percy Liang
- Luke Zettlemoyer
affiliations:
- Stanford University
- Paul G. Allen School of Computer Science, University of Washington
arxiv_id: '2609.11917'
url: https://arxiv.org/abs/2609.11917
pdf_url: https://arxiv.org/pdf/2609.11917
published: '2026-09-10'
collected: '2026-09-11'
category: Training
direction: LLM 训练 · 数据重复 · MoE 正则
tags:
- MoE
- Data Repetition
- Overfitting
- Regularization
- Expert Specialization
- Routing Stability
one_liner: 在重复数据训练下，MoE 比同 active 参数的 dense 模型退化更早更快，且退化程度由 total 参数决定
practical_value: '- 搜索/推荐/广告等业务里若用 MoE 或稀疏 LLM 做召回、排序、query 生成，数据重复是常见场景（行为序列、曝光样本、promo
  物料反复出现）。不要只看 active 参数，要把 total 参数计入训练预算；重复率控制在 4× 以内对 MoE 相对安全，超过 8× 需要警惕。

  - 当业务数据受限必须多 epoch 训练时，优先在 MoE 的输出侧做 masking：FFN output masking、expert dropout 或
  expert output masking，比 router jitter、weight decay 更有效。生成式推荐/query 生成模型可以在 expert
  输出上加 token-level 或 expert-level dropout，缓解重复样本导致的过拟合。

  - 多域数据混合训练时，如果某个域 unique 数据不足，不要无限重复该域；把它与语义相似的未重复域混合可能起到正则化作用，而语义差异大的域（如 code 与
  web）混合无此效果。对电商多源数据（商品、内容、广告、搜索词）做配比时值得验证。

  - 路由早稳定是一个可工程化的监控信号：若 MoE 在训练早期 router 决策就接近冻结，并且 train loss 快速降到很低，通常意味着 expert
  在过拟合固定 token 子集。可定期做 expert knockout 分析，量化专家冗余与过度 specialization，作为是否继续训练或切换架构的依据。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：真实可用文本逐渐耗尽，重复训练数据已成常态；与此同时，MoE 凭借稀疏激活成为大模型训练的主流架构。此前数据重复研究主要针对 dense Transformer，对 MoE 的重复数据过拟合行为缺少系统认识。MoE 把 total 参数与 active 参数解耦，数据重复把 total tokens 与 unique tokens 解耦，两者叠加会改变现有 scaling law 与训练策略的有效性。

**方法关键点**：
- 在 80M / 200M / 1B active 参数尺度下，固定 total token 预算 T≈20·N_a，只改变 unique token 数，使 repetition rate R∈{1,...,1024}。
- 对比 dense 与多种 MoE：expert 数 n∈{8,16,32,64,128,256}，expert granularity g∈{1/2,...,1/32}，稀疏度 s∈{2,...,64}。
- 数据覆盖 DCLM web、StarCoder code、peS2o 学术、Wikipedia 百科，并设置单域、多域混合、不同过滤比例与不同域级重复率。
- 正则化手段包括 dropout、gradient clipping、weight decay、FFN output masking、expert dropout、expert output masking、router jitter。
- 机制分析：固定 token 集合上统计 router 稳定性、expert 共激活、load balance，以及 expert knockout 的 loss 影响。

**关键结果**：
- 80M dense 在 8× 重复下退化仍较小，MoE 从 4× 即开始明显变差；到 32× 重复时，MoE 全面被 dense 反超。
- 退化程度由 total 参数而非 active 参数决定；将 total/active token 比从 20 提升到 80 也基本不改变重复过拟合曲线。
- 单域、过滤质量、数据混合等场景结论高度一致：MoE 比 dense 更早过拟合。
- dropout 及 FFN/output/expert 级别的 masking 正则能有效降低重复过拟合；强 dropout 下 MoE 在 64× 重复时仍可超过 dense，但没有任何方法能达到 all-unique 数据效果。
- Router 在训练早期迅速 ossify，最终稳定性 >95%；重复率越高，ossification 越强。专家 knockout cost 随重复率上升，且 expert 数越多、上升越快；dropout 不显著改变 router 稳定性，但能降低专家过度 specialization。
