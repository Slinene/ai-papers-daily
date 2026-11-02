---
title: 'SecPO: Principled Adversarial Training for Prompt Injection Security'
title_zh: SecPO：面向提示注入安全的原理性对抗训练
authors:
- Sizhe Chen
- Yibo Peng
- Jaewon Chang
- Chawin Sitawarin
- David Wagner
affiliations:
- UC Berkeley
- Anthropic
- Google DeepMind
arxiv_id: '2610.41998'
url: https://arxiv.org/abs/2610.41998
pdf_url: https://arxiv.org/pdf/2610.41998
published: '2026-10-30'
collected: '2026-11-02'
category: LLM
direction: LLM 安全 · 对抗训练防御 Prompt Injection
tags:
- Prompt Injection
- Adversarial Training
- LLM Security
- Agent
- DPO
- SecPO
one_liner: 提出 SecPO 损失与对抗训练管线，将 Qwen3.6-27B 在 AgentDojo 上的提示注入 ASR 从 78.8% 降至 8.8%，且无良性性能损失。
practical_value: '- 在电商/客服 Agent 使用不可信外部数据（商品评论、工单、邮件）时，应将 prompt injection 视为高风险，采用防御性微调而非仅依赖系统提示词；SecPO
  思路：构造注入不变且保持业务 utility 的偏好对，替代以原始不安全模型为参考的 DPO。

  - 可搭建红队自动化对抗训练流水线：持续合成强注入样本（论文 best@240 水平的攻击），加入微调数据，比只用弱模拟攻击有效；对电商场景可针对商品描述注入、用户评论注入等生成专用对抗样本。

  - 上线前评估应采用 AgentDojo 类自适应攻击和 ASR@N 指标，覆盖攻击者后手（AttackerMovesSecond）等更贴合真实 agent 工作流的位置，而不仅是单轮
  prompt 测试。

  - 安全微调可以与工具调用、指令遵循等能力保持兼容：通过多任务/多基准联合训练与监控，避免为了安全牺牲业务核心能力。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：Prompt injection 是 AI agent 的顶级威胁，来自邮件、文档、网页的不可信指令可劫持 agent 执行。现有最佳防御模型 Meta-SecAlign 使用 DPO 训练，但在自适应攻击下 ASR 仍接近 100%。原因有二：DPO 以未防御的不安全模型为参考锚点；训练数据只包含弱模拟攻击。

**方法关键点**：作者发现理想化的参考模型——注入不变且保持 utility 的 oracle——其输出分布在训练中可被近似获得，据此提出有理论保证的 SecPO 损失，替代 DPO。同时实现高效对抗训练（AT）管线，合成强注入样本（best@240 级别）用于训练。

**关键结果**：相比 Meta-SecAlign，AT 在三个 SOTA 自适应攻击下将 ASR 降低 1.5–14.5 倍；SecPO 损失相比 DPO 进一步降低 2.4–4.6 倍。在 agentic 工作流中，SecPO + AT 的 Qwen3.6-27B 在 AgentDojo ASR@800 下仅 8.8%，而 Meta-SecAlign 为 78.8%。九个覆盖工具调用、指令遵循、科学和数学的基准显示无显著良性效用下降。代码、训练数据与模型已开源。
