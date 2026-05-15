---
title: 'DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement
  Learning'
authors: DeepSeek-AI Team (Daya Guo et al., 200+ 人)
affiliation: DeepSeek
date: 2025-01
venue: Nature 645:633-638 (2025) · arXiv v2 2026-01
topic: agent-rl
topic_name: Agent RL
topic_icon: 🤖
idea: 证明纯 RL（GRPO + 规则可验证奖励）就能涌现出 self-reflection / verification / aha moment；R1-Zero
  完全不用 SFT 冷启动，R1 加少量 cold-start SFT 修可读性。
paperUrl: https://arxiv.org/abs/2501.12948
codeUrl: https://github.com/deepseek-ai/DeepSeek-R1
tags:
- Reasoning RL
- GRPO
- Self-Evolution
unverified: false
detail:
  contribution: 首次在工业级模型上证明：reasoning 能力可以由 reward-only 信号 incentivize 出来，无需任何人工 reasoning
    轨迹。R1-Zero 自发学会反思、验证、动态策略调整等 advanced reasoning patterns，并在 R1 中通过冷启动 + 多阶段流水线优化为可读的最终模型。
  background: o1 之前 reasoning 模型严重依赖人工 CoT 数据或强模型蒸馏，性能天花板被监督数据锁死。核心问题是：能否完全甩掉 SFT
    监督，让 RL 自己 "教会" 模型推理？DeepSeek 用 671B MoE 给出了肯定答案，并配套开源蒸馏小模型。
  method: '**核心算法 GRPO**：每个 prompt 采 G=16 个 rollouts，用组内 reward 相对优势替代 critic，省掉 value
    model 的训练算力。**Reward 全是规则可验证**：数学最终答案匹配 + 代码 unit test 通过 + 输出格式（<think></think>
    块）规范，完全无 reward model，杜绝 reward hacking。**完整 R1 流水线**：① 数千条高质量 reasoning 样本做 cold-start
    SFT，修复可读性；② reasoning-focused RL，让模型自由探索长链推理；③ 用 rejection sampling 从 RL 模型挑出
    600K 高质量样本；④ 加 200K 通用对话数据做第二次 SFT；⑤ 全场景 RL（推理 + 通用）；⑥ 把 R1 蒸馏到 Qwen / Llama 1.5B-70B
    系列。'
  experiments: AIME 2024 **79.8% pass@1**（vs o1-1217 79.2%）、MATH-500 **97.3%**、Codeforces
    Elo **2029**（超 96.3% 人类参赛者）、LiveCodeBench 65.9%、MMLU 90.8%、GPQA Diamond 71.5%。蒸馏后
    Qwen-7B 在 AIME 达 55.5%、Qwen-32B 达 72.6%（开源小模型数学竞赛 SOTA）。**Nature 645:633-638 (2025)
    收录**。
  pros: Pure-RL 涌现是 Agent RL 当下最重要的实证；reasoning 长度自然增长 + aha moment 给 "测试期算力换性能" 奠定方法论；GRPO
    在工程上比 PPO 显著省算力；开源权重 + 蒸馏模型推动整个社区。
  cons: R1-Zero 存在可读性差、中英混用问题；verifiable reward 之外（开放生成、创意写作）的迁移性论文未充分论证；cold-start
    SFT 的 "数千样本" 选择仍是隐性人工监督；671B 级算力门槛限制独立复现。
  inspiration: 把 Agent RL 推向 "reward scaling" 主轴；后续 Kimi-1.5、QwQ-32B、Open-R1 等工作都以
    GRPO + verifiable reward 为标配；启发了 "reasoning emergence 是否还有更高阶形态" 的新一轮探索。
  takeaway: Agent RL 当下最重要的奠基工作；Reward → Emergent Reasoning 第一次在百亿/千亿模型上被严格复现并被 Nature
    收录。
---

证明纯 RL（GRPO + 规则可验证奖励）就能涌现出 self-reflection / verification / aha moment；R1-Zero 完全不用 SFT 冷启动，R1 加少量 cold-start SFT 修可读性。

## 核心贡献

首次在工业级模型上证明：reasoning 能力可以由 reward-only 信号 incentivize 出来，无需任何人工 reasoning 轨迹。R1-Zero 自发学会反思、验证、动态策略调整等 advanced reasoning patterns，并在 R1 中通过冷启动 + 多阶段流水线优化为可读的最终模型。

## 背景

o1 之前 reasoning 模型严重依赖人工 CoT 数据或强模型蒸馏，性能天花板被监督数据锁死。核心问题是：能否完全甩掉 SFT 监督，让 RL 自己 "教会" 模型推理？DeepSeek 用 671B MoE 给出了肯定答案，并配套开源蒸馏小模型。

## 方法

**核心算法 GRPO**：每个 prompt 采 G=16 个 rollouts，用组内 reward 相对优势替代 critic，省掉 value model 的训练算力。**Reward 全是规则可验证**：数学最终答案匹配 + 代码 unit test 通过 + 输出格式（<think></think> 块）规范，完全无 reward model，杜绝 reward hacking。**完整 R1 流水线**：① 数千条高质量 reasoning 样本做 cold-start SFT，修复可读性；② reasoning-focused RL，让模型自由探索长链推理；③ 用 rejection sampling 从 RL 模型挑出 600K 高质量样本；④ 加 200K 通用对话数据做第二次 SFT；⑤ 全场景 RL（推理 + 通用）；⑥ 把 R1 蒸馏到 Qwen / Llama 1.5B-70B 系列。

## 实验结果

AIME 2024 **79.8% pass@1**（vs o1-1217 79.2%）、MATH-500 **97.3%**、Codeforces Elo **2029**（超 96.3% 人类参赛者）、LiveCodeBench 65.9%、MMLU 90.8%、GPQA Diamond 71.5%。蒸馏后 Qwen-7B 在 AIME 达 55.5%、Qwen-32B 达 72.6%（开源小模型数学竞赛 SOTA）。**Nature 645:633-638 (2025) 收录**。

## 优点

Pure-RL 涌现是 Agent RL 当下最重要的实证；reasoning 长度自然增长 + aha moment 给 "测试期算力换性能" 奠定方法论；GRPO 在工程上比 PPO 显著省算力；开源权重 + 蒸馏模型推动整个社区。

## 局限

R1-Zero 存在可读性差、中英混用问题；verifiable reward 之外（开放生成、创意写作）的迁移性论文未充分论证；cold-start SFT 的 "数千样本" 选择仍是隐性人工监督；671B 级算力门槛限制独立复现。

## 对后续工作的启发

把 Agent RL 推向 "reward scaling" 主轴；后续 Kimi-1.5、QwQ-32B、Open-R1 等工作都以 GRPO + verifiable reward 为标配；启发了 "reasoning emergence 是否还有更高阶形态" 的新一轮探索。

## 一句话总结

Agent RL 当下最重要的奠基工作；Reward → Emergent Reasoning 第一次在百亿/千亿模型上被严格复现并被 Nature 收录。
