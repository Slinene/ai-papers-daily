---
title: 'Video-RSI: Recursive Self-Improvement of Video Understanding Agents via Harness
  Evolution'
title_zh: Video-RSI：通过 Harness 进化的视频理解 Agent 递归自我改进
authors:
- Bingjun Luo
- Jialin Guo
- Siqi Li
affiliations:
- Tsinghua University
- Harbin Engineering University
arxiv_id: '2609.37950'
url: https://arxiv.org/abs/2609.37950
pdf_url: https://arxiv.org/pdf/2609.37950
published: '2026-09-28'
collected: '2026-10-12'
category: Agent
direction: Agent 自我改进与工具/harness 进化
tags:
- Video Understanding
- Agent Self-Improvement
- Executable Harness
- Cost-Aware Evolution
- Active Investigation
- LLM
one_liner: 让视频理解 Agent 用自身 LM 修正可执行 harness，通过主动回访视频与成本感知进化提升精度并降低视觉成本
practical_value: '- 可将「看哪些帧/片段、调用哪些工具、如何利用观察」抽象成可执行 harness 层，在电商直播切片、商品视频理解等场景中，按准确率与视觉成本（如帧采样数、API
  调用量）做多目标筛选与保留，控制推理成本。

  - 失败诊断时不要只依赖当前执行 trace，可让 Agent 主动回访原始视频/用户行为序列等原始数据，用额外观察区分竞争性失败解释（是检索遗漏、描述丢失还是推理错误），这一思路可迁移到搜索推荐
  Agent 的调试与自改进。

  - 利用 Agent 自身 LLM 生成 harness 修订，并用验证集筛选可复用修改，形成递归自我改进闭环，减少人工调优工具/策略的工作量。

  - 直接业务价值有限：论文面向视频理解基准，与电商推荐核心链路（召回、排序、query 推荐）结合度不高，但层次化工具控制与成本感知进化思路值得 Agent 架构设计参考。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：视频理解 Agent 依赖可执行 harness 控制观察什么、如何利用观察。但执行轨迹只包含当前 harness 获得的证据，无法区分多种竞争性失败解释，限制了自我改进的基础。

**方法关键点**：
- 提出 Video-RSI，让视频理解 Agent 使用自己的语言模型修改 harness，而不改变模型权重。
- 通过主动视频调查，模型重新访问原始训练视频，用额外观察测试竞争失败解释，使改进基于现有轨迹之外的证据。
- 成本感知 harness 进化将诊断转化为可重用修订，并综合考虑答案准确率与视觉成本决定保留哪些修订。

**关键结果**：在视频理解基准上，进化后的 Agent 准确率提升，同时处理更少帧，取得与现有视频理解 Agent 有竞争力的精度-效率权衡。代码已开源。
