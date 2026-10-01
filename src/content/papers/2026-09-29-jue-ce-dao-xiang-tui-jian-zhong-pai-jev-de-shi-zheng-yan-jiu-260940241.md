---
title: 'Decision-Oriented Recommendation Reranking: An Empirical Study of Jev'
title_zh: 决策导向推荐重排：Jev 的实证研究
authors:
- Hanjia Lyu
- Yinglong Xia
affiliations:
- Singapore Management University
- Meta AI
arxiv_id: '2609.40241'
url: https://arxiv.org/abs/2609.40241
pdf_url: https://arxiv.org/pdf/2609.40241
published: '2026-09-29'
collected: '2026-10-01'
category: RecSys
direction: 决策导向模型与 LLM 重排权衡
tags:
- decision-oriented
- reranking
- LLM
- latency
- hard negatives
- empirical study
one_liner: 在候选集大小为20-200的受控重排中，Jev效果与点式Qwen相当且延迟增长更缓，占据独特质量-延迟区间
practical_value: '- 当重排任务本质是「从预定义候选集中做选择」时，可以尝试决策导向模型（直接输出候选概率分布）替代通用 LLM 的点式/列表式重排，在候选集增大时延迟增长更缓，适合对
  latency 敏感但希望保留文本语义理解的场景。

  - 评估重排器必须把候选集大小 K 作为核心维度：小 K 下 listwise Qwen 效果尚可，K≥100 时 NDCG@10 从 0.519 骤降到 0.065（Movies），结论不能跨
  K 泛化；工程选型时应在目标 K 区间内实测质量-延迟曲线。

  - 构造 hard negatives 时可用 retrieval 模型 SASRec 的 top-K 非目标项，而不是随机负样本，这样能更好隔离重排能力与检索失败，并让所有方法在同一批
  behavioral plausible 候选上对比。

  - 对比 hosted API 模型与本地 GPU 模型时，延迟必须统一口径为 observed serving latency（包含网络、重试、排队），否则会严重低估远程模型的真实耗时；业务上线前应同时记录
  median 和 P25/P75 分布。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：推荐系统通常采用两阶段架构，重排阶段需要从几十到几百个候选物品中选出最优排序。LLM 重排虽然表达能力强，但点式方法延迟随候选数线性增长，列表式方法在候选集变大时排序质量下降明显。本文研究一种新的决策导向模型 Jev（TypeSafe AI 的“System One Model”），它不走自由文本生成，而是直接输出候选集上的概率分布，看它能否在推荐效果和延迟之间提供不同的权衡点。

**方法关键点**：
- 受控硬候选重排：用 SASRec 作为检索模型，只保留 ground-truth 在 top 200 内的用户；对每个用户构造候选集 {ground-truth} ∪ SASRec top-K 非目标项，K∈{20,50,100,200}，所有方法共享同一批候选，候选顺序随机化。
- 对比方法：SASRec 和 DCNv2 作为推荐专用 baseline；Qwen2.5 7B Instruct 分别做点式（每个候选独立打 relevance 分）和列表式（所有候选联合打分）重排；Jev 把用户近期交互历史作为 decision state，候选物品作为 choice alternatives，直接返回每个候选的概率作为排序分。
- 数据集：Amazon Reviews 2023 中的 Movies and TV、Video Games、Books 三个领域，采用 5-core leave-last-out 划分；对语言类方法使用标题、类目、描述前 250 字符等文本元数据，并只暴露最近 10 条交互。
- 延迟测量：本地模型在单块 A800 GPU 上计时，Jev 通过 hosted API 记录 observed serving latency。

**关键结果**：
- 推荐效果上，Jev 在三个领域均保持高 NDCG@10，尤其在 Video Games 和 Books 上普遍超过点式 Qwen；点式 Qwen 在小 K 时接近 Jev，但列表式 Qwen 在 K≥100 时质量急剧下降（如 Movies K=200 时 NDCG@10 仅 0.039，Jev 为 0.080）。
- 延迟扩展上，点式 Qwen 从 K=20 到 200 延迟约从 1.5s 增到 14.9s，Jev 仅从约 0.5s 增到 0.9s，增长远更缓慢；但 SASRec 和 DCNv2 仍保持在毫秒级。
- 质量-延迟图上，Jev 在多数 K 和领域落在非支配边界上，形成独特的运行区域。

**最值得记住的一句话**：当排序本身是主要输出且候选集预定义时，决策导向模型提供了一种在推荐质量与延迟之间更平缓扩展的替代方案，但需警惕 hosted API 与本地模型的延迟不可直接比较。
