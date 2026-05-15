---
title: Non-Collaborative User Simulators for Tool Agents
authors: Jeonghoon Shim, Woojung Song, Cheyon Jin, Seungwon Kook, Yohan Jo
affiliation: Seoul National University
date: 2025-09
venue: arXiv / OpenReview
topic: user-simulation
topic_name: User Simulation
topic_icon: 👥
idea: 现有 simulator 默认用户配合，太理想。提出能模拟四类不配合行为的 simulator：请求不存在服务 / 跑题 / 不耐烦 / 信息不全；同时保证关键
  intent 与信息最终能被传达，让训练信号不假。
paperUrl: https://arxiv.org/abs/2509.23124
tags:
- User Simulator
- Non-Collaborative
- Adversarial
- Tool Agents
unverified: false
detail:
  contribution: 首次系统化构造 "不配合用户" simulator：覆盖四类非合作行为，同时严格保证任务必需信息会被传达，弥补主流 "全配合用户"
    假设下训练得到的 agent 在真实场景下脆弱的问题。
  background: MUA-RL / UserRL 等用的 simulator 都极配合——用户问对问题、答对答案、不偏题。但真实用户经常情绪化、跑题、提不可能要求；用全配合
    simulator 训出的 agent 一上真实流量就翻车。
  method: 定义四类非配合行为：(1) **请求不可用服务**（系统不支持的功能）；(2) **跑题**（聊天偏离任务）；(3) **不耐烦**（中途催促
    / 中断）；(4) **信息不全**（关键字段遗漏）。Simulator 架构上叠加 "intent guard"，保证四类行为不破坏最终任务必要信息的传达。
  experiments: 在 tool-agent 评测上，非配合 simulator 测试出的 agent error rate 显著高于 vanilla simulator；进一步用其训练的
    agent 在真实流量上鲁棒性提升（论文报告）。
  pros: 补足 user-simulator 研究最大的盲区 "用户都很乖"；四类行为分类清晰，可单独 ablation；对工业 deployment robustness
    直接有用。
  cons: 四类未必穷尽现实长尾；intent guard 设计仍偏规则；与主流 simulator 训练框架（MUA-RL / UserRL）的整合方式未给出。
  inspiration: 提示后续 simulator 工作把 "realism" 拆成更细的子维度（合作度、情绪、信息密度等）逐一覆盖；与 SAGE 的 "知识接地"
    形成多维 realism 矩阵。
  takeaway: User simulator 在 robustness / adversarial 维度上的代表性补丁。
---

现有 simulator 默认用户配合，太理想。提出能模拟四类不配合行为的 simulator：请求不存在服务 / 跑题 / 不耐烦 / 信息不全；同时保证关键 intent 与信息最终能被传达，让训练信号不假。

## 核心贡献

首次系统化构造 "不配合用户" simulator：覆盖四类非合作行为，同时严格保证任务必需信息会被传达，弥补主流 "全配合用户" 假设下训练得到的 agent 在真实场景下脆弱的问题。

## 背景

MUA-RL / UserRL 等用的 simulator 都极配合——用户问对问题、答对答案、不偏题。但真实用户经常情绪化、跑题、提不可能要求；用全配合 simulator 训出的 agent 一上真实流量就翻车。

## 方法

定义四类非配合行为：(1) **请求不可用服务**（系统不支持的功能）；(2) **跑题**（聊天偏离任务）；(3) **不耐烦**（中途催促 / 中断）；(4) **信息不全**（关键字段遗漏）。Simulator 架构上叠加 "intent guard"，保证四类行为不破坏最终任务必要信息的传达。

## 实验结果

在 tool-agent 评测上，非配合 simulator 测试出的 agent error rate 显著高于 vanilla simulator；进一步用其训练的 agent 在真实流量上鲁棒性提升（论文报告）。

## 优点

补足 user-simulator 研究最大的盲区 "用户都很乖"；四类行为分类清晰，可单独 ablation；对工业 deployment robustness 直接有用。

## 局限

四类未必穷尽现实长尾；intent guard 设计仍偏规则；与主流 simulator 训练框架（MUA-RL / UserRL）的整合方式未给出。

## 对后续工作的启发

提示后续 simulator 工作把 "realism" 拆成更细的子维度（合作度、情绪、信息密度等）逐一覆盖；与 SAGE 的 "知识接地" 形成多维 realism 矩阵。

## 一句话总结

User simulator 在 robustness / adversarial 维度上的代表性补丁。
