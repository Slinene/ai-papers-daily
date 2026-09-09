---
title: 'Where to Look and What to Use: Retrieve-Localize-Generate for Long-Term Conversational
  Memory Question Answering'
title_zh: 看哪里与用什么：面向长期对话记忆问答的检索-定位-生成框架
authors:
- Yifan Wang
- Xinkui Lin
- Yongxiu Xu
- Shen Gao
- Ruochen Yang
- Kun Huang
- Yubin Wang
- Jie Wu
- Wei Liu
- Jian Luan
affiliations:
- University of Electronic Science and Technology of China, Chengdu, China
- Institute of Information Engineering, Chinese Academy of Sciences, Beijing, China
- School of Cyber Security, University of Chinese Academy of Sciences, Beijing, China
- MiLM Plus, Xiaomi Inc., China
- State Key Laboratory of Internet Architecture, Tsinghua University, Beijing, China
arxiv_id: '2609.07093'
url: https://arxiv.org/abs/2609.07093
pdf_url: https://arxiv.org/pdf/2609.07093
published: '2026-09-07'
collected: '2026-09-09'
category: RAG
direction: 长时对话记忆QA · RAG
tags:
- RAG
- Long-term Memory
- Evidence Localization
- Graph-based Retrieval
- SHPO
- Lost-in-the-Middle
one_liner: 提出MemLoc框架，通过多粒度检索、证据定位与位置ID引导生成，解决长期对话记忆问答中的碎片化与噪声问题
practical_value: '- 借鉴多粒度记忆单元与图路由：在用户长期行为序列建模（如电商会话历史）中，将 session 按不同时间粒度/主题切分为多粒度单元，用图结构建模跨会话依赖，配合熵基粒度选择，可提升对长周期用户兴趣的召回精度，避免只依赖全局
  embedding。

  - 引入证据定位层压缩上下文：在 RAG 生成前增加一个“定位器”，从检索到的多个文档或历史记录中抽取关键片段并重排，输出轻量位置 ID 而非全文，能显著降低无关噪声干扰，缓解
  lost-in-the-middle 效应，可复用于客服对话摘要、用户评论分析等场景。

  - SHPO 训练技巧：用“自反思提示策略优化”训练定位器，即让模型生成推理过程并依据反馈调整，可将此方法用于训练业务中的证据提取/重排模块，提升定位精度。

  - 工程实现上，位置 ID 作为 grounding 信号比直接拼接原文更省 token，同时保留原文索引方便回溯，适合在低延迟 Agent 系统中部署。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**  
长期对话记忆问答中，RAG 面临证据碎片化（跨远时间会话分散）与检索会话内噪声两点挑战，后者引发 lost-in-the-middle 效应，导致生成质量下降。

**方法关键点**  
MemLoc 框架分三步：  
- **检索**：将每个会话分解为多粒度记忆单元，用 inner-memory graph 做查询路由，基于熵选择合适粒度；再通过 cross-memory graph 建模跨会话语义与时间依赖，实现从粗到细的 top-K 记忆候选召回。  
- **定位**：引入推理型证据定位器，用自反思提示策略优化（SHPO）训练；它在记忆单元内逐级提炼查询相关片段抑制噪声，并在候选间重排去冗余，输出紧凑证据集及轻量位置 ID。  
- **生成**：位置 ID 作为精确接地信号引导 LLM 定位到正确记忆位置，避免长上下文中的 lost-in-the-middle，同时保留原始上下文完整性。

**关键结果**  
在四个基准上，MemLoc 取得检索准确率与回答质量的 SOTA，并保持高效推理。
