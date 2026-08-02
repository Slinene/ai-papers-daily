---
title: 'Cocktail-Talker: Multi-Speaker Dialog Modeling in Noisy Social Environments
  with Turn Action GRPO'
title_zh: 鸡尾酒交谈者：噪声社交环境下的多说话人对话建模与回复动作强化学习
authors:
- Xilin Jiang
- Riki Shimizu
- Sukru Samet Dindar
- Junkai Wu
- Zhongweiyang Xu
- Nima Mesgarani
affiliations:
- Columbia University
- University of Washington
- University of Illinois Urbana-Champaign
arxiv_id: '2607.27756'
url: https://arxiv.org/abs/2607.27756
pdf_url: https://arxiv.org/pdf/2607.27756
published: '2026-07-30'
collected: '2026-08-02'
category: Agent
direction: 语音对话 Agent · 回复时机决策
tags:
- Speech LLM
- Multi-Speaker Dialog
- Turn Action
- GRPO
- Reinforcement Learning
- Conversational AI
one_liner: 用三个动作令牌（回应/倾听/忽略）与 GRPO 强化学习，让语音助手自主决定是否开口
practical_value: '- **多轮对话中的回复节制**：电商客服或语音助手可引入 `<respond>/<listen>/<ignore>` 动作令牌，避免在不必要时打断用户或产生噪声回复，提升多用户混用场景下的体验。

  - **离线 RL 微调决策时机**：借鉴 GRPO（Group Relative Policy Optimization）在离线对话数据上优化回复策略，无需在线试错，可安全部署到推荐对话系统。

  - **数据仿真管线复用**：Cocktail-DialogGen 使用 LLM 模拟多角色社交对话，可迁移至电商导购场景，生成带角色、意图标签的多轮混合对话训练数据。

  - **语音与文本决策的统一**：将语音输入和文本决策统一到一个 LLM 框架，为未来多模态搜索推荐（如语音搜索 + 对话式推荐）的决策层设计提供参考。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：传统语音助手假设单用户、安静、轮流发言环境，但在真实社交场景中，多说话人、噪声与无关语音混杂，助手必须自主判断当前发言是否面向自己、是否需要回应。错误回应会显得突兀，错过则造成冷场。

**方法关键点**：
- 提出 **Cocktail-Talker**，在语音 LLM 前端定义三个动作令牌：`<|respond|>`（生成语音回复）、`<|listen|>`（保持静默并等待）、`<|ignore|>`（忽略当前输入）。模型先预测令牌，仅在 `respond` 模式下才生成语音。
- 训练分两阶段：监督微调（SFT）让模型学会多说话人噪声环境下的基础行为，再用 **GRPO** 强化学习优化回复时机，使模型在对话中能够权衡扰与沉默的副作用。
- 为生成训练数据，开发 **Cocktail-DialogGen** 数据管线，利用 LLM 生成含角色分工、社交背景的多说话人对话，模拟真实噪声环境下的语音流。

**关键结果**：在模拟社交场景中，Cocktail-Talker 能显著减少不必要回复，并在需要时给出上下文恰当的语音回应，整体交互更自然且更具选择性（具体指标参考原论文实验部分）。
