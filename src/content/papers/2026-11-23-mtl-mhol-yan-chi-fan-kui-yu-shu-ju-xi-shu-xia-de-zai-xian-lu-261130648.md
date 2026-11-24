---
title: 'MTL-MHOL: Predicting Online Conversions under Delayed Feedback and Data Sparsity'
title_zh: MTL-MHOL：延迟反馈与数据稀疏下的在线转化率预测
authors:
- Mario Tejera Vicente
- Eva Hagen
- Emma van Breukelen
- Quinten van de Vijver
- Kathrin Gruber
affiliations:
- Erasmus School of Economics, Erasmus University Rotterdam
arxiv_id: '2611.30648'
url: https://arxiv.org/abs/2611.30648
pdf_url: https://arxiv.org/pdf/2611.30648
published: '2026-11-23'
collected: '2026-11-24'
category: RecSys
direction: 广告CVR预估 · 延迟反馈 + 多任务
tags:
- CVR Prediction
- Delayed Feedback
- Multi-Task Learning
- Multi-Head Online Learning
- Data Sparsity
- Survival Analysis
one_liner: 提出MTL-MHOL框架，用分桶多头部在线学习联合多任务学习同时解决CVR预测中的延迟反馈与数据稀疏问题
practical_value: '- **延迟反馈的时间分桶 + 风险集 mask 可直接迁移到电商/广告转化预估**。将转化窗口（例如 7 天或 14 天）拆成互斥时间片，每个时间片一个
  head 预测条件转化概率（hazard），最终用生存概率乘积得到总 CVR。训练时每个 head 只使用“已成熟”且“仍处于风险集”的样本：早期未转化的样本可提前参与短窗口
  head 训练，不需要等整段窗口结束；已转化样本后续 head 不再参与。这能显著减少 label 假负样本，同时保持 CVR 的合理概率分解。尤其适合线上流式更新，新的短窗口标签一成熟即可更新对应
  head。

  - **用 hard parameter sharing + 高密度辅助任务缓解稀疏正样本**。在转化数据极少时，可以把点击、加购、浏览深度等高频信号作为辅助任务与转化主任务共享底层表示。连续型辅助目标建议用多分位数回归（pinball
  loss）而不是单点 MSE；同时加 soft monotonicity penalty 保证分位数有序，能提供更丰富的分布监督信号。Criteo 实验证明该辅助任务在
  MHOL 基础上仍有稳定 RCE 提升。

  - **长延迟窗口下校准是关键，分桶多头部能天然避免基率上偏**。单头模型只用全成熟样本会导致 recent converters 被纳入、recent non-conversions
  未成熟，从而高估 CVR；论文中单头模型校准误差约 0.034，多头部降到 0.0026，无需事后 Platt scaling。如果你的转化窗口较长（如 7 天以上），这一偏差不可忽视；通过分桶利用
  partially mature 样本，直接从源头提高校准。

  - **backbone 选择看特征形态**：稀疏类别特征多、存在低频交互时 DeepFM 更优（私域数据 RCE 提升达 10%）；匿名特征多或高阶隐式表示重要时
  MLP 更优（Criteo 数据）。实际落地可以先看特征基数与可解释性，再决定是否引入 FM component。另外，滚动窗口交叉验证比随机切分更贴近线上部署，值得在
  CVR 建模中作为标准评估。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

**动机**：在线广告 CVR 预测同时面临延迟反馈、数据稀疏和样本选择偏差。已有工作往往单独处理：MHOL 用时间分桶解决延迟反馈，但只在单任务 click-space 下工作；ESMM 用全空间多任务缓解稀疏，却忽略转化延迟结构。缺少一个能在线更新、模型无关的框架把两者融合。

**方法关键点**：
- 将转化观察窗口 H 分成 B 个互斥时间桶，每个桶一个 head 输出危险概率 h_ib = Pr(y_ib=1 | 未在前桶转化, X_i)，总 CVR = 1 - ∏(1-h_ib)，无需额外独立性假设。
- 训练时引入 maturity mask m_ib（桶已到期）和 risk-set indicator r_ib（尚未转化），只有两者均为 1 的样本才参与该 head 的 BCE loss，保证 survival 分解有效。
- 辅助任务通过 hard parameter sharing 共享底层 trunk：二元目标用交叉熵；连续目标用多分位数回归 pinball loss + 软单调性惩罚；总 loss = 主任务 masked BCE + λ_aux·L_aux。
- backbone 可替换，论文实现 MLP 与 DeepFM。

**关键结果**：
- Criteo 数据（30天观察、12天延迟窗口、4.93% 转化率）：MTL-MHOL NLL 0.1215、RCE 36.704，比 LR RCE 提升 81%，比 ESMM 高 21.5%，比神经网络延迟反馈 FSIW 高约 1%；消融呈 MLP<MTL<MHOL<MTL-MHOL，校准误差从单头 0.034 降到 0.0026。
- 两个私域客户数据：MTL-MHOL 均优于 LR/RF/消融变体；DeepFM 在私域比 MLP RCE 最高提升 10%，Criteo 上 MLP 高约 3%。
- 分桶预测准确复现单调与非单调转化时序模式，说明不仅能预测 if 还可预测 when。

**最值得记住的一句话**：把转化延迟窗口切成多个 time bucket，用风险集 mask 训练各 bucket 的 hazard 头，再叠加密集辅助任务，是从架构层面同时解决延迟反馈、校准偏差和数据稀疏的有效组合。
