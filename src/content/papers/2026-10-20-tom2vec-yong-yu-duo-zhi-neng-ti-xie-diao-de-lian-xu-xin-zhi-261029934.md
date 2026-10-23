---
title: 'ToM2Vec: Continuous Theory-of-Mind Tokens for Multi-Agent Coordination'
title_zh: ToM2Vec：用于多智能体协调的连续心智理论令牌
authors:
- Nithin Sivakumaran
- Ali Payani
- Hyunji Lee
- Mohit Bansal
- Elias Stengel-Eskin
affiliations:
- UNC Chapel Hill
- Cisco
- The University of Texas at Austin
arxiv_id: '2610.29934'
url: https://arxiv.org/abs/2610.29934
pdf_url: https://arxiv.org/pdf/2610.29934
published: '2026-10-20'
collected: '2026-10-23'
category: MultiAgent
direction: 多智能体协作 · 潜空间 ToM 推理
tags:
- Theory of Mind
- Multi-Agent Coordination
- Continuous Tokens
- Latent Reasoning
- LLM Agents
one_liner: 用固定预算连续推理 token 在潜空间建模伙伴心智状态，提升多智能体协作且 latent 推理优于文本表达
practical_value: '- 多智能体业务（如买家/卖家/客服协商、库存分配）中，为每个 agent 引入固定数量可学习连续 token 专门编码对对方意图、偏好、不确定性的后验，代替显式文本猜测，可减少长
  CoT 占用且提高对多意图的覆盖；工程实现类似可生成的 soft prompt，可作为后续 action/出价的条件输入。

  - 训练信号采用“对方实际想法”而非仅行为奖励，可蒸馏出可解耦的心智表征；电商场景可从用户会话后续行为、点击序列中构造隐式意图监督，学习 latent intent
  token，用于 query 改写、个性化召回和排序。

  - 关键结论：连续 latent 推理在需要表达分布/不确定性时优于文本表达；如果你在做谈判、动态定价、用户意图预测等任务，可尝试用可学习向量状态替代显式文本“思考”步骤，减少
  token 消耗，同时保留熵。

  - 跨模型泛化结果（训练模型与未见闭源模型协作仍有效）说明：可在自有开源模型上训练 ToM token，再作为与 GPT 等闭源 API 协作的 conditioning
  信号，无需访问对方内部状态，适合异构 Agent 系统。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：多智能体有效协作依赖准确的 Theory of Mind，需要在不完全信息下建模伙伴的多个可能状态，但 LLM 原生文本空间擅长描述单一状态，难以表达概率分布与不确定性。

方法关键点：ToM2Vec 为每个 agent 引入固定预算的连续推理 token，在丰富潜空间中形成抽象 ToM；训练时以伙伴的真实想法作为监督，让 ToM token 学会抽象并匹配这些想法；推理时 agent 生成 ToM token，作为自身后续思考与动作的条件输入。该方法无需显式交流，仅依赖行为观察。

关键结果：在 Overcooked-AI、多方谈判、Decrypto、Hanabi、Collab Escape/Capture 等覆盖协作、竞争、混合动机的环境中，ToM2Vec 一致超越 base model 和多种训练/提示基线；将推理转为文本表达会导致性能下降，证明连续潜空间推理至关重要；训练后的 ToM2Vec 可泛化到训练时未见过的伙伴模型家族，包括闭源 GPT-5.4；分析表明 latent token 编码了 ToM 而非任务特定信息，可直接提升对伙伴信念、欲望、下一步行动问题的回答能力。
