---
title: 'Memory is Reconstructed, Not Retrieved: Graph Memory for LLM Agents'
title_zh: 记忆重构而非检索：面向LLM Agent的图记忆
authors:
- Shuo Ji
- Yibo Li
- Bryan Hooi
affiliations:
- National University of Singapore
arxiv_id: '2606.06036'
url: https://arxiv.org/abs/2606.06036
pdf_url: https://arxiv.org/pdf/2606.06036
published: '2026-06-04'
collected: '2026-06-06'
category: Agent
direction: LLM Agent 记忆重建 · Cue-Tag-Content 图
tags:
- memory reconstruction
- graph memory
- LLM agents
- associative memory
- active retrieval
one_liner: 提出MRAgent，将记忆组织为Cue–Tag–Content图，通过LLM推理驱动的主动重建替代被动检索，长时记忆推理性能提升23%并大幅降低Token消耗。
practical_value: '- **记忆图设计**：Cue–Tag–Content结构以Tag作为语义中间层，可复用到电商客服Agent的长期交互记忆，支持多跳关联检索，避免一次性全图遍历的噪声和成本。

  - **主动重建机制**：将LLM推理嵌入记忆访问循环，允许Agent根据中间证据动态调整检索路径，适合处理复杂查询或多轮对话中的上下文积累，避免被动检索的一次性固化缺陷。

  - **按需检索降低成本**：通过Tag先筛选再访问具体内容，显著减少Token消耗（实验中仅118k，对比A-Mem的632k），适合需要控制推理开销的生产环境。

  - **多层记忆分层**：融合场景记忆、语义记忆与话题抽象，可用于构建用户长期画像和交互历史存储，支持个性化推荐或服务中的稳定知识抽取与事件回溯。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
LLM Agent在长期交互中的记忆推理能力受限于被动检索范式：现有RAG或图记忆方法一次性固定检索内容，无法根据推理过程中的中间证据动态调整，导致噪声积累和多跳推理失败。认知神经科学表明人类记忆是一个主动、关联的重构过程，这启发我们将记忆访问从“检索”转变为“重建”。

**方法关键点**  
- **Cue–Tag–Content记忆图**：将记忆组织为异构图，其中Cue是细粒度关键词，Content是具体记忆单元，Tag作为两者之间的语义桥梁，编码关联关系。  
- **多层记忆**：包含Episodic（事件）、Semantic（稳定知识）和Topic（话题抽象）三个层次，支持不同粒度的推理。  
- **主动重建过程**：LLM在每步根据当前重建状态（已积累的证据）选择前向或反向遍历动作，动态探索记忆图并剪枝无关路径，逐步重构出可回答问题的最小证据集。  
- **理论保证**：证明了给定检索预算下，主动策略的表达能力严格强于被动策略。

**关键实验**  
- 数据集：长对话记忆基准LOCOMO和LONGMEMEVAL。  
- 基线：RAG、A-Mem、MemoryOS、LangMem、Mem0等。  
- 结果：在Gemini骨干下，MRAgent的LLM-Judge分数达到84.21（相对提升23.3%），全面超越基线；Token消耗仅118k，远低于A-Mem的632k；消融实验证实多步推理和Tag引导是主要增益来源。  

**一句话**：记忆不是一次检索的静态结果，而是基于中间证据的迭代重构过程。
