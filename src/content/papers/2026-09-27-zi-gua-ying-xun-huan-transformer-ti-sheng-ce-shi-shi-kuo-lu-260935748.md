---
title: Improving Test-Time Scaling with Adaptive Looped Transformers
title_zh: 自适应循环 Transformer 提升测试时扩展效率
authors:
- Yichen You
- Tianyu Fu
- Aosong Feng
- Xingtai Lv
- Xuefei Ning
- Ning Ding
- Yu Wang
affiliations:
- Tsinghua University
- Yale University
arxiv_id: '2609.35748'
url: https://arxiv.org/abs/2609.35748
pdf_url: https://arxiv.org/pdf/2609.35748
published: '2026-09-27'
collected: '2026-09-29'
category: Reasoning
direction: 自适应循环 Transformer 的测试时缩放
tags:
- Test-time scaling
- Looped Transformer
- Adaptive computation
- LLM reasoning
- AIME
one_liner: 提出 TaH2 自适应循环 Transformer，通过前瞻深度监督让模型仅对收益 token 增加迭代，测试时计算斜率提升 53%
practical_value: '- 在 LLM 推理服务中（如搜索 query 改写、商品卖点生成、推荐理由），可采用 TaH2 的自适应计算思路：训练一个轻量
  iteration decider，对简单 token 少迭代、困难 token 多迭代，同等精度下可显著降低 decode FLOPs，适合降低电商场景的推理成本与延迟。

  - lookahead depth supervision 的在线标签方法可迁移到动态路由/级联模型：判断“继续计算是否能提升预测”来训练 router，例如
  MoE 中选择专家数、广告出价/策略分析中的多步推理是否继续，避免固定深度浪费。

  - 该后训练方案不改变 backbone 结构，只加轻量 decider 并进行联合微调，适合对已部署的 7B/13B 模型做后训练优化，快速验证收益；对需要高精度推理的任务（如商品属性逻辑校验、A/B
  分析）尤其值得尝试。

  - 结论提示：全局固定深度 loop 在最大深度增加时会饱和，而自适应分配能让增益持续增长；在 Agent 多步推理中，可以按 token 难度动态分配思考步数，减少低效
  rollout 的算力消耗。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：Looped Transformer 通过重用层提升参数效率，但以往研究只在参数或 per-token FLOPs 匹配下比较，未深入考察输出变长时的测试时扩展能力。本文发现现有 looped 模型虽然 accuracy-compute 斜率更陡，但在相同计算量下反而不如 non-looped 基线，且固定深度循环对每个 token 都额外迭代，许多 token 并未受益。

**方法关键点**：提出 TaH2，联合后训练 backbone 与一个 iteration decider。采用 lookahead depth supervision，利用在线标签判断“进一步迭代是否能改善当前 token 的预测”，让模型仅对有益 token 增加迭代次数。训练不改变主结构，只加入轻量决策模块，兼顾效率与精度。

**关键结果**：在 AIME24–26 基准上，TaH2 的 accuracy-compute 斜率较 non-looped 基线提升 53%（2.74 vs. 1.79），在相同测试时计算量下超过基线峰值精度约 3.4 点。当最大迭代深度从 2 增至 8 时，现有 looped 模型趋于饱和，而 TaH2 相对 non-looped 的增益从 +2.8 点持续增长到 +3.9 点，证明自适应分配能持续从更深迭代中获益。
