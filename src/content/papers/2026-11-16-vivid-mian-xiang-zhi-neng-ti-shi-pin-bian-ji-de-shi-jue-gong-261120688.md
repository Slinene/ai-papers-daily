---
title: 'VIVID: A Visual Harness for Agentic Video Editing'
title_zh: VIVID：面向智能体视频编辑的视觉工具层
authors:
- Wenhan Yu
- Zhaoxi Zhang
- Zhilong Tan
- Weikang Li
- Lei Sha
affiliations:
- Beihang University
- Peking University
arxiv_id: '2611.20688'
url: https://arxiv.org/abs/2611.20688
pdf_url: https://arxiv.org/pdf/2611.20688
published: '2026-11-16'
collected: '2026-11-22'
category: Agent
direction: Agent 视觉 harness 增强视频编辑
tags:
- Agent
- Visual Harness
- Video Editing
- Evidence Memory
- Multimodal
- Tool Use
one_liner: 为通用 coding agent 增加视听检查、证据记忆与渲染反馈工具，无需训练即显著提升视频编辑任务表现
practical_value: '- **多模态工具层复用**：在电商短视频广告混剪中，用通用 coding agent + ffmpeg 等原生工具，提供按需取样帧/音频/转写接口，而非一次性传入整段视频；能显著降低
  token 成本并保留时间定位。

  - **证据记忆与版本管理**：把每次观察和对应媒体版本、时间坐标存入 evidence memory，agent 在多轮编辑中主动检索；适合长直播切片或多版本商品素材，避免重复压缩导致上下文溢出。

  - **渲染输出闭环**：编辑后让 agent 检查渲染结果，与原目标对比并继续修订；在广告素材生成、商品视频修正中可复用，提升自动迭代质量。

  - **工具层与模型解耦**：同一 harness 可接入 Codex/Claude/OpenCode，说明先建通用多模态工具层比逐模型微调更划算，业务上可标准化工具接口，快速尝试不同底座模型。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

动机：视频编辑需要智能体依据视听观察和精确时间定位做决策，并在渲染输出中评估效果；通用 coding agent 具备理解、推理和代码执行能力，但缺少面向视频的媒体交互与证据管理。

方法：VIVID 作为视觉 harness，无需额外训练模型。它提供按需视频检查、音频分析和转写工具，并把每次观察与对应媒体版本、时间坐标一起保存到证据记忆中；agent 可主动检索这些观察，利用原生 coding/shell 工具执行剪辑，再检查渲染输出来指导后续修订。同一 harness 可集成 Codex、Claude Code、OpenCode 等多个 coding agent。

结果：在 AgenticVBench 的 100 个任务（涵盖 Assembly、Repair、Sequencing、Repurpose）上，Codex+VIVID 平均得分 58.6%，较原生 Codex 提高 20.2 个百分点；Claude Code 和 OpenCode 接入后分别为 55.1% 和 37.1%，同样显著超过各自基线。
