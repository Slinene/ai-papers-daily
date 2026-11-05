---
title: Adversarial Speculative Reasoning Improves Long Horizon Agents
title_zh: 对抗式投机推理提升长时程 Agent 推理能力
authors:
- Hongyin Luo
- Wei Fang
- Lijie Yang
- Owen Stepan
- Daniel Suit
- Jeff Krapf
- Dana Wensberg
- Jack O&#39;Brien
affiliations:
- Subconscious Systems Technologies, Inc.
- Massachusetts Institute of Technology
- Princeton University
- Northeastern University
arxiv_id: '2611.05345'
url: https://arxiv.org/abs/2611.05345
pdf_url: https://arxiv.org/pdf/2611.05345
published: '2026-11-02'
collected: '2026-11-05'
category: Agent
direction: Agent 推理 · Speculative Decoding 精度分配
tags:
- Speculative Decoding
- Long-horizon Agents
- Draft Model Training
- Adversarial Preference
- Context Precision
one_liner: 训练 draft model 故意在关键推理点被拒绝，将投机解码从加速器变为上下文精度分配器
practical_value: '- 长程 Agent 任务中，投机解码不应只当加速器；可以主动用 draft 的接受/拒绝来标记关键决策点，让 target 模型在低噪声
  slot 重新采样，提升关键推理的精度和稳定性。

  - 训练一个小型 draft model（参数占比 0.06%-0.28%）来对抗性偏好关键 tokens 被拒绝，是一种轻量方法，不需改动 target 模型或输出分布，适合在已有
  Agent 系统上叠加。

  - 对于电商搜索推荐里的 Agent（如多步商品筛选、对话式导购、多轮查询改写），关键决策步骤（如选择属性、筛选条件）的推理精度对最终结果影响大，可以借鉴在关键分支位置强制
  target 模型重新生成，降低长程噪声累积。

  - 工程上可以把 draft model 当作“精度分配器”，在关键步骤拒绝草稿，重新触发 target 验证，以较低成本提高长程任务成功率；注意数值噪声在 verify
  window 内每 slot +4% 到 +34%，要控制窗口大小。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**

Speculative decoding 传统上被当作纯系统优化，只追求加速和 draft acceptance rate。但论文发现：在 long-horizon agent reasoning 中，draft 接受/拒绝会改变模型输出分布，特别是 30 步之后；数值噪声在 verify windows 内累积（每 slot +4% 到 +34%），导致关键推理 tokens 被编码在较高噪声上下文中，最终影响推理准确性。因此需要主动控制这种噪声。

**方法关键点**

- 在 agent traces 中识别关键推理点（如决策分支、重要中间结论）。
- 训练 draft model 使用对抗性偏好（adversarial preference），让这些关键 tokens 被拒绝。
- 推理时，draft 与 target 在决策点分道扬镳，verification 重启，关键思考 tokens 由 target 在最低噪声条件下采样，从而更好地索引和保存长期推理。

**关键结果**

在复杂 agentic coding benchmarks 上，端到端成功率提升；未改变 target model 或其输出分布；仅训练了 0.06% 到 0.28% 的 hosted parameters。
