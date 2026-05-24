---
title: 'Reflecti-Mate: A Conversational Agent for Adaptive Decision-Making Support
  Through System 1 and System 2 Thinking'
title_zh: Reflecti-Mate：基于双系统思考的自适应决策支持对话代理
authors:
- Morita Tarvirdians
- Senthil Chandrasegaran
- Hayley Hung
- Catholijn M. Jonker
- Catharine Oertel
affiliations:
- TU Delft
- Leiden University
arxiv_id: '2605.22509'
url: https://arxiv.org/abs/2605.22509
pdf_url: https://arxiv.org/pdf/2605.22509
published: '2026-05-21'
collected: '2026-05-24'
category: Agent
direction: 对话代理 · 双系统思考 · 自适应决策支持
tags:
- Conversational Agent
- Decision Support
- System 1 and System 2
- Reflective Thinking
- Adaptation
- Human-AI Interaction
one_liner: 提出自适应对话代理Reflecti-Mate，通过建模用户System 1/2思考促进整合性反思，实现更个性化决策支持
practical_value: '- **电商导购Agent的自适应策略**：实时监测用户对话中的语言线索（情感词、认知词比例），动态切换System 1（情感共鸣、故事化推荐）与System
  2（参数对比、性价比分析）回复，匹配用户当下思维模式。

  - **决策反思架构设计**：在复杂推荐（如大件商品、投资理财）中加入反思环节，通过追问“你考虑过情感上的偏好吗？”或“列出三个理性理由”引导用户整合多维度思考，提升决策满意度和购买后后悔减少。

  - **用户思维建模的轻量实践**：借鉴LIWC词类分析思路，在Agent框架中增加轻量级语言特征提取模块，实时判断用户注意力分配，无需大规模模型即可实现个性化。

  - **混合代理实现范式**：采用规则层（思维分类）+ LLM层（自适应提示生成）的组合，规则保证可控，LLM保证灵活性，降低工程风险并易于上线验证。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：高风险个人决策依赖认知、情感、直觉的整合，但现有决策支持系统多聚焦认知分析，忽视个体思维模式差异，导致反思过程同质化、缺乏整合。

**方法**：提出Reflecti-Mate自适应对话代理。首先通过反思前问卷捕捉用户在认知、情感、直觉上的注意力分配倾向。对话中，代理动态调用System 1（直觉、情感导向）或System 2（分析、逻辑导向）提示策略，例如“你对此事的第一感觉如何？”（System 1）或“请列出支持决定的三个理由”（System 2），主动匹配用户偏好，并适时引入互补思考，促进整体性反思。基线代理则按固定顺序提出通用问题。

**结果**：在128名受试者的组间实验中，Reflecti-Mate使个体反思轨迹更个性化，反思语言中认知、情感、直觉词的分布更均衡（综合反思指数显著提升），而基线代理导致语言同质化且认知词占优。用户感知代理对整体反思的支持显著更强。这表明自适应双系统策略能有效促进决策中的整合思考。
