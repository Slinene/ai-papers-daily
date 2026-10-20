---
title: 'OneChord: Distill What You Rank, Recommend in One Pass'
title_zh: OneChord：蒸馏所排名的融合分布，单 pass 完成生成式推荐
authors:
- Zesheng Li
- Chengchang Pan
- Honggang Qi
affiliations:
- University of Chinese Academy of Sciences
arxiv_id: '2610.25805'
url: https://arxiv.org/abs/2610.25805
pdf_url: https://arxiv.org/pdf/2610.25805
published: '2026-10-19'
collected: '2026-10-20'
category: GenRec
direction: 生成式推荐 · Semantic ID 融合蒸馏
tags:
- Semantic ID
- Generative Recommendation
- Knowledge Distillation
- Ranking Consistency
- One-Pass Inference
- Fusion
one_liner: 学习 SID 与 item 匹配的 catalog 归一化融合分布，并通过蒸馏将 refined 排序迁移到 one-pass 推理，平均 NDCG@5
  提升 7.12%，推理更快
practical_value: '- 在生成式召回/精排融合场景，把最终线上融合打分（如 SID 概率 + 双塔相似度）作为唯一训练和蒸馏目标，而不是分别训练后手工调权；学一个全局混合系数
  α，实验显示比固定 0.5 融合在所有数据集都有提升，且对 α 不敏感，业务可安全上线。

  - 蒸馏时保持「先 catalog 归一化，再融合，最后才 candidate conditioning」的顺序，否则两分支在子集上的相对权重会发生偏移，导致排序反转；工程实现上先在完整合法库算
  normalizer，再取候选子集。

  - 用 frozen denoiser 从 one-pass 学生生成部分可见的合法 SID 状态，学生自己评估这些状态得到 refined 目标，再和直接预测在
  shared hard candidates（label + 100 negatives + 双方 top-32）上做温度 KL 蒸馏；推理仍是单次前向，成本不增。

  - 通过共享 decoder 同时产出 SID 概率和 item 相似度，用 stop-gradient 隔离 catalog 侧 embedding，缓存 item
  向量，serving 只需一次 encoder + 一次 parallel decoder + catalog scoring，适合低延迟线上；相比最快 baseline
  还能快 4–18%。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
语义 ID 推荐部署时通常结合 SID 概率和 item 相似度，但两者归一化与权重直接决定最终排序；现有方法要么分别训练后手工融合，要么蒸馏时在非融合分布上做一致性，SID 一致不代表 item 排序一致，导致线上排序不是训练优化目标。需要一个训练目标直接对齐线上 served 分布，并且把训练时 refinement 的有效性迁移到 one-pass 推理。

## 方法关键点
- 共享 encoder/decoder 同时预测 SID 概率（mixture of categorical products）和 item 匹配分数，分别在全 catalog 上归一化，再通过可学习的全局 gate α 融合为最终 serving 分布 q。
- 直接在 next-item 监督上训练 q（fused likelihood），使 α 和两个分支的共享参数都按最终概率校准；分支梯度按 responsibility 加权。
- 用 frozen denoiser 提供合法部分 SID 状态，当前学生评估这些状态得到 refined 融合目标；在 shared hard candidates 上（label + 100 negatives + 学生和 refined 各自 top-32）做温度缩放 KL 蒸馏，将 refined 排序转移到 one-pass。
- 关键顺序：先 catalog 归一化，再融合，再对候选子集 conditioning；避免 candidate conditioning 改变分支权重。
- SID 一致性 loss（boundary + composition）辅助训练，但 ranking consistency 是核心。
- 推理只需一次前向：一次 encoder、一次 parallel decoder、catalog scoring（可缓存 item vectors）。

## 关键结果数字
- 六个 Amazon 数据集（Sports, Beauty, Toys, Scientific, Instruments, Games）上，OneChord 在所有数据集上 Recall@5 和 NDCG@5 最高；相对最强 baseline 平均 Recall@5 +6.30%，NDCG@5 +7.12%，Beauty 上 NDCG@5 +9.96%。
- 生成速度比最快 baseline 快 1.04–1.18x，完整测试集 Top-10 生成 0.23–1.24 秒。
- 消融：去掉 fused likelihood 后 NDCG@5 掉 5.20–14.75%；去掉 ranking distillation 也有明显下降；学习的 α 在所有数据集上优于单分支，固定等权融合不如学习 α。
- 稀疏性划分：中频 item 上 Recall@5 +14.92%，NDCG@5 +17.70%；长历史用户 NDCG@5 +12.82%。

## 最值得记住的一句话
让训练、蒸馏和 serving 都优化同一个 catalog-归一化的融合排序分布，排序才不会被两分支相对尺度绑架。
