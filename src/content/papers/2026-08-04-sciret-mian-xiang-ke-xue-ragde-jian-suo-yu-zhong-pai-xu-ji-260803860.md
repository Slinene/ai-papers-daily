---
title: 'SciRet: A Compute-Aware Empirical Study of Retrieval and Reranking for Scientific
  RAG'
title_zh: SciRet：面向科学RAG的检索与重排序计算感知实证研究
authors:
- Kaysarul Anas Apurba
- Md. Hasibul Hasan
- Rofiqul Alam Shehab
- Asab Azad
affiliations:
- Laurentian University
- North South University
arxiv_id: '2608.03860'
url: https://arxiv.org/abs/2608.03860
pdf_url: https://arxiv.org/pdf/2608.03860
published: '2026-08-04'
collected: '2026-08-07'
category: RAG
direction: 科学RAG检索与重排序实证分析
tags:
- RAG
- retrieval
- reranking
- domain mismatch
- hybrid search
- scientific QA
one_liner: 在科学问答RAG中，混合检索更鲁棒，跨域重排序可能有害，且生成忠实度随语料规模增大而提升。
practical_value: '- 电商搜索/推荐场景的 RAG 系统应优先采用混合检索（稀疏 BM25 + 稠密向量），它在不同索引规模下均更鲁棒，可避免单一方式在长尾或新类目上的性能塌陷。

  - 重排序模型必须使用领域内数据微调；直接使用通用 Web 数据（如 MS MARCO）训练的 cross-encoder 会因领域不匹配而损伤检索精度，建议用业务日志中的点击/转化数据构建正负例进行微调。

  - 随索引语料规模增大，生成回答的忠实度（faithfulness）可能自然提升，但需权衡计算成本；在工程上可考虑分层检索或动态调整检索深度。

  - 句子窗口分块策略简单有效，适用于商品描述、用户评论等长文本场景，可作为 baseline 快速验证。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：科学文献问答中，RAG 流水线常直接沿用通用搜索组件，但领域差异可能导致检索、重排序、生成的行为未知，尤其在不同语料规模下的效果缺乏控制实验。

**方法**：在 CORD-19 数据集上抽取 1K、5K、15K 论文样本，固定流水线配置：句子窗口分块、BM25 稀疏检索、BGE-M3 稠密检索、倒数秩融合（RRF）混合，可选 MS MARCO 训练的 cross-encoder 重排序，最后以有根据的生成方式回答。检索评估使用混合系统导出的伪相关标签，不依赖人工标注。

**关键结果**：
- 混合检索在 1K 和 15K 规模上都达到 Recall@10 = 1.000，比稀疏或稠密单用更稳定。
- 加入 cross-encoder 重排序后，检索精度反而下降，体现领域不匹配的负面效应。
- 生成忠实度（RAGAS 指标）随索引规模增大而提升。
- 实验代码、索引、评估结果已开源，便于复现。
