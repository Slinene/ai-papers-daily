---
title: 'Interactive Visual Gym: Evaluating Visual Interaction Models with Simulated
  Users in Interactive Worlds'
title_zh: 交互式视觉健身房：用模拟用户在可执行世界中评测视觉交互模型
authors:
- Chenhao Zheng
- Zixian Ma
- Kai Li
- Kanchana Ranasinghe
- Jieyu Zhang
- Artemis Panagopoulou
- Weikai Huang
- Jianxu Shangguan
- Yuanyuan Tan
- Silvio Savarese
affiliations:
- University of Washington
- Salesforce AI Research
arxiv_id: '2611.08286'
url: https://arxiv.org/abs/2611.08286
pdf_url: https://arxiv.org/pdf/2611.08286
published: '2026-11-04'
collected: '2026-11-12'
category: Eval
direction: 多模态交互式闭环评估与训练
tags:
- Visual Interaction
- Closed-loop Evaluation
- Simulated Users
- VLM
- Benchmark
- GRPO
one_liner: 提出闭环评估框架 IVG-Bench，结合可执行环境与 persona 模拟用户，发现顶尖 VLM 任务完成率仅 53.4% 且闭环训练有效
practical_value: '- 电商导购/客服 Agent 评测可借鉴“环境+模拟用户”闭环：不只评单轮回答，而是把用户后续点击、纠错、任务完成纳入评估；用
  persona 控制用户画像（新客、价格敏感、赶时间等）生成差异化行为。

  - 用户模拟器要显式注入执行错误和计划外行为，例如用户误解指令、漏步骤、执行超时，否则评测会高估助手鲁棒性；电商场景可模拟用户找不到按钮、买错规格、中途退出。

  - 把响应延迟作为硬指标：论文显示 VLM 常因太慢导致无法阻止错误，电商 Agent 涉及比价、库存确认、下单防错时，延迟直接决定防错成功率，建议评估中设时间阈值并监控
  tail latency。

  - 闭环环境可提供 GRPO 训练信号，适合用业务沙箱/模拟器对较小 VLM/LLM 做强化微调；先在小范围场景验证闭环训练提升，再上线 A/B。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有视觉交互模型评测主要基于离线回放，无法刻画助手响应对用户后续行为和任务结果的闭环影响。

**方法关键点**：提出 Interactive Visual Gym 框架，联合模拟可执行任务环境和人类用户；覆盖烹饪、家务操作、移动界面三类日常任务，提供 persona 条件的用户模拟 harness，支持受控执行错误和计划外行为。实例化为 IVG-Bench，包含 315 个交互场景。

**关键结果**：评估当前顶尖 VLM，最好模型 Gemini 4 Argon 在限时任务中完成率仅 53.4%；在事实 grounding 和可执行指导上明显薄弱，且考虑响应延迟后经常来不及阻止用户错误。人类研究验证交互质量指标与参与者偏好一致性达 78.5%。概念验证 GRPO 实验显示，在烹饪环境中闭环训练同时提升 Qwen3.5-4B 的任务成功率和交互质量。
