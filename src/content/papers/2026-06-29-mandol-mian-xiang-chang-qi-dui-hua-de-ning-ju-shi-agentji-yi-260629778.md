---
title: 'Mandol: An Agglomerative Agent Memory System for Long-Term Conversations'
title_zh: Mandol：面向长期对话的凝聚式Agent记忆系统
authors:
- Yuhan Zhang
- Zhiyuan Guo
- Ziheng Zeng
- Wei Wang
- Wentao Wu
- Lijie Xu
affiliations:
- Institute of Software, Chinese Academy of Sciences
- Microsoft Research
arxiv_id: '2606.29778'
url: https://arxiv.org/abs/2606.29778
pdf_url: https://arxiv.org/pdf/2606.29778
published: '2026-06-29'
collected: '2026-06-30'
category: Agent
direction: 长期对话代理记忆系统 · 统一内存架构
tags:
- agent memory
- hierarchical memory
- semantic graph
- quantitative retrieval
- long-term conversation
- in-memory architecture
one_liner: 通过统一层次记忆模型与凝聚式数据结构，将碎片化存储融合为单一内存原生架构，在长期对话基准上达到最优准确率与最低延迟
practical_value: '- 在推荐Agent或电商客服中，可借鉴**层次记忆模型**：将原始对话/行为拆分为基本记忆单元，并自动凝聚为事件链、实体图、用户偏好等高阶抽象，所有抽象保留与原始记忆的溯源链接，方便证据回查。

  - **统一内存语义数据结构**（SemanticMap+SemanticGraph）可替代常见的向量数据库+图数据库的混合方案，消除跨库I/O，将检索延迟降低一个数量级，适合低延迟交互场景。

  - **定量检索机制**不依赖LLM参与召回，通过查询自适应路由、基于MAD的动态去噪、跨源冲突仲裁（结合时间衰减与信源置信度）以及MMR驱动的Token预算上下文拼接，可直接用于构建干净、不冲突的长期记忆上下文，避免RAG式检索引入的噪声与冗余。

  - **Token效率优化**技巧：用MMR联合优化相关性与多样性，避免简单Top-K导致关键证据丢失，可在有限上下文中保留互补信息，对推荐系统整理用户长期画像或Agent生成多跳推理线索都有参考价值。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
长期对话Agent需要记忆跨会话、多类型的复杂关联信息（对话、意图、事件、实体状态等），现有系统普遍采用向量数据库+图数据库的异构存储，导致记忆碎片化、跨库I/O高、检索噪声大且缺乏Token预算控制。复杂查询（时间推理、跨会话多跳推理、状态更新）常因证据缺失或上下文截断而失效。  

**方法关键点**  
- **层次记忆模型**：将记忆分为基本层与抽象层，统一表示为结构化语义图。基本层存储原始对话单元及其显式/隐式关系；抽象层通过LLM自动凝聚为事件链（情节记忆）、实体图（语义记忆）和偏好演化链（情感记忆），并保留回溯到基本单元的溯源链接。  
- **凝聚式语义数据结构**：在单一进程内使用SemanticMap（融合键值存储、稠密/稀疏向量索引、倒排索引）和SemanticGraph（邻接表存储显式边，按需获取隐式边），统一支持混合检索，消除跨库I/O。  
- **定量查询机制**：用轻量意图分类器进行查询自适应路由，选择相关记忆源；通过MAD中值绝对偏差动态去噪（式1），并基于时间衰减与信源置信度的仲裁得分解决跨源冲突（式2）；最后以MMR（最大边际相关性）准则在Token预算内贪心选取高相关、多样化证据（式3），全部过程不调用LLM。  
- **实现**：Python单进程内维护绝大部分记忆，冷数据通过DuckDB持久化，异步换页。  

**关键结果**  
在LoCoMo基准上，Mandol + GPT-4.1-mini达到92.21%总体准确率（比EverMemOS高0.24pp），LongMemEval上达到88.40%（比EverMemOS高5.4pp）。检索延迟方面，10 QPS并发下搜索平均延迟82.2ms（比MemOS快5.4倍），插入平均延迟39.7ms（快4.8倍），且在消费级RTX 5090笔记本上仍保持166.5ms搜索延迟。同时Token消耗相比EverMemOS减少17%~20%。
