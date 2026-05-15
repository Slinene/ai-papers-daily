---
title: 'Learning to Evolve: A Self-Improving Framework for Multi-Agent Systems via
  Textual Parameter Graph Optimization'
authors: Shan He et al. (7 人)
affiliation: 待确认（论文署名机构尚未公开核实）
date: 2026-04
venue: arXiv
topic: agent-rl
topic_name: Agent RL
topic_icon: 🤖
idea: 把 MAS 抽象成一张 "文本参数图"（agent / tool / workflow 都是可优化节点），用 GRAO（Group Relative Agent
  Optimization）做元学习式的图优化，使多 agent 系统能自动 debug 自己。
paperUrl: https://arxiv.org/abs/2604.20714
tags:
- Multi-Agent
- Self-Improvement
- Textual Gradient
- GRAO
unverified: false
detail:
  contribution: 提出 Textual Parameter Graph Optimization (TPGO) 框架：把多 agent 系统统一抽象成一张可优化的
    "文本参数图"，并用受 GRPO 启发的 GRAO（Group Relative Agent Optimization）作为元学习式优化器，让 MAS 学会自我演化、且优化器本身也随时间变强。
  background: 现有 MAS 自动优化方法（DSPy、TextGrad 等）对系统结构毫无感知，无法 debug 跨 agent 的交互错误；同时优化器是静态的，不会从过去的优化经验中学习改进。论文要解的是
    "系统级" 自迭代——不是单 agent 的能力上升，而是整个 multi-agent system 的 prompt / tool / workflow
    协同优化。
  method: 三层设计。**(1) TPG 抽象**：把 MAS 建模为一张图，节点 = agent prompt / tool 描述 / workflow
    步骤，边 = 数据流，所有节点都是可被自然语言优化的 "文本参数"。**(2) Textual Gradient**：用执行 trace 产生结构化自然语言反馈（"这一步因
    X 失败，应改成 Y"）作为反向传播信号沿图回传。**(3) GRAO 优化器**：受 GRPO 启发，对图上一组候选优化方案打分，用组内相对优势更新优化器；同时聚类历史错误模式、检索过去成功的优化策略，做
    meta-learning，让优化器随训练轮次本身也变强。
  experiments: 在多个 multi-agent benchmark 上对比传统 prompt-tuning / textual gradient baseline
    报告显著提升（具体设置与数字需读论文 v1 全文核实）。
  pros: 把 GRPO 的 "组内相对优势" 思想从 token 空间迁移到 agent-graph 空间，方法创新有趣；TPG 抽象统一性强，对工程化 MAS
    有指导意义；优化器自身能学习是相比 TextGrad 的关键提升。
  cons: Textual gradient 高度依赖 LLM judge 自身能力，反馈误差会沿图传播放大；图节点粒度仍靠人工先验切；论文非常新，社区复现尚未跟上；缺少与端到端
    RL（如直接 fine-tune agent）的横向对比。
  inspiration: 把 "MAS = 一张可微化的图" 推到具体可操作框架；与 Agent-World 形成 "环境侧 vs. 系统侧" 的对照——一个扩环境、一个优化系统结构。
  takeaway: Agent Self-Improvement 在 system 层的代表性新工作。
---

把 MAS 抽象成一张 "文本参数图"（agent / tool / workflow 都是可优化节点），用 GRAO（Group Relative Agent Optimization）做元学习式的图优化，使多 agent 系统能自动 debug 自己。

## 核心贡献

提出 Textual Parameter Graph Optimization (TPGO) 框架：把多 agent 系统统一抽象成一张可优化的 "文本参数图"，并用受 GRPO 启发的 GRAO（Group Relative Agent Optimization）作为元学习式优化器，让 MAS 学会自我演化、且优化器本身也随时间变强。

## 背景

现有 MAS 自动优化方法（DSPy、TextGrad 等）对系统结构毫无感知，无法 debug 跨 agent 的交互错误；同时优化器是静态的，不会从过去的优化经验中学习改进。论文要解的是 "系统级" 自迭代——不是单 agent 的能力上升，而是整个 multi-agent system 的 prompt / tool / workflow 协同优化。

## 方法

三层设计。**(1) TPG 抽象**：把 MAS 建模为一张图，节点 = agent prompt / tool 描述 / workflow 步骤，边 = 数据流，所有节点都是可被自然语言优化的 "文本参数"。**(2) Textual Gradient**：用执行 trace 产生结构化自然语言反馈（"这一步因 X 失败，应改成 Y"）作为反向传播信号沿图回传。**(3) GRAO 优化器**：受 GRPO 启发，对图上一组候选优化方案打分，用组内相对优势更新优化器；同时聚类历史错误模式、检索过去成功的优化策略，做 meta-learning，让优化器随训练轮次本身也变强。

## 实验结果

在多个 multi-agent benchmark 上对比传统 prompt-tuning / textual gradient baseline 报告显著提升（具体设置与数字需读论文 v1 全文核实）。

## 优点

把 GRPO 的 "组内相对优势" 思想从 token 空间迁移到 agent-graph 空间，方法创新有趣；TPG 抽象统一性强，对工程化 MAS 有指导意义；优化器自身能学习是相比 TextGrad 的关键提升。

## 局限

Textual gradient 高度依赖 LLM judge 自身能力，反馈误差会沿图传播放大；图节点粒度仍靠人工先验切；论文非常新，社区复现尚未跟上；缺少与端到端 RL（如直接 fine-tune agent）的横向对比。

## 对后续工作的启发

把 "MAS = 一张可微化的图" 推到具体可操作框架；与 Agent-World 形成 "环境侧 vs. 系统侧" 的对照——一个扩环境、一个优化系统结构。

## 一句话总结

Agent Self-Improvement 在 system 层的代表性新工作。
