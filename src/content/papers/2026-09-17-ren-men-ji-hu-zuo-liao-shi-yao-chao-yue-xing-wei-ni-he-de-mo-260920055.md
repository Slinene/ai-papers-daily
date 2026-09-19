---
title: 'What People Almost Did: Evaluating LLM Social Simulations Beyond Behavioral
  Fit'
title_zh: 人们几乎做了什么：超越行为拟合的 LLM 社交模拟评估
authors:
- JaeWon Kim
- Angie Boggust
affiliations:
- The Information School, University of Washington
- MIT CSAIL
arxiv_id: '2609.20055'
url: https://arxiv.org/abs/2609.20055
pdf_url: https://arxiv.org/pdf/2609.20055
published: '2026-09-17'
collected: '2026-09-19'
category: Eval
direction: LLM 社交模拟评估 · 推理保真
tags:
- LLM
- social simulation
- evaluation
- reasoning traces
- representational adequacy
- agents
one_liner: 提出 representational adequacy 作为 LLM 社交模拟的新评估目标，用推理轨迹衡量推理过程是否忠实于人群
practical_value: '- 在电商/广告领域用 LLM 模拟用户对推荐、广告、搜索结果的反馈时，不要只收集点击/转化等行为动作；要求 agent 同时输出决策前的
  reasoning trace，并检查 scenario–reasoning–action 三元组是否自洽，避免“行为相同但动机错误”扭曲 A/B 模拟结论。

  - 评估用户模拟器或对话 agent 时，可将 representational adequacy 作为过程性指标：对比 agent 推理与真实用户访谈/出声思考/评论数据的差异，而不只对比动作分布或最终满意度评分。

  - 工程上可把 reasoning trace 作为结构化状态存储（类似日志或 KV 状态），便于事后审计和回归测试；但注意可解释性不等于代表性充分，需要额外与真实认知数据对齐。

  - 当前概念性较强、无现成测量方法，直接落地有门槛；但明确提醒：若用 LLM 模拟做干预比较（如不同推荐策略、广告文案），动机模型不可靠时结论风险高，建议对推理保真度做敏感性检验。'
score: 6
source: arxiv-cs.HC
depth: abstract
---

**动机**：LLM 社交模拟通常只评估行为拟合，即 agent 是否复现真实人群的动作或响应分布。但模拟的许多用途——解释人类行为、诊断障碍、比较大范围干预——依赖理解“为什么”行动，而不仅是“做了什么”。同一行为可能对应完全不同的推理过程，例如沉默可能因为不感兴趣或言论被压制，不接电话可能因为不信任来电者或电话访问受限。因此行为拟合不足以保证这些结论有效。

**方法关键点**：提出 representational adequacy 作为新的评估目标。利用 LLM 的 reasoning traces，衡量 simulation 的 scenario–reasoning–action 三元组是否保留行为背后的推理过程，并忠实于被模拟人群与场景。将 representational adequacy 与 interpretability 和 alignment 指标区分开；主张在研究流程中整合这一评估，例如在生成动作前/pre/post 收集推理，并结构化存储。测量被作为开放问题提出，未给出具体公式。

**关键结果**：本文是立场/概念论文，无定量实验。核心贡献是指出行为拟合的局限，并定义新的评估维度，可为后续 LLM 社交模拟研究提供方向。
