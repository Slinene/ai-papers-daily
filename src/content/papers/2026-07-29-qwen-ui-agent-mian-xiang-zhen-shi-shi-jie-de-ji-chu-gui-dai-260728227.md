---
title: 'Qwen-UI-Agent Technical Report: Toward Next-Generation Real-World Centric
  Foundation GUI Agents'
title_zh: Qwen-UI-Agent：面向真实世界的基础 GUI 代理技术报告
authors:
- Hanzhang Zhou
- Panrong Tong
- Xu Zhang
- Quyu Kong
- Chenglin Cai
- Tianyu Xia
- Gongjie Zhang
- Jianan Zhang
- Long Li
- Long Chen
affiliations:
- Alibaba Group
arxiv_id: '2607.28227'
url: https://arxiv.org/abs/2607.28227
pdf_url: https://arxiv.org/pdf/2607.28227
published: '2026-07-29'
collected: '2026-07-31'
category: Agent
direction: GUI Agent 基础模型与训练
tags:
- GUI Agent
- Online RL
- Data Flywheel
- Action Batching
- Proactive Service
one_liner: 统一移动/电脑/网页的 GUI 代理，结合真实设备环境与数据飞轮，实现多平台 SOTA 性能。
practical_value: '- **统一动作空间设计**：将 GUI 操作与 CLI 命令交错批处理，可借鉴用于电商 Agent 在网页/App 上执行多步推荐、广告投放任务，减少推理轮次。

  - **自动化数据飞轮**：用 Agent 自身构造任务、诊断失败并迭代，能显著降低人工标注成本，适合为电商搜索推荐 Agent 持续生成训练数据。

  - **大规模在线 RL 训练**：支持 100+ 步长轨迹训练，利用 10,000+ 并发环境加速，可迁移至电商多轮对话或流程自动化 Agent 的训练。

  - **主动服务与跨平台状态保持**：轻量 harness 层允许 Agent 主动发起推送或跨设备续接任务，类似电商场景中的主动推荐、缺货提醒或跨端购物车同步。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 GUI 代理离真实世界使用仍有差距，需在真实设备上可靠运行、跨平台执行、结合 GUI 与 CLI、完成长任务、主动服务并自主进化。

**方法**：Qwen-UI-Agent 构建了覆盖移动、电脑、网页、深度搜索的统一代理系统。亮点：① 统一动作空间，将 GUI 操作与 CLI 执行交错批处理，单轮生成多个动作；② 大规模真实设备移动运行时（Real-device Runtime）与多样沙盒环境结合；③ AutoResearch 风格数据飞轮，用 Agent 自建任务、环境，诊断失败并规划迭代；④ 在线 RL 支持超 100 步长训练，并发环境超 1 万，加速 rollout；⑤ 轻量级 harness 支持主动服务触发和跨设备有状态工作流。

**结果**：移动端 MobileWorld 82.1%、MobileWorld-Real 92.2%、AndroidDaily 97.5%；电脑端 OSWorld-Verified 79.5%、OSWorld-v2 40.0% partial-progress；浏览器 WebArena 73.6%；GUI 定位 ScreenSpot-Pro 81.5%，整体优于或比肩 Opus 4.8、Gemini 3.1 Pro、GPT-5.6 Sol 等前沿模型。
