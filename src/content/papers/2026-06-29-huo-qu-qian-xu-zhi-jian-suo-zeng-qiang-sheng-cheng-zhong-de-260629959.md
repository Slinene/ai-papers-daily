---
title: 'Know Before You Fetch: Calibrated Retrieval-Budget Allocation for Retrieval-Augmented
  Generation'
title_zh: 获取前须知：检索增强生成中校准的检索预算分配
authors:
- Zhe Dong
- Fang Qin
- Manish Shah
- Yicheng Wang
affiliations:
- University of Maine at Presque Isle
- Stanford University
- Independent Researcher
arxiv_id: '2606.29959'
url: https://arxiv.org/abs/2606.29959
pdf_url: https://arxiv.org/pdf/2606.29959
published: '2026-06-29'
collected: '2026-06-30'
category: RAG
direction: 自适应检索预算分配 · RAG 校准
tags:
- RAG
- Calibration
- Retrieval Budget
- Uncertainty Estimation
- Probability Interface
- Adaptive RAG
one_liner: 为 RAG 提出校准概率接口，依置信度分配检索预算（闭卷/紧凑/完整/弃答），实现延迟与准确率权衡
practical_value: '- 在检索增强的推荐或搜索系统中，可以根据模型置信度自适应调整检索深度（如仅用闭卷回答或检索少量文档），节省计算资源并减少延迟。

  - 将序列对数概率等不确定性信号校准为正确性概率，用于选择性召回或拒绝回答，避免低质量输出影响用户体验，尤其适合高可靠性要求的排序或问答环节。

  - 提供校准后的概率接口，允许系统在延迟和准确率之间显式权衡，可通过设置不同阈值适应不同场景（如高吞吐的广告检索与低延迟的在线推荐）。

  - 离线校准步骤（如 Platt scaling）能大幅降低预期校准误差（ECE），直接移植到电商 RAG 管道中，提升检索决策的可靠性。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机：**传统 RAG 对每个查询固定检索相同数量的段落，既浪费计算，又可能引入噪声。当模型已掌握答案时，多余检索是冗余的；无关或部分相关的段落反而会干扰 reader。

**方法：**将自适应 RAG 形式化为校准检索预算分配：给定查询，根据置信度决定闭卷回答、检索 1 条、检索 5 条或弃答。核心贡献是提供一个概率接口，而非新的原始不确定性信号。具体步骤：先用序列对数概率或前缀 logit 边缘等信号表征不确定性，再通过 out-of-fold 校准（如 Platt scaling）将其转化为“回答正确”的校准概率。基于这些概率设定阈值，实现分级上下文选择、选择性弃答，并支持显式的延迟/ token 权衡。

**关键结果：**在 TriviaQA、NQ、MS MARCO 等 QA 数据集上，校准显著提升概率质量：序列对数概率的 ECE 从 0.275 降至 0.062（TriviaQA）、0.643 降至 0.009（NQ）、0.711 降至 0.031（MS MARCO）。分级检索改善了完整上下文和段落预算前沿，而检索调用 AUC 与二元门控基本持平。延迟测试揭示门控并非总是更快：Qwen3-8B 延迟增加 27%，但 Qwen3-32B 节省约 8%，表明需结合系统特性权衡。该方法提供了一套在任务和系统约束下分配检索预算的可重用接口。
