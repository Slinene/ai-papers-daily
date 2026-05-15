---
title: 'Agent-World: Scaling Real-World Environment Synthesis for Evolving General
  Agent Intelligence'
authors: Guanting Dong, Junting Lu, Junjie Huang, …, Ji-Rong Wen, Zhicheng Dou
affiliation: ByteDance Seed × 人民大学
date: 2026-04
venue: arXiv (Working in progress)
topic: agent-rl
topic_name: Agent RL
topic_icon: 🤖
idea: 端到端 "环境 + agent 共进化" arena：自动从真实主题挖环境、生工具、合成可验证任务，再用多环境 RL 训 agent，由 self-evolving
  arena 自动诊断短板、定向扩环境。共合成 1978 环境 / 19822 工具，平均任务 >15 轮交互。
paperUrl: https://arxiv.org/abs/2604.18292
tags:
- Env Synthesis
- General Agent
- Scaling
- MCP
unverified: false
detail:
  contribution: 把 "环境数据" 提升到 Agent Scaling 的第一公民地位：构建一个能自动合成真实世界环境 + 工具 + 可验证任务的 arena，让
    agent 训练与环境扩张相互推动；首次系统报告环境多样性 / 自演化轮次两个轴上的 scaling 规律，验证 "environment scaling"
    是和 reward / data 并列的独立可扩展轴。
  background: MCP（Model Context Protocol）和 agent skills 提供了统一接口，但工业级 agent 训练严重缺乏
    "真实、可执行、可验证" 的环境，也没有原则性的 life-long learning 机制。环境稀缺已成为 Agent RL Scaling 的最大瓶颈，论文的判断是：算力和数据都将被
    "环境" 反过来限制。
  method: 两大组件。**(1) Agentic Environment-Task Discovery**：① deep-search agent 自主从数千主题中挖掘领域数据库；②
    LLM 自动为每个数据库生成可执行 MCP 工具；③ 基于工具与数据合成可验证任务，难度可控；④ 任务平均 >15 轮交互，覆盖搜索 / 代码 / web
    / 多模态。**(2) Continuous Self-Evolving Agent Training**：① 多环境 RL 训练 agent 策略；② Self-Evolving
    Arena 用动态 task synthesis 探测当前 agent 的 capability gap；③ 针对短板定向合成新环境 / 新工具 / 新任务；④
    策略与环境形成正反馈共进化。整体迭代输出 1978 个真实环境 + 19822 个工具组成的训练 arena。
  experiments: Agent-World-8B / 14B 在 **23 个 challenging agent benchmark** 上一致超过强专有模型与
    "只扩环境不进化" baseline；论文给出 environment diversity 与 self-evolution rounds 两个 scaling
    曲线，展示 "环境多样性 → agent 能力" 的单调关系。
  pros: 把 "environment scaling" 与 R1 的 "reward scaling" 互补地放上 Agent RL scaling map；MCP-aligned
    工具生态贴合工业落地；自动诊断 + 定向扩环境的闭环设计在工程上有可推广性。
  cons: 23 benchmark 是否覆盖工业 agent 真实场景需后续验证；自动 capability-gap 诊断的具体准确率没有充分披露；arxiv
    v1 标注 "Working in progress"，结果仍可能更新；社区独立复现尚未跟上。
  inspiration: 与 R1（reward scaling）、SSP（task scaling）三足鼎立，分别代表 Agent RL 的三条 scaling
    轴；接下来值得关注 "环境合成" 能否做到像数据混合配方一样工程化、可调度。
  takeaway: 字节 Seed 在 Agent RL Scaling 路线上的关键一步，是 "environment-as-data" 思潮的代表作。
---

端到端 "环境 + agent 共进化" arena：自动从真实主题挖环境、生工具、合成可验证任务，再用多环境 RL 训 agent，由 self-evolving arena 自动诊断短板、定向扩环境。共合成 1978 环境 / 19822 工具，平均任务 >15 轮交互。

## 核心贡献

把 "环境数据" 提升到 Agent Scaling 的第一公民地位：构建一个能自动合成真实世界环境 + 工具 + 可验证任务的 arena，让 agent 训练与环境扩张相互推动；首次系统报告环境多样性 / 自演化轮次两个轴上的 scaling 规律，验证 "environment scaling" 是和 reward / data 并列的独立可扩展轴。

## 背景

MCP（Model Context Protocol）和 agent skills 提供了统一接口，但工业级 agent 训练严重缺乏 "真实、可执行、可验证" 的环境，也没有原则性的 life-long learning 机制。环境稀缺已成为 Agent RL Scaling 的最大瓶颈，论文的判断是：算力和数据都将被 "环境" 反过来限制。

## 方法

两大组件。**(1) Agentic Environment-Task Discovery**：① deep-search agent 自主从数千主题中挖掘领域数据库；② LLM 自动为每个数据库生成可执行 MCP 工具；③ 基于工具与数据合成可验证任务，难度可控；④ 任务平均 >15 轮交互，覆盖搜索 / 代码 / web / 多模态。**(2) Continuous Self-Evolving Agent Training**：① 多环境 RL 训练 agent 策略；② Self-Evolving Arena 用动态 task synthesis 探测当前 agent 的 capability gap；③ 针对短板定向合成新环境 / 新工具 / 新任务；④ 策略与环境形成正反馈共进化。整体迭代输出 1978 个真实环境 + 19822 个工具组成的训练 arena。

## 实验结果

Agent-World-8B / 14B 在 **23 个 challenging agent benchmark** 上一致超过强专有模型与 "只扩环境不进化" baseline；论文给出 environment diversity 与 self-evolution rounds 两个 scaling 曲线，展示 "环境多样性 → agent 能力" 的单调关系。

## 优点

把 "environment scaling" 与 R1 的 "reward scaling" 互补地放上 Agent RL scaling map；MCP-aligned 工具生态贴合工业落地；自动诊断 + 定向扩环境的闭环设计在工程上有可推广性。

## 局限

23 benchmark 是否覆盖工业 agent 真实场景需后续验证；自动 capability-gap 诊断的具体准确率没有充分披露；arxiv v1 标注 "Working in progress"，结果仍可能更新；社区独立复现尚未跟上。

## 对后续工作的启发

与 R1（reward scaling）、SSP（task scaling）三足鼎立，分别代表 Agent RL 的三条 scaling 轴；接下来值得关注 "环境合成" 能否做到像数据混合配方一样工程化、可调度。

## 一句话总结

字节 Seed 在 Agent RL Scaling 路线上的关键一步，是 "environment-as-data" 思潮的代表作。
