---
title: 'SpatialWorld: Benchmarking Interactive Spatial Reasoning of Multimodal Agents
  in Real-World Tasks'
title_zh: SpatialWorld：多模态Agent真实世界交互式空间推理基准
authors:
- Hongcheng Gao
- Hailong Qu
- Jingyi Tang
- Jiahao Wang
- Zihao Huang
- Hengkang Qiao
- Shihong Huang
- Junming Yang
- Yi Li
- Hongyixuan Yuan
affiliations:
- Tsinghua University
- Chongqing University
- Peking University
- ZenoMind AI
- Xi’an Jiaotong University
arxiv_id: '2606.09669'
url: https://arxiv.org/abs/2606.09669
pdf_url: https://arxiv.org/pdf/2606.09669
published: '2026-06-07'
collected: '2026-06-09'
category: Eval
direction: 多模态Agent · 交互式空间推理评测
tags:
- Spatial Reasoning
- Multimodal Agents
- Benchmark
- Interactive Evaluation
- Embodied AI
one_liner: 构建统一基准评估多模态Agent在真实任务中的交互式空间推理，集成8个模拟器、760个人工任务，最强模型成功率仅17.4%
practical_value: '- 统一评估层协议（simulator-agnostic, text-based action interface）可借鉴到多模态Agent评测
  pipeline，屏蔽底层仿真差异，聚焦决策能力。

  - 任务设计强调 partial observability 与主动探索，类似推荐系统中用户意图不明确时的多轮对话，可参考其“基于当前观察逐步求索”的交互范式。

  - 终态验证器（terminal-state verifier）提供可复用的自动化评判模板，用于评估推荐Agent的最终目标达成（如购物车完成态）。

  - 主要为学术基准，业务可借鉴点多在评估框架设计，空间推理本身在电商直接应用有限。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：现有空间推理测评多为被动 VQA 或单一模拟器，无法衡量多模态 Agent 的通用交互式空间理解能力。

方法：构建一个统一基准 SpatialWorld，集成 8 个异质模拟后端（如家居、旅行、社交场景），提供 760 个人工标注任务。Agent 仅通过第一人称视觉输入（partial observability）主动探索，输出统一文本动作接口，由环境返回新观察。每个任务包含人工核验的初始状态、参考轨迹和终态验证器，确保可靠评估。

结果：评测 15 个先进多模态 Agent，最强闭源模型 GPT-5 平均任务成功率仅 17.4%，最强开源模型 Qwen-3.5 为 14.1%。分析显示任务成功与执行效率脱节，不同领域表现差异显著，主动探索和长期规划仍是核心瓶颈。
