---
title: Scalable, Transferable Meta-network for Data Selection Requires a Different
  Loss (and Why the Obvious Choice is Problematic)
title_zh: 可扩展可迁移的元网络数据选择需要不同损失
authors:
- Zilin Du
- Bowen Yang
- Boyang Albert Li
affiliations:
- Nanyang Technological University
arxiv_id: '2610.02092'
url: https://arxiv.org/abs/2610.02092
pdf_url: https://arxiv.org/pdf/2610.02092
published: '2026-10-01'
collected: '2026-10-03'
category: Training
direction: LLM 训练数据选择与迁移
tags:
- Data Selection
- Meta-learning
- LLM Training
- Transferability
- Pointwise Value Matching
one_liner: 提出TESS框架与PVM损失，解决元数据选择网络中的权重抑制与易学特征依赖，实现跨数据集跨模型迁移
practical_value: '- 在电商/推荐/Agent 场景中，可以用小模型或子集训练一个数据选择网络，再直接用于大模型或全量语料，降低多领域语料（商品描述、搜索日志、指令数据）的清洗与配比成本。

  - 工程实现上，数据打分网络建议使用 pointwise value matching 回归目标，而不是直接嵌入现有 MTS 排序或对比损失，以避免权重抑制和依赖易学特征导致的不稳定优化。

  - 该方法支持跨数据集迁移，可训练一个通用数据选择器对 query 改写、商品标题生成、会话数据等异构语料动态赋权，提升指令微调效率。

  - 若业务存在安全或领域定向微调需求，可复用该框架在目标验证集上自动学习数据权重，替代手工规则或启发式评分。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

## 动机
LLM 训练依赖大规模异构语料，数据选择至关重要。现有基于 Meta-learning 的训练数据选择（MTS）方法在细粒度估值和迁移性之间存在权衡：逐样本权重难以泛化到未见数据，而直接引入选择网络会因权重抑制和依赖易学特征导致优化不稳定、泛化差。

## 方法关键点
- 提出 TESS（Transferable Example Scoring and Selection）框架，用选择网络替代 per-sample weights，实现可扩展与可迁移的数据估值。
- 核心是 Pointwise Value Matching（PVM）损失，以逐点价值匹配的方式训练选择网络，避免将网络直接嵌入现有 MTS 目标导致的权重抑制与易学特征依赖。
- 框架支持从子集到全量语料、从较小模型到较大模型的迁移。

## 关键结果
实验覆盖 LLM 安全训练与定向指令微调，结果显示 TESS 在跨数据集、从子集到全量、从小模型到大模型场景下均表现出强迁移能力，优于直接使用现有 MTS 目标的基线。
