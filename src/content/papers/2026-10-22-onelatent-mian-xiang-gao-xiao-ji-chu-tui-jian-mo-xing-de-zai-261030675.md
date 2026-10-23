---
title: 'OneLatent: Latent Reasoning for Efficient Foundation Recommendation Models'
title_zh: OneLatent：面向高效基础推荐模型的潜在推理框架
authors:
- Hao Jiang
- Peiru Du
- Pengfei Yao
- Mengting Li
- Siyuan Lou
- Kuo Cai
- Sheng Yu
- Qiang Luo
- Jian Liang
- Ruiming Tang
affiliations:
- Kuaishou Technology
arxiv_id: '2610.30675'
url: https://arxiv.org/abs/2610.30675
pdf_url: https://arxiv.org/pdf/2610.30675
published: '2026-10-22'
collected: '2026-10-23'
category: GenRec
direction: 生成式推荐 · Latent Reasoning
tags:
- Latent Reasoning
- Generative Recommendation
- Semantic ID
- CoT Distillation
- Inference Efficiency
- Foundation Recommendation Models
one_liner: 用可学习潜在 token 压缩显式 CoT 推理，实现 Latent-Reason-then-Answer，精度与吞吐双提升
practical_value: '- 用固定数量的可学习 latent tokens 替代显式 rationale 生成：在用户上下文和目标 SID 之间插入 2-3
  个 latent token，训练时用教师 CoT 对齐，推理时只解码目标 item，可将 LLM 推荐的吞吐提升 17 倍以上且精度不降；适合在需要低延迟的生成式召回或重排中落地。

  - Multi-View Adaptive CoT 构造互补监督：设计意图探索、正样本评估、行为归因三个视角，并让教师根据用户行为复杂度自适应输出推理长度，相比单一模板能覆盖更多样兴趣且减少
  35% 冗余；这套 CoT 数据构造思路可直接迁移到 query 推荐、广告文案生成等场景。

  - 三阶段对齐 + 课程后训练：先 rationale 对齐，再 SID 对齐，最后混合 latent/standard SFT 1:1，能同时保留直接生成和
  latent 推理两种模式，避免显式 CoT 训练损害通用能力；适合渐进式上线 LLM 推荐。

  - 生产推理架构：行为触发异步刷新、价值感知调度、结果缓存 Redis，将大模型推理移出在线请求路径，只在候选融合时消费缓存结果；这是把 LLM 推荐落地到高
  QPS 电商/广告场景的可行工程范式，可直接参考。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
显式 Chain-of-Thought（CoT）虽能提升基础推荐模型（FRMs）的可解释性，但存在推理冗余、低 ROI 和兴趣漂移问题，且逐 token 生成 rationale 导致推理延迟高，难以线上部署。因此需要一种既能利用 CoT 监督、又能在推理时避免生成自然语言推理的高效方案。

## 方法关键点
- **MV-ACoT 多视角自适应 CoT**：从 Exploration（意图探索）、Evaluation（正样本匹配）、Attribution（行为归因）三个互补视角生成教师 CoT，并通过 prompt 引导教师根据实例复杂度自适应推理长度，减少冗余。
- **Latent Token Alignment 三阶段对齐**：在用户上下文和目标 SID 之间插入 3 个可学习 latent tokens；先单视角 rationale 对齐，再多视角对齐，最后推荐上下文对齐（用 latent tokens 直接预测 SID）。
- **课程后训练**：先按用户活跃度从高到低做推荐 SFT，再混合 latent reasoning 与 standard SFT 样本（1:1）激活 latent 推理接口，同时保留直接生成模式。
- **生产部署**：采用行为触发异步推理、价值感知调度和缓存结果，将大模型推理移出在线关键路径。

## 关键实验结果
在快手工业本地生活数据集和公开 Kuaishou LLM-Rec 基准上，基于 Qwen3.5-0.8B 的 OneLatent 均优于 ID/SID 基线及 OneReason 显式 CoT 变体。工业数据集上 SID@64 为 0.1993，较 Think-OR 提升 17.44%，较 No-Think-OR 提升 9.33%；吞吐 QPS 为 274.29，是显式 CoT 的 17.49 倍。扩展至 9B 后，SID@64 达 0.2008，较同规模 direct 基线提升 8.13%。LLM-as-judge 显示 MV-ACoT 各维度评分均显著高于 OneReason-CoT，且自适应策略将平均推理长度降低 35%。在线 A/B 测试中，收入提升 9.6%。

> 最值得记住的一句话：用少量可学习 latent tokens 将教师 CoT 蒸馏为隐式推理接口，在几乎不增加推理成本的前提下获得显式推理的收益。
