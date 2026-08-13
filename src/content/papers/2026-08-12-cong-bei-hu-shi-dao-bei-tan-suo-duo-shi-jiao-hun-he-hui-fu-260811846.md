---
title: 'From Overlooked to Explored: Recovering Item Relations via Mixture of Perspectives
  for Sequential Recommendation'
title_zh: 从被忽视到被探索：多视角混合恢复序列推荐中的物品关系
authors:
- Junyoung Kim
- Wonbin Kweon
- Woojoo Kim
- Jaehyung Lim
- Dongha Kim
- Hwanjo Yu
affiliations:
- Pohang University of Science and Technology
- University of Illinois Urbana-Champaign
arxiv_id: '2608.11846'
url: https://arxiv.org/abs/2608.11846
pdf_url: https://arxiv.org/pdf/2608.11846
published: '2026-08-12'
collected: '2026-08-13'
category: RecSys
direction: 序列推荐 · 注意力校准 · 多视角 MoE
tags:
- Sequential Recommendation
- Attention Calibration
- Mixture of Experts
- Similarity Bias
- Item Relations
- Contrastive Learning
one_liner: 识别并缓解自注意力相似性偏差，提出多视角透镜模块恢复同构与异质物品关系，序列推荐效果显著提升
practical_value: '- 诊断注意力失效：对线上 transformer 推荐模型，在验证集上计算 last-layer attention 与因果重要性（逐个
  mask item 看目标概率下降）的 Spearman/Align@1；若出现低相关或负相关，说明注意力被相似商品主导，模型实际依赖的 item 未被看到，可作为上线前诊断指标。

  - 双视角轻量插件：在 SASRec/BERT4Rec 等主干层间插入 PRISM 式模块，用一个小 router 把 item 分到 K 个语义组（noisy
  gating），每个 lens 只对同组 key 做 mask 并 boost logits；同一模型内自然出现 Affinity（同组强化）和 Contrast（跨组恢复）两类输出，再按
  g 加权融合。适合挖掘跨类目兴趣，如跑步鞋与运动水壶、手机与车载支架。

  - 工程性价比：所有 lens 共享参数，每增加一个 K 仅多 2d 参数（实验中 K=8 只比 K=2 多 768 参数），训练/推理显著快于常规 MoE；可以在已有模型上以极小成本验证收益。

  - 多视角训练防塌缩：如果需要序列级对比学习，使用 same-target 正样本时建议加入 stochastic perspective masking 随机屏蔽非主视角，防止不同视角被过度拉齐；同时对各视角输出做加权
  SKL 一致性约束，避免直接加权和导致表示空间冲突。这个适用于多兴趣/多专家模型。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

动机：transformer 序列推荐中的点积自注意力会系统性地偏向相似物品，忽略异质但重要的关系。论文通过因果重要性诊断发现，注意力分布与 item 对目标预测的贡献之间相关性低甚至为负；干预实验显示，提高被忽略 item 的注意力能显著提升目标置信度。这说明相似性偏差是限制推荐的隐性原因。

方法关键点：
- 在 transformer 层间插入 PRISM 模块。Semantic Anchor Router 用 noisy gating 将 item 表示分到 K 个语义组，得到主导语义 anchor（PSA）和语义组成比率 g。
- K 个 Perspective Lens 共享参数，每个 lens 根据 PSA 构造 Semantic Focus Mask，对前一层的 attention logits 加上 relational boost signal，得到 Perspective Guided Attention。
- 当 query 与 lens 组相同为 Affinity View，强化同质关系；不同为 Contrast View，恢复被相似性抑制的跨组关系。每个 item 恰好有一个 Affinity 视角和 K-1 个 Contrast 视角。
- 输出按 g 加权融合，过 FFN 后进入下一层。训练目标包含 L_SPCL（same-target 序列级对比学习 + stochastic perspective masking 防止视角塌缩）和 L_CCL（对 lens 输出分布做加权 SKL 对齐），总体为 L_rec + λ(L_SPCL + L_CCL)。

关键结果：在 7 个数据集（Amazon Toys/Beauty/Games/Sports/Electronics、ML-1M、Yelp）上对比 13 个 baseline，包括 SASRec、BERT4Rec、AC-SASRec、CL4SRec、DuoRec、ICLRec、ICSRec、FAME、FamouSRec、STAR-Rec 等。PRISM 在所有指标上均有提升，如 Toys H@5 从最强基线 0.0757 提升到 0.0802（+5.94%），ML-1M N@20 从 0.1772 提升到 0.1913（+7.96%），Yelp N@20 提升 11.17%。复测诊断显示 PRISM 的 attention 与因果重要性对齐大幅提升，干预收益接近零或为负。消融证明 Only Affinity 和 Only Contrast 均优于 SASRec，二者结合最佳；去除 relational boost 性能明显下降。效率上，K=4 时参数 909K，少于 FamouSRec 的 965K，训练快约 5 倍。

**最值得记住**：点积 self-attention 会把注意力过度集中在相似物品上，而真正驱动下一次点击的常常是跨类目、异质关系；用轻量多视角 lens 同时做同质精修和异质补充，能以极小参数代价恢复这些被忽视的信号。
