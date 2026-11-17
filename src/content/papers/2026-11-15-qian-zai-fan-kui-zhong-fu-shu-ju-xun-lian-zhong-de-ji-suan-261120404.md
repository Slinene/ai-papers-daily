---
title: Latent Feedback Is a Compute and Data Amplifier
title_zh: 潜在反馈：重复数据训练中的计算与数据放大器
authors:
- Benhao Huang
- Chaitanya Dwivedi
- Xuezhe Ma
- Alexander Moreno
- Hector Liu
affiliations:
- Institute of Foundation Models
- University of Southern California
- Carnegie Mellon University
arxiv_id: '2611.20404'
url: https://arxiv.org/abs/2611.20404
pdf_url: https://arxiv.org/pdf/2611.20404
published: '2026-11-15'
collected: '2026-11-17'
category: Training
direction: 训练效率 · 重复数据 scaling law
tags:
- latent feedback
- scaling law
- compute efficiency
- data efficiency
- Transformer training
one_liner: 复用上一 token 顶层状态作为下一 token 输入，最多省 48% 计算与 47% 独特数据
practical_value: '- **替换多 epoch 训练**：当你在 LLM4Rec 或 Agent 模型收尾阶段数据短缺、只能重复数据时，优先试 latent
  feedback 而不是无限增加 epochs；论文显示同 compute 下更优，且越重复、unique data 越高收益越明显。

  - **低成本架构改造**：只需把上一 token 的 top-layer hidden state 通过可学习线性映射 W 加回下一 token 输入，不动
  attention/KV cache；可以在商品文本、用户行为序列等 token 化场景快速 A/B。

  - **先小网格拟合 scaling law 再放量**：用 60M–271M 小模型网格拟合 loss vs compute/data，再预测业务大模型能否省数据/省算力；论文外推
  778M 误差 0.3%，节省 48% compute / 47% unique data，适合在训练预算有限时做决策。

  - **判断适用条件**：只有当 unique data 相对模型参数量不稀缺时才划算；推荐域有大量行为 log、长尾 item 描述，通常 unique token
  充足，条件匹配。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：高质量数据紧缺时，常见做法是多 epoch 重复训练，但边际收益递减；latent feedback（将每个 token 的 top-layer state 反馈给下一 token）是另一种消耗同等 FLOP 的方式，此前未与同等 compute 的多 epoch vanilla Transformer 公平比较。

**方法关键点**：在 60M 至 778M 模型、不同 unique data 和 epoch 组合上，对两种模型逐点调参；latent feedback 通过可学习线性映射 W 将上一 token 的顶层 hidden state 注入下一 token 输入；进一步用统一 scaling law 拟合，把 latent feedback 视作“拥有更多参数的 Transformer”。

**关键结果**：在 unique data 固定时，latent feedback 用更少 compute 达到 vanilla Transformer 同样 loss；在 epoch 固定时，用更少 unique data 达到同 loss。两项节省随 unique data per parameter 和重复次数增长，下游任务一致。在 60M–271M 上拟合的 scaling law 对 held-out 778M 的 loss 预测误差 <0.3%，两模型差距误差 <0.05%。最多省 48% 计算和 47% unique data；当数据而非算力是瓶颈时，latent feedback 是给定模型规模下更好的 FLOP 投向。仅在 unique data 相对模型规模稀缺时例外，当前大模型通常远离该区间。
