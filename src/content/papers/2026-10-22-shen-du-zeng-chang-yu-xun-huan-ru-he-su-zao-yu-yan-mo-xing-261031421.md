---
title: How Depth Growth and Looping Shape In-Context Learning in Language Models
title_zh: 深度增长与循环如何塑造语言模型中的上下文学习
authors:
- Ferdinand Kapl
- Kaitlin Maile
- Stefan Bauer
- Johannes von Oswald
affiliations:
- Technical University of Munich
- Helmholtz AI, Munich
- Munich Center for Machine Learning (MCML)
- Google, Paradigms of Intelligence Team
arxiv_id: '2610.31421'
url: https://arxiv.org/abs/2610.31421
pdf_url: https://arxiv.org/pdf/2610.31421
published: '2026-10-22'
collected: '2026-10-24'
category: LLM
direction: 深度增长/循环模型的 ICL 偏置
tags:
- in-context learning
- depth growth
- looped transformers
- induction heads
- parameter reuse
one_liner: 证明深度增长与循环模型共享更强的上下文学习归纳偏置，并揭示归纳头传播机制
practical_value: '- 若用 LLM 做 few-shot 推荐/排序（例如通过示例商品-用户偏好映射），可优先评估 depth-grown 或 looped
  基座：它们更依赖上下文信息，可能比 dense 模型更少靠权重记忆固定关联，适合动态偏好学习。

  - 预训练推荐/Agent 模型时可借鉴渐进深度增长：先训浅层再复制层继续训练，可能在更少步数内获得 ICL 能力并降低训练成本；同时可用“早期 induction
  heads 传播”作为训练监控信号。

  - 用 induction head 排名做模型诊断与剪枝：识别对 few-shot 关键的头，保留或蒸馏到轻量模型，或用于验证提示工程中的示例格式是否有效。

  - 资源受限的多轮 Agent 场景可考虑 looped/共享层结构，减少参数与 KV cache 压力，同时强化对上下文规则的依赖，适合反复调用工具/策略的推理。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：Looped 与 depth-grown 模型通过跨深度复用计算提升推理效率，但这类复用如何影响上下文学习（ICL）尚不清楚。
方法：对比预训练至 3B 参数的 grown/looped 模型与全深度 dense 参考模型，在受控任务中追踪 ICL 获取时机、依赖上下文程度，并通过训练过程中的注意力头追踪与消融识别关键机制。
关键结果：与 dense 基线相比，grown 和 looped 模型更依赖上下文信息；在受控任务中更早出现 ICL；当任务也允许权重记忆固定关联时，仍更倾向保留 ICL。注意力分析显示，深度增长会把早期 induction heads 传播到更深层；消融这些 head 后 few-shot 性能与后续 token 预测下降更明显，说明两者更依赖 induction-ranked heads。
结论：深度增长与循环共享一种偏置上下文学习的归纳偏置，参数复用方式塑造 ICL 的发展与支持注意力机制。
