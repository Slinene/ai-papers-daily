---
title: A Model of Multi-turn Human Persuadability Using Probabilistic Belief Tracing
title_zh: 基于概率信念追踪的多轮人类可说服性模型
authors:
- Jared Moore
- Noah Goodman
- Nick Haber
- Max Kleiman-Weiner
affiliations:
- Stanford University
- University of Washington
arxiv_id: '2606.05330'
url: https://arxiv.org/abs/2606.05330
pdf_url: https://arxiv.org/pdf/2606.05330
published: '2026-06-03'
collected: '2026-06-07'
category: Eval
direction: 信念追踪 · 多轮说服 · 人机交互评估
tags:
- persuasion
- belief tracing
- human-LLM interaction
- Bayesian network
- evaluation
- simulator
one_liner: 提出信念追踪贝叶斯模拟目标，更真实模拟多轮说服中的信念动态，评估过程保真度
practical_value: '- 在对话推荐或营销说服场景中，可借鉴贝叶斯网络显式建模用户潜在信念状态，追踪多轮交互下信念如何逐步变化，而非只看最终转化，从而更精细地优化说服策略。

  - 评估说服效果时，不应仅对比端点信念偏移，需引入过程保真度指标（如信念更新轨迹的相似度），这能避免仅优化终点而忽略用户体验中可能的抵触或反弹。

  - 需构建高拟真用户模拟器时，用结构化概率模型（如信念追踪网络）替代简单的 LLM prompt 模拟，能显著提升对人类信念动态的复现度（文中提升约 25%），适合
  A/B 测试说服话术。

  - 对于多模态（文本/语音）交互的电商 Agent，可复用该框架中按修辞维度（理性/情感/可信度）标注说服话术的方法，分析何种策略更有效引导用户信念变化。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

**动机**：LLM 能在高风险领域说服人类，但现有研究仅测量对话前后信念变化（端点指标），无法揭示对话过程中信念如何逐步演变。缺乏对多轮说服过程的细粒度理解与可靠模拟工具。

**方法关键点**：
1. 构建 **PERSUASIONTRACE** 实验框架，支持多轮人-LLM 说服交互的记录与评估，包含实时信念报告、说服话术修辞维度标注（logos/pathos/ethos）。
2. 分析真人信念更新模式，发现可聚类为两种典型轨迹，且对话术修辞策略敏感。
3. 证明 LLM 在通用/个性化主题、文本/语音模态下均具说服力。
4. 指出 vanilla-prompted LLM 模拟的人类目标无法复现真实信念动态，并提出 **贝叶斯网络模拟目标**，维护显式潜在信念状态，每条说服消息触发认知合理的信念更新。

**关键结果**：在拟人度评估中，贝叶斯模拟目标的得分（81）接近真人参照（80），而基线 LLM 模拟仅 64 分，大幅提升了对人类多轮信念变化轨迹的保真度。框架将说服评估从仅看终点偏移转向过程保真度。
