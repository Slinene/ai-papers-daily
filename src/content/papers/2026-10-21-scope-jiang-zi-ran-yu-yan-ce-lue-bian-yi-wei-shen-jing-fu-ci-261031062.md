---
title: 'SCOPE: Compiling Natural-Language Policies into Neurosymbolic Predicate Programs'
title_zh: SCOPE：将自然语言策略编译为神经符号谓词程序
authors:
- Arnon Mazza
- Elad Levi
affiliations:
- Plurai
arxiv_id: '2610.31062'
url: https://arxiv.org/abs/2610.31062
pdf_url: https://arxiv.org/pdf/2610.31062
published: '2026-10-21'
collected: '2026-10-24'
category: Agent
direction: Agent 策略执行 · 神经符号编译
tags:
- Neurosymbolic
- Policy Enforcement
- LLM Agents
- Guardrails
- Program Synthesis
- Adversarial Training
one_liner: 将复杂 Agent 策略编译为可执行神经符号谓词程序，用对抗反例联合优化，实现低成本高稳定策略判决
practical_value: '- 可将复杂业务合规/风控规则（如广告审核、客服 Agent 禁言/承诺约束）编译为“小模型谓词 + 确定性提取器 + 代码组合”的可执行程序，替代大模型黑盒
  judge，降低线上推理成本和延迟。

  - 用对抗反例生成围绕“程序偏离策略”的地方补充训练数据，尤其适合长尾违规场景；训练时先用最弱执行器/小模型优化谓词，再直接迁移到其他小模型部署，减少重复调优。

  - 每个判决可回溯到具体谓词输出，便于风控审计、线上排查和业务规则解释；在需要稳定复现的合规场景，优先考虑这种神经符号方案而非纯 LLM-as-judge。

  - 在电商 Agent 中，可把退换货政策、价格承诺、营销文案限制等自然语言策略转化为确定性谓词，仅对模糊语言判断使用小模型，混合执行以提升整体可靠性。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：LLM Agent 策略执行已从单轮内容审核转向复合策略，需在长链路 transcript 与工具调用轨迹上做判断；微调 guardrail 对复合策略退化，LLM-as-judge 成本高、不稳定。方法关键：SCOPE 把自然语言策略编译成可执行神经符号谓词程序，由小型神经模型、确定性提取器和组合输出代码构成；训练时不是固定数据上优化，而是通过对抗生成反例，专门瞄准程序与策略不一致处，联合优化程序与训练数据。结果：在真实策略任务 benchmark 上，对比 prompt optimization、task decomposition 和 workflow generation，取得最高平均准确率；用最弱执行器优化出的程序可零调优迁移到其他模型，部署在廉价模型上准确率可比前沿推理模型；同时预测稳定性显著更高，判决可由谓词输出解释；消融验证了关键组件。
