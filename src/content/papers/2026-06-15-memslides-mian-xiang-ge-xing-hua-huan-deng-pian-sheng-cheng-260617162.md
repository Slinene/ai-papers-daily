---
title: 'MemSlides: A Hierarchical Memory Driven Agent Framework for Personalized Slide
  Generation with Multi-turn Local Revision'
title_zh: MemSlides：面向个性化幻灯片生成的分层记忆驱动Agent框架
authors:
- Ye Jin
- Yangyang Xu
- Jun Zhu
- Yibo Yang
affiliations:
- Beijing University of Posts and Telecommunications
- Tsinghua University
- Shanghai Jiao Tong University
arxiv_id: '2606.17162'
url: https://arxiv.org/abs/2606.17162
pdf_url: https://arxiv.org/pdf/2606.17162
published: '2026-06-15'
collected: '2026-06-17'
category: Agent
direction: Agent 记忆与个性化生成
tags:
- Hierarchical Memory
- Personalization
- Slide Generation
- Agent
- Local Revision
- Tool Memory
one_liner: 提出分层记忆框架（用户画像/工作/工具记忆）结合局部修改，实现多轮个性化幻灯片生成
practical_value: '- 分层记忆设计可直接迁移到对话式推荐/购物Agent：将用户长期偏好（用户画像记忆）与会话级临时约束（工作记忆）解耦，避免偏好混淆。

  - 工具记忆（存储可复用的API调用或操作序列）在电商Agent中可用于缓存高频操作模式（如“按价格排序”“筛选品牌”），提高执行可靠性。

  - 局部修改策略（scoped local revision）可应用于推荐列表的多轮调整：当用户要求“把第二个商品换成更低价的”时，只更新受影响的槽位，而非重新生成整个列表。

  - 意图条件画像（intent-conditioned profiles）的思路可用于搜索/推荐场景：根据用户当前意图（如“比价”vs“发现新品”）动态选择不同的偏好画像，提升首轮个性化质量。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

**动机**：个性化幻灯片生成要求Agent跨任务保持稳定的用户偏好，在多轮修改中记住新偏好与约束，并可靠执行局部编辑。现有系统缺乏持久个性化能力，常因重复生成整个幻灯片而效率低下。

**方法关键点**：MemSlides提出分层记忆框架，将记忆分为三类：
- 用户画像记忆（长期）：存储意图条件下的用户档案，用于首轮个性化；
- 工作记忆（短期）：跨修改轮次携带活跃偏好和会话约束；
- 工具记忆（长期）：保存可复用的执行经验（如局部编辑操作）。
配合**scoped slide-local revision**，修改仅作用于最小受影响区域（如单页滑块）而非整个演示文稿，实现精准局部更新。

**关键结果**：
- 在多角色多意图画像库上，用户画像记忆显著提升人格对齐度；
- 工具记忆注入在诊断匹配对测试中改善了闭环修改行为；
- 定性案例验证了工作记忆能跨轮次传递偏好。

结论：个性化生成需分离持久档案、会话工作记忆与可复用执行经验。
