---
title: 'SPRINT: Single-Step Generative Recommendation via Average Probability Velocity'
title_zh: SPRINT：基于平均概率速度的单步生成式推荐
authors:
- Zhuo Cai
- Shoujin Wang
- Peilin Zhou
- Min Xu
- Julian McAuley
- Fang Chen
affiliations:
- University of Technology Sydney
- New York University Abu Dhabi
- University of California, San Diego
arxiv_id: '2609.34306'
url: https://arxiv.org/abs/2609.34306
pdf_url: https://arxiv.org/pdf/2609.34306
published: '2026-09-28'
collected: '2026-09-29'
category: GenRec
direction: 生成式推荐 · Semantic ID · 单步生成
tags:
- Generative Recommendation
- Semantic ID
- Single-Step
- Flow Matching
- Contrastive Learning
- Inference Efficiency
one_liner: 把 Semantic ID 生成建模为平均概率速度，单次前向输出完整 SID，并用双层级流对比保持 token 连贯性
practical_value: '- 如果做 SID 生成式召回/排序，优先尝试 OPQ 而非 RQ-VAE/RQ-Kmeans：OPQ 的并行独立子空间更适合一次性预测全部
  token；本文消融显示换 RQ 会明显掉点，可作为架构选型依据。

  - 在单步并行解码 SID 时，单纯 per-token CE/contrastive 不够，必须加 SID 级整体打分：把 decoder 的 L 个位置隐状态
  concat 后 MLP 成 user 侧表示，与 item SID embedding 做 cosine 对比，能显著抑制“每个 token 合理但组合非法”的问题；item
  侧 SID embedding 可离线预计算，线上只多一次矩阵乘。

  - 线上推理保持 all-mask 输入、trie 约束解码，分数 = token 概率 log-sum + SID 级相似度，单次 forward 即可出 topK；相比
  masked diffusion 可拿到 8-10×加速，适合对 latency 敏感的电商推荐候选生成。

  - 训练时把 source time 以较大概率锚定在 all-mask（ρ=0.75~1），并采样约 100 个 negative SID 做对比，可在不大幅增加训练成本下同时提升收敛速度和精度。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**

生成式推荐（GR）用 Semantic ID 表示 item，但 AR 逐 token 解码需 L 次 forward；masked diffusion NAR 虽然并行，实际仍需多步 refine 才能保持竞争力。在 latency-sensitive 推荐系统中，这种多步成本难以接受。现有单步尝试如 RPG 把 SID 膨胀到 16-64 token、扩大 embedding 表，OneGR 依赖 A* 搜索，都还不够轻量。

**方法关键点**

- 把 SID 生成看作从全 mask 到目标 SID 的概率流，提出 average probability velocity；证明该平均速度由每个位置 token 的平均生成概率决定，因此可用 bidirectional Transformer 单次 forward 同时输出 L 个位置的概率。
- 设计 dual-level flow contrastive：token 级对 target token 与 negative SID token 做对比，提升单位置准确率；SID 级把 L 个 token 拼成整体 item 表示并与 negative SID 对比，恢复独立解码丢失的 token 间 coherence。
- 采用 OPQ 而非 RQ tokenizer，4-token SID，1-layer encoder + 4-layer decoder；inference 用 all-mask 输入 + trie 约束输出 valid SID，分数由 token 概率和 SID 级 cosine 得分组合。

**关键实验**

在 8 个真实数据集（Amazon 2014/2023、Yelp）上全面优于 baseline；R@5 最大提升 11.50%，N@5 最大提升 10.26%，平均比次优高 7.77%。相比最快 baseline RPG 加速 8.39-10.04×；相比 AR 方法 25.35-56.68×；相比 masked diffusion LLaDA-Rec 最高 125.94×。

**最值得记住的一句话**

单步 SID 生成可行且更准，关键是学习 average probability velocity 而不是 instantaneous velocity，并用 SID 级整体打分弥补 token 独立解码的 coherence 缺失。
