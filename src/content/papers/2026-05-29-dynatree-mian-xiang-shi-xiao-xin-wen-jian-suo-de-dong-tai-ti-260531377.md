---
title: 'DynaTree: Dynamic Agentic Retrieval Tree for Time-Sensitive News Retrieval'
title_zh: DynaTree：面向时效新闻检索的动态智能体检索树
authors:
- Siyuan Qi
- Xinyuan Wang
- Yingxuan Yang
- Haochuan Guo
- Jianghao Lin
- Weiwen Liu
- Yong Yu
- Weinan Zhang
affiliations:
- Shanghai Jiao Tong University
- Orion Arm AI
arxiv_id: '2605.31377'
url: https://arxiv.org/abs/2605.31377
pdf_url: https://arxiv.org/pdf/2605.31377
published: '2026-05-29'
collected: '2026-06-01'
category: Agent
direction: 多 Agent 协作检索树 · 动态子树选择
tags:
- Agentic RAG
- Retrieval Tree
- News Retrieval
- Subtree Selection
- Time-sensitive Retrieval
- Semantic Expansion
one_liner: 解耦语义扩展与在线检索，用多 Agent 构建可复用检索树，再通过轻量子树选择适应新闻时效性，召回与部署效果显著提升。
practical_value: '- **离线持久化语义结构**：将用户意图的语义扩展固化为树结构，避免每次查询重复推理。在电商推荐中，可将长期稳定的品类（如“户外运动装备”）构建成
  Topic 树，召回时直接复用，大幅降低 LLM 调用成本。

  - **多 Agent 角色分工实现可控探索**：Planning、Retrieval、Augmented、Reflection 各司其职，路径感知规划、自适应路由、证据标准化与结构自我修正的组合，可迁移到商品知识图谱构建、复杂查询的迭代改写等场景，尤其适合需要平衡覆盖率和漂移的召回链路。

  - **轻量子树选择应对分布漂移**：日常通过评估代理（小型采样集 + LLM 弱标注）快速选优子树，无需重跑昂贵 Agent，类似推荐系统中固定候选池但动态调整召回通道权重，适合促销、季节变化等时变场景下的低成本自适应。

  - **评估代理与弱监督**：只需 200 个文档的 LLM 标注即可稳定挑选子树，可借鉴到标注缺失的推荐场景，例如基于少量曝光日志构建代理集，指导召回策略的日常微调。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：新闻检索中用户查询抽象且话题快速演化，现有 agentic RAG 将语义扩展与在线检索紧耦合，推理成本高、无法复用，难以适应时变分布。为此，DynaTree 解耦为两阶段：离线构建可复用的检索树，在线轻量自适应。

**方法关键点**：
1. **Stage I – Agentic 检索树构建**：四种角色 Agent 协作——Planning Agent 基于当前路径生成规划查询；Retrieval Agent 自适应选择 BM25/稠密/混合检索；Augmented Agent 在预算内压缩证据并去冗余；Reflection Agent 基于检索反馈对节点执行 Add/Prune/Revise 操作，控制漂移和冗余。最终生成一棵层次化语义树，每个路径作为有序扩展单元。
2. **Stage II – 动态子树选择**：通过全树检索构造候选文档池，聚类配额采样得到约 200 个文档的评估代理集，LLM 弱标注后计算各候选子树在代理上的 Recall@α，选最优子树。日常每天轻量执行一次，无需重新推理。
3. **路径集成评分**：检索时对子树内所有路径-文档相似度取平均，鼓励多路径一致支持的文档。

**关键实验结果**：在 Syft 七日新闻数据集（50 个主题）和 BEIR 五个公开数据集上，DynaTree 的 Recall@100 和 NDCG@10 均全面优于 ReAct、Reflexion、FreshLLMs、RAPTOR、HyDE 等基线（Syft 平均 Recall 0.475 / NDCG 0.757，次优分别为 0.380 / 0.695）。消融证实所有 Agent 模块有益，Shapley 分析显示 Planning 对召回贡献最大，Reflection 对 NDCG 贡献最大；子树选择优于使用全树。在线 A/B 测试（10 天）：动态子树选择端口生存率 0.59–0.73，较固定子树端口（0.32–0.53）普遍提升约 1.5 倍，且在所有生产召回器中表现最优。
