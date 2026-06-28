---
title: 'Graph Neural Networks Applications Across Domains: All Insights You Need'
title_zh: 图神经网络跨领域应用：全貌与核心洞见
authors:
- Abderaouf Bahi
affiliations:
- Computer Science and Applied Mathematics Laboratory (LIMA), Chadli Bendjedid University
arxiv_id: '2606.27202'
url: https://arxiv.org/abs/2606.27202
pdf_url: https://arxiv.org/pdf/2606.27202
published: '2026-06-25'
collected: '2026-06-28'
category: RecSys
direction: GNN应用综述 · 部署关键约束
tags:
- Graph Neural Networks
- Survey
- Recommender Systems
- Knowledge Graphs
- GraphRAG
- Over-smoothing
one_liner: 一份跨越12个应用领域的GNN调查，揭示部署关键限制与设计选择真实收益
practical_value: '- **构图成本与收益权衡**：在电商推荐中，用户-商品二部图构造和维护成本高，应先评估简单基线（如LightGCN）是否已足够；异配性普遍存在（如商品共现与用户社交混合），复杂GNN反而可能被简单模型反超。

  - **时序图增量更新优先**：用户行为序列本质是时序图，但时态GNN在部署中难度大，工程上可优先采用流式增量更新与高效序列特征抽取，避免引入重型时态建模。

  - **避免领袖榜陷阱**：公共基准上SOTA的GNN架构在真实推荐场景中常因鲁棒性、延迟和分布偏移而失效，必须用自有业务数据严格测试，并重视过平滑、过挤压、公平性等部署级约束。

  - **LLM集成保持谨慎**：将GNN与LLM结合（如GraphRAG做商品知识增强）目前证据仅为暗示性，可从轻量化的文本构图（如商品描述相似度图）起步，逐步验证知识注入效果。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

GNN已从利基表征技术成为关系数据建模的默认选择，但在实际部署中图结构所带来的计算成本是否值得仍存在争议。本调查围绕统一设计空间展开，从谱方法和空间方法的共同原理推导，并将表达性与Weisfeiler-Lehman层次的分离能力明确对应。以此为方法论骨架，论文跨12个领域（推荐与社交网络、知识图谱与LLM集成、药物发现、医疗、视觉、交通、能源、无线通信、欺诈检测、工业预测、材料科学、气候建模）详细拆解：各领域的构图选择与成本、主导架构家族及其原因，并将真正增益与弱基线或数据划分偏差导致的假象区分开来。

跨领域比较揭示出重复出现的模式：异配性和大规模几乎在所有领域损害相同模型；时序图始终比静态图更难；公共排行榜上顶尖的架构极少能投入实际部署。论文将过平滑、过挤压、鲁棒性、分布偏移、公平性和可解释性视为决定采用与否的现实约束，而非次要清单。最后，作者评估了图基础模型和LLM集成是否构成真正的范式突破，认为现有证据仅具有提示性而尚未定论。
