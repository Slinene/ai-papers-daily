---
title: 'Training with Missed Targets in Generative Recommendation: Separating Supervision
  from Probability Competition'
title_zh: 生成式推荐中未召回目标的训练：解耦监督与概率竞争
authors:
- Xuesi Wang
- Yangbin Shi
- Xiaolin Zheng
affiliations:
- Zhejiang University
- Independent Researcher
arxiv_id: '2610.10124'
url: https://arxiv.org/abs/2610.10124
pdf_url: https://arxiv.org/pdf/2610.10124
published: '2026-10-07'
collected: '2026-10-08'
category: GenRec
direction: 生成式推荐 · 候选补全与重排训练
tags:
- generative recommendation
- semantic ID
- candidate completion
- listwise learning
- reranking
- probability competition
one_liner: 用 WN/Cond/Full 三损失分离补全候选的监督收益与跨组概率竞争，证明竞争可损害重排。
practical_value: '- 在生成式推荐/固定候选池重排中，不要默认把离线未召回目标直接 append 到训练 list；append 同时改变已召回目标权重、增加
  training-only 监督并引入跨组 softmax 概率竞争。建议用 WN/Cond/Full 等效三损失做消融，定位端到端提升/下降来自监督还是竞争。

  - 若必须使用 missed targets 作为训练专属正样本，可对 returned group 与 appended group 分别归一化（Cond），避免二者竞争总概率；实现只需训练两个
  group 内 listwise CE 的加权和，无需构造 offset。

  - 多路召回/多候选源可扩展为每个 source 一个共享 offset 的分组条件训练；soft/nonuniform target weights 同样适用，零质量
  source 用相应无限 offset 极限。

  - 上线决策：用 development 用户比较 best returned-only 与 best appended-target reranker，指标用
  FT-NDCG@20（分母保留未召回 target）；仅当调整后 lower CI > τ 才切换，并按 generator 独立决定，避免全局默认 append。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：生成式推荐先由 generator 产出 semantic ID 候选集，reranker 只排序这些 returned candidates；但离线观测目标中未被 generator 召回的部分经常被 append 到训练 list，inference 却不会再出现。这个操作一次性改变三件事：已召回目标的 loss 权重、对 missed targets 的额外监督、以及 returned 与 appended 两组之间的 softmax 概率竞争。简单比较 append/no-append 无法定位排序变化来源。

**方法关键点**：把完整 listwise CE 分解为 T_N=αL_N、T_A=γL_A、T_mass。固定相同候选、scorer、优化器，构造三种损失：WN=T_N；Cond=T_N+T_A，对 N 和 A 分别归一化，消除跨组概率竞争；Full=T_N+T_A+T_mass，单 softmax 包含竞争。Cond 可通过给所有 appended score 加同一 offset δ 并最小化 Full 得到，实施时直接训两个 within-group 损失。比较 Cond−WN 可评估 appended 监督收益，Cond−Full 可评估竞争伤害。Inference 仍只对 N 排序；评估覆盖所有用户。

**关键结果数字**：RecIF-Ads/OneRec 上 epoch60 时，Cond−Full FT-NDCG +0.007423 [0.004978,0.009744]，Cond−WN +0.001877；把 Full 初始化到正确 appended-group 概率提升 +0.009233。Amazon Video Games 预设对比中，去掉竞争四个估计全部为正，提升 7.8%–22.2%（MLP 22.23%、12.84%，attention 7.83%、13.16%）。A-Health held-out 上按开发集规则全部保持 returned-only，避免强制 append 的 1.7% FT-NDCG 损失。

**最值得记住**：候选补全不是中性提监督操作；必须把“训练专属候选的监督”与“跨组概率竞争”拆开，并按每个 generator 用开发集下界决定是否启用。
