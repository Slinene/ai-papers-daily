---
title: 'DocMemo: Dynamic Evidence Discovery via Probabilistic Memory-Guided Retrieval
  for Multi-Modal Document Understanding'
title_zh: DocMemo：面向多模态长文档理解的概率记忆引导动态证据检索
authors:
- Hanshu Yao
- Janfeng Zhong
- Niu Lian
- Jinpeng Wang
affiliations:
- Harbin Institute of Technology, Shenzhen
- Tsinghua Shenzhen International Graduate School, Tsinghua University
arxiv_id: '2608.07067'
url: https://arxiv.org/abs/2608.07067
pdf_url: https://arxiv.org/pdf/2608.07067
published: '2026-08-07'
collected: '2026-08-10'
category: Multimodal
direction: 多模态文档理解 · 动态证据检索与记忆
tags:
- Document Understanding
- Multi-modal
- Agent Memory
- Dynamic Retrieval
- Thompson Sampling
- Bayesian Updating
one_liner: 提出三层记忆状态与贝叶斯页信念更新机制，将长文档推理建模为动态证据探索过程
practical_value: '- **Agent 记忆机制设计**：三层记忆（结构模式记忆、页信念记忆、问题情景记忆）可借鉴用于多轮对话推荐系统中，管理用户状态、商品上下文与推理轨迹，解决长对话场景下兴趣漂移与证据跟踪问题。

  - **不确定性驱动的探索**：汤普森采样与贝叶斯页信念更新提供了一种平衡探索与利用的范式，可迁移至推荐系统的冷启动或动态兴趣建模，例如在新商品或新用户场景下自适应调整曝光策略。

  - **结构感知的自适应粒度检索**：根据文档结构（目录、节标题）动态选择检索粒度（整页、段落、视觉区域），对应电商场景中商品详情页的结构化信息（标题、图文、参数表）的分层次检索，提升证据定位效率。

  - **空间邻近传播**：利用相邻页面的相关性平滑信念，可启发推荐系统中基于会话内邻近商品或协同过滤的置信传播，增强对强相关 item 的召回。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：长文档多模态问答（DocVQA）需在数百页中定位稀疏异构证据，现有单轮固定 top-k 检索难以修正早期错误，迭代方法又缺乏跨轮状态传播机制，无法动态跟踪页面相关性变化。

**方法**：提出 DocMemo，将长文档推理视为动态证据探索，维护三层记忆状态：文档结构记忆（结构先验）、页信念记忆（动态相关性估计）和问题情景记忆（推理轨迹）。推理过程中，通过贝叶斯页信念更新结合汤普森采样迭代选择页面，利用空间邻近传播平滑相邻页信念，并根据结构信号自适应选择页面、段落或视觉区域粒度，同时补充细粒度视觉特征。

**结果**：在3个基准测试上达到 SOTA，消融实验验证了结构化记忆与动态页信念更新的有效性。
