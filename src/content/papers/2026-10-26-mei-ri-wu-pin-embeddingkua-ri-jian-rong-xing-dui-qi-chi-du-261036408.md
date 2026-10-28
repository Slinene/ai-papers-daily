---
title: 'Cross-Day Compatibility of Daily Item Embeddings: An Empirical Study of Alignment,
  Scale Management, and CTR Adaptation'
title_zh: 每日物品Embedding跨日兼容性：对齐、尺度管理与CTR适应实证研究
authors:
- Yicheng Wang
affiliations:
- LY Corporation
arxiv_id: '2610.36408'
url: https://arxiv.org/abs/2610.36408
pdf_url: https://arxiv.org/pdf/2610.36408
published: '2026-10-26'
collected: '2026-10-28'
category: RecSys
direction: Embedding跨日对齐与尺度管理
tags:
- item embeddings
- cross-day compatibility
- CTR prediction
- warm start
- scale management
- orthogonal alignment
one_liner: 实证对比48种配置，发现warm start + 全局尺度重缩放将跨日GAUC提升4.0%，下游CTR编码器可进一步对齐残差漂移
practical_value: '- 每日更新 item embedding 的团队：优先评估 warm start + 每日全局 rescale（warm_norm），它把跨日
  norm 漂移从 +102.5% 压到 +8.2%，并取得最高 GAUC +4.0%；若无法维护 state，先上 OP 对齐，保留 cosine 检索排序且
  GAUC +2.6%。

  - 评估 embedding 质量不要只看 recall：XSimGCL recall 高出 Word2Vec 76.4%，但 GAUC 反而 -0.5%；必须联合
  GAUC/LogLoss 和检索指标，cosine/L2 只适合做漂移监控。

  - 在 CTR 模型里加一个共享 item encoder（降维）而非直接接原始 embedding，可以进一步吸收跨天残差；对照 random projection
  / SVD / untrained encoder 能诊断是否真的学到跨版本对齐。

  - 工程上先以 OP 为低成本基线，再用 warm_norm 做 A/B；注意 warm_norm 的 scale 管理通过后续训练动态生效，不是简单最终归一化。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
每日 item co-occurrence embedding 搭配次日点击日志训练 CTR，会让同个 item 在不同天方向/norm 漂移；即使单版本检索好，混合多版本也不一定利于下游共享网络。该工作系统比较 48 种配置，量化对齐、尺度管理、下游适配的收益。

## 方法关键点
- 上游：Word2Vec(SGNS) 和 item–item XSimGCL；干预含 ID-init、OP 正交对齐、affine/MLP 映射、unit norm、warm start、每日全局 rescale (warm_norm)、spherical 约束、temporal regularization、下游 noise/历史版本增广。
- 评估：跨日 cosine/L2/norm、Recall@100、GAUC、LogLoss；统一报告相对 Word2Vec 的百分比变化；下游 DNN 固定 embedding 并共享 encoder。

## 关键实验
- OP/ID-init 提升 cosine 93.4%/51.2%，GAUC 2.6%/2.2%。
- warm start 提升 cosine 127.0%、GAUC 3.5%，但 norm 漂移达 102.5%；warm_norm 把 norm 增长压到 8.2%，取得最高 GAUC 提升 4.0%，Recall +15.9%。
- XSimGCL recall +76.4% 但 GAUC -0.5%，说明检索不能替代 CTR 证据。
- CTR 训练的 encoder 在 6 个上游方法中 4 个获得最高 train-to-test cosine；Word2Vec+OP 比 untrained/SVD 高 10.8/4.0 pp。

最值得记住的一句话：跨日 embedding 兼容性需要“上游稳定化 + 继承尺度管理 + 下游任务学习”三层互补，几何/检索指标只能作辅助，最终以 GAUC/LogLoss 为准。
