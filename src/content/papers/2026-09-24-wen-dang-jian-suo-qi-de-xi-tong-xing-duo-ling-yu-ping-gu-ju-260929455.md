---
title: A Systematic Multi-Domain Evaluation of Document Retrievers
title_zh: 文档检索器的系统性多领域评估：33模型×7数据集
authors:
- Valentin Velev
- Andreas Spitz
affiliations:
- University of Konstanz
arxiv_id: '2609.29455'
url: https://arxiv.org/abs/2609.29455
pdf_url: https://arxiv.org/pdf/2609.29455
published: '2026-09-24'
collected: '2026-09-27'
category: Eval
direction: 检索模型评测与选型
tags:
- document retrieval
- evaluation
- dense retrieval
- sparse retrieval
- SPLADE
- NV-Embed
one_liner: 统一算力预算下离线评测33个检索器，揭示NV-Embed-v2质量高但延迟大、SPLADE-v3低延迟且MS MARCO最强、GritLM指令跟随最优。
practical_value: '- 在电商搜索/推荐召回或 RAG 中，若在线 query 延迟敏感，优先考虑 SPLADE-v3：作为 sparse retriever，其质量接近
  top dense 模型，且 MS MARCO 上达到最高分，延迟显著低于 NV-Embed-v2。

  - 对需要遵循指令的检索任务（如个性化 query 改写后的召回、多意图搜索），优先评估 GritLM 这类指令跟随 dense retriever；可将其作为指令检索路的候选模型。

  - 选型时不要只看单一 benchmark：本论文的多域评估和失败点分析表明不同模型/家族存在互补性，可在工程上采用 sparse+dense 多路召回融合提升鲁棒性。

  - 复现论文的 off-the-shelf + 统一 compute budget 实验方式，可作为内部检索模型基线评测流程，避免过度调参导致不可比较。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：文档检索器种类繁多，但已有对比研究通常局限于单一基准、领域或模型家族，难以判断不同方法在质量、延迟和失效模式上的真实 trade-off。

**方法**：覆盖 sparse、dense、expansion-based 三类共 33 个检索器，在 7 个 IR 数据集上做统一评测。所有模型均采用公开文档可重建的 off-the-shelf 配置，不单独调参，并在统一算力预算下分析检索质量、query 延迟和 failure points。

**关键结果**：
- NV-Embed-v2 在 4/7 数据集上取得最强性能，但 query 延迟较高；
- SPLADE-v3 作为 sparse retriever，质量接近 top 模型且延迟低很多，并在 MS MARCO 上拿到最高分；
- GritLM 在指令跟随数据集上表现最佳；
- 失效点分析显示不同模型和家族间存在明显差异，提示混合/互补策略还有未挖掘的检索性能空间。
