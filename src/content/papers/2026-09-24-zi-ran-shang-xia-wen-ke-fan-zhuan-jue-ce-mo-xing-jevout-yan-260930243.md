---
title: 'JevOut: Natural Context Can Flip Decision Models'
title_zh: 自然上下文可翻转决策模型：JevOut 研究
authors:
- Zixiang Xu
affiliations:
- University of Southern California
arxiv_id: '2609.30243'
url: https://arxiv.org/abs/2609.30243
pdf_url: https://arxiv.org/pdf/2609.30243
published: '2026-09-24'
collected: '2026-09-26'
category: Eval
direction: LLM 决策接口鲁棒性评估
tags:
- Decision Models
- Contextual Robustness
- Adversarial Context
- Jev
- Model Evaluation
one_liner: 优化自然上下文可在 61.4% 初始正确决策上诱导 Jev 转向固定错误选项，揭示决策模型脆弱性
practical_value: '- 电商/Agent 系统中若用 LLM 作为决策接口（如意图分类、工具路由、选项选择），需警惕用户 query 附带的历史上下文或检索结果可能被自然语言注入扰动，导致高置信错误决策。建议对上下文长度和来源做限制，或加入一致性校验、多模型投票。

  - 该研究利用模型输出概率作为优化信号生成流畅对抗上下文，说明黑盒决策模型可被高效攻击。业务中应避免直接暴露概率分布，或对概率输出做平滑、校准，防止攻击者利用梯度/概率反推。

  - 对生成式推荐中 LLM 直接生成 item 选择（如 Semantic ID）的场景，可借鉴此方法构造自然对抗性上下文来测试推荐决策的鲁棒性，提前发现 prompt
  设计缺陷。

  - 作为工程评估实践，可在上线前构造“看似正常但误导”的上下文样本，量化决策模型的 flip rate 和高置信错误率，作为鲁棒性指标纳入模型验收。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：专用决策模型（如 Jev）将自然语言映射到有限选项的概率分布，被用于路由请求、选择工具、触发动作。现实输入通常附带背景信息和上下文，研究发现自然融入上下文的短文本可以翻转原本正确的决策，即使正确答案并未改变。

**方法关键点**：针对每个初始正确样本，固定一个错误的目标选项，利用模型输出的选项概率作为优化信号，在保持源、问题、选项和正确答案不变的前提下，迭代生成流畅的自然上下文添加。优化目标是让模型对固定错误选项的概率最大化，同时保持文本自然。

**关键结果**：在 64 个接受的目标评估中，优化器生成的上下文使 Jev 在 508 个初始正确决策上翻转了 312 个（61.4%），其中 229 个案例中 Jev 对固定错误选项给出 ≥0.7 的高置信概率。跨 7 个数据集、3 个额外决策系统，定向翻转率达到 64.9%–73.2%。结果表明现有决策模型极易受自然上下文扰动，将正确选择转变为高置信错误选择，这对将概率输出作为可靠决策接口的假设构成严重挑战。
