---
title: 'CLIFT: Conformal Self-Verification for Web Agent Training and Test-Time Scaling'
title_zh: CLIFT：基于共形自验证的 Web Agent 训练与测试时扩展
authors:
- Yifan Zhang
- Yutong Dai
- Viraj Prabhu
- Zhiyuan Hu
- Ran Xu
- Zeyuan Chen
affiliations:
- Salesforce AI Research
arxiv_id: '2610.06829'
url: https://arxiv.org/abs/2610.06829
pdf_url: https://arxiv.org/pdf/2610.06829
published: '2026-10-05'
collected: '2026-10-06'
category: Agent
direction: Web Agent 强化学习与测试时选择
tags:
- Web Agent
- Reinforcement Learning
- Conformal Prediction
- Test-Time Scaling
- Self-Verification
- GRPO
one_liner: 将昂贵 judge 反馈蒸馏为可认证的验证问题库，训练时做稠密奖励，测试时做无需 judge 的保守轨迹选择
practical_value: '- 把昂贵 judge 反馈蒸馏成可复用的「验证问题库」：每个问题带 URL scope、polarity sign 和 conformal
  trust weight，训练时用非对称 reward 融合（只加不减，防止 reward collapse），可按 URL 状态做分层优势归一化，明显改善 agent
  RL 的 credit assignment。推荐/搜索 agent 训练中可借鉴此方式，针对领域定义可验证问题，用 lift 和 conformal 筛选后作为过程奖励。

  - 测试时用同一冻结问题库做轨迹选择（CTS）：greedy + diverse retries，自验证器输出结构化证据，保守多数投票默认保留 greedy，无需外部
  judge 即可实现 test-time scaling，且能保证不回归。在线推理中可对 agent 轨迹做低风险 reranking，适合预算受限场景。

  - 验证知识可与策略解耦：在 open model 上训练的 question bank 可直接迁移到 closed model（GPT-5.5）使用，节省强模型
  fine-tune 成本。业务上可先在小模型上构建验证器，再用于大模型推理阶段的选择。

  - 工程上采用 CEGAR 循环从 judge rationales 定期挖掘新验证问题，并用 polarity veto 纠正错误标签；Mondrian-ACI
  跟踪器按 global/host/URL-path 分层动态校准信任权重，对分布漂移具有拒绝能力，可借鉴到构建自适应质量监控或评估器。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
Web agent 强化学习面临奖励稀疏与 judge 成本高的矛盾：二元成功信号太稀疏导致 GRPO 优势估计坍塌，而 frontier LLM judge 训练时昂贵且测试时不可用。CLIFT 的核心思想是把 judge 反馈转化为一个可复用的验证器，而非训练单独的 process reward model 或仅做 best-of-N 重排。

**方法关键点**
- **验证问题库**：自然语言 YES/NO 问题，每个问题带 URL scope 和 polarity sign（progress/failure/ambiguity）。通过 Compositional Conformal Certifier (CCC) 使用 Mondrian-ACI 和 polarity-aware lift 进行认证，只有 lift 显著、错误率可控的问题才获得带符号信任权重。
- **训练阶段**：在 GRPO 基础上，将认证库的 verifier score 通过非负截断（max(0, RVQ)）加到 judge 的 per-step reward 上，保证不拖低 judge 基线；并按 (rollout-group, step-position, URL-state) 做 URL 分层优势归一化，改善 credit assignment。CEGAR 循环定期从 judge rationales 挖掘新问题并校准。
- **测试阶段（CTS）**：冻结问题库，采样 greedy 轨迹 + diverse retries，自验证器为每个 URL trace 生成结构化证据，通过保守多数投票决定是否替换当前轨迹，默认保留 greedy，避免噪声导致的有害 swap。

**关键结果**
- **WebArena Infinity**：Gemma-4 + CLIFT + CTS 达 74.6%，超过 Gemini 3 Flash + BU（70.1）和 Claude Opus 4.6 参考（69.8），较 base Gemma-4 提升 12.8 pp；消融显示训练贡献 10.8 pp，CTS 再加 2.0 pp，无 app 回归。
- **VisualWebArena**：训练于 open model 的 bank 迁移到 GPT-5.5，CLIFT + CTS (K=4) 达 53.7，超过 WALT 52.9。
- **Online Mind2Web**：零样本迁移，GPT-5.5 high-effort + CTS 从 49.7 提升到 61.0（+11.3 pp），验证问题库具有跨 benchmark 可复用性。

**最值得记住的一句话**：昂贵的 judge 反馈可以被蒸馏成一个可认证、可迁移、可审计的验证问题库，训练时做稠密奖励，测试时做无需 judge 的保守轨迹选择。
