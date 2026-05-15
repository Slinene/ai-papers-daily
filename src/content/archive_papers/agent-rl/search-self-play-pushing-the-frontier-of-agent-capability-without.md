---
title: 'Search Self-play: Pushing the Frontier of Agent Capability without Supervision'
authors: Hongliang Lu, Yuhang Wen, Pengyu Cheng, …, Guanjun Jiang
affiliation: Alibaba (Qwen Applications)
date: 2025-10
venue: arXiv (v2 2025-12)
topic: agent-rl
topic_name: Agent RL
topic_icon: 🤖
idea: 同一 LLM 同时扮演 task proposer 与 problem solver；用 RAG 验证 proposer 出的题有 ground truth，从而无需人工标注就能持续提升
  deep-search agent。
paperUrl: https://arxiv.org/abs/2510.18821
codeUrl: https://github.com/Qwen-Applications/SSP
tags:
- Self-Play
- Search Agent
- Unsupervised
- RLVR
unverified: false
detail:
  contribution: 首次在 deep-search agent 上跑通 self-play RLVR——把 "task synthesis" 与 "task
    verification" 同时交给同一个模型完成，用 RAG 自动验证保证 proposer 出的题有 ground truth，从而彻底去除人工标注且难度可自适应增长。
  background: RLVR（Reinforcement Learning with Verifiable Rewards）已是 LLM agent 主流范式，但严重依赖
    "题目 + 标答"。在多轮搜索这种长程交互场景下，人工出题根本扩展不动；而纯任务合成又难以控难度——出得太简单 RL 没信号，出得太难 solver 学不会。
  method: ① **Proposer 出题**：同模型多轮调用搜索引擎 → 综合多个网页提出一道 deep-search 问题，并给出自己认定的标准答案；②
    **RAG 验证**：把 proposer 检索到的全部文档作为外部知识，让一个独立 RAG agent 试解——若解对，说明该题 "在提供完整资料时确有
    ground truth"，纳入合法训练集；③ **Solver 在不开 RAG 的条件下尝试解题**，reward 用答案匹配；④ Proposer 与
    Solver 是同一模型同步更新，竞争（出更难的题）+ 合作（保证题有解）共同进化；这套机制让难度自然随 solver 能力上升。
  experiments: 在 7 个 deep-search benchmark（HotpotQA、Musique、Bamboogle、2Wiki 等）上 from-scratch
    与 continuous RL 两种设置都获得显著、统一的提升；Qwen3-8B + SSP 在多个 benchmark 超过 Search-R1、ZeroSearch
    baseline；难度自适应曲线显示 proposer 出题难度随训练轮次单调上升。代码与模型完全开源。
  pros: '"难度自适应靠 RAG 客观验证、不靠模型自评" 是相比朴素 self-play 的关键工程创新，大幅降低 reward hacking；端到端无人工监督；代码
    + 模型开源使复现门槛低。'
  cons: RAG 验证假设 "能搜到的就是对的"，对 web 噪声 / 谣言敏感；目前主要在 Qwen 系列验证；proposer 容易学出 "RAG 易解、solver
    易错" 的特定题型分布，长期可能塌缩；只覆盖 search agent 一类工具，未推广至 code / browse。
  inspiration: 把 Self-Play（围棋 / AlphaZero 范式）真正落到 LLM agent 上的代表作；下一步是把 RAG 验证替换为更通用的
    "环境可执行性" 验证，迁移到 code agent / browse agent。
  takeaway: Self-Play 路线在 search agent 上首个干净跑通的工作，是 "task synthesis as scaling axis"
    思潮的旗帜性论文。
---

同一 LLM 同时扮演 task proposer 与 problem solver；用 RAG 验证 proposer 出的题有 ground truth，从而无需人工标注就能持续提升 deep-search agent。

## 核心贡献

首次在 deep-search agent 上跑通 self-play RLVR——把 "task synthesis" 与 "task verification" 同时交给同一个模型完成，用 RAG 自动验证保证 proposer 出的题有 ground truth，从而彻底去除人工标注且难度可自适应增长。

## 背景

RLVR（Reinforcement Learning with Verifiable Rewards）已是 LLM agent 主流范式，但严重依赖 "题目 + 标答"。在多轮搜索这种长程交互场景下，人工出题根本扩展不动；而纯任务合成又难以控难度——出得太简单 RL 没信号，出得太难 solver 学不会。

## 方法

① **Proposer 出题**：同模型多轮调用搜索引擎 → 综合多个网页提出一道 deep-search 问题，并给出自己认定的标准答案；② **RAG 验证**：把 proposer 检索到的全部文档作为外部知识，让一个独立 RAG agent 试解——若解对，说明该题 "在提供完整资料时确有 ground truth"，纳入合法训练集；③ **Solver 在不开 RAG 的条件下尝试解题**，reward 用答案匹配；④ Proposer 与 Solver 是同一模型同步更新，竞争（出更难的题）+ 合作（保证题有解）共同进化；这套机制让难度自然随 solver 能力上升。

## 实验结果

在 7 个 deep-search benchmark（HotpotQA、Musique、Bamboogle、2Wiki 等）上 from-scratch 与 continuous RL 两种设置都获得显著、统一的提升；Qwen3-8B + SSP 在多个 benchmark 超过 Search-R1、ZeroSearch baseline；难度自适应曲线显示 proposer 出题难度随训练轮次单调上升。代码与模型完全开源。

## 优点

"难度自适应靠 RAG 客观验证、不靠模型自评" 是相比朴素 self-play 的关键工程创新，大幅降低 reward hacking；端到端无人工监督；代码 + 模型开源使复现门槛低。

## 局限

RAG 验证假设 "能搜到的就是对的"，对 web 噪声 / 谣言敏感；目前主要在 Qwen 系列验证；proposer 容易学出 "RAG 易解、solver 易错" 的特定题型分布，长期可能塌缩；只覆盖 search agent 一类工具，未推广至 code / browse。

## 对后续工作的启发

把 Self-Play（围棋 / AlphaZero 范式）真正落到 LLM agent 上的代表作；下一步是把 RAG 验证替换为更通用的 "环境可执行性" 验证，迁移到 code agent / browse agent。

## 一句话总结

Self-Play 路线在 search agent 上首个干净跑通的工作，是 "task synthesis as scaling axis" 思潮的旗帜性论文。
