---
title: 'SAGE: A Top-Down Bottom-Up Knowledge-Grounded User Simulator for Multi-turn
  AGent Evaluation'
authors: Ryan Shea, Yunan Lu, Liang Qiu, Zhou Yu
affiliation: Columbia University
date: 2025-10
venue: EACL 2026 Findings
topic: user-simulation
topic_name: User Simulation
topic_icon: 👥
idea: Simulator 不能脱离业务知识：Top-down 用 ideal customer profile / persona 灌入业务逻辑，Bottom-up
  把 agent infra 的商品目录、FAQ、知识库灌进 simulator，让用户 "知道自己要什么、要怎么问"。比基线多发现 33% 的 agent error。
paperUrl: https://arxiv.org/abs/2510.11997
tags:
- User Simulator
- Knowledge Grounded
- Evaluation
- Persona
unverified: false
detail:
  contribution: 提出 SAGE：把业务知识 (top-down) 与 agent 端知识 (bottom-up) 同时灌入 user simulator，使生成的交互既真实又能精准触发
    agent error，作为 evaluation 工具显著强于无知识 baseline。
  background: 现有 user simulator 多数 persona 空泛，提的问题脱离业务场景，导致评测 "找不到真问题"。真实客户带着 business
    intent 与 background knowledge 来，但既有 simulator 不知道商品目录长什么样、也不知道 FAQ 写了啥。
  method: '**Top-down 知识注入**：ideal customer profile (ICP) + 业务 policy → persona 模板；**Bottom-up
    知识注入**：从 agent infra 抓取商品目录、FAQ、知识库片段 → 注入 simulator context，使其 "知道该问什么 / 期望得到什么"；两路信息融合后驱动
    multi-turn user behavior 生成。'
  experiments: 用 SAGE 模拟用户跑同一组 agent，发现的 agent error 比无知识 baseline 多 **33%**；diversity
    与 realism 的人工评分也显著更高。
  pros: 把 "simulator realism" 和 "评测可发现 bug 的能力" 直接挂钩，工程导向极强；两路知识注入方法可推广至任意领域；EACL
    Findings 收录。
  cons: 强依赖业务侧已有结构化知识（catalog / FAQ），冷启动域无法套用；ICP 设计还是要业务人工写；33% 的提升来自 evaluation
    视角，不直接等于训练增益。
  inspiration: 提示后续工作把 simulator realism 与 evaluation coverage 这两件事拆开优化；与 SimulatorArena
    形成 "评估 simulator vs. 用 simulator 评估" 的方法论双子星。
  takeaway: 面向 evaluation 场景的知识接地 simulator 代表作。
---

Simulator 不能脱离业务知识：Top-down 用 ideal customer profile / persona 灌入业务逻辑，Bottom-up 把 agent infra 的商品目录、FAQ、知识库灌进 simulator，让用户 "知道自己要什么、要怎么问"。比基线多发现 33% 的 agent error。

## 核心贡献

提出 SAGE：把业务知识 (top-down) 与 agent 端知识 (bottom-up) 同时灌入 user simulator，使生成的交互既真实又能精准触发 agent error，作为 evaluation 工具显著强于无知识 baseline。

## 背景

现有 user simulator 多数 persona 空泛，提的问题脱离业务场景，导致评测 "找不到真问题"。真实客户带着 business intent 与 background knowledge 来，但既有 simulator 不知道商品目录长什么样、也不知道 FAQ 写了啥。

## 方法

**Top-down 知识注入**：ideal customer profile (ICP) + 业务 policy → persona 模板；**Bottom-up 知识注入**：从 agent infra 抓取商品目录、FAQ、知识库片段 → 注入 simulator context，使其 "知道该问什么 / 期望得到什么"；两路信息融合后驱动 multi-turn user behavior 生成。

## 实验结果

用 SAGE 模拟用户跑同一组 agent，发现的 agent error 比无知识 baseline 多 **33%**；diversity 与 realism 的人工评分也显著更高。

## 优点

把 "simulator realism" 和 "评测可发现 bug 的能力" 直接挂钩，工程导向极强；两路知识注入方法可推广至任意领域；EACL Findings 收录。

## 局限

强依赖业务侧已有结构化知识（catalog / FAQ），冷启动域无法套用；ICP 设计还是要业务人工写；33% 的提升来自 evaluation 视角，不直接等于训练增益。

## 对后续工作的启发

提示后续工作把 simulator realism 与 evaluation coverage 这两件事拆开优化；与 SimulatorArena 形成 "评估 simulator vs. 用 simulator 评估" 的方法论双子星。

## 一句话总结

面向 evaluation 场景的知识接地 simulator 代表作。
