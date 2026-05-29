---
title: 'AgentDoG 1.5: A Lightweight and Scalable Alignment Framework for AI Agent
  Safety and Security'
title_zh: AgentDoG 1.5：轻量级可扩展AI Agent安全对齐框架
authors:
- Dongrui Liu
- Yu Li
- Zhonghao Yang
- Peng Wang
- Guanxu Chen
- Yuejin Xie
- Qinghua Mao
- Wanying Qu
- Yanxu Zhu
- Tianyi Zhou
affiliations:
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2605.29801'
url: https://arxiv.org/abs/2605.29801
pdf_url: https://arxiv.org/pdf/2605.29801
published: '2026-05-27'
collected: '2026-05-29'
category: Agent
direction: Agent 安全对齐与在线护栏
tags:
- agent safety
- alignment
- lightweight model
- guardrail
- influence function
one_liner: 用影响函数纯化约1k样本训练0.8B-8B模型，实现与GPT-5.4相当的Agent安全审核性能，并作为无训练在线护栏部署。
practical_value: '- **构建安全分类体系与数据引擎**：针对电商Agent（如自动客服、订单操作）可能遇到的风险场景，可先建立细粒度的安全分类法，然后基于分类法指导数据构建，用少量高质量样本训练轻量安全审核模型，降低数据成本。

  - **影响函数纯化训练数据**：从大量候选数据中筛选对模型安全性提升最有价值的样本，去噪提纯，仅用约1k条数据即可让小模型（0.8B）达到大模型水准，这种数据提纯思路可直接用于业务中安全模型的迭代。

  - **极低部署开销的在线护栏**：在Docker级环境实现推理时延与成本降低两个数量级，适合在电商Agent系统（如导购、售后）的实时交互中插入安全检查，能以极低计算资源运行，且无需额外训练即可作为即插即用的安全护栏。

  - **开源模型与基准**：提供了多尺寸模型和训练环境，可直接基于其架构微调适应电商特定安全需求，或将其安全判别能力迁移至自己的Agent管道中。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现代开放世界Agent（如OpenClaw）具备强大的跨环境执行能力，但也引入大量新安全风险，且前沿模型降低了攻击门槛，现有对齐框架难以满足实际部署需求。

**方法**：
- 更新Agent安全分类法，覆盖Codex和OpenClaw场景下的新兴风险。
- 构建分类法引导的数据引擎，利用影响函数对数据进行提纯，仅使用约1k高质量样本。
- 训练轻量AgentDoG 1.5变体（0.8B, 2B, 4B, 8B），同时构造高效的Agent安全SFT和RL训练环境，在Docker层面降低部署开销两个数量级。
- 将AgentDoG 1.5作为无需重新训练的在线护栏（guardrail）直接用于实时安全审核。

**结果**：在R-Judge、ATBench-Pro、AT-Codex、AT-Claw、Risk Source等多个基准上达到SOTA，性能与GPT-5.4等闭源大模型相当甚至更优（如AT-Codex上AgentDoG-4B-U得分87.6，GPT-5.4为78.1）。全部模型与数据集开源。
