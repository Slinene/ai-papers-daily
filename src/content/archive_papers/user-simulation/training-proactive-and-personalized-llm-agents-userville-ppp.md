---
title: Training Proactive and Personalized LLM Agents (UserVille / PPP)
authors: Weiwei Sun, Xuhui Zhou, Weihua Du, Xingyao Wang, Sean Welleck, Graham Neubig,
  Maarten Sap, Yiming Yang
affiliation: CMU × OpenHands
date: 2025-11
venue: arXiv
topic: user-simulation
topic_name: User Simulation
topic_icon: 👥
idea: UserVille 把精确指令 "打散" 成模糊用户输入并配多种交互偏好的 simulator；PPP 是多目标 RL，联合优化 productivity（完成度）+
  proactivity（主动澄清）+ personalization（适配偏好）。
paperUrl: https://arxiv.org/abs/2511.02208
codeUrl: https://github.com/sunnweiwei/PPP-Agent
tags:
- User Simulator
- Multi-objective RL
- Proactive
- Personalization
unverified: false
detail:
  contribution: 把 user-centric agent 训练目标从单一 task success 扩展到 "P×P×P"：productivity
    + proactivity + personalization 三目标联合优化，并提供 UserVille 这一可模拟模糊用户输入与多偏好的环境。
  background: 现有 user-in-the-loop RL 默认用户给的指令清晰且单一偏好，与现实差很远。真实用户的 query 是模糊的（"帮我看看这个"），且每个用户偏好不同（喜欢被打断
    vs. 不喜欢被打断）。光优化 task success 训出的 agent 在真实场景下显得 obtuse。
  method: '**UserVille**：① 把精确 spec 打散成 vague user prompt；② 模拟器内置多种 interaction preference（要不要主动问、几轮内拍板等）；③
    提供 user-centric metric（productivity + proactivity + personalization）。**PPP**：多目标
    RL，三 reward 加权联合优化，惩罚 "该问不问" 与 "问太多"。'
  experiments: 在 UserVille 环境上 PPP-Agent 三维度评分一致超过 productivity-only RL baseline，特别是在偏好多样化测试集上
    personalization 提升显著。
  pros: 首篇明确把 proactivity 与 personalization 作为 RL 目标的 user-centric 工作；对真实部署场景关切度高；UserVille
    环境可作为后续公平 benchmark。
  cons: 三目标权重需要任务相关调参；偏好 simulator 仍是 LLM 生成，可能过于规整；与 UGST / Persona-Sim-RL 在 simulator
    侧的工作没有横向对照实验。
  inspiration: 提示 user-centric RL 正在从 "能不能完成" 走向 "用得舒不舒服"；下一步可与 UGST simulator 拼接，形成
    "goal-tracked simulator × proactivity-aware agent" 完整 stack。
  takeaway: CMU 用多目标 RL 把 user-centric agent 训练从 productivity 扩到 P×P×P 的代表作。
---

UserVille 把精确指令 "打散" 成模糊用户输入并配多种交互偏好的 simulator；PPP 是多目标 RL，联合优化 productivity（完成度）+ proactivity（主动澄清）+ personalization（适配偏好）。

## 核心贡献

把 user-centric agent 训练目标从单一 task success 扩展到 "P×P×P"：productivity + proactivity + personalization 三目标联合优化，并提供 UserVille 这一可模拟模糊用户输入与多偏好的环境。

## 背景

现有 user-in-the-loop RL 默认用户给的指令清晰且单一偏好，与现实差很远。真实用户的 query 是模糊的（"帮我看看这个"），且每个用户偏好不同（喜欢被打断 vs. 不喜欢被打断）。光优化 task success 训出的 agent 在真实场景下显得 obtuse。

## 方法

**UserVille**：① 把精确 spec 打散成 vague user prompt；② 模拟器内置多种 interaction preference（要不要主动问、几轮内拍板等）；③ 提供 user-centric metric（productivity + proactivity + personalization）。**PPP**：多目标 RL，三 reward 加权联合优化，惩罚 "该问不问" 与 "问太多"。

## 实验结果

在 UserVille 环境上 PPP-Agent 三维度评分一致超过 productivity-only RL baseline，特别是在偏好多样化测试集上 personalization 提升显著。

## 优点

首篇明确把 proactivity 与 personalization 作为 RL 目标的 user-centric 工作；对真实部署场景关切度高；UserVille 环境可作为后续公平 benchmark。

## 局限

三目标权重需要任务相关调参；偏好 simulator 仍是 LLM 生成，可能过于规整；与 UGST / Persona-Sim-RL 在 simulator 侧的工作没有横向对照实验。

## 对后续工作的启发

提示 user-centric RL 正在从 "能不能完成" 走向 "用得舒不舒服"；下一步可与 UGST simulator 拼接，形成 "goal-tracked simulator × proactivity-aware agent" 完整 stack。

## 一句话总结

CMU 用多目标 RL 把 user-centric agent 训练从 productivity 扩到 P×P×P 的代表作。
