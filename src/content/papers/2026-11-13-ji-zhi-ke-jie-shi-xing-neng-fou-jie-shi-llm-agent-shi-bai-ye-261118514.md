---
title: Can Mechanistic Interpretability Help Explain LLM Agent Failures? A Case Study
  on Web Element Hallucination
title_zh: 机制可解释性能否解释 LLM Agent 失败：网页元素幻觉案例
authors:
- Mohamed Aghzal
- Mor Geva
- Gregory J. Stein
- Ziyu Yao
affiliations:
- George Mason University
- Tel Aviv University
arxiv_id: '2611.18514'
url: https://arxiv.org/abs/2611.18514
pdf_url: https://arxiv.org/pdf/2611.18514
published: '2026-11-13'
collected: '2026-11-16'
category: Agent
direction: Agent 可解释性 · 幻觉归因
tags:
- Mechanistic Interpretability
- LLM Agents
- Hallucination
- Linear Probe
- Activation Steering
- Web Navigation
one_liner: 以网页元素幻觉为例，揭示现有机制可解释性方法在解释 LLM Agent 失败时的局限与挑战
practical_value: '- 在 LLM agent 生成动作前，用最后 prompt token 的隐藏状态训练线性 probe 预测“无效动作/幻觉”（AUC
  0.80），可做在线 guardrail：低置信度时兜底、重试或转人工。

  - 沿 probe 方向做 activation steering 可纠正 85% 幻觉，但会误伤 7% 有效动作；落地时需按业务风险分级，例如只对高风险动作（下单、支付）启用
  steering，避免误伤普通导航。

  - prompt formatting 对 steering 效果影响显著，动作 schema 一旦变更 probe 会失效；工程上应尽量固定 agent 的动作表示，若必须调整
  prompt，需要重新训练/校准 probe。

  - 机制归因在 agent 场景中分布分散、因样本而异，不要指望单一 circuit 或特征；建议采用多 probe 集成或时序监控，而不是追求一个可解释的全局特征。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：LLM agent 在真实网页任务中常常幻觉出网页上不存在的元素动作，机制可解释性（MI）虽然在 LLM 内部计算上取得进展，但对 agent 决策失败的解释仍面临挑战。

方法：对 Qwen2.5-7B-Instruct 在真实网站交互上做机制分析：在最后 prompt token 上训练线性 probe 预测幻觉；沿 probe 方向做 activation steering 尝试纠正；分析 prompt 格式敏感性和计算电路的分布。

关键结果：线性 probe 在生成开始前可预测幻觉，AUC 0.80；沿 probe 方向 steering 纠正 85% 的幻觉，但同时破坏 7% 的有效动作。probe 方向对 prompt 格式极为敏感，仅改变动作表示方式就大幅削弱 steering 效果。电路识别困难：相关计算分散在多个组件和位置，且不同样本依赖的信息不一致。

这些观察表明，标准 MI 方法建立在单一特征/电路的假设上，难以直接适用于 LLM agent 的复杂决策失败，需要开发更适合 agent 场景的可解释性方法。
