---
title: Personalized Recommendation Tool Learning via Autonomous Language Agents
title_zh: 基于自主语言代理的个性化推荐工具学习
authors:
- Mingdai Yang
- Zhiwei Liu
- Weizhi Zhang
- Yibo Wang
- Hao Peng
- Philip Yu
affiliations:
- Univ. of Illinois Chicago
- Microsoft
- Beihang University
- Hangzhou Innovation Institute of BUAA
arxiv_id: '2607.19739'
url: https://arxiv.org/abs/2607.19739
pdf_url: https://arxiv.org/pdf/2607.19739
published: '2026-07-22'
collected: '2026-07-23'
category: Agent
direction: Agent 个性化推荐工具学习
tags:
- LLM agent
- tool learning
- recommender systems
- full-ranking
- reflection mechanism
- personalization
one_liner: 用LLM代理调用多个推荐模型作为工具，通过反射机制个性化选择工具，实现全排名推荐。
practical_value: '- **多工具集成架构**：将LightGCN、SASRec、SimpleX等异构推荐模型包装为工具，由LLM agent统一调度，通过加权融合（Personalized
  Tool Memory）得到最终排序。业务中可用类似方式组合协同过滤、序列模型、图模型等多路召回，agent负责动态权重分配，无需改造底层模型。

  - **反射记忆更新机制**：提出三种反射信号——局部工具评估（基于行为序列相关性）、全局工具比较（跨工具选择最佳）、排名比较（基于留出物品的排名倒数加权），在线更新每个用户的工具权重。该机制可低成本迁移到个性化重排或广告混排场景，用LLM定期（如每日）优化不同打分器/策略的权重。

  - **轻量上下文重排**：在工具融合分数生成top-N后，用LLM根据用户摘要和物品描述进行二次重排，提升语义匹配度。适用于精排后的小候选集重排，计算开销可控（单张V100
  GPU每用户<0.5秒），适合作为排序流水线的最后一环。

  - **工程并行化与成本控制**：每个用户的工具记忆独立更新，可完全并行；训练时仅需少量用户采样（如160人）进行agent优化，推理时所有用户复用相同工具，Agent阶段可离线完成。这种解耦设计使得LLM调用集中在离线批量任务，不增加在线延迟。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
传统推荐模型（如LightGCN、SASRec）依赖行为数据建模，缺乏语义理解与跨领域推理。直接使用LLM做推荐面临幻觉（生成不存在物品）和上下文长度限制，无法对全量商品库做全排名。已有LLM agent方法仅在少量候选中评测，偏离实际需要。本研究旨在通过架构设计而非模型内部改造，将行为建模与语义推理解耦：让LLM agent负责高层个性化工具选择，传统推荐模型负责全排名评分，从而规避LLM的核心缺陷。

## 方法关键点
- **框架设计（PRTA）**：LLM作为中央规划器，为每个用户维护一个个性化工具记忆（PT memory，长度为工具数的权重向量）。工具集包含LightGCN、SASRec、SimpleX三个预训练推荐模型，每个工具输出全量物品得分。最终排序通过对各工具得分加权求和得到。
- **反射机制更新PT memory**：
  - *局部工具评估*：LLM比较各工具top-k物品与用户最近交互物品（训练时不可见）的文本相关性，给出{-1,0,1}信号，更新对应工具权重。
  - *全局工具比较*：LLM在所有工具中选出最相关的一个，更新其权重。
  - *排名比较*：基于留出物品在各工具列表中的排名倒数加权更新，提供非文本、纯排名的互补信号。
  - 更新采用学习率衰减，支持多轮迭代。
- **上下文重排**：在加权融合产生top-N候选后，LLM根据用户画像和最近行为对这批物品进行重排，输出最终列表。
- **成本与效率**：工具在所有用户上预训练，agent优化仅采样少量用户（每数据集160人），每个用户独立更新，可并行。使用量化Phi-4通过vLLM部署，总API调用次数为 4×用户数×训练轮数 + 2×用户数。

## 实验结果
在Amazon、Yelp、Goodreads三个公开数据集上进行leave-one-out全排名评测。
- 对比基线：工具基模型（LightGCN、SASRec、SimpleX）、其他协同过滤模型（ENMF、DiffRec、FEARec）、文本检索（BM25）、零样本LLM排序器（LLMRank）、以及RAG式单个工具+LLM重排变体。
- 主要指标：Recall@10/20、NDCG@10/20。
- 关键提升：Amazon上R@10从最优baseline的0.0438提升至0.1000（+128%），N@10从0.0206至0.0535（+160%）；Yelp上R@10从0.0688至0.1063（+55%），N@10从0.0413至0.0598（+45%）；Goodreads上R@10从0.1000至0.1688（+69%），N@10从0.0539至0.0809（+50%）。所有数据集上PRTA均显著优于所有基线，且消融实验验证了每个反射模块和重排模块的贡献。

**一句话核心**：让LLM做“选工具”而非“做推荐”，用多个传统模型的互补能力解决全排名问题，同时通过反射机制实现个性化。
