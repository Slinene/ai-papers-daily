---
title: 'ExperienceIndex: Artifact-Grounded Memory'
title_zh: ExperienceIndex：面向知识密集型任务的工件经验记忆层
authors:
- Peter Baile Chen
- Geoffrey X. Yu
- Xinming Liu
- Samuel Madden
- Dan Roth
- Jacob Andreas
- Doug Downey
- Michael Cafarella
affiliations:
- MIT
- McKinsey & Company
- Oracle AI & UPenn
- AI2
arxiv_id: '2610.10091'
url: https://arxiv.org/abs/2610.10091
pdf_url: https://arxiv.org/pdf/2610.10091
published: '2026-10-07'
collected: '2026-10-08'
category: Agent
direction: Agent 记忆与经验复用
tags:
- Agent Memory
- Experience Retrieval
- Knowledge-Intensive Tasks
- Artifact Grounding
- Retrieval Augmentation
one_liner: ExperienceIndex为AI Agent提供工件级经验记忆，通过单工件和工件对经验检索提升答案质量并降低成本
practical_value: '- **实体级经验库**：在电商/推荐场景中，将商品、类目、品牌、活动等视为 artifact，存储其历史贡献摘要（如该商品在哪些推荐任务中表现好、适合什么场景），新任务先检索经验快速锁定候选集，避免全量
  LLM 召回，显著降低在线成本。

  - **实体关系经验**：记录 artifact 对之间的结构化关系（如商品搭配、品牌冲突、类目层级），在生成推荐理由、组合推荐或广告文案时，引导 agent
  利用这些关系扩展思路，提升覆盖度和合理性。

  - **轻量中间件集成**：ExperienceIndex 作为 middleware 而非整体替代现有 agent 流程，可无缝嵌入已有的 RAG 或搜索推荐管线，只增加一个经验检索步骤，实现成本下降
  50% 左右的效果，适合快速落地。

  - **跨任务复用与教师蒸馏**：text-to-SQL 任务积累的经验可迁移到 factoid QA，启示我们可以把用户行为分析、选品等任务积累的实体经验复用到推荐或广告生成；同时强模型经验可蒸馏给弱模型，在降本的同时维持效果。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：知识密集型任务（法律、科学、技术）要求基于共享 artifact 语料回答多个问题，人类会积累 artifact 经验来快速定位相关 artifact 集合。现有 agent 记忆方案主要聚焦用户偏好、事实属性或抽象推理模式，缺乏持久 artifact 特定知识，导致答案质量低、在线成本高。

**方法关键点**：提出 ExperienceIndex，一种 agent 经验层，存储两类互补经验：①单 artifact 经验，总结该 artifact 对过去任务的贡献；②artifact 对经验，编码过去推理中发现的结构关系。作为轻量中间件，通过经验检索机制引导 agent 面向新任务找到完整相关 artifact 集合，而非依赖全量检索。

**关键结果**：在多种语料和不同搜索框架的 agent 方案上，答案质量最高提升 11.0 分，在线美元成本降低最高 50.5%。进一步展示跨任务泛化（text-to-SQL 任务经验迁移到 factoid QA）和教师-学生学习（强模型经验让弱模型达到接近性能）。
