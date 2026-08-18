---
title: 'Impression Share Prediction: An Offline Evaluation Task for Ranking Systems'
title_zh: 曝光份额预测：排序系统的离线评估任务
authors:
- Mohsen Malmir
- Houssam Nassif
- Danish Nasir Shaikh
- Taher Rahgooy
- Murat Ali Bayir
affiliations:
- Meta Platforms, Inc.
arxiv_id: '2608.16872'
url: https://arxiv.org/abs/2608.16872
pdf_url: https://arxiv.org/pdf/2608.16872
published: '2026-08-17'
collected: '2026-08-18'
category: RecSys
direction: 排序系统离线评估 · 曝光份额预测
tags:
- Impression Share
- Offline Evaluation
- Counterfactual Prediction
- Delivery Capacity
- Ranking
- A-B Testing
one_liner: 提出曝光份额预测作为离线评估任务，用因果模型识别并预测候选排序模型的目标桶曝光分布，首小时Transformer rollout提升22% L1
practical_value: '- 在电商/广告多目标排序上线前，除了 AUC/NE/RIG，增加一个“曝光份额偏移”预测器：用候选模型离线打分分布（log-bin
  直方图 + mean/var）和 coverage 向量预测其可能把曝光从高价值目标（成交/支付）挪到低价值目标（点击/浏览）的比例，提前拦截收益风险。

  - 识别环节可用论文的 SCM：由于模型状态 A 由架构/训练决定、不受当前容量状态 D 反向影响，P(Y|do(A),D)=P(Y|A,D)，无需 IPW/domain
  adversarial 等复杂纠偏；如果业务中有类似“策略不反向影响系统状态”的结构，可直接用观测数据做反事实预估。

  - 工程上优先用简单 RF + 特征（22维置信度 + 容量）即可拿到 seen models 的 49% L1 提升；若做新模型冷启动预测，首小时必须替换成近期容量动态的序列编码器（如
  PatchTST 2h rollout），否则可能比均值基线还差 20%。

  - 对 LLM/Agent 生成式推荐：若未来要把 LLM 作为 ranking 模块放进共享流控/预算系统，其 score distribution 和 coverage
  特征同样可以用来预估曝光分配，避免只盯文本质量指标。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
标准离线指标（NE、RIG、AUROC、GAUC）只衡量模型在 logged data 上的预测准确度，无法捕捉候选模型上线后会把曝光从高价值目标桶（如成交、视频观看）重新分配到低价值桶（如点击）的风险。这类曝光再分配可能让离线指标变好但下游效用变差。工作定义“曝光份额预测”任务：给定候选排序模型和当前系统状态，预测其会在各 objective bucket 上产生的曝光分布。该任务本质是反事实预测，因为候选模型从未服务过线上流量。

### 方法关键点
- 用结构因果模型（SCM）刻画三变量：模型状态 A^m_t、曝光份额 Y^m_t、共享 delivery capacity 状态 D_t。DAG 中 A→Y、D→Y、Y→D_{t+1}、D→D_{t+1}，且无 D→A 边。因此后门路径消除，P(Y|do(A),D)=P(Y|A,D)，无需 IPW 或 balanced representation。
- 学习目标：从 (A^m_0, D_0) 直接预测 24h 窗口内的曝光份额向量 Y^m_T ∈ simplex；不展开中间步动态，避免误差累积。
- 特征：模型置信度特征 22 维（20-bin log-scale histogram + mean/var）和 coverage vector；容量特征 5×C 维（总容量、已消耗、剩余、pacing multiplier、活跃 campaign 数）。
- 两个预测器：Random Forest 独立预测每个分量后投影到 simplex；PatchTST-style encoder 摄入 2 小时容量历史（15 分钟 patch、8 tokens、2 层 Transformer、d_model=64、GELU），条件 MLP head 输出 share，用 KL loss 训练。

### 关键实验
数据来自 150 个候选模型、约 5 周、~1.8M 分钟级快照；时间切分 23 训练/15 测试，测试集中 20 个模型为新出现、83 个训练期已存在。指标为 L1 和 Spearman，对比 constant baseline（训练集平均 share 向量）。
- seen models：capacity only +25.3% L1；confidence+coverage +42.9%；full +48.6%。说明候选模型的 score distribution 是主要信号。
- held-out models 按首现时间分桶：0–1h 时 RF 为 −20.5%（差于基线），但 encoder-conditioned Transformer 为 +22.1%，摆动 42.6 个百分点；7d+ 后 RF 恢复到 +37.9%，Transformer +33.8%。

### 最值得记住的一句话
**首小时是 offline-to-online gap 真正所在；用近期 auction dynamics 做短 rollout 的 encoder，比只用当前快照更能预测新模型的曝光分配。**
