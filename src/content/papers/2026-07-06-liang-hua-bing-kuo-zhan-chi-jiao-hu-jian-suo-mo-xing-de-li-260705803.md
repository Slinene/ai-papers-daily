---
title: Quantifying and Expanding the Theoretical Capacity of Late-Interaction Retrieval
  Models
title_zh: 量化并扩展迟交互检索模型的理论容量
authors:
- Julian Killingback
- Varad Ingale
- Hamed Zamani
- Cameron Musco
affiliations:
- Center for Intelligent Information Retrieval, University of Massachusetts Amherst
arxiv_id: '2607.05803'
url: https://arxiv.org/abs/2607.05803
pdf_url: https://arxiv.org/pdf/2607.05803
published: '2026-07-06'
collected: '2026-07-08'
category: RecSys
direction: 迟交互检索理论容量分析
tags:
- MaxSim
- Late-Interaction
- Retrieval
- Theory
- Signed MaxSim
- ColBERT
one_liner: 证明 MaxSim 可复制任意非负稀疏内积并引入 Signed MaxSim，实现任意实向量内积复制，带来理论解释和实验提升。
practical_value: '- 在搜索/推荐中遇到带否定词的查询（如"无糖巧克力"），可直接使用 Signed MaxSim 建模负向信号，比标准 MaxSim
  有理论保障且效果显著提升（实验 nDCG@10 从 0.008 到 0.788）。

  - MaxSim 等价于软 OR 聚合，能评估正 CNF 逻辑表达式（如"红色 AND (裙子 OR 连衣裙)"），可将其作为复杂用户意图分解与合并的工具，为多条件筛选提供统一相似度计算。

  - 理论证明 MaxSim 的表达能力至少不弱于向量内积，且更节省表示空间（k 稀疏只需 O(k) 维），在物品量巨大的电商图库中可替代点积作为高效匹配算子。

  - Signed MaxSim 使迟交互模型能处理既有正例又有负例的混合向量，适合用户多兴趣建模与多模态表示，可直接用于召回或精排阶段的相似度计算。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：以 ColBERT 为代表的迟交互检索模型依赖 MaxSim 相似度，经验表现强于单向量稠密/稀疏检索，但 MaxSim 的理论表达能力与局限性长期未被阐明。

**方法关键点**：
- 通过构造性证明，MaxSim 可精确复制任意非负 k 稀疏向量的内积，且只需 O(k) 表示空间；而内积在相同空间下达不到某些 MaxSim 能表达的相似度。
- 提出 Signed MaxSim，引入正负标记，使迟交互模型能够复制任意实值向量内积，弥补标准 MaxSim 无法表达负交互的缺陷。
- 进一步揭示 MaxSim 可看作多个软 OR 的聚合，并能评估正合取范式（CNF）逻辑表达式，赋予其组合语义能力。

**关键结果**：
- 理论上，MaxSim 对非负向量、Signed MaxSim 对任意向量，表达力均不低于同维度内积，且具有内积无法复制的额外能力。
- 在带否定词的检索任务中，Signed MaxSim 显著提升零样本泛化：词汇偏移时 nDCG@10 从 0.597 提升至 1.000；纯否定查询上从 0.008 提升至 0.788，验证了理论优势。
