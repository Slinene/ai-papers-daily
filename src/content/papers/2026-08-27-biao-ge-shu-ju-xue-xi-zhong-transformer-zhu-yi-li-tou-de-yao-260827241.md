---
title: Importance Scoring of Transformer Attention Heads in Learning Tabular Data
title_zh: 表格数据学习中 Transformer 注意力头的重要性评分
authors:
- Ahmad Jad Allah
- Kazi F. Akhter
- Md. Kamrozzaman Bhuiyan
- Manar D. Samad
affiliations:
- Tennessee State University
- Enosis Solutions
- North Carolina Agricultural and Technical University
arxiv_id: '2608.27241'
url: https://arxiv.org/abs/2608.27241
pdf_url: https://arxiv.org/pdf/2608.27241
published: '2026-08-27'
collected: '2026-08-29'
category: Training
direction: 表格 Transformer 注意力头可解释性与剪枝
tags:
- tabular data
- attention heads
- head importance
- pruning
- transformer interpretability
one_liner: 首次将注意力头重要性评分用于表格 Transformer，72.5% 实验中移除最低重要性头最稳健
practical_value: '- 若业务中正在用 Transformer 处理用户/物品/上下文特征或表格型特征，可直接对每层每个 head 计算重要性分数，按低重要性逐步剪枝；论文在
  40 个 tabular 数据集上显示，先删最低重要性 head 在 72.5% 实验中性能损失最小，适合做线上模型压缩和降本。

  - 重要 head 跨层分散，没有稳定层规律；因此剪枝/降载时不要固定保留最后一层或某几层，最好在目标业务数据上重新度量。

  - 不同 dataset/schema 的 head 重要性差异大，意味着多域推荐或不同场景（CTR、CVR、push 文案）下不宜共用一套 head mask，可分场景/分域计算重要性，甚至做成
  feature-based importance 监控。

  - 该方法可以作为解释工具，排查表格型 Transformer 里哪些 head 捕捉重要交叉特征/高基数类别特征，辅助特征工程和模型调试；源码可直接复用。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：深度 Transformer 在 CV/NLP 中已得到广泛研究，但在表格数据上的应用仍相对不足；同时模型计算昂贵且不透明，需要更细粒度的解释与优化手段。

**方法关键点**：该工作提出 attention head importance score，对学习表格数据的 multi-head transformer 进行单 head 重要性度量；在 40 个多样表格数据集上开展 head drop 实验，比较移除最低 importance head 与移除最高 importance head 后的分类性能变化，并分析六层 attention 中重要 head 的分布。

**关键结果数字**：72.5% 的实验中，逐渐移除最低重要性 head 时模型性能最稳健；先移除最高重要性 head 则带来最大的分类性能下降；重要 heads 跨层分散，未呈现一致的层特化趋势；与图像/语言领域不同，表格数据在不同 schema/feature space 下 head importance 差异很大。代码已公开。
