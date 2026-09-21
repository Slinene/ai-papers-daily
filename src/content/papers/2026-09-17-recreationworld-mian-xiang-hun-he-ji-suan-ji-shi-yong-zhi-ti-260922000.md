---
title: 'RecreationWorld: Scalable and Verifiable Environments for Hybrid Computer-Use
  Agents'
title_zh: RecreationWorld：面向混合计算机使用智能体的可扩展可验证环境
authors:
- Shuai Bai
- Jiayong Deng
- Yikun Fu
- Chang Gao
- Xuhao Hu
- Mianqiu Huang
- Yizhen Jiang
- Yuheng Jing
- Dehui Kong
- Keliang Li
affiliations:
- Alibaba Token Hub, Alibaba Group
arxiv_id: '2609.22000'
url: https://arxiv.org/abs/2609.22000
pdf_url: https://arxiv.org/pdf/2609.22000
published: '2026-09-17'
collected: '2026-09-21'
category: Agent
direction: 混合计算机使用智能体基准与训练
tags:
- Computer-Use Agents
- Hybrid Agents
- Benchmark
- Execution-Grounded Reward
- GUI Automation
- SFT
one_liner: 以“复刻运行中应用”为核心任务，构建跨五平台的混合 GUI/代码智能体基准与训练框架
practical_value: '- 用“reference-as-oracle”做自动化回归：电商页面改版、前端重构、配置迁移时，把旧版/线上版本作为运行 reference，自动采集动作-响应和截图，生成
  Programmatic + VLM 断言，替代人工比对，得到可回放、可量化的验收指标。

  - 复制混合工作流到业务 Agent：不要硬限制 GUI-only 或 code-only；给 Agent 同时开放 GUI 观察、代码编辑、构建/运行三类工具，让它自主切换。论文显示这种混合轨迹在长程任务中切换频繁，且基于可验证环境做
  SFT 能迁移到 OOD 编码/计算机使用任务。

  - 用拒绝采样 + 可执行奖励造 SFT 数据：如果业务中有可自动评分的交互环境（如商品页面结构化抽取、RPA 流程、店铺装修），可跑多模型 rollout，用隐藏测试套件打分，选高奖励轨迹微调，减少人工标注。

  - 工程降本技巧：把链式 MCP 原语调用改成持久化 REPL + typed SDK，让模型在本地循环处理中间结果，可大幅降 token 和成本（输入 -40.7%、tool-result
  -65.5%、成本 -54.1%），质量不降，适合 GUI Agent 落地。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：当前计算机使用智能体沿 GUI 操作和终端编程两条独立路径发展，各有一半盲区：GUI 代理无法构建软件，终端代理看不见自己产出的界面。真实数字工作需要两者在同一长程任务中不断交织。复刻任务要求智能体在无规定流程下探索运行中的参考应用并写出可运行实现，天然形成 explore–implement–verify 循环，并因 reference 可执行而提供客观、执行锚定奖励。

方法关键点：
- 任务定义：给定运行 reference app，智能体自主探索 GUI、编写代码、构建并视觉验证，提交完整源代码；评估只看可观察行为，不限制实现架构与语言。
- 五平台环境：Ubuntu / macOS / Windows / Android / Web，统一 harness 提供原生 GUI 控制与编码工具，配合本地权限与网络隔离保证公平。
- 测试构造：reference 作为 oracle，生成程序化断言（AT-SPI / AX / UIA / UiAutomator / DOM）与视觉断言（VLM judge），覆盖多交互深度，经人工审核后冻结。
- 基准：RecreationBench 包含 250 个任务，每平台 50 个。
- 训练数据：由 Qwen3.8-Max rollout 产生轨迹，rejection sampling 选取高评分子集，构成 35,000 条 SFT 轨迹，用于两个模型初始化微调。

关键实验：
- GPT-6 Astra 平均得分 58.1%，领先第二名 Claude Opus 5 13.9 个百分点；但其程序化测试满分通过率仅 2.8% 任务，说明离完全行为保真仍有很大差距。
- 在两个训练臂上，复刻训练在五个 OOD 编码/计算机使用基准（ProgramBench、GameCraft-Bench、Vision2Web、OSWorld 2.0、WeaveBench）相对首个 checkpoint 全部提升，最高 +17.9 个百分点。
- RecreationBench 轨迹中位 282.5 个顶层工具调用、每 100 次调用 9.08 次 GUI–编辑切换，混合性高于 WeaveBench；智能体复现静态界面结构比交互和计算输出更可靠，生成应用远小于 reference 且更单体。
- 持久化可编程 SDK 相比 direct MCP：输入 token -40.7%、tool-result -65.5%、成本 -54.1%、wall-clock -26.1%，质量基本持平。

最值得记住的一句话：运行中的参考应用作为 oracle，可自动生成隐藏行为测试，提供客观、执行锚定的奖励。
