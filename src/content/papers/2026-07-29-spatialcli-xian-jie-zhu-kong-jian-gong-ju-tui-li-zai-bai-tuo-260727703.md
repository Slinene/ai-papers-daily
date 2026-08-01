---
title: 'SpatialCLI: Learning to Reason With Spatial Tools, Then Without Them'
title_zh: SpatialCLI：先借助空间工具推理，再摆脱工具
authors:
- Yang Zhou
- Zixuan Huang
- Sunzhu Li
- Zhuo Yang
- Chen Zhang
- Shunian Chen
- Caijun Yan
- Jianyao Xu
- Shunyu Liu
- Weijie Fu
affiliations:
- Zhejiang University
- Zhuoyu Technology
- Beihang University
- University of Electronic Science and Technology of China
- Nanyang Technological University
arxiv_id: '2607.27703'
url: https://arxiv.org/abs/2607.27703
pdf_url: https://arxiv.org/pdf/2607.27703
published: '2026-07-29'
collected: '2026-08-01'
category: Agent
direction: Agent 工具学习与能力内化
tags:
- spatial reasoning
- tool use
- knowledge internalization
- agentic RL
- vision-language model
- benchmark
one_liner: 提出三阶段框架让 VLM 学会调用空间工具，再将工具能力内化到自身，推理时无需工具仍高性能
practical_value: '- 三阶段训练策略：先用工具增强数据做冷启动 SFT，再用 Agentic RL 提升工具调用准确率，最后将成功轨迹转化为 SFT
  数据内化能力，可直接迁移到推荐/搜索 Agent 的工具调用训练中，比如让 LLM Agent 学会调用推荐 API 再内化推荐知识。

  - 延迟敏感的线上场景：通过内化将工具能力蒸馏到小模型，实现推理时无工具调用，降低延迟，适用于电商搜索/推荐的高并发服务。

  - 冷启动 SFT + RL 的组合：先通过格式化示例让模型学会工具调用格式，再用环境反馈优化决策，可提升 Agent 在复杂决策任务（如多步推荐、交互式搜索）中的鲁棒性。

  - 评估基准设计：SpatialCLI-Bench 聚焦组合感知，类似思路可构建面向推荐领域的组合能力基准，评估 Agent 在 item 检索、过滤、排序等多步骤中的表现。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：通用 VLM 能进行高层任务推理但缺少空间细节感知，专用视觉模型能捕捉细节但无法做任务决策，传统工具调用虽能增强感知但带来延迟。SpatialCLI 旨在让 VLM 学会调用空间工具（定位、分割、深度、姿态），并逐步内化工具能力，实现推理时摆脱工具依赖，兼顾性能与延迟。

**方法**：分为三阶段——（1）Call：将专用视觉模型封装为空间工具供 VLM 调用；（2）Learn：先用冷启动 SFT 使 VLM 掌握工具调用格式，再用 Agentic RL 根据环境奖励优化工具使用策略；（3）Internalize：收集成功工具使用轨迹，提取中间步骤和最终答案，构造 SFT 数据对 VLM 进行知识蒸馏，使模型直接输出结果而不调用工具。同时构建了包含 516 个示例的 SpatialCLI-Bench，覆盖定位、分割、深度、姿态的组合感知任务。

**关键结果**：在 MindCube 基准上，Qwen3-VL-8B-Instruct 使用工具后准确率从 29.3% 升至 84.6%，超越 GPT-5.6 Sol 加工具（72.1%）；内化后无工具准确率仍保持 73.8%，大幅优于未内化基线。
