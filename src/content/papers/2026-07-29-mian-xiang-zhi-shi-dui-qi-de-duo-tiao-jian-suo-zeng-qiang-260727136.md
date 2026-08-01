---
title: 'KAMR: Grounding Generation via Knowledge-Aligned Multi-hop Retrieval'
title_zh: 面向知识对齐的多跳检索增强生成
authors:
- Xiaochen Wang
- Yuan Zhong
- Haoyu Wang
- Ting Wang
- Fenglong Ma
affiliations:
- The Pennsylvania State University
- University at Albany, State University of New York
- Stony Brook University, State University of New York
arxiv_id: '2607.27136'
url: https://arxiv.org/abs/2607.27136
pdf_url: https://arxiv.org/pdf/2607.27136
published: '2026-07-29'
collected: '2026-08-01'
category: RAG
direction: 知识图谱多跳检索与对齐学习
tags:
- graph-retrieval
- multi-hop
- knowledge-alignment
- contrastive-learning
- RAG
one_liner: 区分锚点与链接三元组，通过全局召回与局部扩展提升图多跳检索的证据完整性
practical_value: '- **知识图谱驱动的商品多跳问答**：在电商场景构建商品-属性-类目等知识图谱后，可借鉴 KAMR 的“先全局检索锚点三元组，再沿图局部扩展收集弱相关证据”的两阶段策略，解决复杂查询（如“适合油皮的平价控油粉底液有何副作用？”）需要组合多条知识才能回答的问题。

  - **弱对齐事实的补救机制**：采用对比学习 pair-level 与 element-level 匹配，配合 LLM 掩码生成部分对齐数据的训练方式，能有效召回语义上弱相关但结构必要的三元组，适合推荐系统中低频长尾属性（如冷门成分）的补全。

  - **支持 Agent 的推理链路构建**：在 Agent 需调用知识库进行多步推理时，该检索方法可输出有序的证据链，增强答案的可解释性，尤其适用于合规审查、导购解释等场景。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**  
多跳检索要求组合多个知识图谱三元组才能回答查询，但现有方法独立排序三元组，忽略结构连接，且缺乏查询-三元组对齐标注，导致弱对齐但结构必要的证据被遗漏。  
**方法**  
提出 KAMR，将三元组分为两类：锚点（强约束）与链接（弱对齐但结构相连）。训练时，用 LLM 掩码三元组元素生成对应查询，构造部分对齐数据集，优化 pair-level 和 element-level 的对比损失，迫使模型对齐查询与弱相关三元组。推理时，先全局检索锚点，再沿图局部扩展到链接三元组，收集完整证据链。  
**结果**  
在四个多跳问答基准、三种 LLM 主干上，KAMR 较 14 个基线一致提升检索与下游问答性能，尤其是在需要多条弱对齐三元组的问题上提升显著。
