---
title: 'FLMNet: Self-Ensemble Distillation from Masks to Seeds for Single-Tower CTR
  Prediction'
title_zh: FLMNet：从 mask 到 seed 的单塔 CTR 自集成蒸馏
authors:
- Yifan Wang
- Yifei Du
affiliations:
- National University of Singapore
- University of Science and Technology of China
arxiv_id: '2610.26143'
url: https://arxiv.org/abs/2610.26143
pdf_url: https://arxiv.org/pdf/2610.26143
published: '2026-10-19'
collected: '2026-10-20'
category: RecSys
direction: 单塔 CTR 训练 · 自蒸馏闭式正则
tags:
- CTR prediction
- self-ensemble distillation
- dropout
- single-tower
- knowledge distillation
- closed-form variance
one_liner: 把 masked 自集成目标推到无穷 mask 极限，得到闭式 Jensen gap 正则，单塔一次前向即可训练；再叠加跨 seed 蒸馏
practical_value: '- 工程上若现有 CTR 塔含 dropout 且想做 self-ensemble，不必采样多次：把 gate 改成读未 mask
  的 embedding、readout 保持 affine、层间 coordinatewise rescale，就能用高斯-埃尔米特闭式代理训练，成本接近单次前向，可直接迁移到
  DCN/DeepFM 类单塔。

  - 调参时注意：普通 dropout 对应 κ=1，FinalNet/QNN 式自蒸馏是 κ>1；单独去掉辅助 loss 而不调 dropout rate 会同时降低有效剂量
  κ·ρ/(1-ρ)，容易误判增益来源。

  - 离线蒸馏：训练同架构不同 seed 的 K 个塔，用 pooled logit 做 teacher，student 只回归 logit（不读 label），可吸收部分集成增益，上线仍是单塔；成本
  K+1 次训练，适合广告/电商模型定期刷新。

  - 门控自蒸馏中，gate 必须读未 mask 输入，不能读上层的 masked carrier；否则 mean logit≠clean forward pass，闭式失效，实测
  Criteo 上 AUC 掉 10.5e-4。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

动机：FinalNet、QNN 等 CTR 模型通过在不同 dropout mask 下自集成蒸馏获得 AUC 提升，但为什么有效、是否需要随机采样一直不清楚。生产系统要求单次前向，采样多 mask 训练成本高。

方法关键点：
- 将 QNN 式 masked self-ensemble 目标在 mask 数量 S→∞ 时推导为 label loss at mean logit + κ × Jensen gap；其中 Jensen gap 是 softplus 在 mask 上的期望减去 softplus 在 mean logit 上的值，本质是 mask 成员间 disagreement。普通 dropout 是 κ=1，self-ensemble 是 κ>1。
- 设计 FLMNet 单塔满足三个条件：gate 读未 mask 的输入、readout 是 affine、每层 coordinatewise rescale carrier。此时 mean logit 恰好等于 clean forward pass logit，variance 也有闭式形式；训练用 Gaussian + 3 点 Gauss-Hermite 代理，不需要采样 mask。
- 进一步提出 FLMNet-KD：训练 K 个不同 seed 的同架构塔，用 pooled logit 做 teacher，student 只回归 logit，把跨 seed 的集成增益蒸馏进单塔。

关键结果：在 Criteo、Avazu、KKBox、Frappe、ML-1M 五个公开 benchmark 上对比 17 个 baseline，FLMNet-CF 和 FLMNet-KD 在 AUC 和 Logloss 上占据前两名。闭式方差截断误差相对精确方差只有 0.035%，一阶截断会损失 8% 方差。去掉 QNN 自集成 loss 在 Criteo 上掉 0.06 个点 AUC，在 Frappe/KKBox 上掉 0.17/0.19 个点；闭式惩罚和跨 seed 蒸馏的增益在多数 benchmark 上可叠加。

最值得记住的一句话：自集成蒸馏的本质是抑制 mask 成员间 disagreement，单塔门控读未 mask 输入可把这一正则项变成确定性闭式。
