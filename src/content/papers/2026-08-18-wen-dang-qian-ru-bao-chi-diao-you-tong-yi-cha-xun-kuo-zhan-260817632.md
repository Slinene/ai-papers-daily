---
title: 'DEPT: Document Embedding Preservation Tuning for Unified Query Expansion and
  Retrieval'
title_zh: 文档嵌入保持调优：统一查询扩展与检索
authors:
- Jingyuan Wang
- Richong Zhang
- Zhijie Nie
- Mingxin Li
- Yanzhao Zhang
affiliations:
- Beihang University
arxiv_id: '2608.17632'
url: https://arxiv.org/abs/2608.17632
pdf_url: https://arxiv.org/pdf/2608.17632
published: '2026-08-18'
collected: '2026-08-19'
category: QueryRec
direction: LLM 统一查询扩展与稠密检索
tags:
- Query Expansion
- Dense Retrieval
- LLM
- Document Embedding Preservation
- Whitening
- Straight-Through
one_liner: 通过文档嵌入保持、白化、在线硬负样本与直通解码，实现 LLM 在统一查询扩展与稠密检索中的稳定端到端训练
practical_value: '- 在电商搜索 query 改写/扩展中，可借鉴 DEPT 思路：用同一 LLM 做改写和向量编码，但保持文档侧嵌入稳定，避免频繁重建全库向量索引；工程上可先缓存文档嵌入，微调时只更新
  query 侧，上线时直接复用原有向量库，节省推理与索引成本。

  - 采用固定白化（whitening）预处理向量空间，缓解 LLM 原始嵌入的各向异性，提升 cosine 检索效果；实践中可以基于已有文档向量估计白化矩阵，训练时保持文档分布稳定，该矩阵可持续有效。

  - 直通解码（straight-through）将检索排序损失直接传到生成 logits，可用来优化 query 生成策略，让生成式改写直接以召回/排序指标为学习信号，而非仅文本相关；在线硬负样本挖掘能提供与当前
  query 行为匹配的难负样本，提升训练效率。

  - 短扩展变体（DEPT-K）用关键词式 prompt 控制生成极短扩展（~9 tokens），在几乎不增加线上延迟的情况下达到接近长扩展效果，适合电商搜索高并发低延迟场景。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：LLM 可同时完成查询扩展和稠密检索编码，但现有系统要么仅用提示扩展、要么分阶段训练，扩展生成与最终检索损失不对齐。直接端到端训练统一 LLM 会带来 moving-target 问题：检索梯度一方面应改善 query 侧扩展，另一方面也移动文档嵌入，导致检索目标漂移、生成能力退化。

**方法关键点**：
- 单一 decoder-only LLM 生成扩展并编码扩展查询与文档。
- DEP 损失：将当前文档嵌入与初始模型缓存的文档嵌入的角距离作为惩罚，保持文档侧稳定。
- 固定白化：在缓存文档嵌入上估计 whitening 变换，缓解嵌入各向异性，与 DEP 保持配合。
- 直通解码：通过 top-k soft embedding 的直通估计把 InfoNCE 检索损失传回扩展 token logits。
- 在线硬负样本：使用固定白化文档索引每步搜索难负样本，再重新编码当前模型参与对比学习。
- 采用 LoRA 训练，参数量小。

**关键实验**：在 Qwen3-4B-Instruct-2507 与 LLaMA-3.2-3B-Instruct 两个 backbone 上，在 BEIR 的 SciFact、ArguAna、NFCorpus、FiQA、SCIDOCS 五个数据集评估。DEPT 平均 nDCG@10 最高：Qwen 42.59 vs 最佳 baseline ExpandR 41.09；LLaMA 39.60 vs 38.17。短扩展 DEPT-K 仅用约 9 tokens 在 Qwen 上达 41.45。消融显示去除白化损失最大下降（50.82→42.09）；去除 DEP 损失也明显下降（46.95）。缓存索引兼容：DEPT 在 cached-index 与 re-encoded 索引上表现接近；无 DEP 损失时 cached-index 平均 nDCG 下降 42.77。生成能力：DEPT 平均表现 76.28，接近基座 77.56，而普通对比学习坍塌至 9.32。

**最值得记住的一句话**：训练 query 行为要激进，但保持文档嵌入可复用。
