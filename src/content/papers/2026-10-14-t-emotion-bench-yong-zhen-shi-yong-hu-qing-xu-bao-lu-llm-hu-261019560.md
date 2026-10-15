---
title: 'τ-Emotion-Bench: Exposing the Interaction Fragility of LLM Agents through
  Real-World User Emotions'
title_zh: τ-Emotion-Bench：用真实用户情绪暴露 LLM Agent 交互脆弱性
authors:
- Rishitosh Kumar Singh
- Amir Saeidi
- Shamanthak Hegde
- Shrinidhi Kumbhar
- Chitta Baral
affiliations:
- Arizona State University
arxiv_id: '2610.19560'
url: https://arxiv.org/abs/2610.19560
pdf_url: https://arxiv.org/pdf/2610.19560
published: '2026-10-14'
collected: '2026-10-15'
category: Agent
direction: 情绪化用户交互下工具调用 Agent 评估与训练
tags:
- LLM Agents
- Tool Use
- User Simulation
- Emotion-Conditioned Interaction
- Interaction-Aware Training
- Benchmark
one_liner: 提出情绪化用户交互基准与 Tracer 数据管线，用交互感知信号训练工具调用 Agent 提升可靠性与跨域迁移
practical_value: '- 在电商导购/售后 Agent 的轨迹合成中，可引入“用户不满可提前终止”的交互感知 reward，过滤最终成功但频繁追问、过度依赖用户的轨迹；让模型优先通过工具查库存/价格/订单，信息不可得时才向用户确认。

  - 用户模拟器压测时，不要把情绪作为独立任务或改变任务目标，而应在同一任务上叠加情绪条件（如焦虑、不耐烦、低信任）并保留原成功判定，能更稳定地暴露 Agent
  的交互鲁棒性。

  - 用“工具调用/追问比”作为线上会话 Agent 的诊断指标：成功会话通常工具调用明显多于追问；可以在 prompt 或 reward 中约束“先查工具，再必要时追问”。

  - 借鉴 Tracer 的依赖图 + 反写自然指令流程，可以为业务领域低成本生成 policy-valid 多步任务和训练轨迹；少量高质量交互感知数据比大批普通成功轨迹更利于跨域迁移。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：现有工具调用 Agent 评测和训练主要看最终任务是否完成，忽视交互效率。真实用户会因 Agent 反复追问或进展缓慢而提前终止对话，导致即使最终能完成任务的 Agent 在情绪化互动中也不可靠。

**方法关键点**：
- 在 τ-Bench 框架上引入情绪条件 e，用户响应由 u_t ~ π_user(·|u,e,h_t) 生成；用户可发 ###UNSATISFIED### 提前终止，轨迹获得 -1 reward。
- 任务构建：先建立工具依赖图，采样 policy-valid 多步工作流，再反向生成自然用户指令；情绪采用 Atlas of Emotions 五大情绪族、22 种细粒度情绪 × 3 行为维度（礼貌、紧急、信任），共 594 种条件，但保持任务目标和成功判定不变。
- Tracer 用同一 harness 生成训练轨迹，交互感知信号过滤过度依赖用户的成功轨迹，偏好工具执行与必要追问的平衡。

**关键实验与结果**：
- 580 个任务、10 个领域。以 Qwen3-235B 用户模拟器测试，最强模型 DeepSeek-V4.1-Flash Avg@3 仅 55.9%，Pass^3 仅 32.2%；GLM-5.2 模拟器下 GLM-5.3 Avg@3 78.6% 但 Pass^3 66.5%。
- Tracer-High 微调 Qwen3 1.7B/4B/8B，Avg@3 提升 13.8–19.7 个百分点；仅用 1,498 条四领域轨迹训练的 Tracer-Low，在 6 个 unseen 领域 Pass^3 优于 EnvScaler、Simia 等方法，并迁移到 τ-Bench / τ-Trait。
- 成功交互与工具调用/追问比平衡相关：Simia 51.9% 轨迹追问多于工具调用，而 Tracer 仅约 10.6–12.8%。

**最值得记住**：交互是否高效、用户是否愿意继续，本身就是重要的训练信号；不要把任务成功当作唯一奖励。
