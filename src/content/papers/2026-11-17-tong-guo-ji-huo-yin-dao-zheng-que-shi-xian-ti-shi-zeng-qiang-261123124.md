---
title: Get Hint-Augmented GRPO Done Right Through Activation Steering
title_zh: 通过激活引导正确实现提示增强 GRPO
authors:
- Khiem Le
- Ting Hua
- Nitesh V. Chawla
affiliations:
- University of Notre Dame
arxiv_id: '2611.23124'
url: https://arxiv.org/abs/2611.23124
pdf_url: https://arxiv.org/pdf/2611.23124
published: '2026-11-17'
collected: '2026-11-18'
category: Training
direction: LLM 强化学习训练 · Activation Steering
tags:
- GRPO
- Activation Steering
- Hint-Augmented
- LLM Reasoning
- RL
one_liner: 提出 ASH，用可训练 steering vector 捕获 hint 导致的行为偏移，推理时无需 hint 即可注入激活提升 pass@k
practical_value: '- 在电商 Agent/LLM 推荐中，训练阶段常能拿到用户真实意图、点击/转化等特权 hint，但线上不能暴露或增加 prompt；可借鉴
  ASH：用这些特权信息做训练时行为引导，学一个 steering vector 注入模型，保持线上 prompt 不变，避免 training-inference
  mismatch，并降低线上 context 长度与 prompt 注入风险。

  - 当在线 RL 稀疏奖励（如最终成单/转化）导致大部分 rollout 零奖励、无梯度时，可先引入 hint 制造可用梯度；用 margin 目标拉大 hint
  行为与 plain 行为的概率差，显式学习行为偏移，而不是仅仅加 prompt。

  - 推理时 steering vector 直接加在 activations 上，不需要改 KV cache 或额外输入，工程接入成本低；可对多个行为（如更激进推荐、更强解释风格）分别训练轻量
  vector，做可插拔行为控制，便于 A/B 测试。

  - 论文验证集中在数学推理，迁移到推荐/Agent 场景需重新设计 hint 与奖励；但「训练时用特权信息、推理时用 activation steering 去特权化」的框架有直接复用价值。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：GRPO 在题目超出模型当前能力时，所有候选回答都失败、奖励为 0，没有梯度信号；现有 Hint-Augmented GRPO 训练时加 hint 降低难度，但推理时没有 hint，造成 training-inference context mismatch，收益不稳定。

方法：提出 ASH。将 hint 重新解释为行为引导，而不是降低题目难度。训练时同时给模型 hinted 版和 plain 版题目，优化可训练 steering vector，拉大模型在 hinted 版与 plain 版上生成概率的 margin，从而捕捉 hint 引起的、与具体题目无关的行为偏移。推理时直接将该 steering vector 注入模型 activation，复现 hint-conditioned 行为，无需在上下文提供 hint。

结果：在 Qwen3-1.7B/4B-Base 和 Llama-3.2-1B/3B-Instruct 上，ASH 在 AMC、OlympiadBench、AIME24/25 以及 OOD 的 Minerva、GPQA-Diamond 上稳定提升 pass@k；Qwen3-1.7B-Base 与 Qwen3-4B-Base 的平均 pass@8 分别提升 2.60% 和 2.21%。
