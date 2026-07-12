---
title: Conversational Retrieval and On-the-Fly Knowledge Modeling of Historical Penitentiary
  Repression Records
title_zh: 历史档案对话检索与即时图知识建模系统
authors:
- Paula Font Solà
- Adrià Molina Rodríguez
- Josep Lladós
affiliations:
- Computer Vision Center, Universitat Autònoma de Barcelona
arxiv_id: '2607.08459'
url: https://arxiv.org/abs/2607.08459
pdf_url: https://arxiv.org/pdf/2607.08459
published: '2026-07-09'
collected: '2026-07-12'
category: RAG
direction: RAG + 图记忆的对话式知识检索
tags:
- RAG
- Graph Memory
- Knowledge Modeling
- Conversational Retrieval
- Document Analysis
one_liner: 在图结构上动态建模专家知识，充当LLM记忆实现跨文档推理与对话式检索
practical_value: '- 将领域专家知识构建为图索引，作为LLM的外部记忆，在RAG过程中优先检索此类已建模知识，能显著提升问答深度与一致性，特别适合电商商品知识库、政策QA等场景

  - 允许业务专家即时向图中添加/更新事实（如新品属性、促销规则），系统无需重新训练即可动态扩展知识，适合快速变化的电商运营环境

  - 图结构天然支持多跳推理和链接发现，可解决“相似商品对比”“历史订单关联查询”等跨文档复杂问题，弥补纯向量检索的局限

  - 对话中既检索原始文档又检索提炼后的图知识，形成记忆增强的生成流水线，可迁移至客服系统或Agent的长期记忆模块'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：传统RAG在历史档案等场景中仅能处理单文档抽取式任务，缺乏对文档集合的整体理解，且无法动态融入专家知识。系统需要一种能持续积累结构化知识、支持复杂关联推理的对话式检索架构。

**方法关键点**：提出在图数据库中存储由专家或检索过程产生的**事实单元**，形成知识图索引。该索引作为语言模型的**持久记忆**，每次对话既从原始文档检索，也从已有知识图中获取事实。系统支持“即时建模”——专家可在交互中随时向图添加新事实，无需离线更新。图结构使查询能跨越多个文档发现隐藏链路（如人物关系、事件因果），并将检索结果与建模知识融合生成回答。

**关键成果**：系统实现了对非显式信息的综合回答，能够处理包含长期依赖的复杂问句，例如“找出所有在特定时段入狱、后又获赦免的囚犯”。相比于仅依赖文档块的基线，图记忆的引入显著提升了跨文档推理和专家知识集成的能力，生成的信息更具深度和完备性（定性评估为主）。
