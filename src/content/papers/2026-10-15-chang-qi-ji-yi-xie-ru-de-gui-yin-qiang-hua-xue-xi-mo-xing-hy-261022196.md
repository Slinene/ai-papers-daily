---
title: 'Hy-Memory-30B-A3B: Attributed Reinforcement Learning for Long-Term Memory
  Writing'
title_zh: 长期记忆写入的归因强化学习模型 Hy-Memory-30B-A3B
authors:
- Tianxiang Fei
- Jiazheng Kang
- Mao Zheng
- Xingyan He
- Xiang Yu
affiliations:
- Tencent Hunyuan
arxiv_id: '2610.22196'
url: https://arxiv.org/abs/2610.22196
pdf_url: https://arxiv.org/pdf/2610.22196
published: '2026-10-15'
collected: '2026-10-18'
category: Training
direction: Agent 长期记忆写入 · 归因强化学习
tags:
- Long-term memory
- RL
- GRPO
- Memory writer
- Credit assignment
- On-policy distillation
one_liner: 训练跨 Mem0/MemOS/Hy-Memory 的紧凑记忆写入器，用逐块探针和归因奖励实现细粒度信用分配，平均 55.49% 超过 Claude
  Opus 5
practical_value: '- **奖励归因替代稀疏终局奖励**：若业务中存在多轮 agent 状态管理（如对话策略、用户画像更新），可将单个最终答案分数拆解为逐块局部探针（recall
  probes + trap probes）与跨块归因结果奖励，用冻结 judge 打分，解决长序列下 credit assignment 问题。

  - **chunk-level GRPO 思想可迁移**：对任何「每个位置有可观察局部结果」的序列决策任务（如生成式推荐中的 item 序列、搜索会话策略），优势按位置分组归一化而非整个
  trajectory，避免一个坏动作惩罚所有正确动作，每个 rollout 每位置只投一票。

  - **银行隔离与 carry-forward 训练模式**：RL 训练时每个 rollout 写入独立 bank，仅选择最佳 bank 进入下一个窗口，保持训练与部署分布一致，避免
  teacher forcing。此模式适用于任何维护外部状态的 RL 训练（如推荐系统的长期兴趣状态、购物车策略）。

  - **平台故障与策略错误必须区分**：坏策略动作应保留为低奖励 trajectory，平台故障（如 API 失败、分页缺失、checkpoint 空）要重试并从分母排除；同时监控
  teacher token coverage、chunk-to-segment mapping 等静默失败，避免训练看似正常但梯度为零。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：长期记忆系统的质量取决于 write path，但现有框架通常把通用大模型放在长 prompt 后面，成本高且协议不迁移；一个能跨 Mem0/MemOS/Hy-Memory 等框架的统一记忆写入模型尚未被探索。更重要的是，最终答案奖励通常监督整个异构记忆动作序列，只有少数动作真正提供证据，存在严重的 credit assignment 问题。

**方法关键点**：
- 两阶段训练：Stage 1 Memory On-Policy Distillation 在 student 自己生成的状态链上，用 top-50 reverse KL 蒸馏框架特定写入协议；Stage 2 Memory RL 在下游可回答性上优化。
- 奖励构造来自失败表面：逐块探针（正向 recall probes 与 trap probes）提供稠密局部信号；跨块 outcome questions 测量下游效用；gold facts 将证据归因到源 chunk；银行增长惩罚抑制过度存储。
- 信用分配：chunk-level GRPO 按 chunk position 归一化优势，而非整个 trajectory；每个 rollout 每 chunk 投一票，即使框架多次 LLM 调用也只算一票。
- 状态对齐训练：rollout 在隔离 bank 写入，最佳 bank 跨窗口 carry-forward，保持训练与部署分布一致。
- 系统规模：16 节点 × 8 H20 GPUs，batch 64 windows × 8 rollouts，PPO clipped surrogate + chunk-level GRPO advantages，无 KL penalty。

**关键结果**：在固定 20% benchmark 子集上评估 Mem0、Hy-Memory、MemOS、held-out EverMemOS 四个 harness，每个 harness 平均六个指标。Hy-Memory-30B-A3B 平均 55.49%，超过 Claude Opus 5 的 54.62%、DeepSeek V4.1 Flash 的 53.64%、Hy3-A3B base 的 47.66%。在 held-out EverMemOS 上优势最大，56.89% vs Opus 5 54.04%（+2.86），Travel SPS +10.65、CMB +13.66。

**最值得记住的一句话**：记忆写入是长周期控制问题，不是泛化摘要；失败驱动探针 + 归因结果奖励 + chunk-level GRPO 将信用分配给外部可验证的 bank 变更。
