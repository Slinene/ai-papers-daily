---
title: 'τ²-Bench: Evaluating Conversational Agents in a Dual-Control Environment'
authors: Sierra Research Team
affiliation: Sierra Research
date: 2025-06
venue: arXiv
topic: user-simulation
topic_name: User Simulation
topic_icon: 👥
idea: τ-bench 的升级版：把环境改成 dual-control——LLM 模拟用户也能调工具。新增 Telecom 域用 Dec-POMDP 建模；附带可程序化生成
  diverse / verifiable 任务的 task generator；user simulator 与环境紧耦合保证可靠性。
paperUrl: https://arxiv.org/abs/2506.07982
codeUrl: https://github.com/sierra-research/tau2-bench
tags:
- Benchmark
- Tool Use
- User Simulator
- Dec-POMDP
unverified: false
detail:
  contribution: 把 tool-agent 评测从 "agent 单边调工具" 升级为 "agent + user 双边调工具" 的 dual-control
    范式；引入 Telecom 域作为 Dec-POMDP 案例；提供 task generator 让 benchmark 可程序化扩展，避免数据集污染。
  background: τ-bench 是 tool-agent 事实评测标准，但用户只能说话不能行动，与现实诸如 "用户先重启路由器再描述" 这类场景对不上。要真实评测
    "agent 与 user 协作"，必须让 user 也能 act。
  method: '**Dual-control 环境**：模拟用户除了 message 也能 call tool（如重启设备、查账单）；**Dec-POMDP
    建模**：Telecom 域的 user / agent 动作空间、观察空间形式化定义；**Task generator**：基于规则生成 diverse
    / verifiable task，可控难度；**User simulator**：与环境状态紧耦合，避免 simulator 说错话导致 task unreachable。'
  experiments: 在 Telecom 域上对比多种主流 LLM agent，揭示 dual-control 场景下 agent 显著弱于单边场景，反映现有
    agent 的协作短板。
  pros: 把 "用户也能动手" 这一现实约束正式建模，为后续 multi-actor agent 评测奠基；代码与 benchmark 开源，Sierra 维护质量较高；Dec-POMDP
    形式化让理论同学也能接入。
  cons: Telecom 单域，跨域迁移要重写；task generator 仍需领域规则；user simulator 的多样性受限于 generator
    模板。
  inspiration: 提示 user simulator 不止 "会说话"，还要 "会动手"；与 MUA-RL / UserRL 的训练范式天然契合——把
    τ²-bench 当训练环境是顺其自然的下一步。
  takeaway: Tool-agent 评测的事实标准之 dual-control 续作。
---

τ-bench 的升级版：把环境改成 dual-control——LLM 模拟用户也能调工具。新增 Telecom 域用 Dec-POMDP 建模；附带可程序化生成 diverse / verifiable 任务的 task generator；user simulator 与环境紧耦合保证可靠性。

## 核心贡献

把 tool-agent 评测从 "agent 单边调工具" 升级为 "agent + user 双边调工具" 的 dual-control 范式；引入 Telecom 域作为 Dec-POMDP 案例；提供 task generator 让 benchmark 可程序化扩展，避免数据集污染。

## 背景

τ-bench 是 tool-agent 事实评测标准，但用户只能说话不能行动，与现实诸如 "用户先重启路由器再描述" 这类场景对不上。要真实评测 "agent 与 user 协作"，必须让 user 也能 act。

## 方法

**Dual-control 环境**：模拟用户除了 message 也能 call tool（如重启设备、查账单）；**Dec-POMDP 建模**：Telecom 域的 user / agent 动作空间、观察空间形式化定义；**Task generator**：基于规则生成 diverse / verifiable task，可控难度；**User simulator**：与环境状态紧耦合，避免 simulator 说错话导致 task unreachable。

## 实验结果

在 Telecom 域上对比多种主流 LLM agent，揭示 dual-control 场景下 agent 显著弱于单边场景，反映现有 agent 的协作短板。

## 优点

把 "用户也能动手" 这一现实约束正式建模，为后续 multi-actor agent 评测奠基；代码与 benchmark 开源，Sierra 维护质量较高；Dec-POMDP 形式化让理论同学也能接入。

## 局限

Telecom 单域，跨域迁移要重写；task generator 仍需领域规则；user simulator 的多样性受限于 generator 模板。

## 对后续工作的启发

提示 user simulator 不止 "会说话"，还要 "会动手"；与 MUA-RL / UserRL 的训练范式天然契合——把 τ²-bench 当训练环境是顺其自然的下一步。

## 一句话总结

Tool-agent 评测的事实标准之 dual-control 续作。
