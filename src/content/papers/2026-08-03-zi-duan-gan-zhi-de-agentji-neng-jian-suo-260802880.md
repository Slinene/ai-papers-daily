---
title: Field Aware Agent Skill Retrieval
title_zh: 字段感知的Agent技能检索
authors:
- Paimon Goulart
- Liang Wu
- Kelly Wan
- Evangelos E. Papalexakis
- Liangjie Hong
affiliations:
- University of California, Riverside
- Nokia
arxiv_id: '2608.02880'
url: https://arxiv.org/abs/2608.02880
pdf_url: https://arxiv.org/pdf/2608.02880
published: '2026-08-03'
collected: '2026-08-05'
category: Agent
direction: Agent技能检索 · 多字段表示
tags:
- skill retrieval
- field-aware
- hybrid retrieval
- MLP scoring
- lifelong agents
- multi-field
one_liner: 保留技能的多字段结构分别计算相似度并学习得分融合，显著提升技能检索召回
practical_value: '- **电商搜索的多字段商品匹配**：商品有标题、描述、属性等多个结构化字段，拼接为单一文档会丢失信息。可借鉴本方法，为每个字段独立计算稀疏（倒排）和稠密（向量）相似度，再用小型
  MLP 学习字段权重，替代人工调权或平权，尤其在多字段重要度差异大的场景（如品牌词 vs 长描述）中收益明显。

  - **Agent 技能库工程实现**：在构建终身学习 Agent 的技能检索模块时，直接保持技能的 field-aware 结构，用独立的相似度打分 + 小
  MLP 融合，比拼接后再编码更简单、可扩展，且效果随技能库增长提升，适合大规模技能管理。

  - **可解释的检索融合策略**：将不同字段的得分显式拆分，便于快速定位哪些字段对匹配贡献最大，可应用到推荐系统中多模态特征（文本、属性、图像）的相似度融合，用轻量
  MLP 替代黑盒交叉注意力。

  - **复用结论**：简单的“分字段计算 + 小 MLP 学习组合”就能超越复杂的拼接式深度模型，表明保留原始数据结构对检索至关重要，这一思想可直接移植到其他多字段文档检索（如
  FAQ、知识库）中。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：终身学习 Agent 的技能库不断膨胀，从技能库中准确检索合适技能成为瓶颈。当前方法将技能的名称、描述、正文等字段拼接为一个平文档处理，忽略了技能天然的结构化多字段特性，每个字段包含不同的使用时机与方式信息。

**方法**：提出字段感知的技能检索框架，将每个技能拆分为独立字段，对每个字段分别计算稀疏相似度（BM25）和稠密相似度（基于 embedding 的点积/余弦），形成字段级相似度张量。然后尝试两种融合方式：①均匀权重直接加和，②用一个小型 MLP 学习各个字段-相似度通道的权重组合。该 MLP 以字段得分向量为输入，输出最终相关性分数，端到端训练排序损失。

**关键结果**：在两个技能检索基准 SkillRet 和 SRA-Bench 上，保持字段分离的混合检索显著优于拼接基线。使用 MLP 学习字段权重达到最佳：SkillRet Recall@10 77.95，SRA-Bench 83.78，均高于同样使用 MLP 但拼接字段的版本。进一步实验表明，当技能库规模增大时，字段感知方法的优势更加明显，说明在检索困难的场景下，结构信息的保留尤为重要。
