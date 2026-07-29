---
title: 'UniMem: Complementary Episodic-to-Parametric Memory for Boundary-Agnostic
  Task Streams'
title_zh: UniMem：边界无关任务流的互补情节到参数记忆框架
authors:
- Siyu Xia
- Chenheng Zhang
- Yanting Wu
- Haoxuan Li
- Jiajun Chai
- Xiaohan Wang
- Guojun Yin
- Wei Lin
- Zhouchen Lin
- Haifeng Zhang
affiliations:
- Institute of Automation, Chinese Academy of Sciences
- Peking University
- Meituan
- University College London
arxiv_id: '2607.26017'
url: https://arxiv.org/abs/2607.26017
pdf_url: https://arxiv.org/pdf/2607.26017
published: '2026-07-28'
collected: '2026-07-29'
category: Agent
direction: Agent 记忆管理 · 参数化与检索互补
tags:
- continual learning
- memory-augmented LLM
- agent memory
- routing tokens
- episodic buffer
- parametric consolidation
one_liner: 受互补学习系统启发，用路由令牌解耦识别与执行，稀疏任务走检索、重复模式自动参数化，实现流式记忆扩展。
practical_value: '- **路由与执行解耦**：用轻量级路由令牌做任务识别，高容量Procedural KV Memory做任务执行，新任务无需标签即可自动分配参数块。电商推荐Agent可直接套用：路由判断用户意图，对应模块调推荐策略。

  - **缓冲与门槛机制**：稀疏/长尾任务保留在情节缓冲走RAG，避免过早参数化导致噪音；当缓冲证据足够且聚类质量过关时才固化为参数记忆。搜索广告场景中，低频query或新item可用此方式积累样本再触发模型更新。

  - **参数隔离避免遗忘**：每个任务独立KV Memory块，与冻结骨干通过可学习门控注入，天然抵抗流式任务间的灾难性遗忘。多租户推荐模型或个性化Agent可参考按用户/场景分配独立记忆单元，互不干扰。

  - **无监督任务发现**：基于NCD计算任务相似度 + HDBSCAN聚类，无需任务ID即可识别重复模式。可迁移到用户行为流中自动挖掘规律性行为簇，驱动推荐策略的自动聚合与迁移。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：LLM Agent在真实部署中面临边界模糊、持续涌入的任务流，单独依赖外部检索记忆（高塑性但无法内化模式）或参数记忆（稳定但需预设任务边界）会导致稳定性-可塑性困境。受脑互补学习系统启发，这篇工作将情节性的快速存储与参数化的渐进巩固结合起来。

**方法关键点**：
- 设计一组可训练**路由令牌**（含已知任务令牌与一个“新颖哨兵”令牌），查询通过冻结骨干计算与令牌的概率匹配进行任务选择；新颖查询进入**情节缓冲**走RAG执行。
- 每个已知路由令牌关联一个**Procedural KV Memory**（层间键值对+可学习门控），将任务执行参数与识别解耦，路由令牌不编码执行细节，执行内存块隔离不同任务。
- **增量记忆扩展**：初始阶段用已知任务和预留伪未见任务校准路由与新颖哨兵；流式部署中，情节缓冲积满后通过NCD相似度+HDBSCAN聚类发现重复模式，经质量过滤的动态分配新路由令牌与KV记忆块，进行SFT巩固。
- 运行中稀疏/长尾任务继续由缓冲+RAG处理，不参与参数化，避免伪模式固化。

**关键实验**：在Super-NaturalInstructions（10/50/100任务模拟流）和SuperGLUE Mix（6任务无边界混合流）上，用LLaMA与Qwen不同尺寸骨干评估。UniMem在SNI-100任务上比Replay LoRA平均EM高6.20（LLaMA-3.2-3B）和2.44点（LLaMA-8B）；在LLaMA-3B SuperGLUE上平均准确率85.95%大幅领先Best基线77.49%。消融表明消除任务专用KV或门控制导致严重性能下降，路由准确率在100任务仍保持85%以上。

**一句话**：通过路由令牌把“这是什么任务”和“如何执行任务”分开，闲置模式走检索，成熟模式走参数，让Agent在连续任务流中自主生长内存。
