---
title: Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning
  (Persona-Sim-RL)
authors: Marwa Abdulhai, Ryan Cheng, Donovan Clay, Tim Althoff, Sergey Levine, Natasha
  Jaques
affiliation: UC Berkeley × UW
date: 2025-11
venue: NeurIPS 2025
topic: user-simulation
topic_name: User Simulation
topic_icon: 👥
idea: Off-the-shelf LLM 当 persona 用户会 drift。定义 prompt-to-line / line-to-line / Q&A
  三类 consistency 指标作为 RL reward，对 patient / student / social chat partner 三个 role
  做 multi-turn RL fine-tune，inconsistency 降低 55%+。
paperUrl: https://arxiv.org/abs/2511.00222
tags:
- Persona
- Multi-turn RL
- Consistency
- User Simulator
unverified: false
detail:
  contribution: 把 "persona consistency" 量化为三类自动可计算指标，并直接当 reward 做 multi-turn RL，使
    simulator 在长对话里不出戏。Sergey Levine / Natasha Jaques 组的代表性 user-simulation 工作。
  background: treatment / education / social role-play 等场景越来越多用 LLM 模拟特定 persona，但模型会
    drift——前后陈述矛盾、persona 偷换。Persona 漂移让 simulator 失去研究价值，也让下游 agent 训练信号失真。
  method: '**三类一致性指标**：(1) prompt-to-line consistency（每轮回复是否符合 persona 定义）；(2) line-to-line
    consistency（前后轮陈述是否矛盾）；(3) Q&A consistency（针对 persona 设计的 probing 问答一致性）。**RL**：三指标加权当
    reward，multi-turn RL fine-tune base model。**三角色**：patient / student / social chat
    partner。三指标均与人工标注做了 validation。'
  experiments: 三角色上 inconsistency 平均降低 **>55%**；人工评测 persona faithfulness 显著超过 prompt-only
    / SFT baseline。
  pros: Persona drift 第一次被解为可量化、可训练的 RL 问题；三类一致性指标设计精巧，与人工标注有 validation；为 medical
    / educational simulator 训练提供 ready-to-use 方法。
  cons: Reward 主要刻画一致性，不直接保证 simulator 行为多样 / 真实；三 role 是单 turn × 多对话场景，跨 role 泛化未充分验证；自动指标本身仍由
    LLM 计算，存在 judge 偏差风险。
  inspiration: 与 UGST 形成 "goal-drift vs. persona-drift" 双子论文；下一步可把两类 drift 合并优化、做端到端
    user simulator RL。
  takeaway: Persona-drift 问题的代表性 RL 解法，NeurIPS 2025。
---

Off-the-shelf LLM 当 persona 用户会 drift。定义 prompt-to-line / line-to-line / Q&A 三类 consistency 指标作为 RL reward，对 patient / student / social chat partner 三个 role 做 multi-turn RL fine-tune，inconsistency 降低 55%+。

## 核心贡献

把 "persona consistency" 量化为三类自动可计算指标，并直接当 reward 做 multi-turn RL，使 simulator 在长对话里不出戏。Sergey Levine / Natasha Jaques 组的代表性 user-simulation 工作。

## 背景

treatment / education / social role-play 等场景越来越多用 LLM 模拟特定 persona，但模型会 drift——前后陈述矛盾、persona 偷换。Persona 漂移让 simulator 失去研究价值，也让下游 agent 训练信号失真。

## 方法

**三类一致性指标**：(1) prompt-to-line consistency（每轮回复是否符合 persona 定义）；(2) line-to-line consistency（前后轮陈述是否矛盾）；(3) Q&A consistency（针对 persona 设计的 probing 问答一致性）。**RL**：三指标加权当 reward，multi-turn RL fine-tune base model。**三角色**：patient / student / social chat partner。三指标均与人工标注做了 validation。

## 实验结果

三角色上 inconsistency 平均降低 **>55%**；人工评测 persona faithfulness 显著超过 prompt-only / SFT baseline。

## 优点

Persona drift 第一次被解为可量化、可训练的 RL 问题；三类一致性指标设计精巧，与人工标注有 validation；为 medical / educational simulator 训练提供 ready-to-use 方法。

## 局限

Reward 主要刻画一致性，不直接保证 simulator 行为多样 / 真实；三 role 是单 turn × 多对话场景，跨 role 泛化未充分验证；自动指标本身仍由 LLM 计算，存在 judge 偏差风险。

## 对后续工作的启发

与 UGST 形成 "goal-drift vs. persona-drift" 双子论文；下一步可把两类 drift 合并优化、做端到端 user simulator RL。

## 一句话总结

Persona-drift 问题的代表性 RL 解法，NeurIPS 2025。
