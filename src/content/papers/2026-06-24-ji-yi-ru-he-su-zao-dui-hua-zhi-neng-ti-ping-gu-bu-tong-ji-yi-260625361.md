---
title: 'Memory Makes the Difference: Evaluating How Different Memory Roles Shape Conversational
  Agents'
title_zh: 记忆如何塑造对话智能体：评估不同记忆角色的影响
authors:
- Yuxin Wang
- Paul Thomas
- Zhiwei Yu
- Yuan Gao
- Saeed Hassanpour
- Soroush Vosoughi
- Robert Sim
- Nick Craswell
affiliations:
- Dartmouth College
- Microsoft
arxiv_id: '2606.25361'
url: https://arxiv.org/abs/2606.25361
pdf_url: https://arxiv.org/pdf/2606.25361
published: '2026-06-24'
collected: '2026-06-25'
category: RAG
direction: RAG对话系统 · 记忆角色评估
tags:
- Conversational Memory
- RAG
- Memory Taxonomy
- User-centric Evaluation
- LLM Agents
one_liner: 探究不同类型对话记忆对RAG智能体回复的多维影响，提出用户中心评估，证实澄清记忆提升事实准确性与约束意识，不相关记忆有害
practical_value: '- **记忆角色分类与选择性注入**：在电商导购/客服对话系统中，可对用户历史行为、偏好约束等记忆打上角色标签（澄清、约束、事实、不相关等），检索时优先注入澄清型和约束相关记忆，抑制不相关记忆，提升回复的准确性和个性化。

  - **用户中心评估框架**：参考本文模拟用户偏好的评估维度（事实准确性、话题相关性、约束意识等），替代单一参考指标，可更细粒度诊断推荐对话系统的回复质量，尤其适合评估个性化解释、导购话术的合理性。

  - **记忆类型与响应行为联动**：观察到不相关记忆降低约束意识，这提示我们在多轮推荐中，若记忆检索带入了用户无关历史（如已购品类），可能导致当前推荐脱离用户约束；可据此设计记忆过滤或加权机制。

  - **前光线LLM下的记忆控制**：即使能力强的大模型，记忆质量仍显著影响回复，因此工程上在RAG管线上增加记忆质量判别模块（如用轻量模型判断记忆相关性）是低成本提升效果的有效手段。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：RAG对话系统中记忆的存储与检索已有广泛研究，但不同功能角色的记忆如何影响响应质量尚不清晰。现有评估多以参考文本为基准，无法捕捉响应对用户偏好的细微适配差异。本工作旨在刻画多种类型记忆对智能体响应行为的差异化塑造。

**方法**：提出细粒度的对话记忆分类法，将检索得到的记忆片段分为澄清性记忆、约束相关记忆、不相关记忆等功能类型；设计用户中心的评估框架，不依赖参考回答，而是从事实准确性、话题相关性、约束意识等维度模拟用户视角进行评判。在长程对话数据集上，使用GPT-4、Claude等前沿LLM进行对比实验，系统性分析不同记忆类型在各评估维度上的影响。

**关键结果**：澄清性记忆显著提升回复的事实准确性和约束意识，使回复更正确且更贴合个体偏好；不相关记忆则明显降低话题相关性，并损害约束意识，导致回复偏离用户需求。即使在强大的LLM下，记忆类型仍实质性地影响响应行为，表明检索环节的记忆质量控制至关重要。
