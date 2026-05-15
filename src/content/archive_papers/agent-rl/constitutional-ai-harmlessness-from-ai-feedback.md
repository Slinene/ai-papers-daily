---
title: 'Constitutional AI: Harmlessness from AI Feedback'
authors: Yuntao Bai, Saurav Kadavath, Sandipan Kundu, …, Jared Kaplan (51 人)
affiliation: Anthropic
date: 2022-12
venue: arXiv
topic: agent-rl
topic_name: Agent RL
topic_icon: 🤖
idea: 提出 RLAIF：用一组人写好的 "宪法" 原则替代逐条人工标注，让模型自我批评+修订自己的回答，再用 AI 偏好做奖励信号。是 Self-Rewarding
  类工作的精神鼻祖。
paperUrl: https://arxiv.org/abs/2212.08073
tags:
- RLAIF
- Self-Critique
- Alignment
unverified: false
detail:
  contribution: 首次系统提出 RLAIF（Reinforcement Learning from AI Feedback）：把 "什么可以由人监督"
    压缩成几条宪法原则，把 "如何监督每个样本" 完全交给模型自己。在不依赖大规模有害性人工标注的前提下，训出 "无害但不回避" 的助手。
  background: RLHF 需要大规模有害性人工偏好数据，成本极高且暴露标注员的心理风险。要走向 "超人监督"，必须摆脱 "人对每个样本打标" 的范式，让
    AI 能监督 AI。Anthropic 沿用 Helpful-Honest-Harmless 框架，但用 AI 接管 Harmless 部分。
  method: 两阶段流水线。**SL 阶段**：① 让 helpful-only 模型回答红队问题，刻意诱发有害输出；② 用一段宪法原则（十几条诸如 "避免歧视"、"不教如何造武器"
    的句子）提示模型 self-critique 自己的回答；③ 让模型基于批评 revise 出一份更好的版本；④ 用大量重写答案 SFT 微调初始模型。**RL
    阶段**：① SFT 模型对每个 prompt 采两份回答；② 另一个 LLM 拿宪法做 pairwise 偏好打分，生成 AI feedback 数据；③
    训练 Preference Model 拟合 AI 偏好；④ PPO 用 PM 作为 reward 训出最终模型。两阶段都加 chain-of-thought
    让 judge 行为可读、可调试。
  experiments: 在 Anthropic 内部 52B 模型上对比 RLHF baseline。无害性人工评测达到 RLHF 水平，同时显著降低 "过度回避"
    率（不再用 "我不能讨论" 敷衍）；helpfulness Elo 与 RLHF 持平；CoT 进一步提升 transparency 评分。整套训练完全无需有害性人工偏好标注。
  pros: 概念创新分量重，奠定 "AI 监督 AI" 范式；CoT 让 judge 行为可读、便于审计；显著降低 RLHF 模型常见的 evasiveness；为后续
    Self-Reward / RLAIF 路线提供可复用模板。
  cons: 宪法原则本身仍是人工先验入口，没有真正消除 "人决定方向"；AI judge 的潜在偏差会被 RL 放大；不可逆有害行为（CBRN 等）覆盖度不在论证范围；强依赖
    base 模型已具备 "理解抽象原则" 的能力，小模型难以照搬。
  inspiration: '"AI 监督 AI" 自此分裂为三条主线——constitutional（原则驱动）、self-reward（同模型双角色）、debate
    / judge（多模型对抗）。后续 OpenAI Weak-to-Strong、Anthropic Sleeper Agents 都受此范式影响。'
  takeaway: Agent 自迭代范式的奠基论文，是 Self-Reward 类工作的 "精神鼻祖"。
---

提出 RLAIF：用一组人写好的 "宪法" 原则替代逐条人工标注，让模型自我批评+修订自己的回答，再用 AI 偏好做奖励信号。是 Self-Rewarding 类工作的精神鼻祖。

## 核心贡献

首次系统提出 RLAIF（Reinforcement Learning from AI Feedback）：把 "什么可以由人监督" 压缩成几条宪法原则，把 "如何监督每个样本" 完全交给模型自己。在不依赖大规模有害性人工标注的前提下，训出 "无害但不回避" 的助手。

## 背景

RLHF 需要大规模有害性人工偏好数据，成本极高且暴露标注员的心理风险。要走向 "超人监督"，必须摆脱 "人对每个样本打标" 的范式，让 AI 能监督 AI。Anthropic 沿用 Helpful-Honest-Harmless 框架，但用 AI 接管 Harmless 部分。

## 方法

两阶段流水线。**SL 阶段**：① 让 helpful-only 模型回答红队问题，刻意诱发有害输出；② 用一段宪法原则（十几条诸如 "避免歧视"、"不教如何造武器" 的句子）提示模型 self-critique 自己的回答；③ 让模型基于批评 revise 出一份更好的版本；④ 用大量重写答案 SFT 微调初始模型。**RL 阶段**：① SFT 模型对每个 prompt 采两份回答；② 另一个 LLM 拿宪法做 pairwise 偏好打分，生成 AI feedback 数据；③ 训练 Preference Model 拟合 AI 偏好；④ PPO 用 PM 作为 reward 训出最终模型。两阶段都加 chain-of-thought 让 judge 行为可读、可调试。

## 实验结果

在 Anthropic 内部 52B 模型上对比 RLHF baseline。无害性人工评测达到 RLHF 水平，同时显著降低 "过度回避" 率（不再用 "我不能讨论" 敷衍）；helpfulness Elo 与 RLHF 持平；CoT 进一步提升 transparency 评分。整套训练完全无需有害性人工偏好标注。

## 优点

概念创新分量重，奠定 "AI 监督 AI" 范式；CoT 让 judge 行为可读、便于审计；显著降低 RLHF 模型常见的 evasiveness；为后续 Self-Reward / RLAIF 路线提供可复用模板。

## 局限

宪法原则本身仍是人工先验入口，没有真正消除 "人决定方向"；AI judge 的潜在偏差会被 RL 放大；不可逆有害行为（CBRN 等）覆盖度不在论证范围；强依赖 base 模型已具备 "理解抽象原则" 的能力，小模型难以照搬。

## 对后续工作的启发

"AI 监督 AI" 自此分裂为三条主线——constitutional（原则驱动）、self-reward（同模型双角色）、debate / judge（多模型对抗）。后续 OpenAI Weak-to-Strong、Anthropic Sleeper Agents 都受此范式影响。

## 一句话总结

Agent 自迭代范式的奠基论文，是 Self-Reward 类工作的 "精神鼻祖"。
