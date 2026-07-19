---
title: Rethinking the Evaluation of Harness Evolution for Agents
title_zh: 重新审视智能体 Harness 进化的评估
authors:
- Yike Wang
- Huaisheng Zhu
- Zhengyu Hu
- Yige Yuan
- Zhengyu Chen
- Shakti Senthil
- Hannaneh Hajishirzi
- Yulia Tsvetkov
- Pradeep Dasigi
- Teng Xiao
affiliations:
- Allen Institute for AI
- University of Washington
- Independent
arxiv_id: '2607.12227'
url: https://arxiv.org/abs/2607.12227
pdf_url: https://arxiv.org/pdf/2607.12227
published: '2026-07-13'
collected: '2026-07-19'
category: Agent
direction: Agent Harness 进化评估
tags:
- LLM Agents
- Harness Evolution
- Evaluation Protocol
- Test-Time Scaling
- Overfitting
- Generalization
one_liner: 自动 Harness 进化在公平比较下未超越简单测试时搜索，且泛化有限，呼吁新评估协议
practical_value: '- **公平基线设计**：在为业务 Agent 引入自动 Harness 优化时，必须以简单 test-time scaling（如多次采样投票）为基线，匹配推理预算，确保增益来自设计改进而非额外搜索。

  - **防过拟合拆分**：搜索配置与最终评估必须使用不同任务集，避免在公共 benchmark 上循环优化导致的过拟合，提升上线后的泛化性。

  - **谨慎采用自动进化**：实验显示自动 Harness 进化并不稳定优于简单基线，落地时优先考虑可靠的固定 Harness，仅当有强泛化证据时才投入自动搜索。

  - **关注现实迁移**：评估 Harness 时增加留出任务集测试，模拟业务中分布外场景，防止在熟悉任务上虚高，确保 Agent 在真实多变环境中有效。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：LLM Agent 常依赖外部 Harness（提示、工具、控制逻辑）与复杂环境交互，手动设计费时费力。自动 Harness 进化方法通过单元测试反复搜索最优配置，声称提升性能，但现有评估存在两个根本缺陷：1）搜索本身消耗大量推理预算，没与简单 test-time scaling 基线公平比较，难以区分增益来源；2）搜索和最终评估使用同一基准，存在严重过拟合风险。

**方法**：设计了一套公平评估协议，在匹配的任务反馈和推理预算下，将 Harness 进化方法与简单的 test-time scaling（如多数投票）和发现基线进行对比，同时在留出的未见任务上测试进化后 Harness 的泛化能力。实验采用 GPT-5.4 和 Claude Opus 4.6 在 Terminal-Bench 2.1 上进行。

**关键结果**：自动 Harness 进化并未一致地超越简单 test-time scaling，在多数设置下增益不显著；进化得到的 Harness 在留出任务上泛化性有限，表明其改进多源于对特定任务集的过拟合。

**结论**：现有自动 Harness 进化的有效性被高估，社区需要建立更严格的评估协议和基准，确保 Agent 能力提升的归因清晰可靠。
