---
title: 'Computation Over Geometry: Meaning Identity Is Computed, Not Shipped in the
  Embeddings'
title_zh: 计算而非几何：意义同一性是计算产生的，不是嵌入自带
authors:
- Jiaqi Deng
affiliations:
- Independent Researcher
arxiv_id: '2609.28290'
url: https://arxiv.org/abs/2609.28290
pdf_url: https://arxiv.org/pdf/2609.28290
published: '2026-09-23'
collected: '2026-09-24'
category: RAG
direction: RAG 语义向量假设的实证挑战
tags:
- Embeddings
- RAG
- Paraphrase
- Bi-encoder
- Cross-encoder
- Probing
one_liner: 系统实证显示同义改写判断依赖句子在同一前向中的联合计算，冻结双塔向量几乎无法读出该关系
practical_value: '- 同义 query 归一化、商品标题同款识别、广告文案去重等任务中，不要依赖双塔向量 cosine 相似度（AUC 仅 0.55-0.65）。直接用
  cross-encoder / 联合前向读头，或现成 BGE-reranker-large（AUC 0.94），1.5B 联合 probe 即可达 0.90+，成本可控。

  - 搭建召回/检索时，dense 双塔召回对 paraphrase 类语义不够敏感，建议增加 hybrid retrieval，并用联合注意力的 reranker
  做第二跳，而不是期望单塔召回解决含义等价问题。

  - 若为线上性能必须保留双塔结构，可从联合教师模型（如 BGE-reranker）蒸馏分数到小型联合读头或非线性 pair 模块；但注意 bi-encoder
  直接 fine-tune 到 paraphrase benchmark 会显著损失 STS-B/QQP 迁移（Spearman 下降约 0.25），需任务隔离或加通用损失。

  - 对 query 改写、push 文案、广告创意等生成后需要判断"是否同一意图/同义"的场景，优先用 LLM/联合编码核对，而不是保存的句子向量比较。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：检索和 RAG 普遍把 meaning identity（两个句子改写后是否同义）当作句子独立编码后的几何距离问题，但缺乏对冻结模型实际能力的检验。

**方法关键点**：在 PAWS-X 重叠匹配子集上，系统比较双塔编码器（BGE/E5/GTE/MiniLM/E5-Mistral-7B）与 Llama 3/Mistral/Qwen 等 LLM 的独立编码、late fusion、joint forward pass、非线性 pair 读头、现成 reranker，以及 bi-encoder fine-tune 后的迁移效果。

**关键结果数字**：独立双塔密集向量 AUC 仅 0.55-0.65（dense peak 0.70）；联合前向读头在 1.5B-32B 上达 0.90-0.96，partner shuffle 后掉到随机水平，GPT-2 XL 也有 0.76；跨因果 LM、双向编码器、encoder-decoder 架构均有相同模式。线性读头无论多少训练对都学不到；非线性 pair 读头在完整 49k 训练对上只能部分恢复（0.68-0.87）。现成 reranker 出现分化：BGE-reranker-large 达 0.94，但 MS-MARCO/Jina reranker 仍在 0.55-0.64。bi-encoder 可 fine-tune 拟合 PAWS（0.87-0.93），但 STS-B Spearman 下降约 0.25。结论：同义身份更像一次联合计算操作，而非句子向量的几何属性。
