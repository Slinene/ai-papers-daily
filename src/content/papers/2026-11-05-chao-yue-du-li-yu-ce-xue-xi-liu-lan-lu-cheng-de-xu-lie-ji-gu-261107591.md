---
title: 'Beyond Independent Predictions: Learning the Browsing Journey for Sequence-Level
  Re-ranking'
title_zh: 超越独立预测：学习浏览旅程的序列级重排评估
authors:
- Jiayi Zhang
- Jingxin Hai
- Zhenjia Ma
- Hongbin Pei
- Dagui Chen
- Han Zhu
- Jian Xu
affiliations:
- Taobao & Tmall Group of Alibaba
- Xi'an Jiaotong University
arxiv_id: '2611.07591'
url: https://arxiv.org/abs/2611.07591
pdf_url: https://arxiv.org/pdf/2611.07591
published: '2026-11-05'
collected: '2026-11-06'
category: RecSys
direction: 序列级重排评估 · 印象-点击联合建模
tags:
- Re-ranking
- Sequence-level evaluation
- Impression modeling
- Click prediction
- Exposure bias
- Generator-Evaluator
one_liner: 提出 JBM 范式与 ICE 框架，建模 display→impression→click 全链，修正重排评估偏差并提升序列选择质量
practical_value: '- 评估器从独立 item CTR 升级到序列级浏览建模时，显式加一个 impression branch 预测浏览深度分布，并用累计函数生成单调曝光概率；这能有效纠正尾部
  item 效用高估，适合直接嵌入现有重排评估器（线上收益 +0.70% clicks / +3.67% revenue）。

  - 把预测曝光概率作为 stop-gradient 信号做上下文去噪：Transformer 用 additive attention bias log(M+ε)，DNN/MLP
  用 feature gating h̃ = g(p_itr)·h；这能过滤未曝光 item 的虚假 context，且不干扰 impression 任务。

  - 在点击建模外加序列级 click distribution matching：点击 logits 做 temperature softmax 得到预测点击分布，与真实
  click 分布做 KL；零点击序列给 uniform 目标。这个 loss 能显式建模序列内点击竞争，对多点击场景提升更明显。

  - 工程上该框架是 backbone-agnostic plug-and-play，延迟增量 <0.5ms；可在不改 generator 的前提下以多任务方式训练，适合低风险接入工业
  G-E 重排链路。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：在 Generator–Evaluator 重排框架中，evaluator 的序列效用估计质量直接决定推荐质量。现有 evaluator 多采用 Independent Behavior Modeling（IBM），把浏览过程拆成独立的 per-item CTR 预测，忽略两个关键事实：display 到 impression 存在曝光衰减（尾部 item 可能根本没被看到），以及序列内 item 之间存在点击竞争。这导致离线评估系统高估尾部效用、给未曝光 item 注入虚假上下文，并且在多点击场景建模能力差。

**方法关键点**：
- 提出 Joint Behavior Modeling（JBM）范式，显式建模 display→impression→click 联合分布，而不是独立乘积。
- ICE 框架包含三个模块：
  1. Browsing-depth Impression Modeling：预测用户浏览深度 T 的 categorical 分布，通过累计分布得到每位置曝光概率 p_itr，保证单调递减。
  2. Impression-aware Dynamic Masking：利用 p_itr 对点击分支做上下文去噪；Transformer 用 log(M+ε) 作为 additive attention bias，DNN 用 feature gating；p_itr 使用 stop-gradient，防止干扰曝光任务。
  3. Sequence-level Click Distribution Matching：对 click logits 做 softmax 得到点击分配分布，与真实点击分布做 KL；零点击序列给 uniform 目标，捕捉序列内点击竞争。
- 训练采用多任务 loss：L_ITR（全部位置的 BCE） + L_CTR（仅曝光位置的 masked BCE） + λ L_ClkDist。推理时用 Σ p_itr_k · p_ctr_k · w_k 计算序列期望效用。

**关键实验**：在 48.38M 用户、141.79M 序列的电商重排数据集上，ICE 在 DNN、DCN、PRM、BiGRNN、Transformer、NLGR-E 六个 backbone 上均带来一致提升。SeqAUC 从 81.22–82.44 提升到 84.33–85.84；Transformer 的 GAUC_ITCTR 从 62.53 提升到 73.91（+11.38%）；PAUC_ITR 从 50.00 提升到 73.84，MAE_T 从 3.92 降到 1.04。14 天在线 A/B 测试中，点击 +0.70%，商业收入 +3.67%，LT-14d +0.23%，延迟增加 <0.5ms，已全量部署。

**最值得记住的一句话**：序列级效用不是 item 的静态属性，而是通过用户浏览旅程动态实现的；只有建模 exposure→click 链和曝光衰减，才能高保真评估候选序列。
