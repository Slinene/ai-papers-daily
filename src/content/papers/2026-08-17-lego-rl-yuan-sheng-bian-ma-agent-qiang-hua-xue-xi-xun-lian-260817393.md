---
title: 'LEGO-RL: Harness-Native Reinforcement Learning for Coding Agents'
title_zh: LEGO-RL：原生编码 Agent 强化学习训练框架
authors:
- Yiming Du
- Yuxin Jiang
- Tao Yuan
- Jianbo Dai
- Shaowei Wang
- Jierun Chen
- Chaofan Tao
- Xianzhi Yu
- Lifeng Shang
- Kam-Fai Wong
affiliations:
- Huawei Technologies Co., Ltd
- The Chinese University of Hong Kong
arxiv_id: '2608.17393'
url: https://arxiv.org/abs/2608.17393
pdf_url: https://arxiv.org/pdf/2608.17393
published: '2026-08-17'
collected: '2026-08-20'
category: Agent
direction: Coding Agent RL · 原生 harness 训练框架
tags:
- RLHF
- Coding Agents
- Harness-Native
- MoE
- Sandbox
- SWE-bench
one_liner: 桥接原生编码 agent harness 与策略梯度优化，在不改控制流下实现可信 RL 训练并显著提升 SWE-bench 解决率
practical_value: '- **Agent 化推荐/搜索场景可复用 in-process proxy**：在业务 Agent（如导购、客服选品）中，用模型
  API 边界代理记录 token ID、log-prob、response mask 和 MoE 路由，训练侧重放，避免 harness 上下文压缩/重写造成轨迹失真；对于
  sparse MoE 模型尤其重要，路由重放可将 rollout-train 概率相关性从 0.9946 提到 0.9993。

  - **异步 rollout + 终止状态过滤**：长 horizon Agent 任务时长差异大，按基础设施失败/超时/有效但不完整分类轨迹，无效轨迹排除出组相对优势估计，防止执行故障污染梯度；组内方差不足的任务需难度筛选，否则零方差组无学习信号。

  - **奖励完整性防御可迁移到任何带执行反馈的推荐 Agent**：限制网络、隐藏评测信息、依赖打包、隐藏仓库历史，防止 Agent 通过外部状态作弊，保证奖励真实反映任务完成。

  - **可观测性设计值得借鉴**：失败原因分布、轨迹查看器、一致性面板，在训练崩溃时快速区分策略退化与执行/集成故障，支持早停与人工诊断，减少无效实验成本。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机

RL 训练 coding agent 依赖长运行 harness 管理工具、仓库上下文与执行反馈，但原生执行环境与策略梯度优化天然不对齐：环境崩溃和 reward hacking 破坏奖励信号，harness 侧上下文重写/压缩导致训练时概率重算与 rollout 时不一致，MoE 路由不匹配进一步加剧误差。通用 RL 框架通常要求改造 agent 适配框架接口，破坏原生控制流。本文需要在不修改 agent 内部逻辑的前提下，桥接原生 harness 与可扩展策略梯度优化。

## 方法关键点

- **Faithful optimization**：in-process LLM proxy 在模型 API 边界捕获原始 token 流、log-prob、response mask 和 MoE 路由；消息粒度对齐历史，工具调用按稳定 ID 匹配；子 agent 隔离；训练时重放 rollout-time 专家路由（R3），确保概率重算一致。
- **Reliable execution**：可扩展沙箱编排，Nydus lazy pull 镜像缓存减少冷启动；阶段级防御（网络限制、隐藏 repo 历史、测试依赖打包）防止 reward hacking；按终止状态过滤轨迹，基础设施失败 mask 掉，有效但不完整轨迹保留。
- **Observable training**：集成插件自动化验证与监控，Live UI 提供终止原因分布、任务网格、轨迹查看、一致性面板，支持轨迹级诊断。
- **训练设置**：基于 verl，支持 GSPO/PPO/GRPO，组相对优势估计；2,699 任务 OpenSWE 池，难度筛选（1-3/4 次解决）保证组内方差；全异步 rollout，最大策略 staleness=1。

## 关键结果

在 Qwen3.5-35B-A3B 上训练三个原生 harness，SWE-bench Verified 解决率提升：OpenHands SDK 64.0→70.4 (+6.4)，Claude Code 62.4→68.2 (+5.8)，OpenCode 57.2→66.6 (+9.4)。rollout-train 概率相关性中位数 >0.998，p99 平均 token log-prob 差 <3e-3。路由重放将相关性从 0.9946 提到 0.9993。异步调度比同步快约 2.5 倍（每步时间），修正优化器吞吐后估计同步每步 1.9h vs 异步 1.0h。轨迹有效性：基础设施失败占 2.4-7.1%，被排除。难度筛选消融：全带/上半带验证 reward 达 0.671/0.670，未筛选池不提升。

## 值得记住的一句话

**长 horizon agent RL 的核心不是更大的模型，而是 faithful optimization + reliable execution + observable training 三支柱同时成立。**
