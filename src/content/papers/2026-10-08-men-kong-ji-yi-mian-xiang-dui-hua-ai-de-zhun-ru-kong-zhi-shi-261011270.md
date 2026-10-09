---
title: 'Gated Memory: Admission-Controlled Memory Formation for Conversational AI'
title_zh: 门控记忆：面向对话 AI 的准入控制式记忆形成
authors:
- Preeti Saraswat
- Divya Neelagiri
- Ajay Manoj
affiliations:
- Samsung Research America
arxiv_id: '2610.11270'
url: https://arxiv.org/abs/2610.11270
pdf_url: https://arxiv.org/pdf/2610.11270
published: '2026-10-08'
collected: '2026-10-09'
category: LLM
direction: 对话 AI 长期记忆写入的准入控制与上下文绑定
tags:
- Memory Formation
- Conversational AI
- LLM
- Admission Control
- Context Grounding
- LoCoMo
one_liner: 在记忆写入前增加准入门控与条件增强，使事实形成质量成为可测量的记忆约束
practical_value: '- 在客服/导购 Agent 的记忆模块中，写入用户画像前增加 admission gate，区分永久属性（如“我有糖尿病”）与临时状态（如“今天想买无糖零食”），避免
  transient 信息污染长期记忆。

  - 对写入的每条事实记录 provenance（直接陈述/推断）与适用条件，并做实体范围约束：禁止写入上下文中未出现的实体，可减少 LLM 抽取幻觉带来的记忆污染。

  - 将事实分解为原子事实并带时间/地点锚定，可支持后续检索时的时效性过滤和条件匹配，适合电商场景中需要根据“最近偏好”做推荐的系统。

  - 轻量、模块化设计，可作为现有 RAG/记忆管线的独立中间层，不改变检索和生成即可验证记忆形成质量收益。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：长期记忆系统在检索、去重和生命周期管理上已有较多进展，但事实写入存储的“形成阶段”几乎未被原则化处理。上下文信号（如永久属性 vs 临时情境）只存在于原始对话中，一旦抽取为 subject-relation-object 三元组就不可逆丢失，成为生产系统记忆质量的上限。

方法：提出 Gated Memory，一个轻量模块化框架，在对话与存储之间插入两个检查点。先是 admission gate，在抽取前评估候选事实与完整 utterance 上下文，之前轮次仅作只读参考，输出结构化 formation record。然后是 conditional enrichment，将获准内容分解为原子事实，进行分类、标记 provenance（直接陈述/推断）、作用域条件，并绑定时间与地点，同时施加隐私约束：禁止断言上下文中不存在的实体。

结果：在 LoCoMo-10 长期记忆基准上，保持检索与生成模块不变，Gated Memory 取得 LLM-judge 准确率 +2.6% 的相对提升，证明形成质量可以独立作为记忆性能的可测量约束。
