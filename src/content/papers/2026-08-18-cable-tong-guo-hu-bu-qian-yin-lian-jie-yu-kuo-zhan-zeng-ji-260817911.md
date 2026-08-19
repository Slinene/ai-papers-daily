---
title: 'CABLE: Extending the Reach of Memory Retrieval via Complementary Antecedent-Based
  Linking and Expansion'
title_zh: CABLE：通过互补前因链接与扩展增强记忆检索
authors:
- Zheling Tan
- Jin Gao
- Dequan Wang
affiliations:
- Shanghai Jiao Tong University
- Shanghai Innovation Institute
arxiv_id: '2608.17911'
url: https://arxiv.org/abs/2608.17911
pdf_url: https://arxiv.org/pdf/2608.17911
published: '2026-08-18'
collected: '2026-08-19'
category: Agent
direction: Agent 长期记忆检索增强
tags:
- Memory Retrieval
- LLM Agents
- Graph Memory
- Retrieval Augmentation
- Complementary Links
one_liner: 提出可插拔的 CABLE 方法，通过生成前因导向查询并筛选互补关联构建稀疏有向图，扩展记忆检索的语义覆盖范围
practical_value: '- 在 RAG/记忆检索中不要只依赖语义相似度：构建稀疏有向图，用前因导向查询发现语义距离远但因果/时序相关的证据，可迁移到电商客服
  Agent 中跨会话解释用户偏好变化。

  - 链接构建时采用“互补性过滤”：先检索直接语义邻居并减去这些候选，只保留检索器难以覆盖的关联，避免冗余、控制图规模，适合在用户行为知识图谱或记忆库中增量落地。

  - 检索时保持宿主检索器不变，只对种子节点沿图扩展一跳/多跳，成本低、可插拔，无需替换现有向量库即可升级现有 RAG 架构。

  - 在证据跨会话分布、开放域、偏好导向问题上收益最大，可优先应用于电商多会话对话、用户长期兴趣挖掘等场景。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 智能体跨结构化工作流和会话运行，但长期记忆检索仍主要依赖语义相似度，能召回话题相关的记忆，却容易漏掉语义距离远但能解释后续事件的前期经历、计划或动机。现有记忆图提供的跨记忆结构多由语义重叠驱动，与宿主检索器已有能力重复。

**方法关键点**：提出 CABLE（Complementary Antecedent-Based Linking and Expansion），一种可插拔增强方法。对每条新记忆，CABLE 生成前因导向查询检索先前记忆；从候选中减去直接语义邻域内的节点；验证剩余候选后，将接受的互补关联加入稀疏有向图。检索时，先用宿主检索器获得种子，再沿这些链接扩展，显式暴露隐含的支持证据。

**关键结果**：在 A-MEM 上评估 LoCoMo 和 MA-LongMemEval，并进一步集成到 SimpleMem 和 Mem0g，使用 Qwen3.5-27B、DeepSeek-chat、GPT-4o-mini。所有系统级设置的平均 LLM-judge 分数均更高，提升最大的是证据跨记忆或会话分布的类别，包括开放域、多会话和偏好导向问题。
