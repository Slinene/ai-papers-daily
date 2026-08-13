---
title: 'FunnelCausalNet: Funnel-aware Joint Conversion-Revenue Uplift for Multi-tier
  Coupon Allocation'
title_zh: 漏斗感知的转化-营收联合 uplift 建模与多层级优惠券分配
authors:
- Yu Zhang
- Zhihan Wang
- Guanlin Chen
- Min Jiang
- Shuai Li
affiliations:
- AMap Alibaba Group
arxiv_id: '2608.11675'
url: https://arxiv.org/abs/2608.11675
pdf_url: https://arxiv.org/pdf/2608.11675
published: '2026-08-12'
collected: '2026-08-13'
category: RecSys
direction: 多臂 uplift · 漏斗耦合 + 预算分配
tags:
- uplift modeling
- causal inference
- zero-inflation
- conformal prediction
- budget allocation
- multi-tier coupons
one_liner: 硬耦合转化概率与条件价值的漏斗结构，配套预算分配与审计不确定性层
practical_value: '- GMV 目标建议改成硬漏斗：`mu_gmv = mu_conv * mu_val`，用 BCE 训练转化头、转化者子集上 log(1+GMV)
  MSE 训练价值头；在转化率 4.6%–45.4% 的零膨胀优惠券场景，比直接 GMV 回归的 PEHE 低 18–48%。

  - 不要用 narrow-α conformal 下界驱动预算分配，重尾/零膨胀下容易塌缩成全不发券；优先用 RCT 臂均值锚定后的点估计输入 Lagrangian
  分配器，或把 α 放宽到 0.10–0.20。

  - 离线评估多臂补贴策略时，建议扫 LP 前沿或 EOM 曲线，得到 (ΔGMV%, ΔROI) 完整 tradeoff，而不是只看单点 AUUC；策略匹配子集上用
  Hájek IPW 估计更贴近 RCT 日志。

  - 若漏斗日志模糊或异步，可换 soft penalty；但在支持关系确定、零膨胀严重的真实 RCT 场景，硬耦合更稳。共享表示可能带来跨头协方差，理论方差优势只能当
  regime heuristic。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

动机：优惠券营销同时影响转化和 GMV，但 GMV 有确定性漏斗结构——未转化时 GMV=0，且高度零膨胀、重尾；多层级券有不同转化/营收弹性。传统 decoupled 管线忽略漏斗恒等式，直接回归 GMV 方差大，转化与 GMV 排序也可能冲突。

方法关键点：
- FunnelCausalNet 用共享表示同时估计各 arm 的转化概率 μ_conv 和非负条件价值 μ_val，硬耦合 μ_gmv = μ_conv · μ_val；训练为转化 BCE + 转化者 log(1+GMV) MSE。
- 理想化 MSE 比率分析（Proposition 2）指出，在参数头速率差与跨头协方差控制下，高零膨胀时漏斗组合有方差优势；仅作 regime heuristic，不保证共享表示神经网络实现。
- 不确定性层：对转化和条件价值 CATE 做 split-conformal，Bonferroni 联合覆盖，Top-K 冲突筛查只做审计，不驱动分配。
- 预算分配：Lagrangian relaxation 解多臂 budgeted allocation，用 RCT 臂均值加性锚定校正 GMV level，百万用户双更新约 0.13s。
- 评估用 EOM：扫 LP 前沿得 (ΔGMV%, ΔROI) 曲线，并用 Hájek IPW 估计。

关键结果：
- Criteo-MT7 半合成 8-arm：AUUC_GMV 0.613，与 EFIN 0.615 差一个 seed 标准差内；硬漏斗较直接 GMV 回归 PEHE 降低 18–48%（ˆp 4.6%–45.4%）。
- 工业 Hotel-Coupon RCT，约 4.93M holdout/seed：LP 前沿上 7/7 个 ΔGMV% 锚点 seed-averaged mean ΔROI 最高；但三 seed 相关，不能算独立锚点显著性。
- Hillstrom 单臂公共 benchmark 上收益导向 ranker 反超，说明该方法并非普适，适用于多层级/多强度轴场景。

最值得记住：多层级优惠券 GMV uplift 要贯穿漏斗恒等式 μ_gmv = μ_conv · μ_val，并让预算分配与评估都锚定 RCT；在单臂或无强度轴场景别假设优势。
