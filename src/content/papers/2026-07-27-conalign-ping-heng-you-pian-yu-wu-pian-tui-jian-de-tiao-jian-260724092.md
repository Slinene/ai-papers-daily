---
title: 'ConAlign: Conditional Alignment Framework for Balancing Biased and Unbiased
  Recommendation'
title_zh: ConAlign：平衡有偏与无偏推荐的条件对齐框架
authors:
- Jingcheng Zhang
- Yihan Wang
- Qi Song
- Liyin Hong
affiliations:
- Kuaishou Technology
arxiv_id: '2607.24092'
url: https://arxiv.org/abs/2607.24092
pdf_url: https://arxiv.org/pdf/2607.24092
published: '2026-07-27'
collected: '2026-07-28'
category: RecSys
direction: 推荐去偏 · 流式条件对齐
tags:
- debiasing
- conditional alignment
- dual-tower
- streaming training
- filter bubble
- unbiased data
one_liner: 提出条件门控对齐机制，选择性传递有偏知识，在流式训练下平衡有偏环境准确度与无偏偏好估计。
practical_value: '- 可用于线上推荐系统，部署小比例随机流量收集无偏数据，训练无偏塔并与有偏塔通过条件对齐连接，在不损害主业务指标的前提下提升长期多样性。

  - 条件门控 I_cond：仅当有偏塔损失更低时才激活对齐，避免无偏塔被过度纠正；电商/广告场景可借鉴，选择性利用曝光偏差信号。

  - 跨塔设计：无偏塔拼接有偏塔倒数第二层隐向量，用 stop-gradient 防止梯度回传，低成本实现知识迁移，适合流式训练。

  - 快手线上 A/B 结果：DAU +0.069%，LT7 +0.029%，兴趣多样性显著提升，验证了去偏对长期留存的正面影响，为电商平台追求用户长期价值提供实证。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：推荐系统训练数据存在曝光、选择等偏差，导致反馈回路形成过滤气泡（filter bubble），用户兴趣坍塌，长期留存下降。尽管引入无偏随机数据可缓解，但现有方法要么忽视有偏环境下的推荐质量，要么计算开销过大，难以工业部署。快手数据分析显示，用户兴趣多样性（VIN）与 LT7 正相关，凸显维持多样性的必要性。

**方法关键点**：
- 双塔架构：有偏塔在大规模有偏数据上训练，无偏塔在少量随机流量数据上训练；最终采用无偏塔的预测分数排序。
- 跨塔输入：无偏塔的输入拼接有偏塔倒数第二层隐向量（LBR），梯度不回传，复用有偏塔学到的协同信号。
- 条件对齐损失：不对所有样本强制对齐，仅当有偏塔的损失小于无偏塔时，对隐层表示施加 L1 损失，对齐在隐层而非预测分数层，避免负迁移。
- 流式训练：两个数据流独立采样构建 batch，实时评估门控条件，在线学习，延迟增加可忽略。

**关键结果**：
- 离线：三个数据集（Coat, Yahoo! R3, KuaiRand-Pure）上，无偏评测 UAUC 和 NDCG 均优于 AutoDebias、InterD 等基线，有偏评测保持竞争力；训练延迟显著低于 AutoDebias 和 InterD（Yahoo! R3 上 ConAlign 122.7s vs. AutoDebias 4560.7s, InterD 10592.1s）。
- 在线 A/B：在快手短视频推荐系统上，DAU +0.069%，LT7 +0.029%，兴趣多样性指标 VIN +0.097%，类别集中度 CC -0.083%，短期播放指标正向或持平。

**最值得记住的一句话**：ConAlign 通过“条件门控 + 隐层对齐”的轻量设计，让无偏去偏学习真正融入工业流式推荐系统，同时提升长期留存与兴趣多样性。
