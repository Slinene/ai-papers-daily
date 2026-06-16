---
title: One Sequential Recommendation Model Pretrained from Synthetic Priors Predicts
  Multiple Datasets
title_zh: 合成先验预训练的单模型跨域序列推荐
authors:
- Woosung Kang
- Jiwon Jeong
- Jonghyeok Shin
- Jeongwhan Choi
- Noseong Park
affiliations:
- Korea Advanced Institute of Science & Technology
arxiv_id: '2606.15752'
url: https://arxiv.org/abs/2606.15752
pdf_url: https://arxiv.org/pdf/2606.15752
published: '2026-06-14'
collected: '2026-06-16'
category: RecSys
direction: 免更新序列推荐 · 合成先验预训练
tags:
- Sequential Recommendation
- PFN
- Synthetic Prior
- Support Set
- Update-Free
- Cross-Domain
one_liner: SRPFN利用合成先验预训练与支持集条件推断，实现序列推荐无更新跨域泛化，平均提升7.53%。
practical_value: '- 冷启动与品类扩展：新品类上线时，仅从已有交互构建低秩SVD嵌入+支持集，一分钟内即可复用预训练模型做推荐，无需重训模型。

  - 长尾物品优化：采用基于转移概率采样支持集的方式，显著提升长尾物品命中率（Beauty Tail HR@5 +55.5%），可在推荐系统中用于长尾item的打捞。

  - 合成先验数据增强：用hDCSBM+变阶随机游走生成海量、多样的合成训练序列，可预训练一个通用推荐基座，提升跨场景泛化能力。

  - 架构迁移：编码器中的门控残差更新与方向性转移嵌入（源/目标分离）可嵌入现有Transformer推荐模型，增强对物品转移方向的敏感度。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机** 传统序列推荐模型针对每个数据集单独训练，参数绑定固定物品目录，跨域泛化需重新训练，成本高。本文观察到SASRec学到的物品嵌入与低秩转移统计高度相关，因此可以用目标域的统计总结作为输入，绕过训练。基于此，提出SRPFN (Sequential Recommendation PFN)，在合成先验上预训练一个条件推断模型，目标域仅需提供支持集，无需梯度更新即可预测。

**方法要点**
- **合成先验**：使用层次度校正随机块模型（hDCSBM）生成物品图，模拟层次社区、幂律度分布和核心-边缘结构；通过带几何分布滞后的随机游走生成序列，覆盖多样化的转移模式。
- **输入构建**：从目标域交互历史构建用户-物品矩阵R和物品转移矩阵P，经PPMI变换和截断SVD得到低秩嵌入：用户协同u_cf，物品协同i_cf，以及方向性转移嵌入i_src/i_dst。
- **支持集**：对每个用户，根据其最后交互物品的转移频率采样16个支持物品，作为局部转移证据。
- **模型架构**：编码器利用门控残差更新处理连续物品对，保留转移方向；Transformer编码序列，对最后隐藏状态进行多头交叉注意力（MHCA）从支持集记忆中聚合证据，经可学习门控融合得到最终表示；与候选物品编码计算内积得分。
- **训练**：在合成数据集上以负采样交叉熵损失预训练，近似后验预测分布。

**关键结果**
在Amazon Beauty、Sports、Toys、Yelp、LastFM五个基准上，SRPFN平均优于第二强基线7.53%；Beauty HR@1=0.2364；推断仅需约1分钟（预处理14s+推理45s），远低于SASRec（约10分钟）和FEARec（约15小时）。在未见Amazon类别上，HR@1大幅超越所有免训练基线。流行度分析显示Tail物品HR@5提升显著（Beauty +55.5%, Sports +81.5%）。消融表明支持集、方向性嵌入和门控均有效。

**值得记住** 单模型预训练于合成先验，通过支持集条件推断，无需任何目标域参数更新，即可在多领域序列推荐中达到甚至超越专门训练的模型性能。
