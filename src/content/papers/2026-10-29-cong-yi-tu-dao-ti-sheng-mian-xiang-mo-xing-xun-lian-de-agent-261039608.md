---
title: 'From Intent to Improvement: Agentic Dataset Search for Better Model Training'
title_zh: 从意图到提升：面向模型训练的 Agent 数据集搜索框架
authors:
- Qiaosheng Chen
- Kaijia Huang
- Fanqi Zhou
- Gong Cheng
affiliations:
- Nanjing University
- State Key Laboratory for Novel Software Technology
arxiv_id: '2610.39608'
url: https://arxiv.org/abs/2610.39608
pdf_url: https://arxiv.org/pdf/2610.39608
published: '2026-10-29'
collected: '2026-10-31'
category: Agent
direction: LLM Agent 约束治理的数据集检索
tags:
- Dataset Search
- LLM Agent
- Typed Plan
- Deterministic Operators
- Training Utility
- NDCG@10
one_liner: 提出契约治理的 AgenticDS 框架，用 typed object 约束 LLM 决策并验证约束，显著提升数据集搜索与下游训练效果
practical_value: '- 在商品召回/广告候选生成中，让 LLM 先输出结构化筛选条件（类目、价格、库存、品牌授权、合规标签）再交给确定性规则引擎执行，避免模型自报匹配但漏硬约束；这种
  typed object + deterministic operators 的边界可提升链路可信度。

  - 稀疏元数据的长尾商品/新广告主：用有界图扩展（如品牌→店铺→商品，或类目→属性）补全语义缺失，但必须限制跳数避免噪声，类似 bounded graph expansion。

  - 当模型输出候选列表时，要求先基于 provenance 证据验证（例如商品属性值、广告审核字段）再排序，不通过时返回可解释诊断与局部修复指令，减少整条链路的无效重试。

  - 对含硬约束的 query（如“高转化且库存>100且配送时效24h”），可借鉴 typed search plan 编译方式，把自然语言 query 解析为可执行计划，而不是直接用向量检索。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**
在百万级 ML 仓库中寻找训练数据时，文本相关性不够。query 耦合了语义训练目标与任务、许可证、训练阶段等约束，而能验证这些约束的元数据常缺失。纯文本检索按相似度排序，无法强制硬约束或沿关系到达稀疏描述的数据集；自由式工具调用 Agent 更灵活，但同一模型既选数据集又声明其匹配，没有机制核验 query 约束是否真正满足；两者都不能证明返回的数据会改善模型训练。

**方法关键点**
AgenticDS 是契约治理的 agentic 框架：每个 LLM 决策先实例化为 typed object，再由确定性代码消费。它将 query 编译为 typed search plan，通过可许可的确定性算子执行混合检索与有界图扩展；在接受排名前，必须验证基于 provenance 的证据；否则发出 typed diagnosis，只允许局部修复。这形成了「LLM 决策—类型约束—确定性执行—证据验证」的闭环，避免模型自报匹配。

**关键结果数字**
在 HuDS-Bench（200 条 query，24,908 条 graded judgments，汇总 15 个系统）上，AgenticDS 的 NDCG@10 比最强 dense-sparse hybrid 高 25.7%，比商业 LLM Agent 高 18.9%；受控 search-to-train 研究显示，其检索的数据集在数学、代码、医学下游准确率最佳。代码与数据已公开。
