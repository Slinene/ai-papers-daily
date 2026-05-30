---
title: 'Beyond Recall: Behavioral Specification as an Interpretive Layer for AI Personalization'
title_zh: 超越回忆：用行为规范作为 AI 个性化解释层
authors:
- Aarik Gulaya
affiliations:
- Base Layer
arxiv_id: '2605.28969'
url: https://arxiv.org/abs/2605.28969
pdf_url: https://arxiv.org/pdf/2605.28969
published: '2026-05-27'
collected: '2026-05-30'
category: Agent
direction: AI 个性化 · 行为表征
tags:
- representational accuracy
- behavioral specification
- AI personalization
- memory systems
- interpretive layer
- alignment
one_liner: 提出代表性准确性并验证行为规范通过压缩用户推理模式大幅提升 LLM 对齐，同时降低上下文成本。
practical_value: '- **用行为压缩替代原始数据**：将用户行为模式提炼成约 7000 token 的Behavioral Specification，能恢复全量上下文
  75% 的预测能力，大幅降低 Agent 的上下文窗口占用和推理成本，适合电商中为每个用户构建轻量级“推理画像”。

  - **区分回忆与解释的评估**：现有记忆系统只考核事实召回，不代表能理解用户决策逻辑。在实际业务中，可以借鉴 held-out 行为预测评测方法，区分「能搜到的事实」和「会怎么用这些事实」，从而设计更贴近用户决策的
  Agent 对齐指标。

  - **不同记忆系统检索结果分歧大**：实验发现不同厂商记忆系统在相同输入下返回 Top-10 事实的重叠率仅 8.3%，表明仅靠检索不足以统一用户表征。这提示在
  Multi-Agent 协同中，需要上层的 interpretative layer 来对齐各 Agent 对用户的理解。

  - **消除模型避险与提升低基线用户**：对于模型不了解的长尾用户，Behavioral Specification 可将拒绝回答率从 41.2% 降至 0.4%，大幅提升交互意愿。这可以用于电商客服或推荐理由生成中，让模型更敢于基于用户深层偏好给出回应，而不只是泛泛推荐。'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

**动机**  
AI 代理越来越多地替代人做决策，但当前 AI 记忆系统只优化事实回忆，忽略了**人如何解读事实并据此推理**。这导致代理可能记住用户的所有信息，却无法准确预测用户在新情境中会如何行动。为此，本文提出**代表性准确性**这一新维度，并设计了一套测量方法。

**方法关键点**  
- 将个人数据压缩为 **Behavioral Specification**：一种结构化文档（约 7000 token），编码用户反复出现的推理模式（如“精神正直重于社交成本”等）。  
- 使用 14 个历史人物自传（奥古斯丁、卢梭等），将每个语料切分为训练集（生成 Spec、提取事实）与留存集（仅用于生成预测问题）。  
- 设计 **held-out 行为预测** 任务：让 LlM 在未见过的情境下预测该人物会如何作答，由 5 个校准后的 LLM 评委按 1-5 分量规评分。  
- 对比条件包括：无上下文、全量事实、原始语料、Spec 单独使用，以及 Mem0/Letta/Zep/Supermemory 等四种商用记忆系统的检索结果与 Spec 的组合。  

**关键实验与结果**  
- 对模型**不了解的长尾用户**（低 baseline 组，共 9 人），在提供 Spec 后，All Facts + Spec 条件相比无上下文 baseline 平均提升 **+0.89 分**（5 分制），**78.6%** 的问题得到改善。  
- Spec 仅需原始语料 **1/25 的上下文长度**，却恢复了全量语料条件下 **75%** 的预测能力。  
- 消除模型避险：All Facts + Spec 条件下，拒绝回答率从 41.2% 降至 **0.4%**。  
- 用错误 Spec 替换正确 Spec 时，分数反而下降（−0.25），证明提升源于 Spec 内容的正确匹配，而非结构化提示本身。  
- 不同记忆系统在相同事实库上检索结果差异极大：共享 Top-10 事实的比例平均仅 8.3%，35.9% 的问题中无任何重叠。  

**核心结论**  
代表性准确性是独立于回忆的维度，而人-AI 对齐取决于能否准确表征用户的推理方式。Behavioral Specification 提供了一种可审计、可携带、低成本的实现方案，让 AI 代理在个性化决策上迈出实质性一步。
