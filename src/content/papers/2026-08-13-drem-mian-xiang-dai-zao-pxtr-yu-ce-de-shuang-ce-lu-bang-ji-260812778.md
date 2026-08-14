---
title: 'DrEM: Dual-Side Robust Ensemble Ranking from Noisy User Preference Predictions
  in Video Recommendation'
title_zh: DrEM：面向带噪 pxtr 预测的双侧鲁棒集成排序框架
authors:
- Canwei Huang
- Tiantian He
- Xiaoxiao Xu
- Jun Zhang
- Ziran Deng
- Weike Pan
- Chunjie Chen
- Kaiqiao Zhan
affiliations:
- Shenzhen University
- Kuaishou Technology
arxiv_id: '2608.12778'
url: https://arxiv.org/abs/2608.12778
pdf_url: https://arxiv.org/pdf/2608.12778
published: '2026-08-13'
collected: '2026-08-14'
category: RecSys
direction: 推荐系统 · 集成排序 · 鲁棒学习
tags:
- Robust Learning
- Ensemble Ranking
- Prediction Noise
- Rank Consistency
- Industrial RecSys
- Denoising
one_liner: 提出 DrEM，用共享 logit 噪声模型同时校正 pxtr 噪声造成的监督侧偏好翻转和特征侧输出不稳定
practical_value: '- 电商/广告多目标融合排序中，上游 pCTR/pCVR/pCVR 等分同时充当特征和代理监督是常见做法；可直接复用 DrEM
  的双侧结构：监督侧做 pair 级 flip 校正，特征侧做一致性正则，并让两侧共享同一噪声参数。

  - 上游预测噪声方差无法观测，工程上可用 DrEM 的 bucketing + probit 估计：按 pxtr 分桶，用后验行为均值与预测均值的聚合偏差反推
  logit 空间 σ²，便于流式更新。

  - 特征侧不要无脑加对抗扰动；先做 preference-preserving filtering，只对扰动前后序一致的 pair 施加 rank consistency，避免与主
  ranking loss 冲突。

  - 线上收益对稀疏互动目标更明显（Follow/Comment 提升超 1%）；如果业务关注收藏、评论、转发等稀疏行为，应优先在这些 pxtr 任务上做 flip
  概率驱动的自适应校正和 item 级扰动。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：工业短视频/推荐系统采用多阶段排序，上游多任务模型输出 pxtr（pctr、pftr 等），下游集成排序既把 pxtr 作为输入特征，又用 pxtr 相对序构造代理监督。真实用户满意度不可观测，pxtr 噪声会双向传播：监督侧导致 pair 偏好翻转、产生错误梯度；特征侧扰动输入导致排序分不稳定。已有方法通常把 pxtr 视为可靠信号，DrEM 专门解决这一噪声问题。

**方法关键点**：
- 在 logit 空间假设加性高斯噪声：z_i = z_i^* + ξ_i, ξ_i ~ N(0, σ_i²)，两个组件共享该噪声模型。
- 监督侧：风险去噪鲁棒 pairwise loss，用估计的 pair 翻转概率 ε̂_ij 校正经验风险：L_rob = Σ[(1-ε̂_ij) ℓ(s_i,s_j) - ε̂_ij ℓ(s_j,s_i)] / (1-2ε̂_ij)；其中 ε̂_ij = Φ(-(z_i-z_j)/√(σ_i²+σ_j²))。
- 特征侧：从同一噪声分布采样 logit 扰动，替换 pxtr 输入；新增 preference-preserving filtering，只在扰动前后偏好序一致的 pair 上施加 ranking consistency，避免与主目标冲突。
- 噪声方差估计：利用后验行为与 pxtr 的聚合偏差，通过分桶 + probit 近似得到 item 级 σ_i²。

**关键结果**：在拥有数亿 DAU 的工业短视频平台数据上，以 EMER 和 EASQ 为 backbone，注入不同强度 pxtr 噪声进行评估。α=1.0 时，EMER 上 pvtr 从 .6899 提升到 .6966，pltr 从 .6622 到 .6725，pftr 从 .6853 到 .6965；EASQ 上同样稳定提升。线上 7 天 A/B（5.1% 流量）中，EMER 加 DrEM 获得 App Stay Time +0.116%、Video View +0.691%、Like +0.625%、Follow +1.197%、Comment +1.388% 等显著正向收益，稀疏行为目标提升更大。

**最值得记住**：上游多任务预测同时当特征和监督时，最容易忽略的是它的预测噪声；用共享 logit 噪声模型分别估计 pair 级翻转概率和 item 级扰动强度，可以实现双侧一体去噪。
