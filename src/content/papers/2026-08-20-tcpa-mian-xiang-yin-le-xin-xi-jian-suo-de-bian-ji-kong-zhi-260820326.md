---
title: '$TCP_α$: Margin-Controlled Confidence estimation for reliable Music Information
  Retrieval'
title_zh: TCPα：面向音乐信息检索的边际控制置信度估计
authors:
- Parampreet Singh
- Anushka Singh
- Sumit Kumar
- Vipul Arora
affiliations:
- Indian Institute of Technology Kanpur
arxiv_id: '2608.20326'
url: https://arxiv.org/abs/2608.20326
pdf_url: https://arxiv.org/pdf/2608.20326
published: '2026-08-20'
collected: '2026-08-22'
category: Eval
direction: 后处理置信度估计与失败预测
tags:
- confidence estimation
- failure prediction
- post-hoc
- margin-controlled
- class imbalance
- music information retrieval
one_liner: 提出 TCPα 置信度目标，通过边际惩罚分离正误预测，显著提升失败预测性能
practical_value: '- 在电商推荐/广告精排中，模型输出概率常被当作置信度但不可靠。可训练一个轻量置信度头（基于冻结特征），对每个候选输出置信度，用于决定是否展示、降低出价或触发人工审核，减少低质推荐曝光。

  - 拒绝低置信预测的策略可直接上线：例如对 CTR 预估置信度低的广告降低出价或放弃展示；对搜索推荐中低置信的结果不展示。论文中 8% 拒绝可将 macro-F1
  从 0.89 提升到 0.98，可量化类似收益。

  - 域偏移（新品类、新场景）下，只需用 5% 标注样本微调置信度头而非重训主模型，成本低、适应快，适合电商快速变化的业务环境。

  - 训练置信度头时错误样本极少导致严重不平衡，论文中的训练策略（加权/重采样等）可迁移到其他二分类失败预测或置信度估计任务。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**
深度神经网络在音乐信息检索（MIR）任务中常常过度自信，即使预测错误也给出高置信度，用户缺乏可信度判断依据。现有后处理置信度估计通过冻结分类器训练轻量辅助头，但目标值设计存在固有歧义：正确和错误预测的置信度重叠，边界附近的错误与正确预测的置信度难以区分。

**方法关键点**
提出 TCPα 置信度目标，对误分类样本引入 margin-controlled penalty。理论证明：TCPα 能够完全分离正确与错误预测的目标值，分离间隔与类别数无关，且随惩罚参数 α 单调增加。由于准确分类器产生的错误样本极少，学习该目标形成严重不平衡回归问题。论文系统研究了不平衡下的训练策略，通过广泛消融确定有效配置。

**关键结果**
在 rāga 识别任务上，拒绝最低置信的 8% 预测，base 模型 macro-F1 从 0.89 提升至 0.98；域偏移下仅用新语料 5% 标注样本微调置信度头即可恢复性能；在 frame-wise ornamentation detection 上无需修改配置也优于现有方法。
