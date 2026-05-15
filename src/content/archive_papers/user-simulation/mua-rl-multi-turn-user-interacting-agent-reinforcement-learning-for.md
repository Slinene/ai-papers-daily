---
title: 'MUA-RL: Multi-turn User-interacting Agent Reinforcement Learning for Agentic
  Tool Use'
authors: Weikang Zhao, Xili Wang, Chengdi Ma, Lingbin Kong, Zhaohua Yang, Mingxiang
  Tuo, Xiaowei Shi, Yitao Zhai, Xunliang Cai
affiliation: Meituan
date: 2025-08
venue: arXiv / OpenReview
topic: user-simulation
topic_name: User Simulation
topic_icon: 👥
idea: 首次把 LLM 模拟用户接进 agent 的 RL rollout 里。GRPO + 真实数据库环境验证 tool call 结果，并配两条 cold-start
  数据合成 pipeline（LLM 模拟工具响应 vs. 真实 MCP server）。
paperUrl: https://arxiv.org/abs/2508.18669
codeUrl: https://huggingface.co/zzwkk/MUA-RL-32B
tags:
- User Simulator
- GRPO
- Tool Use
- Multi-turn RL
unverified: false
detail:
  contribution: 首次在 agentic tool use 领域把 LLM 模拟用户直接嵌入 RL rollouts，配合真实数据库环境验证 tool
    call 结果；额外贡献两条 cold-start 数据合成 pipeline（一条工具响应由 LLM 模拟、一条走真实 MCP server），为 user-in-the-loop
    训练范式提供完整基线。
  background: 多轮交互中用户需求是动态、不确定、随机的，单靠静态指令训练难以泛化。已有 tool-use benchmark（τ-bench 等）虽用模拟用户做评测，但训练阶段普遍没把模拟用户当成环境的一部分；MUA-RL
    要补上 "训练期就能与模拟用户共演化" 这一环。
  method: '**Cold-start**：两条 SFT 数据 pipeline，一条全 LLM 模拟、一条由真实 MCP server 提供 tool response。**RL
    阶段**：GRPO 作为优化器，每个 prompt 多 rollout、组内相对优势替代 critic，省掉 value model；rollout 内 LLM
    模拟用户充当环境，工具结果由真实 DB 返回，reward 基于最终任务完成度。'
  experiments: 在 τ-bench / BFCL 等多轮 tool-use benchmark 上一致超过 SFT-only 基线与不含 user simulation
    的 RL 基线，MUA-RL-32B 权重已开源。
  pros: 把 "user simulator" 从评测搬进训练 loop 的第一篇 RL 工作；GRPO + 真实 DB 验证组合显著降低 reward hacking；两条数据
    pipeline 给社区可复制模板。
  cons: 模拟用户由通用 LLM 直接扮演，存在 goal drift（UGST 那篇正是要解决这个问题）；对工业级长尾用户行为覆盖度有限；公开评测集中在 tool-use
    单一任务族。
  inspiration: 把 user simulator 抬升为和 reward / environment 并列的训练信号源；后续 UserRL、UserVille
    都沿这条路深化。
  takeaway: User-in-the-loop RL 训练范式的奠基性工作。
---

首次把 LLM 模拟用户接进 agent 的 RL rollout 里。GRPO + 真实数据库环境验证 tool call 结果，并配两条 cold-start 数据合成 pipeline（LLM 模拟工具响应 vs. 真实 MCP server）。

## 核心贡献

首次在 agentic tool use 领域把 LLM 模拟用户直接嵌入 RL rollouts，配合真实数据库环境验证 tool call 结果；额外贡献两条 cold-start 数据合成 pipeline（一条工具响应由 LLM 模拟、一条走真实 MCP server），为 user-in-the-loop 训练范式提供完整基线。

## 背景

多轮交互中用户需求是动态、不确定、随机的，单靠静态指令训练难以泛化。已有 tool-use benchmark（τ-bench 等）虽用模拟用户做评测，但训练阶段普遍没把模拟用户当成环境的一部分；MUA-RL 要补上 "训练期就能与模拟用户共演化" 这一环。

## 方法

**Cold-start**：两条 SFT 数据 pipeline，一条全 LLM 模拟、一条由真实 MCP server 提供 tool response。**RL 阶段**：GRPO 作为优化器，每个 prompt 多 rollout、组内相对优势替代 critic，省掉 value model；rollout 内 LLM 模拟用户充当环境，工具结果由真实 DB 返回，reward 基于最终任务完成度。

## 实验结果

在 τ-bench / BFCL 等多轮 tool-use benchmark 上一致超过 SFT-only 基线与不含 user simulation 的 RL 基线，MUA-RL-32B 权重已开源。

## 优点

把 "user simulator" 从评测搬进训练 loop 的第一篇 RL 工作；GRPO + 真实 DB 验证组合显著降低 reward hacking；两条数据 pipeline 给社区可复制模板。

## 局限

模拟用户由通用 LLM 直接扮演，存在 goal drift（UGST 那篇正是要解决这个问题）；对工业级长尾用户行为覆盖度有限；公开评测集中在 tool-use 单一任务族。

## 对后续工作的启发

把 user simulator 抬升为和 reward / environment 并列的训练信号源；后续 UserRL、UserVille 都沿这条路深化。

## 一句话总结

User-in-the-loop RL 训练范式的奠基性工作。
