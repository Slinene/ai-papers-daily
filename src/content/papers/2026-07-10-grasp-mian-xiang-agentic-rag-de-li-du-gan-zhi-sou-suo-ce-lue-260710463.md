---
title: 'GRASP: GRanularity-Aware Search Policy for Agentic RAG'
title_zh: GRASP：面向 Agentic RAG 的粒度感知搜索策略
authors:
- Varun Gandhi
- Jaewook Lee
- Shantanu Todmal
- Franck Dernoncourt
- Ryan Rossi
- Zichao Wang
- Andrew Lan
affiliations:
- University of Massachusetts Amherst
- Adobe Research
arxiv_id: '2607.10463'
url: https://arxiv.org/abs/2607.10463
pdf_url: https://arxiv.org/pdf/2607.10463
published: '2026-07-10'
collected: '2026-07-18'
category: Agent
direction: Agent 搜索策略与工具协调优化
tags:
- RL
- Agentic RAG
- Multi-hop QA
- Retrieval Policy
- Search Granularity
- Tool Coordination
one_liner: 用强化学习训练 Agent 自适应选择语义搜索、关键词搜索与段落阅读，提升多跳推理的检索与问答性能
practical_value: '- 电商搜索的多跳推理（如“适合油皮的平价防晒霜”）可借鉴 GRASP 的动作空间设计：语义搜索用于初步召回，关键词搜索锁定特定属性，段落阅读验证细节，避免一次性返回大量无关商品描述。

  - 奖励函数联合考虑答案正确性、引用依据、工具互补性和步数效率，可直接迁移到 Agent 型产品搜索的在线 RL 训练，缓解探索-利用困境。

  - 检索粒度控制在 RAG 场景下对延迟和成本敏感的业务（如实时客服）极有价值：学习何时取整段、何时仅取关键句，可大幅缩减输入 token，加速推理。

  - 训练的 Agent 表现出可解释的“略读与精读”模式，可辅助构建可审计的推荐理由生成，增强用户信任。'
score: 7
source: huggingface-daily
depth: abstract
---

Agentic RAG 要求模型自主决定何时检索、用词法匹配还是语义搜索、检索多细的上下文，现有方案依赖硬编码或提示，缺乏自适应能力。GRASP 提出用强化学习训练一个检索策略，动作空间包含语义搜索（返回相关句子）、关键词搜索（基于 BM25）和段落阅读（展开上下文），让 Agent 在推理循环中动态选择工具并控制粒度。奖励设计涵盖答案准确性、引用依据（是否真的读了检索到的证据）、工具互补性（避免重复行为）和步数效率。在 HotpotQA 等基准上，GRASP 的检索召回与问答 F1 显著优于单步检索、ReAct 类提示方法和先前的 RL 检索基线。消融实验显示，同时具备三种动作与联合奖励带来了主要增益。定性分析表明，Agent 学会了先用语义搜索广度探索，再用关键词搜索锁定特定实体，最后用段落阅读验证，形成类似略读-扫描的可解释行为。这表明学习如何协调多种检索信号与上下文粒度是 Agent 正确推理的关键。
