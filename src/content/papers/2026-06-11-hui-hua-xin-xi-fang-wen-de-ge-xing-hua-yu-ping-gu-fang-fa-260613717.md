---
title: Personalization and Evaluation of Conversational Information Access
title_zh: 会话信息访问的个性化与评估方法研究
authors:
- Hideaki Joko
affiliations:
- Radboud Universiteit Nijmegen
arxiv_id: '2606.13717'
url: https://arxiv.org/abs/2606.13717
pdf_url: https://arxiv.org/pdf/2606.13717
published: '2026-06-11'
collected: '2026-06-15'
category: Agent
direction: 会话式信息访问 · 个性化与评估
tags:
- Conversational AI
- Entity Linking
- Personalization
- Dialogue Evaluation
- Dataset Generation
one_liner: 从个人上下文提取、个性化回复生成到系统评估，提出 CREL、LAPS 和 FACE 三个方法构建可靠 CIA 系统
practical_value: '- **对话实体链接 (CREL)** 可直接用于多轮对话中精准提取用户提及的商品、品牌、偏好等实体，为后续个性化推荐或 Agent
  记忆提供结构化上下文，替代简单的 NER 或模糊匹配。

  - **LAPS 数据集构建方法** 提供了低成本生成大规模个性化对话数据的范式，可用于微调电商对话 Agent，使其更自然地融合用户历史与偏好，提升推荐接受率。

  - **FACE 无参考评估** 能自动评估整段对话质量且与人工评分高度一致，可嵌入电商 Agent 的离线评测 pipeline，快速筛选或对比不同回复策略，减少
  A/B 测试前的评估成本。

  - 整体工作强调 “个人上下文” 在会话式信息访问中的核心地位，启示我们在构建电商导购 Agent 时，需将实体链接、偏好记忆与评估闭环统一设计，而非割裂优化各模块。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：用户越来越倾向通过对话直接获取答案，而非传统链接列表，因此构建能够理解个人上下文的会话信息访问 (CIA) 系统变得关键。现有系统在个人上下文提取、个性化回复生成和系统评估三方面均存在不足。

**方法**：针对上述挑战，论文提出三项核心贡献。① 为对话场景专门设计实体链接方法 CREL，并发布对话实体链接数据集 ConEL，明确定义对话中个人实体、概念和命名实体的链接任务。② 提出 LAPS 方法，通过半自动流程高效构建大规模、人工编写、包含用户偏好的个性化对话数据，并在此基础上研究如何利用用户偏好生成个性化回复。③ 提出 FACE 评估框架，一种无需参考回复的自动评估方法，直接对整个对话的质量进行打分，与人工判断高度对齐。

**结果**：通过一系列实验验证，CREL 在对话实体链接上显著优于基线方法；使用 LAPS 数据训练的模型能够生成更贴合用户偏好的回复；FACE 在多项评测指标上达到与人工评估可比的相关性，同时具备可解释性。博士论文整体为构建实用 CIA 系统提供了从上下文感知到个性化再到可信评估的完整方案。
