---
title: 'SciAtlas: A Large-Scale Knowledge Graph for Automated Scientific Research'
title_zh: SciAtlas：大规模科学知识图谱赋能自动化研究
authors:
- Shuofei Qiao
- Yunxiang Wei
- Jiazheng Fan
- Bin Wu
- Busheng Zhang
- Mengru Wang
- Yuqi Zhu
- Ningyu Zhang
- Keyan Ding
- Qiang Zhang
affiliations:
- Zhejiang University
- University College London
arxiv_id: '2605.22878'
url: https://arxiv.org/abs/2605.22878
pdf_url: https://arxiv.org/pdf/2605.22878
published: '2026-05-19'
collected: '2026-05-26'
category: Agent
direction: 大规模学术知识图谱与神经符号检索支持AI智能体
tags:
- Knowledge Graph
- Neuro-Symbolic Retrieval
- Automated Research
- AI Agent
- Graph Reranking
- Scientific Discovery
one_liner: 构建含4300万论文、1.57亿实体、30亿三元组的异构学术知识图谱，并设计神经符号检索算法降低智能体推理成本
practical_value: '- **大规模异构知识图谱构建流水线**：将多来源、多形态的学术资源统一为实体-关系三元组，可迁移至电商领域构建商品-属性-场景等知识关联，为推荐与搜索提供结构化背景

  - **神经符号检索范式**：三路协同召回（语义向量、关键词、图结构）结合图重排序，能同时兼顾语义相似与逻辑关联，适合需要可解释性与关联发现的商品推荐、对话Agent等场景

  - **用图谱预存逻辑降低Agent幻觉与成本**：将复杂推理路径固化于图结构，Agent直接查询而非实时推理，在电商智能客服、趋势分析等场景可大幅降低大模型调用频率与延迟

  - **全局视角的任务抽象**：文献综述、趋势合成等任务映射到电商即为用户评论摘要、购物趋势洞察、新品定位，可借鉴其认知地图思想构建领域全景分析工具'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：学术信息爆炸导致知识碎片化，传统关键词或向量检索缺乏拓扑推理能力，Agent深度研究框架易出现逻辑幻觉且推理成本高。亟需结构化的全景知识基底来支撑自动化科学发现。

**方法**：构建多学科异构学术知识图谱SciAtlas，从26个学科中整合4300万篇论文，提炼出1.57亿实体和30亿三元组，打破学科壁垒。设计神经符号检索算法，通过三路协同召回（语义、关键词、图结构）和图重排序，实现从简单语义匹配到确定性关联发现的转换。基于该图谱，开展文献综述、自动化研究趋势合成、想法定位和学术轨迹探索等应用。

**核心结果**：SciAtlas规模达4300万论文、1.57亿实体、30亿三元组，覆盖26个学科。其神经符号检索算法显著降低了智能体在复杂科学任务中的推理成本，并支持全景式知识关联发现。
