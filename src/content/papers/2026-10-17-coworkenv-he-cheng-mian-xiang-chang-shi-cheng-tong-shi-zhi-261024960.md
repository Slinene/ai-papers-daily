---
title: 'CoworkEnv: Synthesizing Training Environments for Long-Horizon Cowork Agents'
title_zh: CoworkEnv：合成面向长时程同事智能体的训练环境
authors:
- Zhongwei Xie
- Yiming Du
- Jiaxin Bai
- Baixuan Xu
- Chunyang Li
- Xiyu Ren
- Wei Fan
- Tianshi Zheng
- Weizhi Du
- Jingqiao Yu
affiliations:
- The Hong Kong University of Science and Technology
- The Chinese University of Hong Kong
- Hong Kong Baptist University
- Independent Researcher
arxiv_id: '2610.24960'
url: https://arxiv.org/abs/2610.24960
pdf_url: https://arxiv.org/pdf/2610.24960
published: '2026-10-17'
collected: '2026-10-20'
category: Training
direction: AI cowork agent 训练环境合成
tags:
- Cowork Agent
- Environment Synthesis
- SFT
- RL
- Tool Use
one_liner: 用工作流需求合成可执行训练环境，同时产出 SFT 演示与 RL 奖励，训练小型 cowork agent
practical_value: '- 电商智能客服/导购 agent 可参考 capability-guided 任务生成：从工作流需求出发，用程序化校验与反馈修复生成请求、工具接口、评分检查，减少人工标注和评审成本。

  - Teacher executions 生成 SFT 演示 + student rollouts 产出 RL 奖励的两阶段数据管线，适合在线学习场景；可直接复用到多轮导购、售后工单处理等长时程任务。

  - 关注 reward processing 与 credit assignment 配置：在长多轮 agent RL 中，分步奖励处理和信用分配对训练动态影响大，建议做消融而非直接套用单轮稀疏奖励。

  - 对推荐系统本身借鉴有限，但可执行环境与程序化验证的思路可用于构建推荐 Agent 的仿真评估器，快速回归多步工具调用策略。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：AI coworkers 需要多轮沟通、工具协调、访问约束下操作工作区状态，但构建训练经验需要连贯请求、服务记录、工具接口和评分检查，人工成本高。

方法：CoworkEnv 是一个 capability-guided 框架，工作流需求指导任务构建；程序化验证配合反馈修复检查生成规格与评分行为。教师执行产生精选演示用于 SFT，学生交互产生 rollouts 和奖励用于 RL。基于这些资源训练紧凑的 PocketWorker 模型。

关键结果：对 Qwen3-VL-8B-Instruct，SFT 将 Claw-Eval 平均分从 46.6 提升至 64.1，其中 Multi-turn 任务提升 31.9 分；SFT-only 扩展到 ClawMark 验证跨基准适用性；RL 训练动态比较了不同 reward processing 与 credit assignment 配置，训练奖励改善初步证明环境支持策略优化。
