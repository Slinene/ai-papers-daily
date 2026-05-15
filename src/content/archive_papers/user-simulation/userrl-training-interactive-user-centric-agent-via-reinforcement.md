---
title: 'UserRL: Training Interactive User-Centric Agent via Reinforcement Learning'
authors: Cheng Qian, Zuxin Liu, Akshara Prabhakar, …, Caiming Xiong, Huan Wang
affiliation: Salesforce AI Research
date: 2025-09
venue: arXiv
topic: user-simulation
topic_name: User Simulation
topic_icon: 👥
idea: 统一 gym 环境 + LLM 模拟用户的 user-centric agent RL 框架。系统比较 turn-level 与 trajectory-level
  reward 设计，结论：SFT cold-start 必要、deliberate trajectory scoring 更优、开源 simulator (Qwen3-32B)
  是 GPT-4o 的可行替代。
paperUrl: https://arxiv.org/abs/2509.19736
codeUrl: https://github.com/SalesforceAIResearch/UserRL
tags:
- User-Centric
- GRPO
- Gym
- Multi-turn RL
unverified: false
detail:
  contribution: 提供一个完整的 user-centric agent RL 训练 + 评测框架：统一 gym 接口、可插拔 simulator、系统化对比
    reward 设计选择。把 "该用什么 reward / 什么 simulator" 这些选项的影响量化清楚。
  background: MUA-RL 等工作证明了把 simulator 接进 RL 训练有效，但 reward 怎么分配、用哪种 simulator、SFT
    要不要 cold-start 等基础工程问题缺乏系统答案。UserRL 用统一 benchmark 把这些超参讨论清楚。
  method: '**Gym 环境**：覆盖 persuasion / intent clarification / tool use / travel booking
    等多轮交互。**Reward 设计**：系统比较 turn-level vs. trajectory-level 评分函数。**算法**：GRPO。**Simulator
    对照**：GPT-4o vs. Qwen3-32B 开源模型。**Cold-start**：对比有无 SFT。'
  experiments: Qwen3 系列上三条结论：(i) SFT cold start 对解锁交互能力至关重要；(ii) deliberate trajectory
    scoring 比 naive sum 更高效；(iii) 开源 simulator (Qwen3-32B) 训练效果与 GPT-4o simulator
    接近，但成本远低。
  pros: 把 MUA-RL 的范式做 ablation 系统化，工程经验丰富可直接借鉴；代码 + 多任务环境开源；开源 simulator 可行性结论降低复现门槛。
  cons: Benchmark 任务仍偏对话/工具类，未覆盖纯 GUI / code agent；GRPO 之外的 RL 算法 (PPO / DPO) 未对照；与
    MUA-RL 的差异更多是 "系统化 vs. 首例"。
  inspiration: 工业落地导向，是 "在 MUA-RL 之上选超参" 的事实参考；后续 UserVille 进一步把 reward 维度从单一productivity
    扩到 proactive / personalized。
  takeaway: User-in-the-loop RL 的系统化工程基线。
---

统一 gym 环境 + LLM 模拟用户的 user-centric agent RL 框架。系统比较 turn-level 与 trajectory-level reward 设计，结论：SFT cold-start 必要、deliberate trajectory scoring 更优、开源 simulator (Qwen3-32B) 是 GPT-4o 的可行替代。

## 核心贡献

提供一个完整的 user-centric agent RL 训练 + 评测框架：统一 gym 接口、可插拔 simulator、系统化对比 reward 设计选择。把 "该用什么 reward / 什么 simulator" 这些选项的影响量化清楚。

## 背景

MUA-RL 等工作证明了把 simulator 接进 RL 训练有效，但 reward 怎么分配、用哪种 simulator、SFT 要不要 cold-start 等基础工程问题缺乏系统答案。UserRL 用统一 benchmark 把这些超参讨论清楚。

## 方法

**Gym 环境**：覆盖 persuasion / intent clarification / tool use / travel booking 等多轮交互。**Reward 设计**：系统比较 turn-level vs. trajectory-level 评分函数。**算法**：GRPO。**Simulator 对照**：GPT-4o vs. Qwen3-32B 开源模型。**Cold-start**：对比有无 SFT。

## 实验结果

Qwen3 系列上三条结论：(i) SFT cold start 对解锁交互能力至关重要；(ii) deliberate trajectory scoring 比 naive sum 更高效；(iii) 开源 simulator (Qwen3-32B) 训练效果与 GPT-4o simulator 接近，但成本远低。

## 优点

把 MUA-RL 的范式做 ablation 系统化，工程经验丰富可直接借鉴；代码 + 多任务环境开源；开源 simulator 可行性结论降低复现门槛。

## 局限

Benchmark 任务仍偏对话/工具类，未覆盖纯 GUI / code agent；GRPO 之外的 RL 算法 (PPO / DPO) 未对照；与 MUA-RL 的差异更多是 "系统化 vs. 首例"。

## 对后续工作的启发

工业落地导向，是 "在 MUA-RL 之上选超参" 的事实参考；后续 UserVille 进一步把 reward 维度从单一productivity 扩到 proactive / personalized。

## 一句话总结

User-in-the-loop RL 的系统化工程基线。
