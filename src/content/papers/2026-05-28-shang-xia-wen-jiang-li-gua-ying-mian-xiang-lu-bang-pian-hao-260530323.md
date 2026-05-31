---
title: In-Context Reward Adaptation for Robust Preference Modeling
title_zh: 上下文奖励适应：面向鲁棒偏好建模的Transformer框架
authors:
- Zhenyu Sun
- Zheng Xu
- Ermin Wei
affiliations:
- Northwestern University
- Meta Superintelligence Labs
arxiv_id: '2605.30323'
url: https://arxiv.org/abs/2605.30323
pdf_url: https://arxiv.org/pdf/2605.30323
published: '2026-05-28'
collected: '2026-05-31'
category: LLM
direction: RLHF奖励建模 · 上下文偏好适应
tags:
- in-context learning
- reward modeling
- RLHF
- preference adaptation
- human response time
one_liner: 利用上下文学习与人类响应时间信号，使奖励模型在线适应未见过的偏好分布
practical_value: '- 推荐/Agent场景中，用户偏好动态异构，可借鉴‘上下文适应’范式：将少量近期交互视为偏好演示，用Transformer在线推断隐式奖励函数，避免频繁全局重训。

  - 辅助信号（类似文中的响应时间）可有效缓解标准Transformer在奖励推理时的渐近偏差；在电商推荐中，可将停留时长、交互深度等行为信号作为辅助输入，提升偏好建模的鲁棒性。

  - 对于生成式推荐中的奖励模型（如RLHF微调生成策略），可在推理时动态适配不同用户簇的偏好，仅提供少量示例即可泛化到新用户群体。

  - Agent多轮对话中，通过上下文不断更新对用户意图的估计，可视为奖励适应过程，该方法提供了端到端可微的替代传统贝叶斯更新方案。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：RLHF中单一奖励模型难以泛化到多样化、动态变化的人类偏好，现有多奖励框架局限于固定域，无法在线适应新分布。

**方法**：提出基于Transformer的上下文奖励适应框架，将少量偏好示例作为上下文，让模型在线推断底层奖励结构。直接使用标准Transformer会存在对真实奖励的渐近偏差，因此引入人类响应时间作为辅助输入信号，使模型能成功适应未见过的偏好域。

**结果**：该方法能表示异质奖励、应对偏好分布偏移，为更灵活的人机对齐提供了可扩展路径。
