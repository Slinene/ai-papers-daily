---
title: 'Breaking the Information Silo: Semantic Personas for Cross-Domain Recommendation'
title_zh: 打破信息孤岛：基于语义画像的跨域推荐
authors:
- Jonathan Mayo
- Moshe Unger
- Konstantin Bauman
affiliations:
- Tel Aviv University
- Temple University
arxiv_id: '2606.01783'
url: https://arxiv.org/abs/2606.01783
pdf_url: https://arxiv.org/pdf/2606.01783
published: '2026-06-01'
collected: '2026-06-02'
category: RecSys
direction: 跨域推荐 · 基于语义画像的知识迁移
tags:
- cross-domain recommendation
- semantic personas
- LLM
- dual-tower
- late-fusion
- contrastive learning
one_liner: 通过LLM诱导共享行为特征并生成语义画像，实现无共享用户/物品的跨域知识迁移
practical_value: '- **用户画像构建新思路**：利用LLM从交互历史中诱导领域无关的行为特征（如刺激寻求、控制感、冲突容忍），生成结构化语义画像，可用于电商跨场景（购物→内容）的用户理解，避免固定标签的僵硬。

  - **跨平台冷启动方案**：通过目标用户画像在源域用户画像空间进行语义检索，聚合Top-K相似邻居构成社区源画像（CSP），为无任何重叠的用户提供偏好信号。可直接迁移到跨平台推荐或新用户冷启动场景。

  - **双塔融合与动态门控**：协同过滤塔和语义塔以残差方式融合，门控权重α用tanh激活（允许负值，能抑制无关语义）。当目标域用户交互稀疏时，模型自动增强语义塔贡献，对推荐系统稀疏场景增强很有参考价值。

  - **跨域迁移策略选择**：论文发现迁移效果主要取决于目标域的结构密度而非语义接近度，提示我们在选择跨域知识源时，应优先评估目标域自身的协同信号强度，而非简单追求领域相似性。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
各数字平台形成信息孤岛，用户行为分散且无法共享，现有跨域推荐方法依赖共享用户、物品或结构相似性，难以在完全异构的独立平台间实施。SPHERE旨在打破这一限制，通过LLM生成的领域无关行为画像实现无实体重叠情况下的知识迁移。

**方法关键点**  
- **共享特征归纳**：LLM联合分析源域和目标域交互语料，动态发现一组行为特征（如“刺激寻求 vs. 熟悉惯例”、“控制感 vs. 外部引导”），作为共享描述词汇。  
- **语义画像生成**：对每个用户，利用共享特征约束LLM生成禁止出现具体物品和媒介术语的结构化文本画像，再用预训练嵌入模型投影到连续语义空间。  
- **社区源画像（CSP）构建**：用目标用户画像嵌入检索源域用户画像空间中最相似的K个邻居，平均池化得到社区源画像，代表行为相似群组的宏观偏好。  
- **双塔架构与动态融合**：一个塔提取目标域协同信号，另一个塔处理CSP与候选物品的语义互动，最后通过残差连接和一个可学习门控（tanh激活，允许负值）进行实例级自适应融合。  
- **训练与评估**：端到端使用对比InfoNCE损失，8个负样本，全量候选物品评估NDCG@10；主干模型可选NCF、SVD++、LightGCN。

**关键实验与结果**  
在Amazon Books、Goodreads、Steam三域六个方向配对中进行严格零重叠评测。SPHERE-CSP在所有主干模型和域对上均取得统计显著的NDCG@10提升。消融实验表明，仅用自身目标画像（SPHERE-Intra）提升有限，同时使用CSP和目标画像（SPHERE-Dual）有时可进一步获益，但以CSP为核心。核心发现：**跨域迁移效果并不由域间的语义接近度决定，而是强烈依赖于目标域的结构密度——稀疏目标域能从社区画像中获得更大增益。**
