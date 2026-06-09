---
title: When Should Queries Be Decomposed? A Stage-Aware Study of Query Decomposition
  for Multi-Condition Retrieval
title_zh: 多条件检索中查询分解的阶段效应研究
authors:
- Bochao Yin
- Xuan Lu
- Zhengyu Qi
- Xiaoyu Shen
affiliations:
- Ningbo Key Laboratory of Spatial Intelligence and Digital Derivative
- Eastern Institute of Technology, Ningbo
- Shanghai Jiao Tong University
arxiv_id: '2606.08577'
url: https://arxiv.org/abs/2606.08577
pdf_url: https://arxiv.org/pdf/2606.08577
published: '2026-06-07'
collected: '2026-06-09'
category: RecSys
direction: 多条件检索 · 查询分解阶段性效应
tags:
- Multi-Condition Retrieval
- Query Decomposition
- Reranking
- Semantic Dilution
- Stage-Aware Framework
- Hard Negative Discrimination
one_liner: 发现查询分解在初始检索时因语义稀释而有害，在重排序时能提升细粒度约束验证，提出分阶段分解框架
practical_value: '- **分阶段使用查询分解**：在召回阶段保留原始完整查询，避免将多条件查询拆成子查询导致语义稀释、召回失败和易负样本增多；仅在重排序阶段引入固定大小（2-3个条件）的子查询分解，配合
  Score-Sum 融合，能显著提升对硬负样本的区分能力。

  - **重排序阶段的细粒度验证**：利用分解后的子查询与候选文档进行逐条件匹配，让 LLM reranker 做 token 级交互验证，提升 win rate
  和 NDCG，尤其适用于电商中带多属性约束的商品搜索（如“轻薄 16GB RAM <$1500 游戏本 512GB SSD”）。

  - **固定大小分解与自适应分解的选择**：固定大小（k=2,j=3）优于单条件朴素分解和 LLM 自适应分解，实现简单且效果稳定；若业务中有更复杂的嵌套意图，可考虑用
  LLM 动态决定分解粒度，但需注意推理成本。

  - **避免召回阶段的查询分解**：实验证明在 dense retriever（BGE、Qwen3-Embedding 系列）上，对复杂查询进行分解再融合会降低
  Recall@50 和 NDCG@10，主要由语义稀释导致，该结论对双塔召回架构下的多条件搜索有直接警示意义。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
多条件检索要求同时满足多个独立约束（如“轻薄、16GB RAM、低于$1500、游戏本、512GB SSD”），现有 dense retriever 常将与主题相关但违反个别约束的“硬负样本”排在高位。查询分解被广泛用于复杂查询处理，但其在不同检索阶段（召回 vs. 重排序）的效果缺乏系统研究。本文针对这一问题，在 MultiConIR 和 SSRB 基准上开展阶段感知的实证分析，并提出分阶段分解框架。

**方法关键点**  
- **现象诊断**：发现查询分解在召回阶段导致性能下降，根源是“语义稀释”——子查询失去全局联合约束，匹配大量仅满足局部条件的易负样本，召回失败率从 <1% 飙升至 3.5%~12%。  
- **阶段感知框架**：在召回阶段保留原始整体查询，避免分解；在重排序阶段对候选集使用固定大小分解（每子查询含2~3个条件），用 Score-Sum 融合各子查询的 reranker 分数，实现细粒度约束验证。  
- **分解策略对比**：比较朴素分解（每子查询1条件）、固定大小分解和 LLM 自适应分解，固定大小分解整体最优，Score-Sum 融合优于 RRF。

**关键实验结果**  
- 在 MultiConIR 上，Qwen3-Embedding-0.6B 在复杂查询（Q4–Q10）上 NDCG@10 从 70.1 降至 67.8（分解召回），而 Qwen3-Reranker-0.6B 用分解重排序后 NDCG@10 从纯重排序的 64.1 提升至 71.7，相对提升 7.6 点；模型增大至 8B 时提升达 11.6 点。  
- 分析表明，重排序下分解显著提高 Win Rate 和正样本排名，对硬负样本区分能力增强。  
- 在 SSRB 三个 schema 上，阶段感知框架的 NDCG@10 均优于基线，验证泛化性。

**一句话结论**：多条件查询的分解应推迟到重排序阶段，用固定大小子查询进行约束级验证，而召回阶段必须保持全局语义完整性。
