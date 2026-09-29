---
title: 'Rubric-Calibrated Preferences: Cross-Query Calibration of LLM Judgments via
  Item Response Theory'
title_zh: 基于 IRT 的 Rubric 校准偏好：跨查询统一 LLM 评判尺度
authors:
- Fabian David Schmidt
- Donato Crisostomi
- Carlos Lassance
- Nils Reimers
affiliations:
- Cohere
arxiv_id: '2609.35739'
url: https://arxiv.org/abs/2609.35739
pdf_url: https://arxiv.org/pdf/2609.35739
published: '2026-09-28'
collected: '2026-09-29'
category: Eval
direction: LLM 评判校准 · IRT 跨 query 尺度统一
tags:
- RCP-nDCG
- LLM-as-a-Judge
- Item Response Theory
- Bradley-Terry
- Reranker Evaluation
- Calibration
one_liner: 用 IRT 将 LLM 的 listwise 偏好与共享 rubric 校准为跨 query 可比的连续相关性分数
practical_value: '- 离线评估：商品/广告 reranker 的人工 qrels 稀疏、噪声大，可对候选池一次性跑两阶段 LLM judge 产出连续
  gain，作为新模型离线指标，避免每轮人工标注。

  - IRT 校准可复用：任何 LLM 相对偏好（pairwise/listwise）都能通过共享 rubric 的 τ_j、α_j 映射到统一 logit 尺度，使跨
  query/campaign/类目分数可比；在电商多 query 聚合排序、Agent 工具选择评估中可直接套用。

  - rubric 设计：5 个递增 yes/no criteria（主题相关→信息有用→属性匹配→直接回答→深度覆盖）比单一有用性更稳；业务可自定义准则，并筛选
  discrimination/difficulty 合理的准则。

  - 工程实现：BT tournament 窗口 w=10，先随机后按估计质量抽窗；Stage B 多次重复取 pass share；离线 label 池固定后，新模型只需重排候选即可算
  RCP-nDCG，成本集中在一次 judge 标注。需注意 LLM judge 可能与 LLM 训练的 reranker 有偏好耦合，上线前用盲评人工子集校验。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：reranker 的标准指标 nDCG 依赖稀疏、离散、噪声大的人类 qrels；随着模型差距缩小，nDCG 大量出现饱和、触底或压缩，难以区分接近的模型。LLM 相对判断细粒度但跨 query 不可比，绝对 rubric 可比但太粗。需要融合两者。

**方法关键点**：
- Stage A：listwise Bradley-Terry tournament，对每个 query 的候选文档窗口打分并拟合 BT 分数，保留细粒度排序。
- Stage B：5 个递增难度的 yes/no rubric 准则（Topical Relevance、Information Utility、Entity/Detail Match、Direct Answer、Thorough Treatment）由 LLM 逐文档判断。
- 2PL IRT 校准：pass 概率为 σ[γ_c(τ_j θ_BT_i + α_j - β_c)]，共享准则参数同时估计 query 的 scale τ_j 和 offset α_j，把 BT logit 映射到统一尺度。
- RCP-nDCG 使用连续 gain g(θ)=Σγ_c σ(γ_c(θ-β_c))/Σγ，其斜率与 Fisher information 成正比；理想排序保持 Stage A 顺序。

**关键实验**：在 NanoBEIR、BRIGHT、ViDoRe v3、TREC-DL 上评估 14 个 reranker。对 46 名盲评标注者，RCP gain 的 AUC 为 0.910，qrels 仅 0.651；query 均值与人工分 Spearman 从 0.538 升到 0.795。在 185 个 contests 中两者仅一方一致时，RCP-nDCG 在 72.4% 对齐人工偏好；所有 NIST-decisive reranker pairs 上一致。灵敏度上，NanoBEIR 的显著区分比例从 qrel-nDCG 的 34.1% 升到 63.5%。

**最值得记住**：单一 query 内用 BT 序，跨 query 尺度由共享 rubric 准则经 IRT 锚定；相对序和绝对标准二者缺一不可。
