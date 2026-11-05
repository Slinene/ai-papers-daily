---
title: 'When Category Means Move: A Paired-Support Audit of Recommendation Logs with
  Random Insertions'
title_zh: 类目均值漂移时：基于随机插入的推荐日志配对支持审计
authors:
- Yu Zhang
- Zhihan Wang
- Yuhang Lu
- Shuai Li
affiliations:
- AMap Alibaba Group
arxiv_id: '2611.05006'
url: https://arxiv.org/abs/2611.05006
pdf_url: https://arxiv.org/pdf/2611.05006
published: '2026-11-03'
collected: '2026-11-05'
category: Eval
direction: 推荐日志测量审计 · 曝光偏差校准
tags:
- measurement audit
- exposure bias
- random insertions
- recommendation logs
- category dashboards
- calibration
one_liner: 用随机插入流量审计类目看板，量化曝光偏差并揭示校准对绝对误差有效但对排名和不同阈值不稳定
practical_value: '- 业务看板中类目/商品均值指标不能直接信：生产日志是被推荐策略筛选过的，均值变化可能来自受众、频控、库存变化而非真实偏好；可引入随机插入流量作为共同
  support，在同一用户-物品重叠上做配对对比。

  - 用户 demean + 随机全局锚点能大幅降低绝对 MAE（论文中约 80%），适合绝对值/规模类指标校准；但若最终决策依赖类目排名或 top-K 选择，需注意该方法对
  centered MAE 和 rank correlation 改善有限。

  - 误差分解可迁移为业务指标归因：把偏差拆成 within-video residual、video mix、random support，定位是模型排序问题还是库存/流量分布问题。

  - 校准评估要按业务 cutoff 做区间估计和 family-wise 检验，不能只报单点；论文中 top-10 显著而 top-5/top-20 不显著，提醒避免仅凭一个阈值下结论。

  - 类别级校准（category calibration）在 frozen test 中比标量校准 MAE 更低，线上预算允许时可做更细粒度校准。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

动机：内容类目看板由生产推荐日志的曝光均值生成，曝光受服务策略影响，导致均值解释偏差。方法：用 KuaiRand 随机插入曝光作为对照，在相同 12,472 用户和 5,486 视频上审计类目均值；比较标准均值、用户 demean 加随机全局锚点、类别校准 vs 标量校准；进行误差三元分解（within-video residual, video mix, random support），并做 cutoff-specific 和 family-wise 推断及 stress test。结果：标准均值 absolute/centered MAE 0.1935/0.0491，rank corr 0.7833；demean+anchor 将 absolute MAE 降 80%，centered MAE 仅降 21%，排名改善不可靠；误差主要来自 within-video residual 72.41% 和 video mix 23.90%，random support 3.65%；frozen later test 中 category calibration MAE 0.0251 vs scalar 0.0531；但 nominal top-10 regret -0.0062 区间不含 0，top-5/top-20 和 family-wise 区间含 0；stress test 暴露 item mix 和 weak overlap 下失败。结论：所有分解为描述性，结果条件于重叠 cohort，不主张内在类别效应或普遍有效修正。
