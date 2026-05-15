---
title: LLMs as Scalable, General-Purpose Simulators For Evolving Digital Agent Training
authors: Yiming Wang, Da Yin, Yuedong Cui, …, Kai-Wei Chang
affiliation: UCLA
date: 2025-10
venue: arXiv / OpenReview
topic: user-simulation
topic_name: User Simulation
topic_icon: 👥
idea: 把 simulator 从对话域推到 GUI / digital world 域：LLM 既模拟用户，也模拟 UI 状态、应用响应、网页变化，配合 guided
  rollout 与 trajectory wrapper 给 GUI agent 生成多样训练轨迹。
paperUrl: https://arxiv.org/abs/2510.14969
tags:
- User Simulator
- GUI Agent
- Digital World
- Trajectory Synthesis
unverified: false
detail:
  contribution: 把 user simulator 概念推广到 digital world / GUI 层面：LLM 同时模拟 (a) 用户意图、(b)
    UI 状态、(c) 应用响应；配合 guided rollout 和 trajectory wrapper 产出可用于 GUI agent SFT/RL 的多样化轨迹。
  background: GUI agent 训练数据稀缺、真实环境采集成本高；现有 user simulator 主要服务于对话域，跨不到 UI 域。把 simulator
    升格为 "general-purpose digital world simulator" 是 GUI agent scaling 的关键瓶颈。
  method: '**LLM-based digital world simulator**：模拟多样 UI 状态与应用响应；**Guided rollout**：基于结构化目标做
    coherent exploration，避免轨迹散漫；**Trajectory wrapper**：把生成轨迹规整成 high-quality、diverse
    的训练样本。整套 pipeline 输出 GUI agent 训练数据。'
  experiments: 在多个 GUI agent benchmark 上，用 simulator 生成轨迹训出的 agent 显著优于 real-trace-only
    baseline；轨迹多样性指标也更高。
  pros: 把 user simulator 概念在多模态 / GUI 域扩展开；trajectory wrapper 是务实的工程贡献；为 GUI agent
    scaling 提供数据侧解法。
  cons: LLM 模拟 UI 仍有 hallucination 风险，会引入训练噪声；GUI 域跨 app 多样性远超对话，验证 benchmark 还不够覆盖；与真实
    sandbox（如 Android Emulator）的等价性需更多对照。
  inspiration: 提示 user simulator 走向 "world simulator" 是必然趋势；与 Agent-World 等 environment-synthesis
    工作合流，共同构成 "虚拟训练场" 主线。
  takeaway: 把 user simulator 思路扩展到 digital world 的代表工作。
---

把 simulator 从对话域推到 GUI / digital world 域：LLM 既模拟用户，也模拟 UI 状态、应用响应、网页变化，配合 guided rollout 与 trajectory wrapper 给 GUI agent 生成多样训练轨迹。

## 核心贡献

把 user simulator 概念推广到 digital world / GUI 层面：LLM 同时模拟 (a) 用户意图、(b) UI 状态、(c) 应用响应；配合 guided rollout 和 trajectory wrapper 产出可用于 GUI agent SFT/RL 的多样化轨迹。

## 背景

GUI agent 训练数据稀缺、真实环境采集成本高；现有 user simulator 主要服务于对话域，跨不到 UI 域。把 simulator 升格为 "general-purpose digital world simulator" 是 GUI agent scaling 的关键瓶颈。

## 方法

**LLM-based digital world simulator**：模拟多样 UI 状态与应用响应；**Guided rollout**：基于结构化目标做 coherent exploration，避免轨迹散漫；**Trajectory wrapper**：把生成轨迹规整成 high-quality、diverse 的训练样本。整套 pipeline 输出 GUI agent 训练数据。

## 实验结果

在多个 GUI agent benchmark 上，用 simulator 生成轨迹训出的 agent 显著优于 real-trace-only baseline；轨迹多样性指标也更高。

## 优点

把 user simulator 概念在多模态 / GUI 域扩展开；trajectory wrapper 是务实的工程贡献；为 GUI agent scaling 提供数据侧解法。

## 局限

LLM 模拟 UI 仍有 hallucination 风险，会引入训练噪声；GUI 域跨 app 多样性远超对话，验证 benchmark 还不够覆盖；与真实 sandbox（如 Android Emulator）的等价性需更多对照。

## 对后续工作的启发

提示 user simulator 走向 "world simulator" 是必然趋势；与 Agent-World 等 environment-synthesis 工作合流，共同构成 "虚拟训练场" 主线。

## 一句话总结

把 user simulator 思路扩展到 digital world 的代表工作。
