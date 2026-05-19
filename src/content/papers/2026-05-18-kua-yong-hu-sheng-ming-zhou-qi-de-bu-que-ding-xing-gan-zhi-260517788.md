---
title: Uncertainty-Calibrated Recommendations for Low-Active Users
title_zh: 跨用户生命周期的不确定性感知自适应推荐
authors:
- Bob Junyi Zou
- Sai Li
- Tianyun Sun
- Wentao Guo
- Qinglei Wang
affiliations:
- Stanford University
- TikTok Inc.
arxiv_id: '2605.17788'
url: https://arxiv.org/abs/2605.17788
pdf_url: https://arxiv.org/pdf/2605.17788
published: '2026-05-18'
collected: '2026-05-19'
category: RecSys
direction: 不确定性感知推荐 · 用户分群差异化策略
tags:
- Uncertainty Quantification
- Expected Prediction Error
- Bayesian Prior
- Upper Confidence Bound
- Low-Active Users
- Exploration-Exploitation
one_liner: 用辅助 Critic 网络预测预期预测误差 + 贝叶斯先验方差，实现低活用户去偏与高活用户 UCB 探索的统一框架
practical_value: '- **轻量级不确定度量**：训练一个辅助 Critic 网络，输入原始特征+推荐器嵌入+输出分数，直接预测实例级 EPE，在线仅增加一次前传，适合低延迟工业系统，避免
  MC Dropout 的多次采样开销。

  - **分群差异化策略**：按活跃天数将用户分组，假设组内噪声方差相近，对低活用户高不确定项加惩罚权重（deboosting）防流失，对高活用户高不确定项加 UCB
  探索奖励促多样性，可在不牺牲核心指标下同时优化留存和兴趣覆盖。

  - **训练数据构造技巧**：使用前一日模型检查点对次日样本计算误差，作为 EPE 的蒙特卡洛样本，既反映模型未见过数据下的泛化误差，又无需额外标注，且能利用每日生产重训流水线。

  - **校准阈值与在线调参**：在留出集上按分位数确定“高风险”阈值，再通过 A/B 测试调整去偏惩罚和探索权重，避免复杂曲率标定，工程实现简洁有效。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：大规模推荐系统中，低活用户（LAU）因行为稀疏导致预测不可靠，高活用户（HAU）则需主动探索以扩展兴趣。现有不确定性量化方法要么计算昂贵（MC Dropout），要么粒度粗（Conformal Prediction），难以在实时排序中提供实例级可靠信号。为此，提出一种统一的生产级框架，利用输入特定的不确定性估计驱动差异化排序策略。

**方法关键点**：
- 对点估计模型，引入 Critic 网络直接预测期望预测误差（EPE），其输入为原始特征、推荐器中间嵌入和最终输出，离线用历史模型检查点产生的误差样本训练。
- 对概率模型（如 Beta 先验），通过经验贝叶斯推断出输入依赖的先验，并将预测方差分解为认知不确定性（先验方差）与偶然不确定性，使用认知部分。
- 在标定集上按分位数设阈值，线上对 LAU 的高不确定性候选施加分数惩罚（deboosting），对 HAU 的高不确定性候选施加 UCB 探索奖励。

**关键结果**：在生产短视频/直播平台 A/B 测试 14 天，LAU 侧 7 日累计活跃时长（HLT7）提升 +0.0577%，优质观看时长比（VWR）提升 +0.512%，同时总观看时长仅微降；HAU 侧展示标签数/U 提升 +2.1%，头部兴趣集中度下降。消融实验表明联合 EPE 与贝叶斯方差的方案优于单用任一信号、多头集成、MC Dropout 及随机基线，验证了显式误差建模的重要性。
