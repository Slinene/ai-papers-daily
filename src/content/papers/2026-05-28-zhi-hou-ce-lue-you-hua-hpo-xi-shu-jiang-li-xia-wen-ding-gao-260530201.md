---
title: 'HPO: Hysteretic Policy Optimization for Stable and Efficient Training under
  Sparse-Reward Regime'
title_zh: 滞后策略优化（HPO）：稀疏奖励下稳定高效的GRPO训练改进
authors:
- Mohamed Sana
- Nicola Piovesan
- Antonio De Domenico
- Fadhel Ayed
- Haozhe Zhang
affiliations:
- Paris Research Center, Huawei Technologies
- Huawei Technologies, China
arxiv_id: '2605.30201'
url: https://arxiv.org/abs/2605.30201
pdf_url: https://arxiv.org/pdf/2605.30201
published: '2026-05-28'
collected: '2026-05-31'
category: Training
direction: 强化学习 · GRPO 优化
tags:
- GRPO
- Hysteretic Learning
- Sparse Reward
- Policy Optimization
- LLM Fine-tuning
one_liner: 通过非对称抑制负优势更新并改用均值长度归一化，缓解 GRPO 在稀疏奖励下的负优势主导与长度偏置，自适应权重免去手动调参
practical_value: '- 在稀疏奖励（如早期 Agent 任务、低资源推荐对话）下，GRPO 会因大量失败样本的负优势更新主导训练，HPO 通过给负优势更新乘上小于
  1 的权重来抑制负面信号，可简单集成到现有 GRPO/PPO 管线

  - 用 batch 内平均长度替代逐响应长度归一化，消除“短正确回答权重过高、长错误回答惩罚不足”的长度偏置，更适合生成长度动态变化的推荐文案、多步 Agent
  推理等场景

  - A-HPO 根据 batch 内正/负优势样本比例自动计算阻尼系数 α，无需针对不同任务或训练阶段手动调 ❧ 唯一超参数，便于快速在新业务场景落地

  - 方法几乎无额外计算开销，只需统计正负优势数量并做一次裁剪，可作为 GRPO 训练的标准增强件，用于电商对话推荐、生成式推荐评估等 RLHF 微调流程'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：在稀疏二进制奖励（如根因分析、算术推理）下，GRPO 早期策略的成功率极低，导致一个 batch 中大多数样本获得负优势，正优势样本稀缺。这种“负优势主导”结合 GRPO 的逐响应长度归一化（短正样本权重大、长负样本权重小）带来两大失败模式：负更新压倒正更新、长度偏置使模型趋向短回答或冗长错误。论文针对此提出 HPO。

**方法关键点**：
1. **不对称优势加权**：正优势更新保持全权重 1，负优势更新乘以一个徘徊因子 α ∈ [0,1]，降低大量失败样本的冲击。
2. **均值长度归一化**：将损失函数中的逐响应长度归一化替换为 batch 内平均响应长度，解除梯度贡献与单个响应长度的逆相关。
3. **自适应 α (A-HPO)**：根据 batch 内正/负优势样本的数量比动态设定 α = clip(ˆp⁺/ˆp⁻, α_min, 1)，自动在稀疏阶段强阻尼、稠密阶段恢复对称更新，免去手动调 α。

**关键实验**：
- 数据集：TeleLogs（5G 网络根因分析）和 Countdown（算术构造任务，含 3 数和 4 数两种难度）。
- 模型：Qwen2.5‑1.5B‑Instruct 为主，另在 Llama3.1‑3B、Qwen2.5‑7B 上验证。
- 对比基线：GRPO、GSPO、SAPO。
- TeleLogs 上 A‑HPO 最终奖励 0.84，分别高出 SAPO 5%、GSPO 11%、GRPO 15%；Countdown‑4 上，Qwen‑7B 的 200 步奖励从 0.58 提升至 0.63，3B 模型提升更显著。
- 消融显示 α=0（仅正样本）导致输出长度坍塌至 16 tokens 且奖励差，α=1（对称）奖励仅 0.72；α≈0.6 时达最优（0.83），A‑HPO 自动逼近该区间。

**核心发现**：在稀疏奖励 RL 微调中，负优势信号不应被丢弃，也不应等权对待；自适应地平衡正负更新贡献，结合均值长度归一化，可大幅提升训练稳定性和样本效率，尤其适合早期训练和低资源场景。
