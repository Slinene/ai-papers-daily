---
title: Beyond Uniform Token-Level Trust Region in LLM Reinforcement Learning
title_zh: 超越统一 token 级信任区域的 LLM 强化学习
authors:
- Renjie Mao
- Xiangxin Zhou
- Lvfang Tao
- Yixin Ding
- Yu Shi
- Yongguang Lin
- Yuheng Wu
- Honglin Zhu
- Qian Qiu
- Wenxi Zhu
affiliations:
- Tencent Hunyuan
arxiv_id: '2606.10968'
url: https://arxiv.org/abs/2606.10968
pdf_url: https://arxiv.org/pdf/2606.10968
published: '2026-06-08'
collected: '2026-06-11'
category: Reasoning
direction: 推理强化学习 · 信任区域
tags:
- RLVR
- PPO
- Trust Region
- Prefix Constraint
- Position-Weighted
- Token Masking
one_liner: 提出 CPPO，通过位置加权与累计前缀预算的 token 掩码，使信任区域匹配自回归结构，显著提升推理 RL 的稳定性和准确率。
practical_value: '- **位置感知的信任区域分配**：在 LLM 强化训练中，不应使用统一的 token 级阈值。可以对早期 token 施加更严格的约束，后期放松，权重可采用线性递减调度（如从
  1 到 w_min）。这在长序列生成任务（如多轮 Agent 对话、推荐解释文本）中特别有用，可防止早期偏差扩散。

  - **累计前缀预算机制**：不要独立评估每个 token 的散度，而是跟踪加权前缀平均散度，一旦累积超过阈值就动态收紧后续 token 的允许散度。此方法可作为
  drop-in 掩码直接嵌入现有 PPO/GRPO 训练流程，无需修改损失函数或优势计算。

  - **通用性**：方法不依赖特定的散度估计（TV/KL 均可），且与不同的 token 级散度近似（Top-K、Binary）兼容。适用于电商场景中的商品描述生成、对话策略优化、生成式推荐序列建模等需要
  RL 微调的场合。

  - **自适应阈值设置**：在基础模型训练初期，可采用基于序列自身散度分位数的自适应 δ_b，避免过度裁剪早期探索。稳定后切换为固定阈值，平衡探索与稳定。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM 强化学习中的信任区域方法（如 PPO 裁剪、DPPO）普遍使用位置无关的统一 token 级阈值。这忽略了自回归生成的两个关键不对称性：(1) 早期 token 的偏差会影响更长的后缀，产生更大的序列级漂移；(2) 逐 token 独立评估忽略了前缀上下文中已累积的偏差，使得模型可能从严重偏离 rollout 策略的状态继续生成，加剧误差。

**方法**：提出 CPPO，通过两个机制修正上述问题：
1. **位置加权阈值**：引入递减权重 w_t 和约束 w_t·D_t ≤ δ，使早期 token 施加更紧的散度限制（D_t ≤ δ/w_t），后期逐渐放松，匹配剩余视界 T−t 的误差传播系数。
2. **累计前缀预算**：跟踪加权前缀散度和 S_t，要求所有前缀满足 S_t ≤ δ + δ_b·W_{t-1}。当历史前缀平均散度超过 δ_b 时，有效阈值 min{δ, δ+δ_b·W_{t-1}−S_{t-1}} 会自动降低，防止偏差沿前缀累积。
掩码规则仅保留使 ratio 靠近 1 的更新，或满足上述双重约束的项，完全兼容现有 GRPO/PPO 目标。

**实验**：在 Qwen3-1.7B、8B、30B-A3B 等模型上，使用 17k 数学推理 prompt 进行 RLVR 训练。CPPO 在所有设置下均取得最佳 AIME24/25/26 Avg@16 分数：1.7B 上 31.88（vs. GRPO 27.91，DPPO 28.19）；8B-Base 上 31.11（vs. 29.72）；30B-A3B-Base 上 54.79（vs. 49.23），相较 DPPO 提升 5.56 点。消融表明位置权重和前缀预算独立有效；位置顺序打乱会降低性能；方法对 TV/KL 散度及 Top-K/Binary 近似均鲁棒。

**核心洞见**：信任区域不应为所有 token 分配相同预算，而应像梯次分配弹药一样——早期 token 影响深远需严控，后期宽容以保留探索，且不超过前缀累积漂移的总预算。
