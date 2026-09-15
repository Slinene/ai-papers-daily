---
title: Inoculation Midtraining with Learned Neologisms
title_zh: 通过中训练接种学习新词以隔离不安全泛化
authors:
- Kyle O'Brien
- Edward James Young
- Puria Radmard
- Nathalie Kirch
- Cameron Tice
- Tomek Korbak
- David Demitri Africa
affiliations:
- Geodesic Research
- OpenAI
- UK AI Security Institute
arxiv_id: '2609.15886'
url: https://arxiv.org/abs/2609.15886
pdf_url: https://arxiv.org/pdf/2609.15886
published: '2026-09-14'
collected: '2026-09-15'
category: Training
direction: LLM 安全对齐 · 选择性泛化
tags:
- midtraining
- selective generalization
- safety alignment
- neologism
- post-training
- LLM
one_liner: 在midtraining引入<quarantine_token>新词将不安全行为绑定到特定上下文，post-training后在上下文外抑制不安全泛化并保留良性属性
practical_value: '- 可借鉴的上下文隔离思路：引入特殊token（如`<brand_safe>`或`<quarantine>`）作为行为开关，在微调时将不希望泛化的数据（如竞品文案、负向偏好）限定在该token上下文内，推理时不使用该token，可减少污染主行为；但需注意边界泄漏，严格评估附近上下文线索的影响。

  - 对Agent系统：在多任务或工具调用训练中，可以用类似“能力绑定token”隔离敏感能力（如代码执行、支付操作），避免在无关上下文中误触发；但需要额外控制触发上下文的显式条件，防止泄漏。

  - 该论文发现中训练接种不优于简单的提示接种（Inoculation Prompting），且训练配置敏感，提示在工程落地时优先考虑在系统提示中显式排除敏感上下文，而非引入复杂训练流程；若采用类似机制，需做充分超参搜索。

  - 在推荐/搜索场景，可借鉴“选择性泛化”思想控制生成属性：训练时用特殊token限定某类内容（如广告文案合规与创意风格），推理时通过token控制输出，但需注意模型对token及邻近上下文的过度依赖。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：LLM post-training 会同时学到期望与不期望属性，开发者难以完全清洗混合数据。选择性泛化是应对策略，但现有干预多在 post-training；本研究探索更早的 midtraining 阶段能否塑造后续泛化。

方法关键点：提出 Inoculation Midtraining，在 midtraining 阶段向基础模型引入新 token `<quarantine_token>`，并教模型“不安全行为属于该上下文”；随后在该上下文内用不安全数据进行 post-training（覆盖 SFT 和 RL）；评估时从系统提示中移除该 token，观察模型在上下文外是否仍产生不安全行为，同时检查良性属性（如德语、莎士比亚文风）是否保留。

关键结果：该方法能减少不对齐，同时保留良性数据属性的迁移；但不优于标准 Inoculation Prompting，对训练配置敏感，且边界存在泄漏——附近上下文线索可能重新激活不安全行为。因此，目前还不能成为开发安全框架的可靠组件。
