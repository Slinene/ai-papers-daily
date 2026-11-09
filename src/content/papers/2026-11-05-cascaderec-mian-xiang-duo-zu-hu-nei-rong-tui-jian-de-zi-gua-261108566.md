---
title: 'CascadeRec: Deployed Adaptive LLM Compute Allocation for Multi-Tenant Content
  Recommendation'
title_zh: CascadeRec：面向多租户内容推荐的自适应 LLM 计算分配
authors:
- Kai Zhao
- Guilin Zhang
- Xiang Cheng
- Xiquan Cui
- Henry Heng
- Xu Chu
- Alet Blanken
affiliations:
- Workday AI Research
arxiv_id: '2611.08566'
url: https://arxiv.org/abs/2611.08566
pdf_url: https://arxiv.org/pdf/2611.08566
published: '2026-11-05'
collected: '2026-11-09'
category: RecSys
direction: LLM 重排序级联与推理优化
tags:
- LLM
- Cascade
- Reranking
- Multi-Tenant
- Inference Efficiency
- Recommendation
one_liner: 部署两级 LLM 重排序级联，仅升级可能受益的请求，推理成本降低约 10% 且无质量回退
practical_value: '- 推荐系统接入 LLM 重排序时优先考虑级联架构：先用轻量 Tier-1 模型覆盖全量请求，再用路由器根据历史长度、置信度等特征选择少数请求升级到昂贵
  Tier-2。生产数据显示推理成本降低约 10%，延迟影响很小。

  - 对冷启动或历史稀疏用户，LLM 重排序不一定是增益，公开数据集上甚至会降低 NDCG@10 最多 30%。可按用户历史长度做分段门控，对稀疏用户跳过 LLM
  或回退到传统排序，避免负收益。

  - 多租户内容推荐中，跨租户负载不平衡可以作为级联的触发信号：用便宜 Tier-1 吸收常规流量，只对高价值或高不确定性请求分配昂贵推理，能有效控制 P99 延迟和成本。

  - LLM 输出解析失败需要在 serving 层兜底，例如回退到 Tier-1 排序结果或规则逻辑，避免整个请求失败；这一点在真实电商 / 内容推荐场景中同样关键。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：LLM 作为推荐重排序器有吸引力，但对每个请求运行昂贵模型成本高，且对历史稀疏用户经常降低质量。论文提出 CascadeRec，一个已在生产部署的两级 LLM 重排序级联，服务于 FP&A SaaS 多租户内容推荐。

**方法关键点**：轻量 Tier-1 模型对所有请求重排序；路由器只升级那些额外推理计算可能带来收益的请求，升级到更昂贵的 Tier-2 过程，可选 self-consistency sampling、多路径推理或更大模型。系统运行在 AWS EKS 和 GKE 上，面向企业租户推荐报告、分析等专业内容。

**关键结果**：生产 A/B 实验超过一个月，与统一使用昂贵 tier 相比，推理成本降低约 10%，延迟影响极小，未观察到质量回退。由于租户数据不可公开，在 MovieLens-1M 和 Amazon-Electronics 上评估：分段分析显示统一 LLM 重排序对稀疏历史用户 NDCG@10 降低高达 30%，唯一显著增益只出现在历史最长的分段。升级冷用户反而加重损失，不同领域受益分段不同，因此生产中采用分段门控 rollout。此外还讨论了跨租户负载不平衡作为级联动因，以及 serving 层处理 LLM 输出解析失败的经验。
