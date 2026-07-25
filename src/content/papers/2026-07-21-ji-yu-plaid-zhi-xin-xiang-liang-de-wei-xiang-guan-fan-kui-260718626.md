---
title: 'PLAID-PRF: Pseudo-Relevance Feedback with Centroid-like Tokens in PLAID'
title_zh: 基于 PLAID 质心向量的伪相关反馈查询扩展
authors:
- Xiao Wang
- Sean MacAvaney
- Craig Macdonald
affiliations:
- University of International Business and Economics
- University of Glasgow
arxiv_id: '2607.18626'
url: https://arxiv.org/abs/2607.18626
pdf_url: https://arxiv.org/pdf/2607.18626
published: '2026-07-21'
collected: '2026-07-25'
category: RecSys
direction: 质心感知的伪相关反馈优化多向量检索
tags:
- Multi-vector retrieval
- Pseudo-Relevance Feedback
- PLAID
- ColBERT
- Centroid
- Efficiency
one_liner: 利用多向量检索索引中的质心向量进行伪相关反馈，以很低计算开销提升检索效果
practical_value: '- **低计算量查询扩展用于检索**：直接复用 PLAID 索引中的质心向量作为“伪 token”，避免对返回文档进行重编码或
  token 聚类，适合电商搜索等低延迟场景。

  - **质心选择策略可迁移**：采用“高用途且多样化”的挑选方式，防止冗余；在商品搜索中可对初检结果提取代表性语义向量作为扩展词，提升长尾查询召回。

  - **反馈检索流程简单**：扩展后的查询仅需再次运行同一索引的向量检索，无需额外模型或复杂工程，易于集成到现有流水线。

  - **思路可泛化到生成式推荐**：若将推荐对象编码为多向量或 token 序列，可利用类似质心反馈机制对用户表示进行实时调整，捕获近期行为偏好。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：多向量检索模型（如 ColBERT）在信息检索中效果突出，但伪相关反馈（PRF）对其应用存在计算瓶颈——需对首次检索到的文档 token 进行在线聚类以生成扩展向量。PLAID 通过质心量化大幅压缩索引并加速检索，但并未利用反馈信号改进查询表示。本文希望在不增加大量计算的前提下，将 PRF 能力引入 PLAID 架构。

**方法**：提出 **PLAID-PRF**，将 PLAID 索引中的质心向量视为类似 token 的单元。对初检结果，选择一小批多样且高信息量的质心向量作为“扩展向量”，直接拼接到原查询的多向量表示后，再次执行 PLAID 检索（包括质心匹配、候选生成和排序）。整个过程无需对原始文档 token 进行重处理，完全在质心空间完成，计算开销极低。

**关键结果**：在 MSMARCO 和四个 BEIR 数据集上，PLAID-PRF 相比 PLAID 提升最高 **4.3% nDCG@10** 和 **7.3% MRR@10**，在多数领域一致优于不使用反馈或使用传统 PRF 的基线。延迟实验中，它比需要在线聚类的 ColBERT-PRF 快 **4.7 倍**，索引尺寸仅增加 0.3%。证明了在质心级别进行 PRF 是一种高效且有效的多向量检索增强方案。
