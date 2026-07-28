---
title: 'Interactive Training 2: Auditable Control Plane for Live Model Training'
title_zh: 交互式训练2：实时模型训练的可审计控制平面
authors:
- Wentao Zhang
- Xuanhe Pan
- Han Zhou
- Yang Lu
- Yuntian Deng
affiliations:
- University of Waterloo
- University of Wisconsin-Madison
arxiv_id: '2607.18314'
url: https://arxiv.org/abs/2607.18314
pdf_url: https://arxiv.org/pdf/2607.18314
published: '2026-07-16'
collected: '2026-07-28'
category: Training
direction: 交互式训练控制平面
tags:
- Interactive Training
- Control Plane
- LLM Agent
- Auditable
- Open-Source
- Training Steering
one_liner: 提供开源控制平面，通过共享协议让人类和智能体对训练过程进行实时、可审计的操控
practical_value: '- **在线训练动态调参**：在电商推荐模型持续训练中，可以借鉴其声明式暴露学习率、dropout 等设置，让算法工程师或自动调参
  Agent 通过统一接口实时调整，无需重启训练任务。

  - **Agent 驱动的训练编排**：将训练控制能力抽象为 Action（如保存检查点、回滚、切换数据源），LLM Agent 可根据监控指标自动决策并提交请求，例如检测到
  loss 异常时自动触发回滚和告警，适合广告模型频繁迭代的场景。

  - **审计与复现**：所有控制请求和结果按时间线记录，可回溯谁在何时做了何种干预，满足工业级模型训练的合规与排障需求，类似模型版本的 Git 日志。

  - **工程实现参考**：其“训练循环负责安全控制点”的设计模式可直接复用，在现有训练框架中插入轻量级控制平面，避免多控制器并发冲突，保证状态一致性。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有实验跟踪器只能观察训练状态，无法通用地在运行时改变训练配置或触发动作，研究者仍依赖定制回调或脚本，工具碎片化。

**方法关键点**：
- 定义共享协议，训练应用声明可改变的设置（如 learning rate）和可请求的动作（如保存检查点、开始评估）。
- 人类、脚本或 LLM Agent 通过同一接口提交控制请求。
- 训练循环在安全控制点验证并应用请求，避免并发冲突，并记录完整审计轨迹。
- 基于 Aim 定制工作空间，融合实时指标、控制面板及请求-结果时间线。

**关键结果数字**：在五个 NLP 和强化学习工作流中验证了系统的通用性和有效性，开源代码与运行轨迹可供复现。
