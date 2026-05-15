---
title: 'Orchard: An Open-Source Agentic Modeling Framework'
title_zh: Orchard：开源可扩展代理建模框架
authors:
- Baolin Peng
- Wenlin Yao
- Qianhui Wu
- Hao Cheng
- Xiao Yu
- Rui Yang
- Tao Ge
- Alessandrio Sordoni
- Xingdi Yuan
- Yelong Shen
affiliations:
- Microsoft Research
- Columbia University
- UIUC
arxiv_id: '2605.15040'
url: https://arxiv.org/abs/2605.15040
pdf_url: https://arxiv.org/pdf/2605.15040
published: '2026-05-13'
collected: '2026-05-15'
category: Agent
tags:
- Agent
- LLM
- Training
- RL
- SWE-bench
- Open-Source
one_liner: 提出轻量级环境层 Orchard Env 实现跨领域、跨训练阶段的 SFT+RL 代理训练，在 SWE-bench 和 GUI 基准上达到开源最优
score: 9
source: huggingface-daily
depth: full_pdf
---

## 动机
大规模语言模型（LLM）代理的训练需要大量沙盒环境进行规划、工具使用和多轮交互。现有开源方案或强依赖特定训练栈，或环境管理耦合于 agent harness，导致数据、训练配方和评估协议难以跨领域复用。Orchard 旨在以薄环境服务为基石，构建可复用、可扩展的开源代理建模框架，填补基础设施与训练可复现性之间的缺口。

## 方法关键点
- **Orchard Env**：一个 Kubernetes 原生的轻量环境服务，仅暴露沙盒生命周期、命令执行、文件 I/O 和网络策略的 REST API。通过运行时 Agent 注入支持任意 Docker 镜像，直连 Pod IP 避免 kubectl exec/WebSocket 开销，实现平均执行延迟 0.28s，支持 1000 并行沙箱无失败。
- **跨领域训练配方**：在 Orchard Env 之上，构建三个可组合的 SFT+RL 训练流水线：
  - **Orchard-SWE**：软件工程代理。从 MiniMax-M2.5 和 Qwen3.5-397B 蒸馏 107K 条轨迹，保留未解决轨迹，引入 **credit-assignment SFT** 提取失败路径中的有效进展段；采用 **Balanced Adaptive Rollout (BAR)** 进行稀疏奖励 RL。骨干模型 Qwen3-30B-A3B-Thinking（约 3B 激活参数）。
  - **Orchard-GUI**：浏览器代理。用 4B 视觉语言骨干，仅 0.4K 蒸馏轨迹和 2.2K 开放式任务进行 SFT+RL，评估 WebVoyager、Online-Mind2Web 和 DeepShop。
  - **Orchard-Claw**：个人助理代理。利用 0.2K 合成任务训练，在 Claw-Eval 上评估，可搭配 ZeroClaw harness 进一步提升。
- **数据复用**：同一环境层支撑蒸馏、在线 RL 采样和评估多个阶段，轨迹数据可用于不同 harness 训练。

## 关键实验结果
- **SWE-bench Verified**：SFT 后 64.3%，SFT+RL 后 67.5%，在同等规模开源模型中达到最高，逼近 10–30 倍参数量的前沿混合专家系统。
- **GUI 代理**：平均成功率 68.4%（WebVoyager 74.1%、Online-Mind2Web 67.0%、DeepShop 64.0%），超越所有开源视觉语言代理，仍能与 OpenAI 和 Gemini 专有系统竞争。
- **个人助理**：Claw-Eval pass@3 达 59.6%，搭配 ZeroClaw harness 后提升至 73.9%。
- **基础设施指标**：Orchard Env 命令执行延迟 0.28s（与 SkyPilot 持平，比 E2B 快 2.7 倍）；128 并行沙箱 240 小时成本仅需 673 美元（spot 实例），为 Daytona 的 10%。

> 一个薄、开放、与 harness 无关的环境层是代理建模复用性的基础，使开源代理训练首次在多个领域达到匹敌专有系统的性能。
