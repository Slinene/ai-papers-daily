---
title: Are We Really Making Progress in Group Recommendation? Unmasking the Tie-Breaking
  Illusion
title_zh: 群组推荐真的在进步吗？揭开 Tie-Breaking 幻觉
authors:
- Song-Duo Ma
- Pu-Jen Cheng
affiliations:
- National Taiwan University
arxiv_id: '2608.11190'
url: https://arxiv.org/abs/2608.11190
pdf_url: https://arxiv.org/pdf/2608.11190
published: '2026-08-11'
collected: '2026-08-13'
category: RecSys
direction: 群组推荐评测偏差与 tie-aware 协议
tags:
- Group Recommendation
- Evaluation Bias
- Tie-Breaking
- BPR
- HR@K
- NDCG@K
one_liner: 揭示近期群组推荐提升源于 sigmoid 分数压缩与确定性 tie-breaking 的评测偏差，提出 tie-aware 评估使提升大幅缩水
practical_value: '- 在推荐系统离线评测中，若模型输出层含 sigmoid 或分数被压缩到 [0,1]，top-K 指标容易产生大量并列分数，而常规
  argsort/top-k 的 tie-breaking 顺序会影响 HR@K/NDCG@K，导致虚高或排名不稳。务必使用 tie-aware 评估（如多次随机打乱
  tie 求期望）或报告置信区间。

  - 对于 BPR 类训练，如果为了提高收敛稳定而加 sigmoid，建议改用 temperature-scaled BPR（例如 sigmoid(logits/tau)
  或 margin 调整），既保留 margin smoothing 的收益，又降低 tie 膨胀风险。

  - 若业务场景是群组推荐或多目标融合打分，分数落点接近时可主动加微小随机扰动或定义次级排序规则，避免隐式 tie-breaking 影响线上评估和 AB 指标。

  - 离线指标波动大时，检查是否由于 tie 造成，尤其在对比新模型和 baseline 时，需要使用相同的 tie 处理策略，否则可能得出误导性结论。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：近期群组推荐方法在标准基准上报告了显著提升，但作者发现这些提升可能源于系统性评测偏差：训练时的额外 sigmoid 变换将分数压缩，使 top 分数大量并列；而评测时的确定性 tie-breaking 使 HR@K 和 NDCG@K 对并列处理高度敏感。

**方法关键点**：在 CAMRa2011 和 Mafengwo 数据集上重访代表性方法及其基线，覆盖群组推荐和用户推荐设置；提出 tie-aware 协议，计算均匀随机 tie-breaking 下 HR@K 和 NDCG@K 的精确期望；进一步分析额外 sigmoid 在优化中的作用，并提出 temperature-scaled BPR 作为替代。

**关键结果**：tie-aware 评估下，许多先前报告的提升大幅缩小，方法相对排名明显改变；额外 sigmoid 可能隐式起 margin smoothing 作用，而 temperature-scaled BPR 能保留大部分收益且不引发严重 tie 膨胀。代码已开源。
