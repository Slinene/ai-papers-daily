---
title: Score Centering Stabilizes Off-policy Reinforcement Learning
title_zh: 分数中心化稳定离线策略强化学习
authors:
- Martin Marek
- Max Ryabinin
affiliations:
- Together AI
arxiv_id: '2609.20807'
url: https://arxiv.org/abs/2609.20807
pdf_url: https://arxiv.org/pdf/2609.20807
published: '2026-09-17'
collected: '2026-09-18'
category: Training
direction: LLM 强化学习训练稳定性校正
tags:
- score centering
- off-policy RL
- training-inference mismatch
- importance sampling
- LLM training
- drift correction
one_liner: 提出加性 score centering 校正项，抵消训练与推理引擎间的漂移，稳定 LLM 的 RL 训练
practical_value: '- 在 RL 微调推荐/对话策略时，若部署推理引擎与训练引擎存在量化、KV cache 压缩或异步参数不一致，可在计算优势或回报时减去漂移项（如训练与推理引擎在同样本上的平均输出差异），低成本稳定训练，避免策略崩溃。

  - Score centering 是加性修正，可与 importance sampling 等乘法修正叠加；在离线策略数据来自旧策略或不同推理引擎时，组合使用可能比单用
  IS 更稳健，尤其 mismatch 严重时。

  - 对于生成式推荐（用 LLM 直接生成 item ID/文案），RL 训练中 reward 常由规则或模型给出，容易受采样分布偏移影响；考虑在 reward
  或 advantage 上做 centering 来抵消环境漂移，可提升训练稳定性。

  - 工程上：漂移估计可通过在固定验证集上比较训练和推理引擎的 logprob/奖励差异得到，开销很小；可作为 RL 训练 pipeline 的常规监控与校正组件。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：大模型 RL 训练对训练与推理引擎之间的微小差异（TIM）极其敏感，但完全消除 TIM 不现实，因为会大幅降低 rollout 效率。已有校正方法（如 importance sampling）在 mismatch 严重时效果有限。

**方法关键点**：将 TIM 导致的不稳定归因于 drift——训练与推理引擎之间随训练步累积的持续偏置。推导出加性“score centering”校正项，在优势或回报中减去漂移估计，从而抵消 drift。该校正简单、加性，且可与 importance sampling 等乘法校正组合。

**关键结果**：在 0.6B 到 30B 参数的模型上，量化场景下 score centering 单独即可匹配或超过 importance sampling 方法，且 mismatch 越严重优势越大；在 staleness 实验中，与 importance sampling 组合后优于纯 importance sampling 基线。例如在 Qwen3-30B-A3B-Base 上，FP8/INT8 量化下 score centering 的训练精度明显高于 TIS、PG、PPO 等基线。
