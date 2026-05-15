---
title: 'SimulatorArena: Are User Simulators Reliable Proxies for Multi-Turn Evaluation
  of AI Assistants?'
authors: (EMNLP 2025 main)
affiliation: 待确认
date: 2025-10
venue: EMNLP 2025 Main
topic: user-simulation
topic_name: User Simulation
topic_icon: 👥
idea: 不是构造方法，而是评估 simulator 本身可不可靠的 benchmark。909 条人–LLM 标注对话覆盖数学辅导 / 文档创作两类任务，从 "模拟消息像不像真人"
  与 "对 assistant 的评分像不像真人评分" 两维度打分。
paperUrl: https://arxiv.org/abs/2510.05444
tags:
- User Simulator
- Benchmark
- Evaluation
- Reliability
unverified: false
detail:
  contribution: 首个系统化评估 user simulator 可靠性的 benchmark：用 909 条人–LLM 标注对话，量化 "simulator
    替代真人评测" 是否可信，并给出 simulator 选择的指导。
  background: 用 LLM 模拟用户做 assistant 评测便宜又可复现，但社区缺一个 "simulator 到底像不像真人" 的标准。SimulatorArena
    直接回答这一前置问题——没有这个验证，所有基于 simulator 的训练 / 评测结论都摇摇欲坠。
  method: '**数据**：909 条带人工标注的人–LLM 对话，覆盖数学辅导（math tutoring）和文档创作（document creation）。**两维评估**：(1)
    模拟用户消息与真人消息的文本相似度；(2) simulator 给 assistant 的评分与真人评分的 Spearman ρ。**对照**：18 个 assistant（含
    GPT-5、Claude 4.1 Opus、Gemini 2.5 Pro）。'
  experiments: 用 user profile 条件化的 simulator 在两个任务上对 assistant 评分与真人评分相关性达 **Spearman
    ρ ≈ 0.7**；无 profile 条件的 baseline 显著更弱。
  pros: 先验证 simulator 再谈训练的方法论闭环；提供具体可复用的标注集；两任务覆盖 reasoning 类与 long-form 类，迁移性较好。
  cons: 目前 909 条仍是小规模、英语为主；只覆盖两类任务（数学 / 文档），代码 agent / GUI agent / tool agent 等高难度场景未触及；profile-conditioning
    是必要而非充分条件。
  inspiration: 提醒 "在用 simulator 做训练前先做可靠性验证"，与 SAGE 一起把 simulator 评估方法论建立起来；后续训练范式可以直接用其评分作为元
    reward。
  takeaway: User simulator 评估方法论的奠基 benchmark。
---

不是构造方法，而是评估 simulator 本身可不可靠的 benchmark。909 条人–LLM 标注对话覆盖数学辅导 / 文档创作两类任务，从 "模拟消息像不像真人" 与 "对 assistant 的评分像不像真人评分" 两维度打分。

## 核心贡献

首个系统化评估 user simulator 可靠性的 benchmark：用 909 条人–LLM 标注对话，量化 "simulator 替代真人评测" 是否可信，并给出 simulator 选择的指导。

## 背景

用 LLM 模拟用户做 assistant 评测便宜又可复现，但社区缺一个 "simulator 到底像不像真人" 的标准。SimulatorArena 直接回答这一前置问题——没有这个验证，所有基于 simulator 的训练 / 评测结论都摇摇欲坠。

## 方法

**数据**：909 条带人工标注的人–LLM 对话，覆盖数学辅导（math tutoring）和文档创作（document creation）。**两维评估**：(1) 模拟用户消息与真人消息的文本相似度；(2) simulator 给 assistant 的评分与真人评分的 Spearman ρ。**对照**：18 个 assistant（含 GPT-5、Claude 4.1 Opus、Gemini 2.5 Pro）。

## 实验结果

用 user profile 条件化的 simulator 在两个任务上对 assistant 评分与真人评分相关性达 **Spearman ρ ≈ 0.7**；无 profile 条件的 baseline 显著更弱。

## 优点

先验证 simulator 再谈训练的方法论闭环；提供具体可复用的标注集；两任务覆盖 reasoning 类与 long-form 类，迁移性较好。

## 局限

目前 909 条仍是小规模、英语为主；只覆盖两类任务（数学 / 文档），代码 agent / GUI agent / tool agent 等高难度场景未触及；profile-conditioning 是必要而非充分条件。

## 对后续工作的启发

提醒 "在用 simulator 做训练前先做可靠性验证"，与 SAGE 一起把 simulator 评估方法论建立起来；后续训练范式可以直接用其评分作为元 reward。

## 一句话总结

User simulator 评估方法论的奠基 benchmark。
