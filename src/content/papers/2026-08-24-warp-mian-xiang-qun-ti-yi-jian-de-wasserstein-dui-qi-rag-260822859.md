---
title: 'WARP: Wasserstein-Aligned RAG for Population Opinions'
title_zh: WARP：面向群体意见的 Wasserstein 对齐 RAG
authors:
- Aman Singh Thakur
- Aditya Agrawal
- Alwarappan Nakkiran
- Alex Karlsson
affiliations:
- Amazon.com
arxiv_id: '2608.22859'
url: https://arxiv.org/abs/2608.22859
pdf_url: https://arxiv.org/pdf/2608.22859
published: '2026-08-24'
collected: '2026-08-25'
category: RAG
direction: RAG 检索校准 · Wasserstein 对齐意见分布
tags:
- RAG
- Calibration
- Wasserstein Distance
- Opinion Summarization
- Retrieval
one_liner: 用 Wasserstein 距离校准 RAG 检索证据的情感分布，避免少数意见被淹没
practical_value: '- 在电商评论摘要、用户反馈聚合等场景，top-k 检索容易偏向主流意见，可借鉴 WARP 思想：先估计总体意见分布（如情感强度分布），再用
  Wasserstein 距离选择文档子集，使检索证据的分布与总体对齐，避免生成有偏的回答。

  - 工程实现上，WARP 提供三种变体适应不同候选池规模（稠密/稀疏/可变），亚秒级延迟，可在线作为 RAG 检索后处理模块，与现有向量检索无缝集成。

  - 将 Wasserstein 距离作为检索校准的优化目标，比 KL/JS 更合理，因为它保留了情感强度之间的序数关系——强烈负面与强烈正面混淆的代价高于相邻强度混淆。在涉及情感、评分等有序标签的场景中可优先考虑。

  - LLM 生成阶段对检索证据分布敏感，WARP 实验表明校准检索能显著提升生成质量（86% 偏好），因此构建“群体意见总结”类 Agent 时，应将检索校准作为生成前必要步骤。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：RAG 系统用于总结大量文档意见时，标准 top-k 检索按查询相似度排序，导致多数观点主导，少数观点被埋没，生成回答看似共识实则失真。现有多样性重排（MMR/DPP）没有目标分布，校准方法（KL/JS）将意见 bin 视为无序，混淆强烈正负与相邻 bin 的代价相同。

**方法**：WARP 是一族检索后校准算法。首先从余弦排名候选池中恢复被埋没的少数意见文档，然后利用 Wasserstein-1 距离（保留序数结构）选择文档子集，使检索到的情感强度分布匹配总体目标分布。针对稠密、稀疏和可变候选池设计了三种变体，平衡校准质量与速度。

**结果**：在 3 个评论领域、35K 文档、156 查询、26 实体上，域匹配变体将分布误差降低至少 43%，延迟亚秒。在生成评估中，五个 LLM 裁判在 k≤5 时对 WARP 生成答案的偏好达 86%（决定性比较）。
