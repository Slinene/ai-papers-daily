---
title: 'OpenForgeRL: Train Harness-native Agents in Any Environment'
title_zh: OpenForgeRL：在任意环境中训练原生 Harness 智能体
authors:
- Xiao Yu
- Baolin Peng
- Ruize Xu
- Hao Zou
- Qianhui Wu
- Hao Cheng
- Wenlin Yao
- Nikhil Singh
- Zhou Yu
- Jianfeng Gao
affiliations:
- Columbia University
- Dartmouth College
- Microsoft Research
arxiv_id: '2607.21557'
url: https://arxiv.org/abs/2607.21557
pdf_url: https://arxiv.org/pdf/2607.21557
published: '2026-07-23'
collected: '2026-07-24'
category: Agent
direction: Agent 端到端 RL 训练与 Harness 解耦
tags:
- Agent Training
- Reinforcement Learning
- Harness
- GUI Agent
- Tool Use
- Open Source
one_liner: 一个开源框架，通过远程容器化与轻量代理解耦，支持用标准 RL（veRL）在任何智能体框架与任何环境中端到端训练 agent
practical_value: '- **训练与推理解耦的工程模式**：用轻量级 Proxy 拦截 Harness 的模型调用，自动重建轨迹，直接将复杂 agent
  的交互过程转为 RL 可消费的样本，适用于内部多轮对话/工具调用 agent 的在线强化学习，无需重写训练代码。

  - **云端容器化 rollout 编排**：Kubernetes 编排远程沙箱，每个 rollout 独立容器，训练节点与 rollout 节点完全分离，可弹性伸缩。在电商推荐中可复现这种「训练
  GPU + 远程 CPU 执行环境」的解耦架构，用于策略学习或 Agent 探索。

  - **自动任务与环境合成流水线**：通过「提出-剪枝-构建-测试-精炼」五步法自动生成大量可执行任务与 Docker 环境，可迁移到推荐系统中生成多样化的用户
  query、对话策略或评测任务。

  - **RL 带来的 agentic 可靠性提升**：实验表明 RL 显著改善自我验证、工具覆盖率和多步规划能力，但纠错能力依然薄弱。这提示在业务 Agent
  训练中，可针对性地引入纠错样例或辅助任务来补强。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
现代 AI agent 严重依赖复杂的推理 Harness（如 Claude Code、Codex）来管理多轮推理、工具调用和外部系统交互。然而，这些 Harness 使端到端训练变得极其困难：开源 RL 栈无法原生表达有状态的多进程 Harness 推理，且 Harness 所需的容器化环境无法与训练节点共存。这导致开源社区的 agent 训练往往在简化的 Harness 重实现中进行，带来训练与部署的错配。OpenForgeRL 旨在填补这一空白，让任意 Harness 与任意环境都能用标准 RL 代码库（如 veRL）进行端到端训练。

**方法关键点**  
- **轻量级 Proxy 解耦**：在 Harness 与模型推理服务器之间插入 Proxy，截获所有模型调用，自动记录 prompt‑response 对并重建完整轨迹，使其与 RL 框架完全兼容。
- **Kubernetes 远程编排**：基于 Orchard 实现，每个 rollout 在独立的云端容器（如 Azure）中运行，与训练节点完全分离，支撑弹性伸缩和超时管理。
- **强可扩展性**：无需修改训练框架，只需为 Harness/环境构建对应容器镜像，即可无缝接入 veRL、Slime 等 RL 后端。
- **任务自动合成流水线**：针对数据稀缺的 claw/GUI 领域，引入「提案→剪枝→构建→测试→精炼」五步法，自动生成可执行任务和 Docker 环境，支撑 SFT 与 RL。

**关键结果**  
- **Claw agent**（30B‑A3B MoE）在 ClawEval 上达到 31.7 (pass3) / 55.9 (pass@3)，QwenClawBench 33.7，MCPAtlas 28.1，显著优于同尺寸开源模型。
- **GUI agent**（8B）在 OSWorld‑Verified 上 37.7，Online‑Mind2Web 63.0，WebVoyager 72.3，在多个基准上超过或匹敌数倍规模模型。
- **分析发现**：（1）不同 Harness 学习难度差异巨大（简洁的 ReACT/ZeroClaw 远好于 OpenClaw/Codex）；（2）单 Harness 训练可迁移至未见的 Harness，多 Harness 联合训练更优；（3）RL 主要提升 agent 的可靠性（自我验证、工具覆盖率、任务完成），但纠错能力仍是薄弱环节。
